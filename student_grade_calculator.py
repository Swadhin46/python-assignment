# STUDENT GRADE CALCULATOR

name = input("Enter Student Name: ")

sub1 = int(input("Enter Python Marks: "))
sub2 = int(input("Enter Mathematics Marks: "))
sub3 = int(input("Enter Physics Marks: "))

if sub1 < 0 or sub1 > 100 or sub2 < 0 or sub2 > 100 or sub3 < 0 or sub3 > 100:
  print("Invalid Marks!")
  print("Try Again.")

total = sub1+sub2+sub3

average = total/3

# DETERMINE GRADE

def grades_calculator(data):
  if data >= 80 and data <= 100:
    return "Grade: A+"
  elif data >= 70 and data <= 79:
    return "Grade: A"
  elif data >= 60 and data <= 69:
    return "Grade: B"
  elif data >= 50 and data <= 59:
    return "Grade: C"
  elif data < 50:
    return "Grade: F"

grades = grades_calculator(average)

print("===================")
print(f"Student's Name: {name}")
print(f"Total Marks: {total}")
print(f"Average: {average:.2f}")
print(grades)
