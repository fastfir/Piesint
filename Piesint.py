import os
import scripts
print("__________.__              .__        __  ")
print("\______   \__| ____   _____|__| _____/  |")
print(" |     ___/  |/ __ \ /  ___/  |/    \   __\ ")
print("|    |   |  \  ___/ \___ \|  |   |  \  |  ")
print("|____|   |__|\___  >____  >__|___|  /__|  ")
print("                 \/     \/        \/      ")
attack = input("What are you researching? ")
if attack == "site":
    site = input("Enter the site: ")
    scripts.site(site)
elif attack == "user":
    user = input("Enter the user:")
    scripts.user(user)
elif attack == "email":
    email = input("Enter the email:")
    scripts.email(email)

