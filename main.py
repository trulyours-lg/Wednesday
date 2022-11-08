import math

#def quadratic_equation_solver(a, b, c): - i didn't have the time to finish both, sorry - i was hoping the user input one will cover both
def find_largest_and_smallest_numbers(num1=0.0, num2=0.0, num3=0.0):
    str_input="Input the 3 numbers for sorting:"
    q_list = input(str_input).split()
    # assigning the simple named variable to allow easier code reading
    num1 = int(q_list[0])
    num2 = int(q_list[1])
    num3 = int(q_list[2])
    my_sort = (num3, num1, num2) # incase they are all equal
    if ((num1 > num2) and (num2 <= num3)):
            my_sort =(num3,num2,num1)

    if ((num1  > num2) and (num2  <= num3)):
            my_sort =(num2,num1,num3)

    if ((num1 < num2) and (num2 <= num3)):
            my_sort = (num1, num2, num3)

    if ((num1 < num2) and (num2 >= num3)):
            my_sort=(num3,num1,num2)

    print("sorted :",my_sort)
def temp_checker(min_temp, temp_1, temp_2, temp_3):
#This function returns True if and only if 2 or more days that are warmer than the threshold
    if (((temp_1 > min_temp) and (temp_2 > min_temp)) or ((temp_2 >min_temp) and (temp_3>min_temp)) or ((temp_1>min_temp) and (temp_3>min_temp))):
        print ("True")
    else:
        print ("False")

def calc_math_expression(num1, num2, operator):
     if operator == "+" :
         return int(num1)+int(num2)
     elif operator == "*" :
         return int(num1)*int(num2)
     elif operator == "-" :
         return int(num1)-int(num2)
     elif operator == "/" :
         return int(num1)/int(num2)
     else: print("error in input")
#for simplicity assuming that the input received contains only single digit numbers, i.e. the input is 3 chars only
def calc_math_expression_from_str(user_input):
     if len(user_input)<3:
      print('error in number of user parameters')
     else:
        num1 = user_input[0:1]
        operator = user_input[1:2]
        num2 = user_input[2:3]
        print ("result :",calc_math_expression(num1,num2,operator))

def quadratic_equation_solver_from_user_input():
    str_input = "Input your quadratic formula parameters:"
    q_list = input(str_input).split()
    # assigning the simple named variable to allow easier code reading
    num1 = int(q_list[0])
    num2 = int(q_list[1])
    num3 = int(q_list[2])
    if type(0.5**(float(num2))**2-4*float(num1)* float(num3))==int:
        solution1 = (-(float(num2)-0.5**((float((num2))**2-4*float(num1)* float(num3))))/2 * float(num1))
        solution2 = (-(float(num2)+0.5**((float((num2))**2-4*float(num1)* float(num3))))/2 * float(num1))
        print(solution1, solution2)
    else:
        print("cant' calc square root as an integer")

str_input= "Input your single digit numbers and math operation:"
my_input = input(str_input)
calc_math_expression_from_str(my_input)
#---------------------------------------------------
# do the  quadratic expression solver
quadratic_equation_solver_from_user_input()
find_largest_and_smallest_numbers(num1=0.0, num2=0.0, num3=0.0)
#----------------------------------------------------
str_input= "Input min temp and 3 different temps:"
q_list = input(str_input).split()
min_temp = int(q_list[0])
temp_1 = int(q_list[1])
temp_2 = int(q_list[2])
temp_3 = int(q_list[3])
temp_checker(min_temp, temp_1, temp_2, temp_3)