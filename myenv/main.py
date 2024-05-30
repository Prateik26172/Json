import json

# Load JSON data from a file
with open('', 'r') as file:
    data = json.load(file)

# Access data
print(data['name'])

# Modify data
data['age'] = 30

# Save JSON data to a file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)
