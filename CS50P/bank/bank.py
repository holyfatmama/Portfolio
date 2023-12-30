x = input("Greeting: ")

answer = x.strip().lower().split()[0]
first_letter_answer = answer[0]

if answer[0:5] == "hello":
    print("$0")
elif first_letter_answer == "h":
    print("$20")
else:
    print("$100")

print answer
