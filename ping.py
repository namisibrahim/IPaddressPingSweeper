##################################################
# File Name				 : Ping.py	             #
# Author				 : Namis Mohamed Ibrahim #
# Date of Development	 : 1st April 2022		 #
##################################################

import subprocess

net = input("Enter the IP address in a dotted decimal format (x.x.x.x) : ")     # Storing User's IP address input as variable "net"
netsplit = net.split('.')                                                       # Splitting the "net" string variable into a list using "." as separator
netadd = netsplit[0] + "." + netsplit[1] + "." + netsplit[2] + "."              # Combining first three elements of list with "." to make up the network portion of IP address

st1 = int(input("Enter the Starting host Number: "))                            # Storing Starting host number as integer variable "st1"
en1 = int(input("Enter the ending host Number: "))                              # Storing ending host number as integer variable "en1"


for host in range(st1,en1+1):                                                   # Using for loop to calculate range for all combinations of addresses
    addr = netadd + host                                                        # Deriving addresses by combining network portion of IP address with host numbers
    result=subprocess.call(['ping','-n', '1', addr])                            # Pinging addresses and assigning results to variable "result"
    if result == 0:                                                             # If result has the value of 0, Ping process successful 
        print( "ping to", addr, "OK")                                           # Displays Successful message
    elif result == 2:                                                           # If result has the value of 2, No response from the address
        print("no response from", addr)                                         # Displays No response message
    else:                                                                       # Any other value for result, ping has failed
        print("ping to", addr, "failed!")                                       # Displays Failed message
