from cryptography.fernet import Fernet

# Diese Funktion darf nur beim ersten mal ausgeführt werden. Danach auskommentieren!
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("Was lautet das Masterpasswort? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
        data = (line.rstrip())
        user, passw = data.split("|")
        print("User:", user, "| Passwort", fer.decrypt(passw.encode()).decode())

def add():
    name = input("Account Name: ")
    pwd = input("Passwort: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "/n")

while True:
    mode = input("Möchtest du ein neues Passwort hinzufügen (add) oder ein vergebenes Passwort anschauen (see)? q beendet das Programm) ").lower()
    if mode == "q":
        break
    if mode == "see":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
