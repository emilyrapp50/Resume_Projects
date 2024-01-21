#WiFi MAC address return

from scapy.all import ARP, Ether, srp

#User enter IP
ip = input("Please enter an IP address: ")

#Define ARP & Ethernet variables
arp = ARP(pdst=ip)
ethernet = Ether(dst="ff:ff:ff:ff:ff:ff")

#Combine Ether & ARP pkts
packet = ethernet/arp

#Send pkt & recieve response
result = srp(packet, timeout=15, verbose=0)[0]

#Check for response
if result: 
    mac = result[0][1].hwsrc
    print("MAC:", mac)
else: 
    print("No response received.")
    

#End WiFi MAC addr
#A moment of silence...
print("Printing ARP table...")
import time
t = 5
time.sleep(t)
#ARP -a return
    
import subprocess

def get_arp_table():
    try:
        # Run the 'arp -a' command and capture the output
        result = subprocess.check_output(['arp', '-a'], universal_newlines=True)
        return result
    except subprocess.CalledProcessError as e:
        print(f"Error executing 'arp -a': {e}")
        return None
# Get and print the ARP table
arp_table = get_arp_table()

if arp_table:
    print("ARP Table:")
    print(arp_table)

#End ARP -a return