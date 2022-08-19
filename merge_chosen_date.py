import csv
import os
import time

# import pandas as pd

CURRENT_PATH = os.path.dirname(os.path.realpath(__name__))
BASE_DIR = r"\\PMPPSSSQLPRD.PMP.CH.PMI\OutboundMmsPRD"

PLACES_MAP = {
    "122-BU": "T0144",
    "122-FC": "T0124",
    "122-OR": "T0134",
    "232-EM1": "T0570",
    "270-EM1": "T0580",
    "920-EM1": "T0872",
    "020-EM1": "T0874",
}


def print_progress(progress):
    print(f"\r [{'#' * int(progress)}{' ' * (100 - int(progress))}] {progress:.2f}%", end="")


def save_data_to_xlsx(csv_file, xlsx_file):
    read_file = pd.read_csv(csv_file)
    read_file.to_excel(xlsx_file, index=None, header=True)


def save_data_to_csv(path, data):
    field_names = [key for key in data[0]]

    with open(path, 'a+', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(data)


def main():
    files = os.listdir(BASE_DIR)
    print(f"Found {len(files)} files in {BASE_DIR}.")
    if len(files) < 1:
        return
    compiled_data = {}

    start = int(round(time.time() * 1000))
    csv_files = [file for file in files if '.csv' in file]
    date = ""
    date_formatted = ""
    while True:
        print("Select the desired date to merge files")
        d = input("Day:")
        if len(d) < 1:
            print("Day can't be empty")
            continue
        m = input("Month:")
        if len(m) < 1:
            print("Month can't be empty")
            continue
        y = input("Year:")
        if len(y) < 2:
            print("Year must have at least 2 digits")
            continue

        if len(d) < 2:
            d = "0" + d
        if len(m) < 2:
            m = "0" + m
        if len(y) < 4:
            y = "20" + y[:2]

        date = y.strip() + m.strip() + d.strip()
        if len(date) < 8:
            # we should never get here
            print(f"Can't get the date from the input. Date was {date}")
            continue
        date_formatted = f"{date[:4]}_{date[4:6]}_{date[6:]}"
        files = [file for file in csv_files if date in file]
        nb_files = len(files)
        print(f"Found {nb_files} csv files corresponding to {date_formatted}")
        if nb_files < 1:
            continue
        if len(date) <= 6:
            print("Date Format is incorrect")
            continue
        if 'y' in input("Continue [y/n] ?"):
            break

    date_formatted = f"{date[:4]}_{date[4:6]}_{date[6:]}"

    print(f"Compiling data from {len(files)} csv files...")
    for i, file in enumerate(files):
        percentage_done = i * 100 / (len(files) - 1)
        print_progress(percentage_done)
        date = file.split("_")[-2]
        file_path = os.path.join(BASE_DIR, file)
        position = file.split('+')[1][0:3]
        iterator = csv.reader(open(file_path))

        dic = {"POSITION": position}
        for row in iterator:
            if 'MOISTURE_METER' in row[0]:
                # remove the "+" sign
                row[1] = row[1][1:]
                # add the place based on the defined map
                dic["PLACE"] = PLACES_MAP[row[1].split('+')[1].strip()]

            elif 'COLLECTION_DATE' in row[0]:
                split = row[1].split(' ')
                dic['DATE'] = split[0]
                dic['TIME'] = split[1]
                continue

            dic[row[0]] = row[1]
        if date in compiled_data:
            compiled_data[date].append(dic)
        else:
            compiled_data[date] = [dic]

    compiled_data_folder = os.path.join(CURRENT_PATH, "CompiledData")
    if not os.path.exists(compiled_data_folder):
        os.mkdir(compiled_data_folder)
    print()
    print("Merging data...")

    for i, key in enumerate(compiled_data):
        percentage_done = (i + 1) * 100 / (len(compiled_data))
        print_progress(percentage_done)
        results_folder = os.path.join(compiled_data_folder, key)
        if not os.path.exists(results_folder):
            os.mkdir(results_folder)

        csv_results_file = os.path.join(results_folder, f"{date_formatted}.csv")
        xlsx_results_file = os.path.join(results_folder, f"{date_formatted}.xlsx")
        if os.path.exists(csv_results_file):
            os.remove(csv_results_file)

        save_data_to_csv(csv_results_file, compiled_data[key])
        # save_data_to_xlsx(csv_results_file, xlsx_results_file)
    print()
    print(f"Script took {int(round(time.time() * 1000)) - start} ms to run")
    input("Press Enter to exit the program...")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
