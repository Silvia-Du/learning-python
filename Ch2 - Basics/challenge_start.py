#chiedre all'utente se vuole uscire o giocare
#se la parola è exit dare feedback di uscita avvenuta 
#se è qualunque altra cosa parte una funzione
#nella funzione trovo qualcosa come split e rimuovi spazi, la trimmo e la ciclo, se uno non è alfanumerico la elimino.

#funz per verificare palindromità..
def is_palindrome(tester):
  if tester == tester[::-1]:
    return True
  return False

#init
def main():

  run = True
  while(run):
    tester = input("Enter string to test for palindrome or 'exit':")

    #verifica condizione d'uscita
    if tester.lower() == "exit":
      print("arrivederci")
      run = False
      break
    
    tester = tester.lower()

    newstr = ""
    for l in tester:
      if l.isalnum():
        newstr += l
    
    print("palindrome test:", is_palindrome(newstr))

if __name__ == "__main__":
    main()