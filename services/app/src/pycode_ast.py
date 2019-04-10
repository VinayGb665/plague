import sys
import ast
import difflib
import operator
import argparse
import itertools
import collections


class FuncNodeCollector(ast.NodeTransformer):
    """
        Part of the astor library for Python AST manipulation.
    """

    def __init__(self):
        super(FuncNodeCollector, self).__init__()
        self._curr_class_names = []
        self._func_nodes = []
        self._last_node_lineno = -1
        self._node_count = 0

    @staticmethod
    def _mark_docstring_sub_nodes(node):
    
        def _mark_docstring_nodes(body):
            if body and isinstance(body, collections.Sequence):
                for n in body:
                    if isinstance(n, ast.Expr) and isinstance(n.value, ast.Str):
                        n.is_docstring = True

        node_body = getattr(node, 'body', None)
        _mark_docstring_nodes(node_body)
        node_orelse = getattr(node, 'orelse', None)
        _mark_docstring_nodes(node_orelse)

    @staticmethod
    def _is_docstring(node):
        return getattr(node, 'is_docstring', False)

    def generic_visit(self, node):
        self._node_count = self._node_count + 1
        self._last_node_lineno = max(getattr(node, 'lineno', -1), self._last_node_lineno)
        self._mark_docstring_sub_nodes(node)
        return super(FuncNodeCollector, self).generic_visit(node)

    def visit_Str(self, node):
        del node.s
        self.generic_visit(node)
        return node

    def visit_Expr(self, node):
        if not self._is_docstring(node):
            self.generic_visit(node)
            if hasattr(node, 'value'):
                return node

    def visit_arg(self, node):
        del node.arg
        del node.annotation
        self.generic_visit(node)
        return node

    def visit_Name(self, node):
        del node.id
        del node.ctx
        self.generic_visit(node)
        return node

    def visit_Attribute(self, node):
        del node.attr
        del node.ctx
        self.generic_visit(node)
        return node

    def visit_Call(self, node):
        func = getattr(node, 'func', None)
        if func and isinstance(func, ast.Name) and func.id == 'print':
            return  # remove print call and its sub nodes for python3
        return node

    def visit_ClassDef(self, node):
        self._curr_class_names.append(node.name)
        self.generic_visit(node)
        self._curr_class_names.pop()
        return node

    def visit_FunctionDef(self, node):
        node.name = '.'.join(itertools.chain(self._curr_class_names, [node.name]))
        self._func_nodes.append(node)
        count = self._node_count
        self.generic_visit(node)
        node.endlineno = self._last_node_lineno
        node.nsubnodes = self._node_count - count
        return node

    def visit_Compare(self, node):

        def _simple_nomalize(*ops_type_names):
            if node.ops and len(node.ops) == 1 and type(node.ops[0]).__name__ in ops_type_names:
                if node.left and node.comparators and len(node.comparators) == 1:
                    left, right = node.left, node.comparators[0]
                    if type(left).__name__ > type(right).__name__:
                        left, right = right, left
                        node.left = left
                        node.comparators = [right]
                        return True
            return False

        if _simple_nomalize('Eq'):
            pass

        if _simple_nomalize('Gt', 'Lt'):
            node.ops = [{ast.Lt: ast.Gt, ast.Gt: ast.Lt}[type(node.ops[0])]()]

        if _simple_nomalize('GtE', 'LtE'):
            node.ops = [{ast.LtE: ast.GtE, ast.GtE: ast.LtE}[type(node.ops[0])]()]

        self.generic_visit(node)
        return node

    def visit_Print(self, node):
        # remove print expr for python2
        pass

    def clear(self):
        self._func_nodes = []

    def get_function_nodes(self):
        return self._func_nodes


