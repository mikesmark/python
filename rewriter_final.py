def min(x,y):
    try:
        if x > y:
            return y
        elif x<y:
            return x
        else:
            print("The two numbers are same!")
    except ValueError:
        print("One or two arguments are not number!! Te buta")

def max(values_list):
    result = int(values_list[0])
    i=0
    for i in values_list:
        if int(i) > int(result):
            result = i
        
    return result

def len(values_list):
    result = 0
    for i in values_list:
        result+=1
    return result




# I need some data...
x=int(input("Please provide the first number: "))
y=int(input("Please provide the second number: "))
print("")





print("x= "+str(x)+"  y="+str(y))
print("The minimum number: "+str(min(x,y)))
print("")

value_list = []
n=0
while n!= "q":
    n=input("Now I need a list, provide numbers (Exit: q) :")
    value_list.append(n)

value_list.remove('q')


print("")
print("Your List: "+str(value_list))
print("The maximum number of the list: "+max(value_list))
print("")

list_stri=[]
ns=0

while ns!= "q":
    ns=input("I need another list (Exit: q) :")
    list_stri.append(ns)
    

list_stri.remove('q')
print(list_stri)
print("Your list has "+str(len(list_stri))+" element(s).")
print("")

def multiply(x, y):
    count = 0
    result = 0
    while count < int(y):
        count += 1
        result += int(x)
    return result

print(str(x)+" x  "+str(y)+" ="+" "+str(multiply(x,y)))
print("")

def powa(x,y):
    try:
        
        count = 1
        result = x
        while True:
            count += 1
            result *= x
            if count == y:
                return result

        
    except ValueError:
        print("One or two arguments are not number")

print(str(x)+" raise to "+str(y)+" = "+str(powa(x,y)))
print("")

def div(x,y):
    try:
        i=0
        while True:
            x=x-y
            i += 1
            if x ==y:
                i+=1
                return i
            elif x<y:
                i+=1
                return i, x
            
                

    except ValueError:
        print("Maybe one or two arguments are NOT number... MAYBE")

print(str(x)+" divided by "+str(y)+" = "+str(div(x,y)))