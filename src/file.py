import csv
import os

import pandas as pd


def save_data_to_xlsx(csv_file, xlsx_file):
    read_file = pd.read_csv(csv_file)
    read_file.to_excel(xlsx_file, index=None, header=True)


def save_data_to_csv(path, data):
    field_names = [key for key in data[0]]

    with open(path, 'a+', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(data)


def get_files_from_directory(path):
    return os.listdir(path)


def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
