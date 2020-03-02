import ember
import os
import json
import re


'''
Preps the files that are in the ember dataset
    The data files are in a messy format in which there is jsons back to back not in a list
    This function creates the needed grammer.
    
    Note this function should be edited to match your repository space.
    
'''
def prep_json_files():
    num_files = 6

    file_ins = [f'train_features_{x}.jsonl' for x in range(num_files)]
    file_outs = [f'train_features_2_{x}.jsonl' for x in range(num_files)]

    for file_path_in, file_path_out in zip(file_ins, file_outs):
        is_first_line = True
        with open(file_path_in, 'r') as read_file:
            with open(file_path_out, 'w+') as write_file:
                for line in read_file.readlines():
                    if is_first_line:
                        write_file.write(re.sub('[,]*{"sha256', '[{"sha256', line))
                        is_first_line = False
                    else:
                        write_file.write(re.sub('[,]*{"sha256', ',{"sha256', line).rstrip(r'\S'))
                write_file.write(']')


if __name__ == '__main__':
    os.chdir("Data\ember2018")
    print(os.getcwd())

    prep_json_files()

    num_files = 6
    file_path = [f'train_features_2_{x}.jsonl' for x in range(num_files)]

    total_data = []

    for file in file_path:
        with open(file) as json_file:
            total_data.append(json.load(json_file))

    print(len(total_data))
    print(type(total_data[0]))

    # ember.create_vectorized_features("Data/ember2018/")
    # ember.create_metadata("Data/ember2018/")

    # X_train, y_train, X_test, y_test = ember.read_vectorized_features("Data/ember2018/")
    # metadata_dataframe = ember.read_metadata("Data/ember2018/")

    # print(metadata_dataframe)
    # print(type(metadata_dataframe))

    # print(y_train)
