3 scripts are present in this folder, they manipulate the CSV files found in the \\PMPPSSSQLPRD.PMP.CH.PMI\OutboundMmsPRD folder:

1. Merge_All_Files will start the script that merges ALL CSV files
2. Merge_Files_From_Chosen_Date will ask the user for a date and will merge the files from that date
3. Merge_Files_From_Latest_Date will find the most recent date and merge all the files from that date

After running the script, a folder called "Compiled Data" will be created, inside, a folder per date will be present
with the csv file corresponding to that date inside it

Folder path is read from config.json file:
eg:
{
"folder": "//PPPSSPMPSTD0001/OutboundMmsPRD"
}

You can also set a path from your computer:
eg:
{
"folder": "C:/PertenFiles"
}

Places are translated using places.json file
eg:
{
"122-BU": "T0144",
"122-FC": "T0124",
"122-OR": "T0134",
"232-EM1": "T0570",
"270-EM1": "T0580",
"920-EM1": "T0872",
"020-EM1": "T0874",
"350-EM1": "T0615"
}

(ADVANCED)
If you have python in your computer, you can create a virtual environment:
python -m venv env

Activate the environment (eg in powershell):
& ./env/Scripts/activate.ps1

Install dependencies:
pip install pandas
pip install openpyxl

Run the python file:
python src/merge_files.py <option> option can be 'all', 'chosen' or 'latest' (for: all files, chosen date or latest date)

# Build

Using python3. Create a virtual environnement, activate it and install requirements:

```powershell
python -m venv env
& .\env\Scripts\Activate.ps1
pip install -r requirements.txt
```

To create an .exe file, [Nuitka](https://github.com/Nuitka/Nuitka) can be used to build this project.

Once you have all the [Nuitka](https://github.com/Nuitka/Nuitka) requirements.

Activate the virtual environnement and build it

```powershell
& ./env/scripts/activate.ps1
python -m nuitka --standalone ./src/main.py --enable-plugin=tk-inter
```
