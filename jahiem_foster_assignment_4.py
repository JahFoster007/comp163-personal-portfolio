student_name = "Jahiem Foster"

current_gpa = 3.1 # Float between 1.0-4.0
study_hours = 10
social_points = 40
stress_level = 50
print("Welcome")
print(f"Student Name: {student_name}")
print(f"Current GPA: {current_gpa}")
print(f"Social Points: {social_points}")
print(f"Stress Level: {stress_level}")
print("Difficulty Levels: Light, Standard, Heavy")
choice = input("Choose a difficulty level:" )
#Step 2
light_mode = "Light: (12 credits)"
standard_mode = "Standard: (15 credits)"
heavy_mode = "Heavy: (18 credits)"

if choice == "Light":
    if current_gpa <= 2.9:
        stress_level -= 20
        study_hours += 0
        social_points += 30
    print("Light mode")
elif choice == "Standard":
    if current_gpa >= 3.0 and current_gpa <= 3.4:
        stress_level += 20
        study_hours +=10
        social_points -= -15
        print("Standard mode")
elif choice == "Heavy":
    if current_gpa >= 3.5 and current_gpa <= 4.5:
        stress_level += 30
        study_hours += 15
        social_points -= 20
        print("Heavy mode")
else:
    print("Invalid Input")
#Step 3
study_options = ["Programming", "Math", "English", "History"]
print("Choose a class to study: ")
print(study_options)
choice = input("Choice selected: ")

if choice in study_options:
    if choice == "Programming":
        current_gpa += 0.2
        social_points -= 5
        print("less free time more studying")
    elif choice == "Math":
        current_gpa += .3
        social_points -= 2
        print("You're better at math but worse at making friends...")
    elif choice == "English" and current_gpa >= 3.0:
        social_points += 10
        print("Good job balanicing work and social life!")
    elif choice == "History" or (choice == "English" and current_gpa < 3.0):
        current_gpa += 0.1
        social_points += 3
        print("Good good, keep it up!")
    elif choice not in study:
        print("Invalid")
if study_options is not 10:
    print("")