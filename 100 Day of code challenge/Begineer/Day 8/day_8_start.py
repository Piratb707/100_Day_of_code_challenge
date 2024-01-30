#
# def greet():
#     print("row 1")
#     print("row 2")
#     print("row 2")
#
# greet()
#
# def greet_with_name(name):
#     print(f"row 1 {name}")
#     print(f"row 2 {name}")
#
# name_input = input()
#
# greet_with_name(name_input)

# name = input("")
# value = input("")
# location = input()

def greet_with(name = "Test", value = 2, location = "New York"):
    print(f"Hello {name}")
    print(f"What is it like in {value}")
    print(f"{location}")

greet_with()
