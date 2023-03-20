import logging
logging.basicConfig(filename="./helloworld.log",encoding="utf-8",level=logging.INFO,format="%(levelname)s: %(asctime)s %(message)s")

userinput = input("Bitte eine Zahl: ")
logging.info("User hat eine Eingabe getätigt. %s",userinput)

try:
    print("Die Multiplikation der Eingabe beträgt:" + userinput*userinput)
except TypeError as t:
    logging.warning("Ihre Eingabe kann nicht verarbeitet werden, da der falsche Datentyp verwendet wird.")
print("Das wird nach der Exception ausgeführt.")