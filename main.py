"""
Main script to find differences between data 
"""

import numpy as np
import pandas as pd
from google_drive_downloader import GoogleDriveDownloader as gdd
import sys
import platform
import csv


os_name = platform.system()

if os_name == "Darwin":
  csvgdd = gdd.download_file_from_google_drive(file_id="13xlzVyC3uk9WEg0SoJwIvkM_HsSVV6pY",
  dest_path="/Users/smol/fun/ITR_ACCESS/Hardware.KitchenSink.csv",
  showsize=True,
  overwrite=True)
elif os_name == "Windows":
    csvgg = gdd.download_file_from_google_drive("13xlzVyC3uk9WEg0SoJwIvkM_HsSVV6pY", dest_path='C:\\Users\\sh\\Desktop\\ITR_ACCESS\\ITR_ACCESS\\Hardware.KitchenSink.csv', showsize=True, overwrite=True)


def fix_NaN(inventory, ITR):
  #Iventory checks
  inventory.fillna(0, inplace=True)
  inventory['ITR'] = inventory['ITR'].astype(int)
  inventory['Student_Number']= inventory['Student_Number'].astype(int)
  
  #ITR Checks
  ITR.fillna(0, inplace=True)

def main():
 # print("Enter the path of where the main Inventory CSV is located")
 # main_inv = input()
 # print("Enter the path of where the ITR Hardware Kitchen sink is located")
 # main_itr = input()
  inv = pd.read_csv("Inventory.csv")
  itr = pd.read_csv("Hardware.KitchenSink.csv")
  
  print("\n")

  fix_NaN(inv, itr)

  #making them a string for easier comparision
  access = inv['ITR'].astype(str)
  ITRDB = itr['InternalID'].astype(str)
 
  # add getting the serial columns from each one
  serial_number_access = inv['Serial']
  serial_number_ITR = itr['SerialNumber']


  # getting the number of found when comparing both files
  found = 0
  
  #Lists to get values use as indexes of ITR and Internal number
  # OR 
  # Getting the actual ITR and Internal Numbers
  access_index = []
  ITR_index = []
  access_values = []
  ITR_values = []

  # We find ITR and InteralID's that are the same 
  for i, r1 in enumerate(access.values):
    for j, r2  in enumerate(ITRDB.values):
     if r1 == r2:
        found = found + 1
        access_index.append(i)
        ITR_index.append(j)
        access_values.append(r1)
        ITR_values.append(r2)
  
  # This block of code get either index's or ITR values and replaces the mismatch serials in ITR to the proper ones
  error = 0
  correct = 0
  index = []
  values = []
  old_itr = []
  for l in range(len(access_index)):
    i1 = access_index[l]
    i2 = ITR_index[l]
    i3 = access_values[l]
    i4 = ITR_values[l]
    v1 = serial_number_access.iloc[i1]
    v2 = serial_number_ITR.iloc[i2]
    if v1 != v2:
      error = error + 1
      index.append(i4)
      values.append(v1)
      old_itr.append(v2)
      itr.iloc[i2, itr.columns.get_loc('SerialNumber')] = v1
    else:
      correct = correct + 1
 
  # Useful Print statements that are used to show what the program found and did
  print("\n")
  print("Rewriting the ITR data")
  itr.to_csv("Hardware.KitchenSink.csv", index=False, encoding='utf-8')
  print("How many matches were found within ITR and InteralID #'s : ", found)
  print("The amount of serial numbers that are not the same between Access and ITR", error)
  print("The amount of serial numbers that are the same between Access and ITR", correct)

  
  # Creating the final change log which gives the proper ITR and correct Serial Number from the 'Inventory.csv'
  d = {'ITR': index, 'NewSerialNumbers': values, 'OldSerialNumbers': old_itr}
  log = pd.DataFrame(d)
  log.to_csv('log.csv', index=False, encoding='utf-8')
 

if __name__ == "__main__":
   main()

