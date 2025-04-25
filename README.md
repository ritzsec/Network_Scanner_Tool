# Network_Scanner Tool 

## 🎯 Objective

The Network Scanner project is designed to scan a given IP range and identify active devices in the network by using the ARP protocol. This tool utilizes the Scapy library to send ARP requests to all IPs in the specified range and collects the responses with the associated IP and MAC addresses of the active devices.

### 🧠 Skills Learned

- Understanding of the ARP (Address Resolution Protocol) used in local network communication.
- Practical experience with the Scapy library for network packet crafting and analysis.
- Familiarity with network scanning and discovery techniques.
- Ability to identify devices in a network by analyzing MAC and IP addresses.

### 🛠 Tools Used

- **Scapy**: A powerful Python-based interactive packet manipulation program.
- **Ethernet Frame**: Used to send data over the network to identify active devices.
- **ARP Requests**: A protocol used to discover devices in a local network.

## 🛠 Step-by-Step Code Breakdown

### **Step 1**: Import Necessary Libraries.
Import Scapy's libraries: ARP for crafting **ARP** requests, **Ether** for creating Ethernet frames, and **srp** for sending packets and receiving responses.
```python
from scapy.all import ARP, Ether, srp
```

### **Step 2**: Define the Network Scanning Function
  - Define a function scan_network() that takes the IP range as input.
  - Create an ARP request and an Ethernet frame with the broadcast address (ff:ff:ff:ff:ff:ff).
```python
def scan_network(ip_range):
    # Create ARP request packet
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    print(f"Scanning {ip_range}... Please wait.")

```

### **Step 3**: Send the Packet and Capture Responses
Use **srp()** to send the crafted ARP request and collect responses within a 2-second timeout.
```python
    # Send the packet and receive responses
    result = srp(packet, timeout=2, verbose=False)[0]

```

### **Step 4**: Process and Display the Results
  - Iterate over the received responses, extracting the IP and MAC addresses.
  - Print the list of available devices in the network.
```python
       # Print out the results
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    print("\nAvailable Devices in the Network:")
    print("IP" + " "*18+"MAC")
    print("-"*40)
    for device in devices:
        print("{:16}    {}".format(device['ip'], device['mac']))
```

### **Step 5**: Main Code Execution
Ask the user for an IP range (e.g., **192.168.__.__/24**) and call the **scan_network()** function to start the scan.
```python
       if __name__ == "__main__":
    target_ip = input("Enter the IP range (e.g., 192.168.1.0/24): ")
    scan_network(target_ip)

```


## 🛠 File Structure
```
│
├── network_scanner.py  # Your Python script

```

## 📖 Overall Explanation 
```
The Network Scanner tool is designed to discover active devices in a local network by utilizing ARP (Address Resolution Protocol) requests. This tool helps users map out devices connected to their network by sending ARP requests to all IP addresses within a specified range. It then collects responses that include the IP and MAC addresses of active devices.

This is achieved by sending out Ethernet frames with ARP requests, and the tool listens for any responses from devices that are reachable within the given IP range. The results are then displayed in a clean format showing the IP and MAC addresses of all the available devices on the network.

The tool uses the Scapy library, a powerful Python library used for network packet crafting and analysis, to automate the process of scanning the network. By utilizing ARP requests, it helps identify devices in the network even without knowing the specific IP addresses of the devices, which is useful for network auditing and discovery tasks.

```
## ⚠️ Disclaimer

This tool is intended for educational and authorized testing purposes only.
Do not use it to scan networks or devices without explicit permission.
Unauthorized scanning of networks can be illegal and unethical.


## 👤 Author

Made with curiosity and caffeine ☕  
**Gumbo**  
[GitHub Profile](https://github.com/your-username)