class FuncInfo(object):
    """
    Part of the astor library for Python AST manipulation.
    """

    class NonExistent(object):
        pass

    def __init__(self, func_node, code_lines):
        assert isinstance(func_node, ast.FunctionDef)
        self._func_node = func_node
        self._code_lines = code_lines
        self._func_name = func_node.__dict__.pop('name', '')
        self._func_code = None
        self._func_code_lines = None
        self._func_ast = None
        self._func_ast_lines = None

    def __str__(self):
        return '<' + type(self).__name__ + ': ' + self.func_name + '>'

    @property
    def func_name(self):
        return self._func_name

    @property
    def func_node(self):
        return self._func_node

    @property
    def func_code(self):
        if self._func_code is None:
            self._func_code = ''.join(self.func_code_lines)
        return self._func_code

    @property
    def func_code_lines(self):
        if self._func_code_lines is None:
            self._func_code_lines = self._retrieve_func_code_lines(self._func_node, self._code_lines)
        return self._func_code_lines

    @property
    def func_ast(self):
        if self._func_ast is None:
            self._func_ast = self._dump(self._func_node)
        return self._func_ast

    @property
    def func_ast_lines(self):
        if self._func_ast_lines is None:
            self._func_ast_lines = self.func_ast.splitlines(True)
        return self._func_ast_lines

    @staticmethod
    def _retrieve_func_code_lines(func_node, code_lines):
        if not isinstance(func_node, ast.FunctionDef):
            return []
        if not isinstance(code_lines, collections.Sequence) or isinstance(code_lines, basestring):
            return []
        if getattr(func_node, 'endlineno', -1) < getattr(func_node, 'lineno', 0):
            return []
        lines = code_lines[func_node.lineno - 1: func_node.endlineno]
        if lines:
            padding = lines[0][:-len(lines[0].lstrip())]
            stripped_lines = []
            for l in lines:
                if l.startswith(padding):
                    stripped_lines.append(l[len(padding):])
                else:
                    stripped_lines = []
                    break
            if stripped_lines:
                return stripped_lines
        return lines

    @staticmethod
    def _iter_node(node, name='', missing=NonExistent):
        """Iterates over an object:

           - If the object has a _fields attribute,
             it gets attributes in the order of this
             and returns name, value pairs.

           - Otherwise, if the object is a list instance,
             it returns name, value pairs for each item
             in the list, where the name is passed into
             this function (defaults to blank).

        """
        fields = getattr(node, '_fields', None)
        if fields is not None:
            for name in fields:
                value = getattr(node, name, missing)
                if value is not missing:
                    yield value, name
        elif isinstance(node, list):
            for value in node:
                yield value, name

    @staticmethod
    def _dump(node, name=None, initial_indent='', indentation='    ',
              maxline=120, maxmerged=80, special=ast.AST):
        """Dumps an AST or similar structure:

           - Pretty-prints with indentation
           - Doesn't print line/column/ctx info

        """

        def _inner_dump(node, name=None, indent=''):
            level = indent + indentation
            name = name and name + '=' or ''
            values = list(FuncInfo._iter_node(node))
            if isinstance(node, list):
                prefix, suffix = '%s[' % name, ']'
            elif values:
                prefix, suffix = '%s%s(' % (name, type(node).__name__), ')'
            elif isinstance(node, special):
                prefix, suffix = name + type(node).__name__, ''
            else:
                return '%s%s' % (name, repr(node))
            node = [_inner_dump(a, b, level) for a, b in values if b != 'ctx']
            oneline = '%s%s%s' % (prefix, ', '.join(node), suffix)
            if len(oneline) + len(indent) < maxline:
                return '%s' % oneline
            if node and len(prefix) + len(node[0]) < maxmerged:
                prefix = '%s%s,' % (prefix, node.pop(0))
            node = (',\n%s' % level).join(node).lstrip()
            return '%s\n%s%s%s' % (prefix, level, node, suffix)

        return _inner_dump(node, name, initial_indent)


class FuncDiffInfo(object):
    """
    An object stores the result of candidate python code compared to referenced python code.
    """

    info_ref = None
    info_candidate = None
    plagiarism_count = 0
    total_count = 0

    @property
    def plagiarism_percent(self):
        return 0 if self.total_count == 0 else (self.plagiarism_count / float(self.total_count))




def diff(a, b):
    a = a.func_ast_lines
    b = b.func_ast_lines

    def _gen():
        for group in difflib.SequenceMatcher(None, a, b).get_grouped_opcodes(0):
            for tag, i1, i2, j1, j2 in group:
                if tag == 'equal':
                    for line in a[i1:i2]:
                        yield ''
                    continue
                if tag in ('replace', 'delete'):
                    for line in a[i1:i2]:
                        yield '-'
                if tag in ('replace', 'insert'):
                    for line in b[j1:j2]:
                        yield '+'

    return collections.Counter(_gen())['-']

def total(a, b):
    return len(a.func_ast_lines)



def detect(pycode_string_list):

    func_info_list = []
    for index, code_str in enumerate(pycode_string_list):
        root_node = ast.parse(code_str)
        collector = FuncNodeCollector()
        collector.visit(root_node)
        code_utf8_lines = code_str.splitlines(True)
        func_info = [FuncInfo(n, code_utf8_lines) for n in collector.get_function_nodes()]
        func_info_list.append((index, func_info))

    ast_diff_result = []
    index_ref, func_info_ref = func_info_list[0]
    if len(func_info_ref) == 0:
        raise "Error in type_three python"

    for index_candidate, func_info_candidate in func_info_list[1:]:
        func_ast_diff_list = []
        for fi1 in func_info_ref:
            min_diff_value = int((1 << 31) - 1)
            min_diff_func_info = None
            for fi2 in func_info_candidate:
                dv = diff(fi1, fi2)
                if dv < min_diff_value:
                    min_diff_value = dv
                    min_diff_func_info = fi2
                if dv == 0:  # entire function structure is plagiarized by candidate
                    break

            func_diff_info = FuncDiffInfo()
            func_diff_info.info_ref = fi1
            func_diff_info.info_candidate = min_diff_func_info
            func_diff_info.total_count = total(fi1, min_diff_func_info)
            func_diff_info.plagiarism_count = func_diff_info.total_count - min_diff_value if min_diff_func_info else 0
            func_ast_diff_list.append(func_diff_info)
        func_ast_diff_list.sort(key=operator.attrgetter('plagiarism_percent'), reverse=True)
        ast_diff_result.append((index_candidate, func_ast_diff_list))

    return ast_diff_result
