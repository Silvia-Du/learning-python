#
# Example file for working with os.path module
# LinkedIn Learning Python course by Joe Marini
#

import os  #operation sistem
from os import path  
import datetime
from datetime import date, time, timedelta
import time


def main():
    # Print the name of the OS
    print(os.name)  #stampa il nome dell'operation sistem ===> nt = internaly(x windows)

    
    # Check for item existence and type
    print("item exists", str(path.exists("textfile.txt")))#check se esiste
    print("item is a file", path.isfile("textfile.txt"))#se è un file
    print("item is a directory", path.isdir("textfile.txt"))#se è una directory

    
    # # Work with file paths
    print("item is a path:", path.realpath("textfile.txt")) #C:\Users\silvi\Documents\BOOLEAN\PYTHON\learning-python\Ch3 - Files\textfile.txt
    print("item's path and name", path.split(path.realpath("textfile.txt"))) #split per separare il name del file dal path ===>C:\\Users\\silvi\\Documents\\BOOLEAN\\PYTHON\\learning-python\\Ch3 - Files', 'textfile.txt'

    
    # Get the modification time  ==> modificare il file modification time  ==>time è una classe
    t= time.ctime(path.getmtime("textfile.txt")) # geltmtime = get the modification time
    print(t)   #===> Tue Nov 29 09:58:53 2022
    print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))   #===> 2022-11-29 09:58:53.266816
    #due modi diversi per avere il m-time , il secondo attraverso il time stamp

    
    # Calculate how long ago the item was modified
    td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
    #prendo il time di adesso e gli sottraggo il modification time
    print("ti has been ", td, "since the file was modified")
    print("Or, ", td.total_seconds(), "seconds")

  
if __name__ == "__main__":
    main()
