name = input("Enter your name: ")
section = input("enter your section: ")
prelim_grade = float(input("Enter your Prelim grade: "))
if prelim_grade <40 or prelim_grade > 100:
    print("invalid grade")
else:
    Midterm_grade = float(input("Enter your Midterm Grade: "))
if Midterm_grade <40 or Midterm_grade > 100:
    print("invalid grade")
else:
    Finals_grade = float(input("input your finals grade: "))
    if Finals_grade <40 or Finals_grade > 100:
        print("invalid grade")
    else:
        prelim_grade = prelim_grade * 0.3333
        Midterm_grade = Midterm_grade * 0.3333
        Finals_grade = Finals_grade * 0.3333
        Average_Grade = prelim_grade + Midterm_grade + Finals_grade
        Average_Grade = round(Average_Grade)
        
        print()
        print("Hello, " + name + "!")
        print("section" + section)
        
        if 99 <= Average_Grade <=100:
            print("Grade 1.00 Execellent Student")
        elif 96 <= Average_Grade <= 98:
            print("Grade 1.25 Outstanding Student")
        elif 93 <= Average_Grade <= 95:
            print("Grade 1.50 Superior Student")
        elif 90<= Average_Grade <= 92:
            print("Grade 1.75 Very Good Student")
        elif 87 <= Average_Grade <= 89:
            print("Grade 2.00 nice Student")
        elif 84 <= Average_Grade <= 86:
            print("Grade 2.25 Satisfactory")
        elif 81 <= Average_Grade <= 83:
            print("Grade 2.50 Fairly Satisfactory")
        elif 78 <= Average_Grade <= 80:
            print("Grade 2.75 fair")
        elif 75 <= Average_Grade <= 77:
            print("Grade 3.00 passed")
        elif 60 <= Average_Grade <= 74:
            print("YOU FAILED")