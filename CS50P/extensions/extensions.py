file_name = input("File name: ")

types = {".gif":"image/gif", ".jpg":"image/jpeg", ".jpeg":"image/jpeg", ".png":"image/png", ".pdf":"application/pdf", ".txt":"text/plain", ".zip":"application/zip"}

for type in types:
    if file_name.endswith(type):
        print(types[type])
    else:
        print("application/octet-stream")
