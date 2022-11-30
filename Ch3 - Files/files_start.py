#
# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini
#


def main():  
    # Open a file for writing and create it if it doesn't exist
    # nomeCheDo = open("nomeDelFile.txt", openMode = l'acceso che voglio ai file)

    myfile = open("textfile.txt", "w+") 
    # w = (w= crea un nuovo file, o overrida tutto da uno che gia esiste)voglio il write access al file ===> + dice a python se nn esite crealo

    
    # Open the file for appending text to the end
    myfile = open("textfile.txt", "a+") #==>a= appende testo al file



    # # write some lines of data to the file
    for i in range(10):
        myfile.write("testoooooo nuovoooo\n")
    
    # # close the file when done
    myfile.close()
    
    # Open the file back up and read the contents
    myfile = open("textfile.txt", "r") # ===> r = per leggere i file
    if myfile.mode == 'r': #dice se il file è aperto correttamente
        # contents = myfile.read()
        # print(contents)

        fl = myfile.readlines()  #fl = file line
        for x in fl:
            print(x)


    
if __name__ == "__main__":
    main()
