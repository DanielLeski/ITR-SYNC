import numpy as np
import pandas as pd
from google_drive_downloader import GoogleDriveDownloader as gdd
import sys
import platform


#getting the os 
os_name = platform.system()

#if os_name == "Darwin":
 # csv = gdd.download_file_from_google_drive(file_id="13xlzVyC3uk9WEg0SoJwIvkM_HsSVV6pY",
 #                                         dest_path="/Users/smol/fun/ITR_ACCESS/Hardware.KitchenSink.csv",
  #                                        showsize=True,
   #                                       overwrite=True)


  #inv = gdd.download_file_from_google_drive(file_id="1hLU-0F9N1xhMPZ1wD4aAUT2Jx0p82dZB",
      #                                    dest_path = "/Users/smol/fun/ITR_ACCESS/Inventory.xlsx",
    #                                      showsize=True,
     #                                     overwrite=True)
#elif os_name == "Linux":
#  csv = gdd.download_file_from_google_drive(file_id="13xlzVyC3uk9WEg0SoJwIvkM_HsSVV6pY",
       #                                   dest_path="/home/smooth/fun/ITR_ACCESS/Hardware.KitchenSink.csv",
        #                                  showsize=True,
         #                                 overwrite=True)


 # inv = gdd.download_file_from_google_drive(file_id="1hLU-0F9N1xhMPZ1wD4aAUT2Jx0p82dZB",
          #                                dest_path = "/home/smooth/fun/ITR_ACCESS/Inventory.xlsx",
           #                               showsize=True,
            #                              overwrite=True)

#else:
 # print("NO OS RE")
  



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

  fix_NaN(inv, itr)

  access = inv['ITR'].astype(str)
  ITRDB = itr['InternalID'].astype(str)
 
  # add getting the serial columns from each one
  serial_number_access = inv['Serial']
  serial_number_ITR = itr['SerialNumber']


  # getting the number of found when comparing both files
  found = 0
  
  access_index = []
  ITR_index = []

  for i, r1 in enumerate(access.values):
    for j, r2  in enumerate(ITRDB.values):
     if r1 != r1:
        print(r1, " ", r2)
     if r1 == r2:
        found = found + 1
       # print(i, r1, " ", j, r2)
        access_index.append(i)
        ITR_index.append(j)

  
  error = 0
  correct = 0
  for l in range(len(access_index)):
    i1 = access_index[l]
    i2 = ITR_index[l]
    v1 = serial_number_access.iloc[i1]
    v2 = serial_number_ITR.iloc[i2]
    if v1 != v2:
      error = error + 1
      #print(i1, v1, " ",  i2, v2)
      print(v2)
      itr.iloc[i2, itr.columns.get_loc('SerialNumber')] = v1
    elif v1 == v2:
      correct = correct + 1

  print("Rewriting the ITR data")
  itr.to_csv("Hardware.KitchenSink.csv", index=False, encoding='utf-8')
  print("How many matches were found within ITR and InteralID #'s : ", found)
  print("The amount of serial numbers that are not the same between Access and ITR", error)
  print("The amount of serial numbers that are the same between Access and ITR", correct)


if __name__ == "__main__":
   main()

