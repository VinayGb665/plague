import difflib
import config
from src import utils

def compare_files(filename_one, filename_two, type_one = False):
	''' Receives filenames as parameters, compares the list of lines received
		Returns the tuple containing the plagiarism percentage
	'''
	file_one, file_two = utils.extract_files(filename_one, filename_two, type_one)
	if file_one is None or file_two is None:
		return None, None
	result = []
	for line in difflib.unified_diff(file_one, file_two):
		result.append(line)

	if not result:
		# If there is no result, then it's 100% same file
		return 100.0, 100.0

	# Exclude the initial three default lines
	result = result[3:]

	#prints the results for file one
	# print("Source code one: ")
	# utils.print_diff(result, '-')
	# print("-" * 40)

	# #prints the results for file two
	# print("Source code two: ")
	# utils.print_diff(result, '+')
	# print("-" * 40)

	number_of_lines_plagiarised = len(file_one) - len(list(filter(lambda x: x[0] == '-', result)))
	file_one_plagiarism_percentage = utils.get_plagiarism_percentage(number_of_lines_plagiarised * 2, len(file_one) + len(file_two))
	file_two_plagiarism_percentage = utils.get_plagiarism_percentage(number_of_lines_plagiarised * 2, len(file_one) + len(file_two))

	return file_one_plagiarism_percentage, file_two_plagiarism_percentage
