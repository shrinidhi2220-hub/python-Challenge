marks = 88
attendance = 92

if marks >= 85 and attendance >= 90:
    print("Student is eligible for scholarship")


number = -25

if number > 0 and number % 5 == 0:
    print("Positive number divisible by 5")
else:
    print("Condition not satisfied")



username = "admin"
password = "python123"

if username == "admin" and password == "python123":
    print("Login successful")
else:
    print("Invalid userne or password")


marks = 82

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B+"
elif marks >= 60:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "Fail"

print("Marks:", marks)
print("Grade:", grade)


attendance = 85
fees_paid = True
has_hall_ticket = True

if attendance >= 75:
    if fees_paid:
        if has_hall_ticket:
            print("Student can attend the exam")
        else:
            print("Hall ticket is required")
    else:
        print("Pay the examination fees")
else:
    print("Attendance is insufficient")



age = 20
marks = 78
sports = True

if age >= 18:
    if marks >= 60:
        if sports:
            print("Eligible for sports scholarship")
        else:
            print("Not eligible: Sports participation required")
    else:
        print("Not eligible: Marks are insufficient")
else:
    print("Not eligible: Age requirement not satisfied")
