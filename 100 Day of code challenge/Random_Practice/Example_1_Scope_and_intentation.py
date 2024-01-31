RUN_INTENTED = True

message = "running unintented"

if RUN_INTENTED:
    message = "running intented"

def my_function():
    greet = 'Hello'
    return greet

print(my_function())