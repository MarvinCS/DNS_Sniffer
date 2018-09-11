# DNS_Sniffer
A python3 based dns sniffing tool. Only works in public wifis

## Requirements
1. `sudo apt install python3 python3-pip python3-tk python3-pyqt4 net-tools tshark`
2. Make python3 default ([link](https://askubuntu.com/questions/320996/how-to-make-python-program-command-execute-python-3#answer-460578)): `sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 10` (Change /usr/bin/python3 to your destination)
3. Install Python libraries with pip: `pip install scapy sympy tldextract matplotlib` 

## Usage
1. Download or clone tis repository
1. (Edit the *config.json*) 
1. Run *main.py* with root permissions to scan a network
1. Run *main.py* to evaluate your results


## TODO
- gui options: 
  - subdomain radio button
  - db name 
