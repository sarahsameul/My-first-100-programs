print("RA2211042010034")

def reverse_str(str1):
    if len(str1)==1:
        return str1
    else:
        return reverse_str(str1[1:]) + str1[0]
str1 = input("Enter word or number:")
str2 = reverse_str(str1)
print(str2)
