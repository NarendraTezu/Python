"""

    Take the name from end user
    print the vowels
    print the consonants

"""

name = input("Enter your name : ")
vowels = ""
consonants = ""

for i in name:
    if i in "aeiouAEIOU":
        vowels += i
    else:
        consonants += i


print("vowels are : ", vowels)
print("consonants are : ", consonants)
