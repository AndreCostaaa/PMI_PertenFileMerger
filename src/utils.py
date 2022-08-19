def print_progress(progress):
    print(f"\r [{'#' * int(progress)}{' ' * (100 - int(progress))}] {progress:.2f}%",
          end="" if progress != 100 else "\n")


def get_date_from_user():
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

        return d, m, y


def ask_user_for_files(file_list):
    while True:
        d, m, y = get_date_from_user()
        date = y.strip() + m.strip() + d.strip()
        if len(date) < 8:
            # we should never get here
            print(f"Can't get the date from the input. Input was {date}")
            continue
        date_formatted = f"{date[:4]}_{date[4:6]}_{date[6:]}"
        files = [file for file in file_list if date in file]
        nb_files = len(files)
        print(f"Found {nb_files} csv files corresponding to {date_formatted}")
        if nb_files < 1:
            continue
        if len(date) <= 6:
            print("Date Format is incorrect")
            continue
        if 'y' in input("Continue [y/n] ?"):
            return files
