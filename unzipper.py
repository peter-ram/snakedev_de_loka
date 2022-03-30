import zipfile

import sys

# month_string = "202202"
month_string = sys.argv[1]


def extractor(month_string):
    path = "datalake///JC-" + month_string + "-citibike-tripdata.csv.zip"
    
    # add line to check if zip file exists
    
    with zipfile.ZipFile(path,"r") as zip_ref:
        zip_ref.extractall("datalake//")
    
    print("unzipping finished")
    

extractor(month_string)


