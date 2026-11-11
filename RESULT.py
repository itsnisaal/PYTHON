# Finding the grade of students based on their marks in different subjects and calculating percentage and GPA.

English=float;
Math=float;
Science=float;
Social=float;
Nepali=float;
computer=float;
optional_math=float;
percentage=float;
GPA=float;
total_marks=float;

english=float(input("Enter English marks: "))
math=float(input("Enter Math marks: "))
science=float(input("Enter Science marks: "))
social=float(input("Enter Social marks: "))
nepali=float(input("Enter Nepali marks: "))
computer=float(input("Enter Computer marks: "))
optional_math=float(input("Enter Optional Math marks: "))
total_marks=english+math+science+social+nepali+computer+optional_math;

while True:
    print("____Result Generation____");
    print("1. Calculate Percentage");
    print("2. Calculate GPA");
    print("3. Calculate Grade");
    print("4. Exit");
    choice=int(input("Enter your choice: "));   
    if choice==1:
        percentage=(total_marks/700)*100
        print("Percentage: ", percentage);
    elif choice==2:
        GPA=(percentage/100)*4.0;
        print("GPA: ", GPA);
    elif choice==3:
        if percentage>=90:
            print("Grade: A+");
        elif percentage>=80:
            print("Grade: A");
        elif percentage>=70:
            print("Grade: B+");
        elif percentage>=60:
            print("Grade: B");
        elif percentage>=50:
            print("Grade: C+");
        elif percentage>=40:
            print("Grade: C");
        else:
            print("Grade: F");
    elif choice==4:
        break;
    else:
        print("Invalid choice! Please try again."); 