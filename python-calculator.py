# Taschenrechner mit Auswahl der Rechenoperation

# Benutzer gibt zwei Zahlen ein
zahl1 = float(input("Gib die erste Zahl ein: "))
zahl2 = float(input ("Gib die zweite Zahl ein: "))

# Benutzer wählt die Rechenoperation
print("Welche Operation möchtest du durchführen?")
print("1: Addition (+)")
print("2: Subtraktion (-)")
print("3: Multiplikation (*)")
print("4: Division (/)")

wahl = input("Gib die Zahl der gewünschten Operation ein: ")

# Berechnung basierend auf der Auswahl
if wahl == "1" or wahl == "+":
    ergebnis = zahl1 + zahl2
elif wahl == "2" or wahl == "-":
    ergebnis = zahl1 - zahl2
elif wahl == "3" or wahl == "*":
    ergebnis = zahl1 * zahl2
elif wahl == "4" or wahl == "/":
    if zahl2 != 0:
        ergebnis = zahl1 / zahl2
    else:
        ergebnis = "Fehler: Division durch Null!"
else:
    ergebnis = "Ungültige Eingabe"

# Ergebnis ausgeben
print("Ergebnis:", ergebnis)

