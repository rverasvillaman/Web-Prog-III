import logging
import socket


def validate_password(password):
    ## contains uppercase?
    contains_uppercase = False
    contains_lowercase = False
    for i in password:
        if i.isupper():
            contains_uppercase = True
        if i.islower():
            contains_lowercase = True
    valid_password = len(password) >= 8 and len(password) <= 15 and contains_lowercase and contains_uppercase
    if not contains_lowercase:
        logging.info("Das PW enthält keinen Kleinbuchstaben")
    if not contains_uppercase:
        logging.info("Das PW enthält keinen Grossbuchstaben")
    if not (len(password) >= 8 and len(password) <= 15):
        logging.info("Das PW zu kurz/lang.")
    return valid_password


def create_account(list_of_users, salutation, first_name, last_name, username, password):
    user = {
        "salutation": salutation,
        "firstname": first_name,
        "lastname": last_name,
        "username": username,
        "password": password
    }
    list_of_users.append(user)
    return list_of_users


def login(list_of_users, username, password):
    for u in list_of_users:
        if u.get("username") == username and u.get("password") == password:
            return True
        else:
            hostname = socket.gethostname()
            ip = socket.gethostbyname(hostname)
            logging.info("Loginversuch mit user %s und PW %s IP Adresse %s fehlgeschlagen",username,password,ip)
            return False