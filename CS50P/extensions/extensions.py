x = input("File name: ")

file_name = x.replace("."," ").lower()

extension_type = file_name[-1]

print(count(file_name))
if len(file_name) <= 2:
    print("application/octet-stream")

