# dictionary (item:count)
grocery_list = {
    "apple":10
}

while True:
    try:
        item = input()
        if item in grocery_list:
            grocery_list.update(item = "int(grocery_list[item]) + 1")
            print(grocery_list[item])
        else:
            grocery_list.update(item = 1)
    except EOFError:
        for item in grocery_list:
            print(f"{grocery_list[item]} {item}")
