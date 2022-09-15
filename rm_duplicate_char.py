"""

    AUTHOR : NARENDRA YADAV M20AIE263

"""

# Remove Duplicate Charectors from string


string = "Hi how are you?"
temp_str = ""
for i in range(len(string)):
    if string[i] not in temp_str:
        temp_str = temp_str + string[i]
print(temp_str)
