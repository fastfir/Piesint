import os
drt = os.path.expanduser("~")
print(drt)
def site(site):
    os.chdir(drt + "/Anubis")
    os.system("anubis -t " + site)
    os.chdir(drt + "/nmap")
    os.system("/nmap -oX /home/fastfir/nmap.xml -Pn " + site)
def user(user):
    os.chdir(drt + "/sherlock/sherlock")
    os.system("python3 sherlock.py " + user)
    os.chdir(drt + "/nexfil")
    os.system("python3 nexfil.py " + user)
    os.chdir(drt + "/maigret")
    os.system("go run maigret.go " + user)
    os.chdir(drt + "/social-analyzer/pip-social-analyzer/social-analyzer")
    os.system("python3 -m social-analyzer --username " + user + " --metadata --top100")
def email(email):
    os.chdir(drt + "/holehe")
    os.system("holehe " + email)
    os.chdir(drt + "/Infoga")
    os.system("python3 infoga.py --info " + email + " -v 3")
    os.chdir(drt + "/theHarvester")
    domain = email.split("@",1)
    domain = domain[1]
    os.system("python3 theHarvester.py -d " + domain + " -b all")
def ip(ip)
    os.chdir(drt + "/nmap")
    os.system("./nmap -oX " + drt + "/nmap.xml -Pn " + ip)
    
