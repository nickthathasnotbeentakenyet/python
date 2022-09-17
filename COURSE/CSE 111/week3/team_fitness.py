from datetime import datetime

def main():
    # user input
    gender = input("Enter Gender[M/F]: ").lower()
    birthdate = input("Enter Birthdate[YYYY-MM-DD]: ")
    weight = float(input("Enter Weight[U.S. pounds]: ")) 
    height = float(input("Enter Weight[U.S. inches]: "))
    # calling function to calculate and return values
    kg = kg_from_lb(weight)
    cm = cm_from_in(height)
    age = compute_age(birthdate)
    bmi = body_mass_index(kg,cm)
    bmr = bmbasal_metabolic_rater(gender, weight, height, age)
    # printing results
    print(f"Age (years): {age}")
    print(f"Weight (kg): {kg:.2f}")
    print(f"Height (cm): {cm:.1f}")
    print(f"BMI: {bmi:.1f}")
    print(f"BMR (kcal/day): {bmr:.0f}")

def kg_from_lb(pounds):
    return pounds * 0.45359237

def cm_from_in(inches):
    return inches * 2.54

def compute_age(birth_str):
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()
    years = today.year - birthdate.year
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1
    return years

def body_mass_index(weight,height):
    return (10000 * weight) / height ** 2

def bmbasal_metabolic_rater(gender, weight, height, age):
    if gender in ("m", "male", "man"):
        return 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age
    else:
        return 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age

main()