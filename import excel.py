###
#Importing data from excel
###

import numpy as np
import pandas as pd 

#Function which defines the filename
def define_file(dataname="SCADA"):
    if dataname=="SCADA":
        filename="190201_mGC.xlsx"
    
    return filename



ExcelRead = pd.read_excel(define_file("SCADA"))
type (ExcelRead)
print(ExcelRead)
