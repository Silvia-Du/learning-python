#creare una nuova directory = results
#conto dei bite dei file
#ignorare ogni altra directory
# creare un text file dentro questa directory
#scriverci dentro tutta la lista di file della core directory
#os.mkdir = x creare una directory, os.listdir()

#importo os
import os

# ho la lista dei file
dirlist = os.listdir()

#calcolo la somma dei bytes
totalbytes = 0
for i in dirlist:
  if os.path.isfile(i):
    filesize = os.path.getsize(i)
    totalbytes += filesize 


# #creo la directory
# os.mkdir("results")


#apro la directory in modalità scrittura
resultsfile = open("results/results.txt", "w+")
if resultsfile.mode == "w+":
#se è in modalità scrittura ci scrivo i bytes e la lista

  print("Total bytecount: " + str(totalbytes) + "\n")
  print("file list: \n")

  for i in dirlist:
    if os.path.isfile(i):
      resultsfile.write(i + "\n")

#chiudo il file quando ha finito
resultsfile.close()






