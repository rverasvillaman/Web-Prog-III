#Aufgabe1

userinput = input("Wollen Sie wirklich einen Account anlegen?")
if userinput == "j" or userinput == "ja":
    salutation = input("Wie ist Ihre Anrede?")
    first_name = input("Wie ist Ihr Vorname?")
    last_name = input("Wie ist Ihr Nachname?")
    username = input("Wie ist Ihr Username?")
    pw = input("Wie ist Ihr Passwort?")
    contains_uppercase = False
    contains_lowercase = False
    for i in pw:
        if i.isupper():
            contains_uppercase = True
        elif i.islower():
            contains_lowercase = True

    if len(pw) >= 8 and len(pw) <= 15 and contains_uppercase and contains_lowercase:
        user = {
            "salutation": salutation,
            "firstname": first_name,
            "lastname": last_name,
            "username": username,
            "password": pw
        }
        confirm = input(f"Vielen Dank. Stimmen Ihre Daten so? (j/ja/n/nein) {user}")
        if confirm == "j" or confirm == "ja":
            print("Ok, wir haben den Account für Sie angelegt")
        else:
            print("Ok, wir legen nichts für Sie an. Bis bald")
    else:
        print("Das Passwort erfüllt die Kriterien nicht")


elif userinput == "n" or userinput == "nein":
    print("Ok, bis dann!")
else:
    print("Leider habe ich Ihre Eingabe nicht verstanden.")

#Aufgabe 2
userinput = input("Wollen Sie wirklich einen Account anlegen?")
if userinput == "j" or userinput == "ja":
    salutation = input("Wie ist Ihre Anrede?")
    first_name = input("Wie ist Ihr Vorname?")
    last_name = input("Wie ist Ihr Nachname?")
    username = input("Wie ist Ihr Username?")
    goon = True
    while goon:
        pw = input("Wie ist Ihr Passwort?")
        contains_uppercase = False
        contains_lowercase = False
        for i in pw:
            if i.isupper():
                contains_uppercase = True
            elif i.islower():
                contains_lowercase = True

        if len(pw) >= 8 and len(pw) <= 15 and contains_uppercase and contains_lowercase:
            user = {
                "salutation": salutation,
                "firstname": first_name,
                "lastname": last_name,
                "username": username,
                "password": pw
            }
            goon = False
        else:
            print("Das Passwort erfüllt die Kriterien nicht")
    confirm = input(f"Vielen Dank. Stimmen Ihre Daten so? (j/ja/n/nein) {user}")
    if confirm == "j" or confirm == "ja":
        print("Ok, wir haben den Account für Sie angelegt")
    else:
        print("Ok, wir legen nichts für Sie an. Bis bald")
elif userinput == "n" or userinput == "nein":
    print("Ok, bis dann!")
else:
    print("Leider habe ich Ihre Eingabe nicht verstanden.")

#Aufgabe 3
userinput = input("Wollen Sie wirklich einen Account anlegen?")
if userinput == "j" or userinput == "ja":
    salutation = input("Wie ist Ihre Anrede?")
    first_name = input("Wie ist Ihr Vorname?")
    last_name = input("Wie ist Ihr Nachname?")
    username = input("Wie ist Ihr Username?")
    goon = True
    while goon:
        pw = input("Wie ist Ihr Passwort?")
        contains_uppercase = False
        contains_lowercase = False
        for i in pw:
            if i.isupper():
                contains_uppercase = True
            elif i.islower():
                contains_lowercase = True

        if len(pw) >= 8 and len(pw) <= 15 and contains_uppercase and contains_lowercase:
            user = {
                "salutation": salutation,
                "firstname": first_name,
                "lastname": last_name,
                "username": username,
                "password": pw
            }
            goon = False
        else:
            print("Das Passwort erfüllt die Kriterien nicht")
    confirm = input(f"Vielen Dank. Stimmen Ihre Daten so? (j/ja/n/nein) {user}")
    if confirm == "j" or confirm == "ja":
        print("Ok, wir haben den Account für Sie angelegt")
    else:
        print("Ok, wir legen nichts für Sie an. Bis bald")
elif userinput == "n" or userinput == "nein":
    print("Ok, bis dann!")
else:
    print("Leider habe ich Ihre Eingabe nicht verstanden.")