###
#Importing data from excel
###

import numpy as np
import pandas as pd 

#Function which defines the filename
def define_file(dataname="GC"):
    if dataname=="GC":
        filename="190201_mGC.xlsx"
    
    #we need to define the other filenames
    #SCADA
    #GC Inferno
    #SPA
    #GCs
    #logging
    return filename

#we need to create the collect_data function

#ExcelRead = pd.read_excel(define_file("GC"))
#type (ExcelRead)
#print(ExcelRead)
