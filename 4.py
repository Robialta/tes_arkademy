import re

def sortNumber(number):
    arr_num_str = re.findall(r'\d+', number )  
    if len(arr_num_str) > 0:
        arr_num_int_sorted = sorted([str(x) for x in ''.join(arr_num_str)]) 
        num_sorted = int(''.join(arr_num_int_sorted))
        print(num_sorted)
    else:
        print("No number found in parameter!")

sortNumber("48172a94")
sortNumber("abc")
sortNumber("94a")