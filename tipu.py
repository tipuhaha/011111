#conditions
total_obtained_marks = int(input("enter number"))

if total_obtained_marks >= 400 and total_obtained_marks <= 500:
    print(f"{total_obtained_marks} number grade A")

elif total_obtained_marks >= 300 or total_obtained_marks<=400:
    print("grade B")

elif total_obtained_marks >= 200:
    print("grade C")

elif total_obtained_marks < 200:
    print("Fail")