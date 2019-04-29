from src import type_zero
from src import type_one
# from src import type_two
file_one  = input("File one: ")
file_two = input("File two: ")

type_zero.compare_files(file_one, file_two)
print(type_one.compare_files(file_one, file_two))