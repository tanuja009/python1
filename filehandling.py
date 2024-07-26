file_path = 'demo.txt'

# Open the file in write mode to truncate it
with open(file_path, 'w') as file:
    file.truncate()

print(f"Contents of '{file_path}' deleted successfully.")
with open("demo.txt","r") as f:
    print(f.read())
    print("delete the data")
