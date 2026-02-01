print ("Enter mark obtained in 3 subjects")
markOne = int(input())
markTwo = int(input())
markThree = int(input())
total = markOne + markTwo + markThree
average = total/3

if average>= 90 and average <= 100:
    print ("Your grade is 7")
elif average>=80 and average <91:
    print ("Your grade is 6")
elif average>=60 and average<70:
    print ("Your grade is 5")
else: 
    print ("Your grade is 4")
