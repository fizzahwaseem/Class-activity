#take an input and find out whethe is an even or odd
val1 = int(input("Enter a Number: "))
def even_odd(val1):
    if val1 % 2 == 0:
        ans = "even"
        return ans
    else:
        ans = "odd"
        return ans
answer = even_odd(val1)
print(answer)