#Exercise 5.1
total=0
count=0
while True:
    num=input("Enter a number:")
    if num =='done' :
        print(total)
        print(count)
        avg=total/count
        print(avg)
        break 
    else:
        try:
            total=total+ int(num)
        except:
            print ("Invalid input")
            continue
    count=count+1

