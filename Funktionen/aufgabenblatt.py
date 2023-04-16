from aufgabenblattfunktionen import *

def run():
    logging.basicConfig(filename="./logging.log",level=logging.INFO, format="%(levelname)s: %(asctime)s %(message)s")
    further_user = True
    users = []
    while further_user:
        try:
            userinput = input("Wollen Sie sich einloggen oder registrieren?")
            if userinput == "r" or userinput == "registrieren":
                userinput = input("Wollen Sie wirklich einen Account anlegen?")
                if userinput == "j" or userinput == "ja":
                    salutation = input("Wie ist Ihre Anrede?")
                    first_name = input("Wie ist Ihr Vorname?")
                    last_name = input("Wie ist Ihr Nachname?")
                    username = input("Wie soll der Benutzername lauten?")
                    goon = True
                    while goon:
                        pw = input("Wie soll das Passwort lauten?")
                        valid_password = validate_password(pw)
                        if valid_password:
                            users = create_account(list_of_users=users, salutation=salutation,
                                                   first_name=first_name, last_name=last_name, username=username,
                                                   password=pw)
                            goon = False
                        else:
                            print("Ihr Passwort erfüllt die geforderten Kriterien nicht. Geben Sie es erneut ein")
                elif userinput == "n" or userinput == "nein":
                    print("ok. Auf Wiedersehen")
                else:
                    print("Ich verstehe Ihre Eingabe nicht")
            elif userinput == "l" or userinput == "login":
                username = input("Ihr Benutzername:")
                pw = input("Ihr Passwort:")
                found = login(users, username, pw)
                if found:
                    print("Sie wurden erfolgreich eingeloggt")
                else:
                    print("Die eingegeben Daten sind falsch.")
            elif userinput == "stop":
                print("Auf Wiedersehen")
                further_user = False
            else:
                print("Ich habe Ihre Eingabe nicht verstanden.")
        except (TypeError,MemoryError):
            logging.error("Es gab ein Problem.")

run()