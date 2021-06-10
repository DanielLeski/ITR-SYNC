import numpy as np
import pandas as pd
import time
import sys

def fix_NaN(inventory, ITR):
  #Iventory checks
  inventory.fillna(0, inplace=True)
  inventory['ITR'] = inventory['ITR'].astype(int)
  inventory['Student_Number']= inventory['Student_Number'].astype(int)
  
  #ITR Checks
  ITR.fillna(0, inplace=True)




def main():
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
      if r1 == r2:
        found = found + 1
        print(i, r1, " ", j, r2)
        access_index.append(i)
        ITR_index.append(j)
  



 # for m in access_index:
  #  for k in ITR_index:
   #   print(m, k)


  print("How many matches were found within ITR and InteralID #'s : ", found)



if __name__ == "__main__":
   main()

