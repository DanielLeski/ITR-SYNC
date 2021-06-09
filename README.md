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
  
