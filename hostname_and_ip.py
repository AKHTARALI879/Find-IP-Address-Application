import socket as sk

from telegram import VideoChatScheduled

my_hostname = sk.gethostname()
print("Your Hostname is: " + my_hostname)

# get IP Address
my_ip = sk.gethostbyname(my_hostname)
print("Your Network IP Address is: " + my_ip)

# name of website for geting ip
host = "insaf.pk"
# StandwithIMRANKHAN
# STANDFORJUSTICE
# fetch IP
ip = sk.gethostbyname(host)
print("The IP Address of " + host + " is: " + ip)
