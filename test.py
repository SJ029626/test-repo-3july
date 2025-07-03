import os

def run_ping(host):
    os.system("ping -c 4 " + host)

# Example usage
user_input = input("Enter a hostname to ping: ")
run_ping(user_input)
