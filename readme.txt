3 scripts are present in this folder, they manipulate the CSV files found in the \\PMPPSSSQLPRD.PMP.CH.PMI\OutboundMmsPRD folder:

1. Merge_All_Files will start the script that merges ALL CSV files
2. Merge_Files_From_Chosen_Date will ask the user for a date and will merge the files from that date
3. Merge_Files_From_Latest_Date will find the most recent date and merge all the files from that date

After running the script, a folder called "Compiled Data" will be created, inside, a folder per date will be present
with the csv file corresponding to that date inside it

If windows blocks the .bat scripts, the scripts in the OutboundMmsPRD Scripts v3.zip folder can be used
(Don't forget to unzip them)

(ADVANCED)
If you have python in your computer, you can create a virtual environment with pandas and openpyxl and run the
merge_files.py file in src folder.
This Script will also create the xlsx file and will run faster than the scripts that use the .exe file
The xlsx file converts the csv file to have the values separated in different columns.

Usage : python merge_files.py <option> option can be 'all', 'chosen' or 'latest' (for: all files, chosen date or latest date)
