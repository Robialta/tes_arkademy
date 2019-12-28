import re

def is_name_valid(name):
    if len(name) >= 3:
        find_blocked_caracter = re.findall(r'[a-z0-9!@~#$%^&=+)(*>.<,/)`:;]', name)
        if len(find_blocked_caracter) == 0:
            print(True)
        else:
            print(False)
    else:
        print(False)   


def is_age_valid(age):
    if len(str(age)) == 2:
        print(True)
    else:
        print(False)

def is_username_valid(username):
    pass

is_name_valid("TIRHGJGGS")
is_age_valid(21)
is_username_valid("yans.333")
# is_username_valid("dian.11")