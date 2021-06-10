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
 # ITR['InteranlID'] = ITR['InternalID'].astype(int)



def main():
  inv = pd.read_csv("Inventory.csv")
  itr = pd.read_csv("Hardware.KitchenSink.csv")

  fix_NaN(inv, itr)

  access = inv['ITR'].astype(str)
  ITRDB = itr['InternalID'].astype(str)
 
  # add getting the serial columns from each one
  found = 0

  print(access.dtypes)
  print(ITRDB.dtypes)

  for i, r1 in enumerate(access.values):
    for j, r2  in enumerate(ITRDB.values):
      if r1 == r2:
       found = found + 1
       print(r1, r2)
  print(found)


if __name__ == "__main__":
   main()

