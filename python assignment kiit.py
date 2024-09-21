#TAX CALCULATOR ASSIGNMENT OF AI CLUB
#SUBMITTED BY ARCHISMITA ADHIKARI
#FROM BRANCH B-TECH CSE
#FIRST YEAR
#FIRST SEMESTER
income =int(input("ENTER YOUR ANNUAL INCOME :-"))
tax=0

if (income<=250000):
    tax=0
elif (income<=500000):
    tax=(income-250000)*5/100
elif (income<=1000000):
    tax=250000*5/100
    tax=tax+(income-500000)*20/100
elif (income>1000000):
    tax=250000*5/100
    tax=tax+income+500000*20/100
    tax=tax+(income-1000000)*30/100
    
print("Tax=",tax)

        
