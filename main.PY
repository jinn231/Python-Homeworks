import caculator as c

try:
    def caculator(first_num, sec_num, operator):
        if operator == "+":
            c.adding(first_num, sec_num)
            usr_select = input("Type (exit) if you want to exit or (no): ").lower()
            if usr_select == "exit":
                exit()
        elif operator == "-":
            c.sub(first_num, sec_num)
            usr_select = input("Type (exit) if you want to exit or (no): ").lower()
            if usr_select == "exit":
                exit()
        elif operator == "x":
            c.multi(first_num,sec_num)
            usr_select = input("Type (exit) if you want to exit or (no): ").lower()  
            if usr_select == "exit":
                exit()         
        elif operator == "/":
            c.dividing(first_num,sec_num)
            usr_select = input("Type (exit) if you want to exit or (no): ").lower()
            if usr_select == "exit":
                exit()

    def main():
        usr_select = input("Do you want to caculate or exit (exit/c for caculate): ")
        while usr_select != "exit":
        # get data
            first_num = int(input("First number: " ))
            sec_num = int(input("Second number: "))
            operator = input(f"choose operator +,-,x,/ :") 
            caculator(first_num, sec_num, operator)
        else:
            exit()
   
    main()

except Exception:
    print("Something went wrong!")
finally:
    print("Thank you:)")