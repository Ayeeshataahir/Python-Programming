total=0
count=0
maximum=None
minimum=None
while True:
    i=input("Enter a number")
    if i=='done':
        break
    else:
        try:
            i=int(i)
            total=total+i
            count=count+1
            if maximum is None and minimum is None:
                  maximum=i
                  minimum=i
            elif i>maximum:
                maximum=i
            elif i<minimum:
                minimum=i
        except:
            print("Invalid input")
print("total"),total ,("count"),count,("Maximum"),maximum,("minimum"),minimum
