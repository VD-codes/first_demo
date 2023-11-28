days = int(input("Enter the days in month : "))
first_day = int(input("Enter the first days of the month : "))
print("Mon\tTue\twed\tthi\tfri\tsat\tsun")
num=1
count=0
while count!=first_day:
    print(end="\t")
    count = count+1
while num<=days:
    if count==7:
        print()
        count=0
    else :
        print(num,end="\t")
        num +=1
        count= count + 1

