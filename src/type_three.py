from src import utils
from tokenize import generate_tokens
from src import pycode_ast

def compare_files(filename_one, filename_two):
	""" Receives filenames as parameters, compares the list of lines received
		Returns the tuple containing the plagiarism percentage
	"""
	if utils.check_file(utils.get_file_path(filename_one)) and utils.check_file(utils.get_file_path(filename_two)):
		file_one = open(utils.get_file_path(filename_one))
		file_two = open(utils.get_file_path(filename_two))

		if filename_one.split(".")[1] == "py":
			# try:
			results = pycode_ast.detect([file_one.read(), file_two.read()])
			# except:
			# print('Error: Non working python code')
			# return 60, 60
			for _, ast_list in results:
				total_count = sum(diff_info.total_count for diff_info in ast_list)
				plagiarism_count = sum(diff_info.plagiarism_count for diff_info in ast_list)
				file_one_plagiarism_percentage = utils.get_plagiarism_percentage(plagiarism_count, total_count)
				return file_one_plagiarism_percentage, file_one_plagiarism_percentage
		else:
			return 60, 60


	else:
		print("Error file format not supported")