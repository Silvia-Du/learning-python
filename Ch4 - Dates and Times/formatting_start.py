#
# Example file for formatting time and date output
# LinkedIn Learning Python course by Joe Marini
#


from datetime import datetime

def main():
    # Times and dates can be formatted using a set of predefined string
    # control codes 
    now = datetime.now()
    
    #### Date Formatting ####
    
    # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
    print(now.strftime("The current year is: %Y")) #prende datetime now e trasforma la porzione richiesta in stringa ===> 2022
    print(now.strftime("%a, %d, %B, %y")) # ===> Tue, 29, November, 22

    # %c - locale's date and time, %x - locale's date, %X - locale's time
    print(now.strftime("local date and time: %c")) # ==> Tue Nov 29 14:26:53 2022
    print(now.strftime("local date: %x")) # ==> 11/29/22
    print(now.strftime("local time: %X")) # ==> 14:26:53


    #### Time Formatting ####
    
    # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
    print(now.strftime("Current time: %I : %M: %S %p"))  # ==> 02 : 29: 56 PM
    print(now.strftime("24-hour time: %H : %M")) # ==> 14 : 29
  

if __name__ == "__main__":
    main()
