x = input("Greeting: ")

answer = x.strip().lower().split()[0]

if answer[0:5] == "hello":
    print("$0")
elif answer[0] == "h":
    print("$20")
else:
    print("$100")
