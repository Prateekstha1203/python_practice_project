import random;

print("Welcome to my computer quiz!")

playing = input("Do you want to play (y/n)?  ")
name = input("What is the name? ")
if playing != "y" and playing != "yes":
    quit()

print("Let's play! 😄")

full_forms = {
    "CPU": "Central Processing Unit",
    "RAM": "Random Access Memory",
    "ROM": "Read-Only Memory",
    "GPU": "Graphics Processing Unit",
    "HDD": "Hard Disk Drive",
    "SSD": "Solid State Drive",
    "LAN": "Local Area Network",
    "WAN": "Wide Area Network",
    "HTTP": "HyperText Transfer Protocol",
    "HTTPS": "HyperText Transfer Protocol Secure",
    "USB": "Universal Serial Bus",
    "BIOS": "Basic Input/Output System",
    "OS": "Operating System",
    "FTP": "File Transfer Protocol",
    "SMTP": "Simple Mail Transfer Protocol",
    "IP": "Internet Protocol",
    "DNS": "Domain Name System",
    "URL": "Uniform Resource Locator",
    "WWW": "World Wide Web",
    "HTML": "HyperText Markup Language",
    "CSS": "Cascading Style Sheets",
    "JS": "JavaScript",
    "PHP": "Hypertext Preprocessor",
    "SQL": "Structured Query Language",
    "API": "Application Programming Interface",
    "IDE": "Integrated Development Environment",
    "P2P": "Peer-to-Peer",
    "GUI": "Graphical User Interface",
    "CLI": "Command Line Interface",
    "DOS": "Disk Operating System",
    "VPN": "Virtual Private Network",
    "MAC": "Media Access Control",
    "JSON": "JavaScript Object Notation",
    "XML": "eXtensible Markup Language",
    "SSH": "Secure Shell",
    "TLD": "Top-Level Domain",
    "NIC": "Network Interface Card",
    "ISP": "Internet Service Provider",
    "DOS": "Denial of Service",
    "CAD": "Computer-Aided Design",
    "CAM": "Computer-Aided Manufacturing",
    "VGA": "Video Graphics Array",
    "DVI": "Digital Visual Interface",
    "HDMI": "High-Definition Multimedia Interface",
    "SATA": "Serial Advanced Technology Attachment",
    "RAID": "Redundant Array of Independent Disks",
    "DNS": "Domain Name System",
    "DHCP": "Dynamic Host Configuration Protocol",
    "ICMP": "Internet Control Message Protocol",
    "SSL": "Secure Sockets Layer"
}

count = 0

random_keys = random.sample(list(full_forms.keys()),10)


for keys in random_keys:
  
    answer = input(f"What does {keys} stands for? ")
    if answer.lower() == full_forms[keys].lower():
       count += 1

print(f"Hey {name}! you have got {count} out of  {len(random_keys)}" );
