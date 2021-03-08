# Problem 1 - Leap year
# A leap year is a year that experiences the addition of one day with the aim of adjusting the date to the astronomical year. In one year not exactly consists of 365 days, but 365 days 5 hours 48 minutes 45.1814 seconds. If this is ignored, then every four years will be deficient almost 1 day. So to compensate for this, every 4 years, given 1 extra day: February 29th.

# Create a python file (.py) that can receive input from the user that can determine an input from the user classified as a leap year or not. When the file is executed, the user is asked to enter a certain number of years, then a result will appear that states that the user input is classified as a leap year or not. Example expected result: (Use Gregorian Dating System)

# Input tahun : 2019
# Hasil : BUKAN TAHUN KABISAT

# Input tahun : 2020
# Hasil : TAHUN KABISAT

print("======Cara 1 ======")

try:
    year = int(input("Masukan Tahun:"))
    if (year % 4) == 0: 
        if (year % 100) == 0:
            if (year % 400) == 0:
                print("Tahun merupakan Tahun Kabisat")
            else:
                "Bukan merupaka tahun Kabisat"
        else:
            print("Bukan merupakan tahun Kabisat")
    else:
        print("Bukan Kabisat")
except:
    print("Hanya Menerima integer")


print("======Cara 2 ======")
def tahun_Kabisat():
    try:
        tahun = input("Maukan Tahun:")
        for i in tahun.isalpha == True:
            tahun = tahun % 400 == 0
            return "Bukan tahun Kabisat"
            if tahun1 != tahun % 400 or tahun % 100 == 0:
                return "Tahun tersebut bukan tahun Kabisat"
            elif tahun != tahun % 4 == 0:
                return "Tahun tersebut bukan tahun Kabisat"
            else:
                return "Tahun tersebut merupakan Tahun Kabisat"

    except:
        return "Maaf tidak menerima selain Numerik" 

print(tahun_Kabisat())