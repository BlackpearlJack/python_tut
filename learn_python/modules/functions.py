# def calculate_total(exp):
#     total = 0
#     for item in exp:
#         total = total +item
#     return total
#
# tom_exp_list = [2100,3400,3500]
# joe_exp_list = [200,500,700]
#
# toms_total = calculate_total(tom_exp_list)
# joes_total = calculate_total(joe_exp_list)
#
# print("Tom's total expenses:", toms_total)
# print("Joe's total expenses:", joes_total)
#

# local variable functions
# def sum(a,b):
#     print("a:",a)
#     print("b:",b)
#
#     total = a+b
#     print("total inside function:", total)
#     return total
#
# n = sum(b=5,a=6)
# print("Total outside function:",n)

# total = 0 #global variable
# def sum(a,b=0):
#     """
#      This function takes two integer arguments and returns
#      the sumo their output
#
#     """
#     print("a:",a)
#     print("b:",b)
#
#     total = a+b
#     print("total inside function:", total)#local variable
#     return total
#
# n = sum(5,8)
# print("Total outside function:",total)

# total = 0
# for item in tom_exp_list:
#     total = total + item
#     print("Tom's total expenses:", total)
#
# total = 0
# for item in joe_exp_list:
#     total = total + item
#     print("Joe's total expenses:", total)

def calculate_triangle_area(base,height):
    return 1/2*(base*height)

def calculate_square_area(length):
    return length*length

