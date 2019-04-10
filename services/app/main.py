from src import type_zero
from src import type_one
from src import type_two
from src import type_three

file_one  = "File_1.py"
file_two = "File_1_NoComments.py"

print(type_zero.compare_files(file_one, file_two ))
print(type_one.compare_files(file_one, file_two))
print(type_two.compare_files(file_one, file_two))
print(type_three.compare_files(file_one, file_two))