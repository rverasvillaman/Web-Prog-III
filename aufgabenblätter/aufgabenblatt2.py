#Aufgabe 1
print("hello world")
name="rob"
print(str(name))

#Aufgabe 2
numberOfCustomers = 10
stockOfApples = 50
stockOfSausages = 22
minStockOfApples = 50
minStockOfSausages = 22

customer = "Marry"
numberOfEntriesCartMarry = 0.0

#Marry buys 5 apples and 2 sausages
numberOfEntriesCartMarry += 5
numberOfEntriesCartMarry += 2
stockOfApples -= 5
stockOfSausages -= 2

print("Stock of apples: " + str(stockOfApples))
print("Stock of sausages: " + str(stockOfSausages))
print("Number od cart entries of Marry: " + str(numberOfEntriesCartMarry))

stockCheck = stockOfApples > minStockOfApples + 10
print(stockCheck)
print(numberOfEntriesCartMarry <= 7)
customer == "Marry"
print(type(numberOfEntriesCartMarry))

#Aufgabe 3
#3.1
pants1 = {
    "size": "short",
    "brand": "GUCCI",
    "color": "red",
    "price": 1099
}

pants2 = {
    "size": "long",
    "brand": "Levis",
    "color": "black",
    "price": 69.99
}

pants3 = {
    "size": "long",
    "brand": "Nike",
    "color": "white",
    "price": 119.99
}

shoe1 = {
    "brand": "Adidas",
    "color": "black",
    "purpose": "sport",
    "price": 79.99
}

shoe2 = {
    "brand": "Lebron",
    "color": "yellow",
    "purpose": "sport",
    "price": 79.99
}

shoe3 = {
    "brand": "Jack Wolfskin",
    "color": "brown",
    "purpose": "hiking",
    "price": 79.99
}

#3.2
#Besuch der PDP von Schuh1
print(shoe1)

#Drei Paar von Schuh 2 zum Warenkorb hinzufügen
cart = []
i = 0
while i <= 3:
    cart.append(shoe2)
    i = i + 1
print(cart)

#Besuch der PDP von Schuh 2
print(shoe2)

#Besuch der PDP von Schuh 3
print(pants3)

#3 mal 3 Hosen zum Warenkorb hinzufügen
j = 0
while j <= 3:
    cart.append(pants3)
    j = j + 1

#Besuch der Warenkorbseite
print("Warenkorb: " + str(cart))

#Entfernen des dritten Elements im Warenkorb
cart.pop(2)

#Besuch der Warenkorbseite
print("Warenkorb: " + str(cart))

#Aufgabe 4
cart4 = ["Tomate","Apfel","SchuhA","Wurst"]
if "Tomate" in cart4:
    print("Tomate wurde im Warenkorb gefunden.")
else:
    print("Tomate wurde nicht im Warenkorb gefunden.")

if "apfel" in cart4:
    print("apfel wurde im Warenkorb gefunden.")
else:
    print("apfel wurde nicht im Warenkorb gefunden.")

if "Apfel" in cart4:
    print("Apfel wurde im Warenkorb gefunden.")
else:
    print("Apfel wurde nicht im Warenkorb gefunden.")

if "Käse" in cart4:
    print("Käse wurde im Warenkorb gefunden.")
else:
    print("Käse wurde nicht im Warenkorb gefunden.")

if "Wein" in cart4:
    print("Wein wurde im Warenkorb gefunden.")
else:
    print("Wein wurde nicht im Warenkorb gefunden.")

if "Wurst" in cart4:
    print("Wurst wurde im Warenkorb gefunden.")
else:
    print("Wurst wurde nicht im Warenkorb gefunden.")



