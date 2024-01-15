# #Factorial function
# def Factorial(n):
#     if n == 0 or n == 1:
#         return 1;
#     else:
#         return n * Factorial(n - 1);

# print(Factorial(6));




#Fibonacci Sequence

# def Fibonacci(n):
#     if n == 0:
#         return 0;
#     elif n == 1:
#         return 1;
#     else:
#         return Fibonacci(n - 1) + Fibonacci(n - 2);

# print(Fibonacci(7));





#Palindrome Check

# def Palindrome(word):
#     word = word.lower()
#     return word == word[::-1]

# Input_word = "deed";
# if Palindrome(Input_word):
#     print(f"{Input_word} is a palindrome.")
# else:
#     print(f"{Input_word} is not a palindrome.")


#(f(x)=a⋅xb) Power Function
a = int(input("enter the exponent"))
b = int(input("enter the co-effecient"))

def f(x):
    if x:
        y = int(x**b);
        return int(a*y);
        
    
print(f(30));