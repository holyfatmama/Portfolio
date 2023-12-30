x = input("Greeting: ")

answer = x.lower().split()[0]
first_letter_answer = answer[0]

if answer == "hello":
    print("$0")
elif first_letter_answer == "h":
    print("$20")
else:
    print("$100")
