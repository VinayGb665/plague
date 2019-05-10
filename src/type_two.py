from src import utils
import tokenize 
from collections import Counter
from src import custom_tokenizer
from src import type_one 
from gst import match

def token_generator(fil, tokens_list):
    with open(fil, 'rb') as file:
        for five_tuple in tokenize.tokenize(file.readline):
            tokens_list.append( five_tuple.type)

def write_to_file(line_list, index):
    with open('./dataset/type_two_dump_' + index + '.py', 'w') as f:
        for item in line_list:
            f.write("%s\n" % item)

def c_token_generator(filename):
    tok = custom_tokenizer.Tokenizer(utils.get_file_path(filename))
    results = tok.full_tokenize()
    return results



def compare_files(filename_one, filename_two):
    """ 
        Receives filenames as parameters, compares the list of lines received
		Returns the tuple containing the plagiarism percentage
    """
    if utils.check_file(utils.get_file_path(filename_one)) and utils.check_file(utils.get_file_path(filename_two)):
        file_one_tokens, file_two_tokens = [], []
        file_one_clean, file_two_clean = utils.extract_files(filename_one, filename_two, True)
        print(file_one_clean)
        print(file_two_clean)
        if filename_one.split(".")[1] == "py":
            write_to_file(file_one_clean, "1")
            write_to_file(file_two_clean, "2")
            token_generator('./dataset/type_two_dump_1.py', file_one_tokens)
            token_generator('./dataset/type_two_dump_2.py', file_two_tokens)
            # print("yyyyyyyyyyy")
        else:
            file_one_tokens = c_token_generator(filename_one)
            file_two_tokens = c_token_generator(filename_two)
        # print(file_one_tokens)
        # print(file_two_tokens)
        ignore_a = ''
        string_a = ",".join(str(e) for e in file_one_tokens)
        string_b = ",".join(str(e) for e in file_two_tokens)
        
        number_of_lines_plagiarised = list(match(string_a, ignore_a, string_b, ignore_a, 6)[0])[2]
        
        # print(string_a)
        # print(string_b)
        # print(match(string_a, ignore_a, string_b, ignore_a, 3)[0])
        file_two_plagiarism_score = utils.get_plagiarism_percentage(number_of_lines_plagiarised * 2, len(string_a) + len(string_b) )
        return file_two_plagiarism_score, file_two_plagiarism_score
        # return type_one.compare_files('type_two_dump_1.py', 'type_two_dump_2.py')
    
    else:
        print("Error file format not supported")

if __name__ == '__main__':
    print(compare_files("../../Test_Folder/File_1.py","../../Test_Folder/File_1_copy.py"))
