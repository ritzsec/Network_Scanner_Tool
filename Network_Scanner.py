#Network_Scanner

# Importing necessary libraries from Scapy
from scapy.all import ARP, Ether, srp

# Function to scan the network for active devices using ARP requests
def scan_network(ip_range):
    # Step 1: Create ARP request packet for the provided IP range
    arp = ARP(pdst=ip_range)  # ARP request targeting the IP range
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")  # Ethernet frame with broadcast MAC address
    packet = ether / arp  # Combine Ethernet frame and ARP request

    print(f"Scanning {ip_range}... Please wait.")

    # Step 2: Send the packet and wait for the responses
    result = srp(packet, timeout=2, verbose=False)[0]  # Send the packet and capture responses

    # Step 3: Process and print the results
    devices = []  # List to hold devices with IP and MAC addresses
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})  # Store IP and MAC

    print("\nAvailable Devices in the Network:")
    print("IP" + " "*18 + "MAC")
    print("-"*40)
    for device in devices:
        print("{:16}    {}".format(device['ip'], device['mac']))  # Display devices' IP and MAC

# Main code block that executes when the script is run
if __name__ == "__main__":
    # Step 4: User input for IP range and scanning the network
    target_ip = input("Enter the IP range (e.g., 192.168.1.0/24): ")
    scan_network(target_ip)  # Start network scan for the provided range
