data = b"This is some binary data"

# Open a file in write binary mode
with open('example.bin', 'wb') as file:
    file.write(data)


print("Binary data written to example.bin")

# Open a file in read binary mode
with open('example.bin', 'rb') as file:
    data = file.read()

print("Binary data read from example.bin:", data)




