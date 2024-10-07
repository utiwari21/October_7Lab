def estimate_grade(age):
    if age < 5:
        return "Pre School."
    elif 5 <= age <= 6:
        return "Kindergarten"
    elif 7 <= age <= 10:
        return f"Grade {age - 5}"
    elif 11 <= age <= 17:
        return f"Grade {age - 5}"
    elif 18 <= age <= 22:
        return "You could be in college."
    else:
        return "You could be out of school or pursuing higher education"

def main():
    name = input("What's your name? ")
    age = int(input("How old are you? "))
    
    grade = estimate_grade(age)
    
    print(f"Hi {name}, based on your age, {age}, you are likely in {grade}.")

if __name__ == "__main__":
    main()

