hindi = 50
english = 40
math = 85
percentage = (int)(((hindi+english+math)*100)/300)
print(f"{percentage}")

if percentage >= 33:
    print("Student passed")
else:
    print("Student failed")