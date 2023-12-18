import csv
import os
#import pandas as pd


def save_data_to_xlsx(csv_file, xlsx_file):
    pass
    #read_file = pd.read_csv(csv_file)
    #read_file.to_excel(xlsx_file, index=None, header=True)


def save_data_to_csv(path, data):

    
    field_names = []
    for line in data:
        x = [key for key in line]
        if len(x) > len(field_names):
            field_names = x
            
    with open(path, 'a+', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(data)


def get_files_from_directory(path):
    return os.listdir(path)


def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)


def remove_file_if_exists(path):
    if os.path.exists(path):
        os.remove(path)
