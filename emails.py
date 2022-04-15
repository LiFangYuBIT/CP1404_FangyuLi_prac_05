emails = {}
email = input("Email: ")
while email.strip() != "":
    email_start = email.split('@')[0]
    parts = email_start.split('.')
    name = " ".join(parts).title()
    correct = input("Is your name {}? (Y/n) ".format(name))
    if correct.upper() != "Y" and correct.strip() != "":
        name = input("Name: ")
    emails[email] = name
    email = input("Email: ")

for email, name in emails.items():
    print("{} ({})".format(name, email))
