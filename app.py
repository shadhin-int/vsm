import json

# file = "file.pdf"
filename = 'file.pdf'
dict1 = {}
with open('file.pdf', 'rb') as fh:
    print(fh, "<-------")
    for line in fh:
        command, description = line.strip().split(None, 1)
        dict1[command] = description.strip()
print(dict1, "<-------")
# creating json file
# the JSON file is named as test1
out_file = open("test1.json", "w")

print(out_file)
json.dump(dict1, out_file, indent=4, sort_keys=False)
out_file.close()
