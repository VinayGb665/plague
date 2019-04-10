import json 

with open('config.json') as json_data_file:
    config = json.load(json_data_file)

#config macros
SOURCE_CODE_FILEPATH = config["source_code_filepath"]

def get_extensions():
	return config["allowed_extensions"]