from pwn import *

def setup():
	hostname = str(input("Enter hostname: "))

	if "\n" in hostname:
		hostname = hostname.split("\n")[0]

	for i in range (0, 100):
		try:
			port = int(input("Port: "))
			break
		except:
			print("Please enter a number")
			
			
			
	print("Execute code below (return a string to send to the server) ")

	caseword = input("Enter an execution key: ")

	function_start = "def return_value():"

	print("> " + function_start)

	execution_str = function_start + "\n"
	while True:
		current_line = input("> ")
		
		if current_line == caseword:
			print("Executing...")
			print(execution_str)
			break
		execution_str = execution_str + current_line + "\n"
		
		
	exec(execution_str)
	print(return_value())
	
	return True

	
def conn_and_exec(hostname, port, r):



	try:
		print(r.recv().decode())
	except:
		print("Something went wrong")

	try:
		print(r.recv().decode())
	except:
		print("Something went wrong")
		

	

