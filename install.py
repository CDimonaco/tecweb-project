from common.utils.auth import AuthManager
import os
from termcolor import colored
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
consolewidth = os.get_terminal_size().columns

def install():
    try:
        connection = MongoClient(serverSelectionTimeoutMS=50)
        connection.server_info()
    except ServerSelectionTimeoutError:
        print("Nessuna connessione al database termino il programma\n")
        return

    print("\n")
    print(colored("ANDRA INSTALLATION WIZARD".center(consolewidth),"red"))
    print("\n")
    print("github.com/cdimonaco/andra-be".center(consolewidth))
    print("Esame di Tecnologie web".center(consolewidth))
    print("Di Monaco Carmine 0124001236".center(consolewidth))
    print("\nCon questa procedura potrai creare il primo account amministratore del sistema\n")
    username = input("Inserisci username\n\n")
    password = input("Inserisci password\n\n")
    email = input("Inserisci email\n\n")
    scelta = input("ACCOUNT: Username: {0} Password: {1} Email: {2} confermi? (y,n)\n\n".format(username,password,email))
    if scelta == "y":
        newuser = AuthManager(connection.tecweb).register(username=username,password=password,email=email,role=1)
        print(colored("ACCOUNT CREATO, ID {0}".format(newuser).center(consolewidth),"green"))
    else:
        return

if __name__ == '__main__':
    install()