import json

# Load JSON data from the file
with open('sample-data.json') as file:
    data = json.load(file)

# Open a new file to write the output
with open('output.txt', 'w') as output_file:
    # Write the header
    output_file.write("Interface Status\n")
    output_file.write("=" * 80 + "\n")
    output_file.write("{:<50} {:<20} {:<10} {:<5}\n".format("DN", "Description", "Speed", "MTU"))
    output_file.write("-" * 80 + "\n")

    # Extract and write the relevant fields from the JSON data
    for item in data['imdata']:
        attributes = item['l1PhysIf']['attributes']
        dn = attributes.get('dn', '')
        description = attributes.get('description', '')
        speed = attributes.get('speed', '')
        mtu = attributes.get('mtu', '')
        output_file.write("{:<50} {:<20} {:<10} {:<5}\n".format(dn, description, speed, mtu))

print("The table has been written to output.txt")