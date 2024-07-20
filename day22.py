'''
Decorators
'''
'''
Miscellaneous Function
'''
'''
Example 1
'''
# def sound(text):
#     return text.lower()
# print(sound("Saturday"))
# obj = sound
# print(obj("Today"))
'''
Passing function as a argument
'''
# #declare one function
# def one(text):
#     return text.upper()
# #declare two function
# def two(text):
#     return text.lower()
# #declare printmsg function
# def printmsg(func):
#     msg = func("Today is Saturday")
#     print(msg)
# #calling the function
# printmsg(one)
# #calling the function
# printmsg(two)

'''
Example 2
'''
'''
just adding two number
'''
# def add_func(a):
#     def add_logic(b):
#         return a+b
#     return add_logic
# add_two=add_func(25)
# print(add_two(25))
'''
start decorator
'''
def start_deco(func):
    def inner():
        print("Saturday")
        func()
        print("Next")
    return inner

@start_deco #similar to msg = start_deco(msg)
def msg():
    print("Inside function here")
# msg = start_deco(msg) # decorator logic
msg()