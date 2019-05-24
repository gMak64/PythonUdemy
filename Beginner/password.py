correct_password = "qwert12345"
name = raw_input("First Name: ")
surname = raw_input("Last Name: ")
password = raw_input("Password: ")

while correct_password != password:
    password = input("Wrong password! Try again: ")

message = "Hi %s %s, you are logged in" % (name, surname)
print(message)