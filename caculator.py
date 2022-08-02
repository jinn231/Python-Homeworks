# --------------------------------------------------------------------------------------

# Plus
def adding(first_num,sec_num):
    print(first_num, " + " , sec_num ," = ",first_num + sec_num)

# ---------------------------------------------------------------------------------------

#multi
def multi(first_num,sec_num):
    ask_usr = input(f"Do you want {first_num} power {sec_num}  (y/n) : ").lower()
    if ask_usr == "y":
        print(f"{first_num} power {sec_num} is: ", first_num ** sec_num)
    elif ask_usr == "n":
        print(first_num, " x " , sec_num ," = ",first_num * sec_num)
    else:
        print("Something went wrong!")

# ----------------------------------------------------------------------------------------

#dividing
def dividing(first_num, sec_num):
    remainder = first_num % sec_num
    remainder_or = input("Do you want remainder(y/n) : ").lower()
    if remainder_or == "n":
        if remainder != 0:
            ask_usr = input("Do you want decimal numbering system? (y/n) : ").lower()
            if ask_usr == "y":
                print(f"{first_num} {chr(247)} {sec_num} = ", float(first_num / sec_num))
            elif ask_usr == "n":
                print(f"{first_num} {chr(247)} {sec_num} = ", int(first_num / sec_num))    
            else:
                print("Something went wrong!")
        else:
            print(f"{first_num} {chr(247)} {sec_num} = ", int(first_num / sec_num))    
    elif remainder_or == "y":
        print(f"{first_num} {chr(247)} {sec_num} = ", first_num % sec_num)
    else:
        print("Just type y or n!")
    

#------------------------------------------------------------------------------------------

# minutes 
def sub(first_num, sec_num):
    if first_num < sec_num:
        ask_usr = input("Do u want negative number? (y/n) : ").lower()
        if ask_usr == "y":
            print(first_num, " - " , sec_num ," = ",first_num - sec_num)
        elif ask_usr == "n":
            print(first_num, " - " , sec_num ," = ",(first_num - sec_num)* (-1))
        else:
            print("Try again!")
    elif first_num > sec_num:
            print(first_num, " - " , sec_num ," = ",first_num - sec_num)

# ------------------------------------------------------------------------------------------