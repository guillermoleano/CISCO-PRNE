import re # Regular expression module for pattern matching

pattern = "GigabitEthernet[1-4]" # Define the pattern to search for
interface = 'interface GigabitEthernet2 ip address 10.11.0.1 255.255.255.0' # Example interface string
result = re.search(pattern, interface) # Search for the pattern in the interface string

print(result)

