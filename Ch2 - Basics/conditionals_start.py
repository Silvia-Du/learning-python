#
# Example file for working with conditional statements
# LinkedIn Learning Python course by Joe Marini
#



def main():
    x, y = 10, 100

    # if x < y:
    #     result = "x è maggiore"
    # else:
    #     result = "y è maggiore"
    # print(result) 

    # se non metto l'else mi darà errore perchè result è dichiarata dentro l'if pertanto non esisterebbe se y è maggiore di x
    # se x e y fossero uguali darebbe un risultato sbagliato quindi::


    # conditional flow uses if, elif, else
    # if x < y:
    #     result = "x è maggiore"
    # elif x == y:
    #     result = "sono uguali"
    # else:
    #     result = "y è maggiore"
    # print(result) 

    # conditional statements let you use "a if C else b"
    # result = "x è piu piccolo di y" if x < y else "x è uguale o maggiore di y"
    # print(result)

    # match-case makes it easy to compare multiple values
    value = "four"
    match value:
        case "one":
            result = 1
        case "two":
            result = 2
        case "three"| "four":
            result = (3, 4)
        case _:   #===> così è il default(se nn è una delle altre)
            result = -1
    print(result)


if __name__ == "__main__":
    main()
