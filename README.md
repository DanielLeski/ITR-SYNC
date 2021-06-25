# ITR_ACCESS

## TODO/Planning:
- Add error checking for ITR numbers if they are blank then skip them
  - if the ITR numbers are blank then we don't add them to the list of changes
- Use mapping instead of array indexing
- Add sql removal and addiiton of other records and etc
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
    
