import csv
import os
import sys
import time

import constants
import file
import utils
import json

def compile_data_from_files(folder: str, files:list[str], places_map:dict[str,str]):
    compiled_data = {}
    for i, x in enumerate(files):
        # calculate percentage done
        percentage_done = i * 100 / (len(files) - 1)
        utils.print_progress(percentage_done)

        date = x.split("_")[-2]
        file_path = os.path.join(folder, x)
        position = x.split('+')[1][0:3]
        iterator = csv.reader(open(file_path))
        dic = {"POSITION": position}
        for row in iterator:
            if 'MOISTURE_METER' in row[0]:
                # remove the "+" sign
                row[1] = row[1][1:]
                # add the place based on the defined map
                raw_place = row[1].split('+')[1].strip()
                dic["PLACE"] = places_map.get(raw_place)
                if not dic["PLACE"]:
                    #print(f"Couldn't find the translation to {raw_place}")
                    dic["PLACE"] = raw_place

            elif 'COLLECTION_DATE' in row[0]:
                split = row[1].split(' ')
                dic['DATE'] = split[0]
                dic['TIME'] = split[1]
                continue
            if "VERSION" in row[0]:
                continue
            dic[row[0]] = row[1]
        if date in compiled_data:
            compiled_data[date].append(dic)
        else:
            compiled_data[date] = [dic]
    return compiled_data


def merge_data_to_result_files(data, results_folder):
    for i, key in enumerate(data):
        date_formatted = f"{key[:4]}_{key[4:6]}_{key[6:]}"
        percentage_done = (i + 1) * 100 / (len(data))
        utils.print_progress(percentage_done)
        date_folder = os.path.join(results_folder, key)
        file.create_folder(date_folder)
        
        csv_results_file = os.path.join(date_folder, f"{date_formatted}.csv")
        file.remove_file_if_exists(csv_results_file)

        file.save_data_to_csv(csv_results_file, data[key])

        xlsx_results_file = os.path.join(date_folder, f"{date_formatted}.xlsx")
        file.remove_file_if_exists(xlsx_results_file)
        file.save_data_to_xlsx(csv_results_file, xlsx_results_file)


def main(args):
    if len(args) < 2:
        print(f"Usage: {args[0]} [instruction]. eg: {args[0]} all")
        return
    # get list of files
    config = json.load(open(constants.CONFIG_PATH))


    base_dir = config.get("folder")
    if not base_dir:
        print(f"Folder not found in config... Please check {constants.CONFIG_PATH}")
        return
    
    files = file.get_files_from_directory(base_dir)

    nb_of_files = len(files)
    if nb_of_files < 1:
        return

    # used to calculate the time the script takes to run
    start = int(round(time.time() * 1000))
    # get the csv files
    csv_files = [x for x in files if '.csv' or '.CSV' in x]

    if 'latest' in args[1]:
        latest_date = max(csv_files, key=lambda file: int(file.split("_")[-2])).split("_")[-2]
        date_formatted = f"{latest_date[:4]}_{latest_date[4:6]}_{latest_date[6:]}"
        files = [x for x in files if latest_date in x]
        print(f"Latest Date Found: {date_formatted}.")
    elif 'chosen' in args[1]:
        files = utils.ask_user_for_files(csv_files)
    elif 'all' in args[1]:
        files = csv_files
    else:
        print(f"Usage: {args[0]} [instruction]. eg: {args[0]} all")
        return

    print(f"Compiling data from {len(files)} csv files...")
    
    places_map = json.load(open(constants.PLACES_MAP_PATH))

    print("Places found in config:")
    for key, val in places_map.items():
        print(f"\t{key} -> {val}")
    
    
    compiled_data = compile_data_from_files(config["folder"], files, places_map)
    results_folder = os.path.join(constants.CURRENT_PATH, "Compiled Data")
    file.create_folder(results_folder)

    print("Merging data...")
    merge_data_to_result_files(compiled_data, results_folder)

    print(f"Script took {int(round(time.time() * 1000)) - start} ms to run")


if __name__ == '__main__':
    main(sys.argv)
