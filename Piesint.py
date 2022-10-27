import os
import scripts
print("__________.__              .__        __  ")
print("\______   \__| ____   _____|__| _____/  |")
print(" |     ___/  |/ __ \ /  ___/  |/    \   __\ ")
print("|    |   |  \  ___/ \___ \|  |   |  \  |  ")
print("|____|   |__|\___  >____  >__|___|  /__|  ")
print("                 \/     \/        \/      ")
attack = input("What are you researching? (user,email,site,ip,name) ")
if attack == "site":
    site = input("Enter the site: ")
    scripts.site(site)
elif attack == "user":
    user = input("Enter the user:")
    scripts.user(user)
elif attack == "email":
    email = input("Enter the email:")
    scripts.email(email)
elif attack == "ip":
    ip = input("Enter the ip:")
    scripts.ip(ip)
elif attack == "name":
    name = input("Enter the first name:")
    lname = input("Enter the last name:")
    scripts.name(name,lname)
