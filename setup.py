import os
direc = input("Enter the directory that you want to install to: ")
try:
    os.chdir(direc + "/sherlock/sherlock")
except:
    os.chdir(direc)
    os.system("git clone https://github.com/sherlock-project/sherlock")
try:
    os.chdir(direc + "/nexfil")
except:
    os.chdir(direc)
    os.system("git clone https://github.com/thewhiteh4t/nexfil")
try:
    os.chdir(direc + "/maigret")
except:
    os.chdir(direc)
    os.system("git clone https://github.com/torerobo/maigret")
try:
    os.chdir(direc + "/social-analyzer")
except:
    os.chdir(direc)
    os.system("git clone https://github.com/qeeqbox/social-analyzer")
try:
    os.chdir(direc + "/Anubis")
except:
    os.chdir(direc)
    os.system("git clone https://github.com/jonluca/Anubis")
try:
    os.chdir(direc + "/nmap")
except:
    os.chdir(direc)
    os.system("git clone https://github.com/nmap/nmap")
    os.system("./configure")
    os.system("make")
    os.system("make install")
try:
    os.chdir(direc + "/holehe")
except:
    os.chdir(direc)
    os.system("git clone https://github.com/megadose/holehe")
    os.chdir(direc + "/holehe")
    os.system("python3 setup.py install")
try:
    os.chdir(direc + "/theHarvester")
except:
    os.chdir(direc)
    os.system("git clone https://github.com/laramies/theHarvester")
try:
    os.chdir(direc + "/Infoga")
except:
    os.system("git clone https://github.com/m4ll0k/Infoga")
try:
    os.chdir(direc + "/DaProfiler")
except:
    os.system("git clone https://github.com/daprofiler/DaProfiler")
os.chdir(direc + "/Piesint")
os.system("pip3 install -r reqs.txt")
