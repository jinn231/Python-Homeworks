
try:
    # get data
    first_num = int(input("First number: " ))
    sec_num = int(input("Second number: "))
    operator = input("choose operator +,-,*,/ :")

    def adding(first_num,sec_num):
        print(first_num, " + " , sec_num ," = ",first_num + sec_num)

    def multi(first_num,sec_num):
        print(first_num, " * " , sec_num ," = ",first_num * sec_num)

    def dividing(first_num, sec_num):
        print(first_num, " / " , sec_num ," = ",first_num / sec_num)

    def sub(first_num, sec_num):
        print(first_num, " - " , sec_num ," = ",first_num - sec_num)

    def caculator(first_num, sec_num, operator):
        if operator == "+":
            adding(first_num, sec_num)
        elif operator == "-":
            sub(first_num, sec_num)
        elif operator == "*":
            multi(first_num,sec_num)
        elif operator == "/":
            dividing(first_num,sec_num)

    caculator(first_num, sec_num, operator)
except ValueError:
    print("OOPS! Something went wrong.")
finally:
    print("Thank for using")
