# ITR_ACCESS

## TODO:
- Get the cvs files properly loaded into a dataframe
  - Get all of the columns to be correctly shown

- Get the comparison between both dataframe files
  - Log the differences between the two files
  - Update the ITR CSV and rename each one so buckley knows which one is up-to-date

- Make the process be able to run stable running in the background on Linux, Unix, Windows machines
  - Windows
    - Get all the dependencies installed and the proper libraries

- Things to look out for when comparing both of the CSV files
  - Format 1 :
    - These can be specific columns or ID numbers that we can see if they changed
    - Show ones that were added
  - Format 2 : 
    - Grab ITR number from "INV" (ACCESS DATA)
      - grab that column and save it to a seperate dataframe to use for comparison
      - Take the original "ITR" and for now do a simple comparison with "InternalID" 
  - Buckley:
    - Make sure ITR and InternalID number are the same and at that point check the serial numbers
  - Be able to fetch the file from using a url.
    - Library googledrivedownloader to get file id and dest_path
- Add error checking for ITR numbers if they are blank then skip them
  - if the ITR numbers are blank then we don't add them to the list of changes 
## Process:
- Downloads the files from google drive
  - If need be update the file_id to get the proper file from the "Junk" folder from google drive
- After downloading, convert xlsx to csv, youll have to open the file after it was downloaded and save it as a csv
  - Will right my own converter because all of these libraries have all of these stars on github but don't work :/
- Code wise
  - When there is a matching set of ITR and InternalID 
  - We check if the serial numbers are the same both ends (using indexes from the dataframe to judge what serial numbers we are using to compare)
    - If they are not the same then we create a new dataframe that we place that in with the index number
    - Then we merge the Access data with the updated Serial numbers from the new dataframe and merge.
    - After merge we double check if everything is correct and upload it to ITR


### Ideas: 
- Check if the ITR Numbers are the same and then check if the serial numbers are the same in both spots and keep going. 
- Read excel file into a dataframe and then convert it into a csv to use for the comparison script
