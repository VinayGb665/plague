import config
import os
import functools
import re

re_comment_strings_for_c_and_cpp = {
	"MULTI_LINES_COMMENT" : "/\*.*?\*/",
	"SINGLE_LINE_COMMENT" : "//.*?\n"
}

re_comment_strings_for_py = {
	"MULTI_LINES_COMMENT" : "\'\'\'.*?\'\'\'",
	"SINGLE_LINE_COMMENT" : "\#.*?\n"
}

TERMCOLORS = {
	"RED"   : "\033[1;31m",  
	"BLUE"  : "\033[1;34m",
	"CYAN"  : "\033[1;36m",
	"GREEN" : "\033[0;32m",
	"RESET" : "\033[0;0m",
	"BOLD"   : "\033[;1m"
}

def check_file(filename):
	''' Checks if the file is written in allowed programming languages
	'''
	file_parts = filename.split('.')
	if len(file_parts) !=2:
		print(file_parts)
		print(filename + ": File name is not correct")
		return False

	# Checks for extension
	if file_parts[-1] not in config.get_extensions():
		print(filename + ": Programming language is not supported")
		return False

	if not os.path.exists(filename):
		print(filename + ": File does not exist")
		return False


	

	return True

def get_file_path(filename):
	
	return config.SOURCE_CODE_FILEPATH + filename

def remove_comments_using_re(string, extension):
	re_comment_strings = re_comment_strings_for_py if extension == 'py' else re_comment_strings_for_c_and_cpp 
	string = re.sub(re.compile(re_comment_strings["MULTI_LINES_COMMENT"],re.DOTALL ) ,"\n" ,string) # remove all occurance streamed comments (/*COMMENT */) from string
	string = re.sub(re.compile(re_comment_strings["SINGLE_LINE_COMMENT"] ) ,"\n" ,string) # remove all occurance singleline comments (//COMMENT\n ) from string
	return string

def join_lines(lines_list):
	return functools.reduce(lambda str_a, str_b: str_a + str_b, lines_list)

def split_lines(lines_string):
	lines_list=lines_string.split('\n')
	return list(map(lambda x: x + '\n', filter(lambda x: x, lines_list)))


def remove_comments(lines_list, file_extension):
	# print(lines_list)
	if(len(lines_list)>0):
		lines_list[-1] += '\n' # Add an extra line at the end of the line
		lines_string = join_lines(lines_list)
		lines_string = remove_comments_using_re(lines_string, file_extension)
		return split_lines(lines_string)
	else:
		return []


def get_readlines(filepath, remove_comments_bool):
	if not check_file(filepath):
		return None
	with open(filepath) as file:
		lines = file.readlines()
	#Only for type one
	if remove_comments_bool:
		lines = remove_comments(lines, filepath.split('.')[-1])
	return lines

def extract_files(filename_one, filename_two, remove_comments_bool):
	''' Receives the filenames as strings, returns list of lines
	'''
	filepath_one = get_file_path(filename_one)
	filepath_two = get_file_path(filename_two)
	return get_readlines(filepath_one, remove_comments_bool), get_readlines(filepath_two, remove_comments_bool)

def get_plagiarism_percentage(number_of_lines_copied, total_number_of_lines):
	return round((number_of_lines_copied*100)/ total_number_of_lines, 2)

def print_diff(plagiarism_result, diff_symbol):
	for line in plagiarism_result:
		if line[0] == ' ':
			print(TERMCOLORS["RED"] + line, end = "")
		elif line[0] == diff_symbol:
			print(TERMCOLORS["GREEN"] + line, end = "")
