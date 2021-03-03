def isgreaterorequal(largest,number):
    number1 = str(largest)[0]
    number2 = str(number)[0]
    if number1==number2:
        number1 = str(largest)+str(number)
        number2 = str(number)+str(largest)
    return number1>number2

def largest_number(a):
    res = ""
    while len(a)>0:
        largest = a[0]
        for number in a:
            if number!=largest:
                flag = isgreaterorequal(largest,number)
                if flag==False:
                    largest = number
        res+=str(largest)
        a.remove(largest)
    return res

n = int(input())
data = input().split()
result = largest_number(data)
print(result)