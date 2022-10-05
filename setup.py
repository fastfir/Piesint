import os
direc = input("Enter the directory that you want to install to: ")
try:
    os.chdir(direc + "/sherlock/sherlock")
except:
    os.system("git clone https://github.com/sherlock-project/sherlock")
try:
    os.chdir(direc + "/nexfil")
except:
    os.system("git clone https://github.com/thewhiteh4t/nexfil")
try:
    os.chdir(direc + "/maigret")
except:
    os.system("git clone https://github.com/torerobo/maigret")
try:
    os.chdir(direc + "/social-analyzer")
except:
    os.system("git clone https://github.com/qeeqbox/social-analyzer")
try:
    os.chdir(direc + "/Anubis")
except:
    os.system("git clone https://github.com/jonluca/Anubis")
try:
    os.chdir(direc + "/nmap")
except:
    os.system("git clone https://github.com/nmap/nmap")
    os.system("./configure")
    os.system("make")
    os.system("make install")
try:
    os.chdir(direc + "/holehe")
except:
    os.system("git clone https://github.com/megadose/holehe")
try:
    os.chdir(direc + "/theHarvester")
except:
    os.system("git clone https://github.com/laramies/theHarvester")
