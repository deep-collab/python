# Write a Python function to calculate the factorial of a number.

# def factorial(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= i;
#     return result;

        
# result = factorial(8);
# print(result)

# If
# is odd, print Weird
# If
# is even and in the inclusive range of to
# , print Not Weird
# If
# is even and in the inclusive range of to
# , print Weird
# If
# is even and greater than , print Not Weird

# def number(n):
#     if n >= 0:
#         for i in range(n):
#            print(i ** 2)

# number(10)
def is_leap(year):
  if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap = True
  else:
        leap = False
  return leap

print(is_leap(2000))