file_name = input("File name: ")

types = {".gif":"image/gif", ".jpg":"image/jpeg", ".jpeg":"image/jpeg", ".png":"image/png", ".pdf":"application/pdf", ".txt":"text/plain", ".zip":"application/zip"}

print(types[0])


if file_name.endswith(".gif"):
    print("image/gif")
elif file_name.endswith(".jpg"):
    print("image/jpg")
elif file_name.endswith(".jpeg"):
    print("")
elif file_name.endswith(".png"):
    print("")

