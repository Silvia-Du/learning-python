#
# Example file for working with loops
# LinkedIn Learning Python course by Joe Marini
#


def main():
    x = 0

    # TODO: define a while loop
    while( x < 5 ):
        print(x)
        x = x + 1

    # TODO: define a for loop

    for x in range(5, 10):
        print(x)
        # l'output qui è 5, 6...9 
        #dove x è l'iterato e range è la funzione che dice da dove a dove(esclude l'ultimo==> il 10 nn viene stampato)


    # TODO: use a for loop over a collection

    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    for d in days:
        print(d)
        #esegue l'iterazione sugli elemnti della collection


    # TODO: use the break and continue statements
    for x in range(5, 10):
        if x == 7:
            break   #===> break rompe l'iterazione (qui al verificarsi di una condizione ps: qui il 7 ovvimente nn viene stampato)
        if x % 2 == 0:
            continue  #===> skippa il resto del codice dentro il loop (in questo caso solo il print, l'output sarà: 5, 7, 9)
        print(x)


    # TODO: using the enumerate() function to get index 

    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    for i,d in enumerate(days) :   # enumerate è una funzione che ritorna nn solo il valore dell'elemento ma anche il suo indice all'interno dell'array
        print( i, d )  # l'output sarà : 0 Mon, 1 Tue ect... 

    
  
if __name__ == "__main__":
    main()
