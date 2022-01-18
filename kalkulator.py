import logging
logging.basicConfig(level=logging.DEBUG)

print("Kalkulator")
action = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
if action == "1":
    data1 =float(input (" Podaj składnik 1 "))
    data2 = float(input (" Podaj składnik 2 "))
    print("Dodaję %s i %s" % (data1, data2))
    print("Wynik to", data1 + data2)
if action == "2":
    data1 = float(input (" Podaj składnik 1 "))
    data2 = float(input (" Podaj składnik 2 "))
    print("Odejmuję %s i %s" % (data1, data2))
    print("Wynik to", (data1 - data2))
if action == "3":
    data1 = float(input (" Podaj składnik 1 "))
    data2 = float(input (" Podaj składnik 2 "))
    print("Mnożę %s i %s" % (data1, data2))
    print("Wynik to", (data1 * data2))
if action == "4":
    data1 = float(input (" Podaj składnik 1 "))
    data2 = float(input (" Podaj składnik 2 "))
    print("Dzielę %s i %s" % (data1, data2))
    print("Wynik to", (data1 / data2))