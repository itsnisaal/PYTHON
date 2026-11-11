
science=float;
math=float;
social=float;
english=float;
computer=float;
opt_math=float;
nepali=float;
percentage=float;
gpa=float;
total_marks=float;

science=float(input("enter your marks of science:"))
math=float(input("enter your marks of math:"))
social=float(input("enter your marks of social:"))
english=float(input("enter your marks of english:"))
computer=float(input("enter your marks of computer:"))
nepali=float(input("enter your marks of nepali:"))
optional_math=float(input("enter your marks of optional_math:"))
total_marks= science + math + social + english + computer + optional_math + nepali      
while True:
    print("____Result generator____")
    print("1)Get percentage")
    print("2)Get gpa")
    print("3)Get grade")
    print("4)Exit")
choice=int(input("enter your choice:"))
percentage=(total_marks/700)*100
if choice == 1:
    percentage=(total_marks/700)*100
    print("you have obtained a total percentage of:",percentage,"%")
elif choice ==2:
    gpa=(percentage/100)*4.0
    print("you have obtained a total gpa of:",gpa)
elif choice ==3:
    if percentage<100 and percentage>=90:
        print("you have obtained a grade of A+")
    elif percentage<90 and percentage>=80:
        print("you have obtained a grade of A")
    elif percentage<80 and percentage>=70:
        print("you have obtained a grade of B+")
    elif percentage<70 and percentage>=60:
        print("you have obtained a grade of B")
    elif percentage<60 and percentage>=50:
        print("you have obtained a grade of C+")
    elif percentage<50 and percentage>=40:
        print("you have obtained a grade of C")
    elif percentage<40:
        print("sorry!! you have failed")
elif choice ==4:
    exit()
else:
    print("invalid choice!! please try again")