"""

    In application take pin = 1234
    Take the pin from end user
    Do the pin verification if pin match congratulations, if pin not matched enter pin
    Repeat 4-times after that say bye bye......


"""

pincode = 233227

for x in range(1,5):
    data = int(input(f"Enter you pin code attempt {x} : "))
    if data == pincode:
        print("Pincode is valid ... congrats.")
        break
    elif x == 4:
        print("Bye Bye your attempts are completed.")
