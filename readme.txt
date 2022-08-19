

3 scripts are present in this folder, they manipulate the CSV files found in the \\PMPPSSSQLPRD.PMP.CH.PMI\OutboundMmsPRD folder:

1. Merge_All_Files will starts the script that will merge ALL CSV files
2. Merge_Files_From_Chosen_Date will ask the user for a date and will merge the files from that date
3. Merge_Files_From_Latest_Date will find the most recent date and merge all the files from that date

At the end a folder called "Compiled Data" will be created, inside a folder per date will be present
In each folder, 2 files are created, one "csv" file and one "xlsx" file

The "xlsx" converts the csv file to have the values separated in different columns.
