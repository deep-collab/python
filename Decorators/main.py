#assiging Functios to variables
# def plus_one(number):
#     return number + 1

# add_one = plus_one


# print(add_one(5))





#Defining Functions inside other function
# def plus_one(number):
#     def add_one(number):
#         return number + 1


#     result = add_one(number)
#     return result
# print(plus_one(4))




#passing functions as arguments to other fuctions
# def plus_one(number):
#     return number + 1

# def function_call(function):
#     number_to_add = 5
#     return function(number_to_add)

# print(function_call(plus_one))




# functions returning other functions

# def hello_function():
#     def say_hi():
#         return "hi"
#     return say_hi
# hello = hello_function()
# print(hello())





# nested functions have acess to the enclosing functions variable scope
def print_message(message):
    "enclosong Function"
    def message_sender():
        "Nested Function"
        print(message)


    message_sender()

print_message("some random message")    