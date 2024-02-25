# Advanced-Python-Backdoor
his repository contains an advanced Python backdoor capable of establishing a covert communication channel between an attacker and a victim machine. The backdoor consists of two main components: attacker.py and backdoor.py, each serving distinct roles in the operation.

**Components:**
1. attacker.py
The attacker script serves as the server-side component, designed to run on the attacker's machine.
It establishes a socket connection and listens for incoming connections from the victim.
Key features include:
Bidirectional communication with the victim machine.
Ability to execute shell commands on the victim's system.
File transfer capabilities (upload and download files).
Communication is encrypted using JSON serialization and Base64 encoding.
2. backdoor.py
The backdoor script is deployed on the victim machine.
It continuously attempts to establish a connection with the attacker's server.
Once connected, it provides a shell interface, allowing the attacker to execute commands on the victim's system remotely.
Additional functionalities include file upload and download.
The script ensures persistence by copying itself to a designated location and adding a registry key for automatic execution upon system startup.

**Usage:**
Clone the repository to your local machine.
Run attacker.py on your system.
Deploy backdoor.py on the target machine.
Once the victim machine connects to the attacker's server, you can issue commands and interact with the victim's system remotely.

Disclaimer:
This backdoor script is provided for educational purposes only. Unauthorized use of this code for malicious intent is strictly prohibited. The author shall not be responsible for any damage caused by the misuse of this software.
