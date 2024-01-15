# syntax error
# exception eroor
def diveide_by(a,b):
    return a/b

try:
    ans = diveide_by(40, 0)
except Exception as e:
    print("something went wrong!", e)
    print(e.__class__)
    