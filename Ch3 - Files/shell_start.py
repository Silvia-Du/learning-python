#
# Example file for working with filesystem shell methods
# LinkedIn Learning Python course by Joe Marini
#

import os
from os import path
import shutil #per copiare i file
from shutil import make_archive
from zipfile import ZipFile

def main():
    # make a duplicate of an existing file

    if path.exists("textfile.txt.bak"):   #==> verifico che il file esista,

        # get the path to the file in the current directory
        src = path.realpath("textfile.txt") # src = source variable ===> prendo il path

        # let's make a backup copy by appending "bak" to the name
        dst =  src + ".bak" # dst= destinazione
        shutil.copy(src, dst) #cosa copio, dove
        
        # rename the original file
        os.rename("textfile.txt", "newfile.txt") #original file da rinominare, il nome nuovo
        
        # now put things into a ZIP archive
        root_dir, tail = path.split(src)
        shutil.make_archive("archive", "zip", root_dir) #(nomeCheDoAll'Archivio, il formato, di che cosa)

        # more fine-grained control over ZIP files

        #creo variabile newzip con classe ZipFile
        with ZipFile("testzip.zip", "w") as newzip:  #(cosacreo, tipo di accesso) # with ===> crea un local scopeche semplifica il lavoro con gli oggetti
            #aggiungo manualmente il file 
            newzip.write("newfile.txt")
            newzip.write("textfile.txt.bak")

      
if __name__ == "__main__":
    main()
