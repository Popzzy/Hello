
name = input('what is your name.\n\t==> ')

"""for i in name:
    if name -= name:
        print(name + ' is a palindrome because it reads the same way forward and back.')"""
"""Mazee pop mtoto wa mamake aki yanani tutaku disown"""

"""Ivi ndio ulifaa kufanya"""
def palindrome():
    reverse_name = []
    for i in range(len(name)):
        reverse_name.append(name[(len(name)-(i + 1))])

    for i in range(len(name)):
        if reverse_name[i] != name[i]:
            print("Not palidrome")
            return
    print("Palindrome")

name = name.lower()
palindrome()