address = ["My Street", "45", "New York"]
pins = {"Grant": 1234, "Joe": 2343, "Jack": 9471}

print[address[1], address[0]]

pin = int(input("Enter your pin: "))


def find_in_file(f):
    myfile = open("sample.txt")
    fruits = myfile.read()
    fruits = fruits.splitlines()
    if f in fruits:
        return "Found!"
    else:
        return "DNE"


if pin in pins.values():
    fruit = raw_input("Enter fruit: ")
    print(find_in_file(fruit))
else:
    print("Incorrect pin!")
    print("This info can only be accessed by: ")
    for key in pins.keys():
        print key
