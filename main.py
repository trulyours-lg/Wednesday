import math

#def quadratic_equation_solver(a, b, c): - i didn't have the time to finish both, sorry - i was hoping the user input one will cover both
def find_largest_and_smallest_numbers(num1=0.0, num2=0.0, num3=0.0): #not finished yet
    str_input="Input the 3 numbers for sorting:"
    q_list = input(str_input).split()
    if (q_list[0]>q_list[1]):
        if (q_list[0]>q_list[2]):
            print(q_list[0],"- the biggest")
        else:
            print ("xxx")
#def temp_checker(min_temp, temp_1, temp_2, temp_3):

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

    if (float(q_list[1]))>0:

        if type(0.5**(float(q_list[1]))**2-4*float(q_list[0])* float(q_list[2]))==int:
            solution1 = (-(float(q_list[1])-0.5**((float((q_list[1]))**2-4*float(q_list[0])* float(q_list[2]))))/2 * float(q_list[0]))
            solution2 = (-(float(q_list[1])+0.5**((float((q_list[1]))**2-4*float(q_list[0])* float(q_list[2]))))/2 * float(q_list[0]))
            print(solution1, solution2)
        else:
            print("cant' calc square root as an integer")
    else:
     print("error in input")


str_input= "Input your single digit numbers and math operation:"
my_input = input(str_input)
calc_math_expression_from_str(my_input)
#---------------------------------------------------
# do the  quadratic expression solver
quadratic_equation_solver_from_user_input()
find_largest_and_smallest_numbers(num1=0.0, num2=0.0, num3=0.0)