from src import utils
from tokenize import generate_tokens
from src import pycode_ast
from src import type_zero
from pycparser import c_parser, c_ast

def write_to_file(line_list, i):
    with open('./dataset/type_three_dump' + "_" + i + ".py", 'w') as f:
        for item in line_list:
            f.write("%s\n" % item)

def explore(ast, a):
	a.append(str(type(ast)))
	for i in ast:
		explore(i, a)

def c_utility(text, index):
	s = ""
	for e in text:
		x = e.strip()
		if(len(x) and x[0] != "#"):
			s += x
			s += " "
	parser = c_parser.CParser()
	ast = parser.parse(s, filename='<none>')
	a = []
	explore(ast, a)
	write_to_file(a, str(index))
				
def compare_files(filename_one, filename_two):
	""" 
		Receives filenames as parameters, compares the list of lines received
		Returns the tuple containing the plagiarism percentage
	"""
	if utils.check_file(utils.get_file_path(filename_one)) and utils.check_file(utils.get_file_path(filename_two)):
		a, b = utils.extract_files(filename_one, filename_two, True)
		write_to_file(a, "1")
		write_to_file(b, "2")
		file_one = open(utils.get_file_path('type_three_dump_1.py'))
		file_two = open(utils.get_file_path('type_three_dump_2.py'))

		if filename_one.split(".")[1] == "py":
			try:
				results = pycode_ast.detect([file_one.read(), file_two.read()])
			except:
				print('Error: Non working python code')
				return 60, 60
			for _, ast_list in results:
				total_count = sum(diff_info.total_count for diff_info in ast_list)
				plagiarism_count = sum(diff_info.plagiarism_count for diff_info in ast_list)
				file_one_plagiarism_percentage = utils.get_plagiarism_percentage(plagiarism_count, total_count)
				return file_one_plagiarism_percentage, file_one_plagiarism_percentage
		else:
			try:
				text_one, text_two = utils.extract_files(filename_one, filename_two, True)
				c_utility(text_one, 1)
				c_utility(text_two, 2)
				return type_zero.compare_files("type_three_dump_1.py", "type_three_dump_2.py")
			
			except:
				print("Error: Non working c/cpp files")
				return 70, 70

	else:
		print("Error file format not supported")