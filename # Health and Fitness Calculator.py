import math
result = None
def safe_float(prompt):
    try:
        return float(input(prompt))
    except:
        print("Invalid input. Returning to menu.\n")
        return None

def safe_int(prompt):
    try:
        return int(input(prompt))
    except:
        print("Invalid input. Returning to menu.\n")
        return None
    
def get_height_cm(prompt):
    try:
        unit = input(f"{prompt} (cm/ft): ").strip().lower()

        if unit == "cm":
            value = float(input("Enter height in cm: "))
            return value

        elif unit == "ft":
            feet = float(input("Feet: "))
            inches = float(input("Inches: "))
            return feet * 30.48 + inches * 2.54

        else:
            print("Invalid unit. Returning to menu.\n")
            return None

    except:
        print("Invalid input. Returning to menu.\n")
        return None
    
def get_weight_kg(prompt):
    try:
        unit = input(f"{prompt} (kg/lbs): ").strip().lower()

        if unit == "kg":
            value = float(input("Enter weight in kg: "))
            return value

        elif unit == "lbs":
            value = float(input("Enter weight in lbs: "))
            return value * 0.453592

        else:
            print("Invalid unit. Returning to menu.\n")
            return None

    except:
        print("Invalid input. Returning to menu.\n")
        return None

def future_height_prediction():
    try:
        your_height = int(input("Put your height in centimeters: "))
        your_age = int(input("How old are you? (number age only): "))
        gender = input("Gender (M/F): ").strip().upper()
        moms_height = int(input("How tall is your mom in cm?: "))
        dads_height = int(input("How tall is your dad in cm?: "))

        PERCENT_ADULT_HEIGHT = {
                "M": {12: 84.0, 13: 87.0, 14: 90.0, 15: 93.0, 16: 96.0},
                "F": {12: 88.0, 13: 91.0, 14: 94.0, 15: 97.0, 16: 99.0}
        }

        if gender not in ["M", "F"]:
            print("Invalid gender input.")
            return

        if your_age not in PERCENT_ADULT_HEIGHT[gender]:
            print("Age not supported by this predictor.")
            return

        midparent = (moms_height + dads_height + 13)/2 if gender == "M" else (moms_height + dads_height - 13)/2
        percent = PERCENT_ADULT_HEIGHT[gender][your_age] / 100
        growth_prediction = your_height / percent
        predicted_height = (growth_prediction + midparent) / 2
        predicted_height = round(predicted_height, 1)

        feet, inches = cm_to_feet_inches(predicted_height)
        print("\nPredicted Adult Height:")
        print(f"- {predicted_height} cm")
        print(f"- {feet} feet, {inches} inches")
    except:
        print("Invalid input put in")


def cm_to_feet_inches(cm):
    total_inches = cm / 2.54
    feet = int(total_inches // 12)
    inches = round(total_inches % 12, 1)
    return feet, inches


def strength_index_calculator():
    body_weight = get_weight_kg("Enter your weight")
    if body_weight is None: return

    bench = safe_float("Max bench press: ")
    if bench is None: return

    squat = safe_float("Max squat: ")
    if squat is None: return

    deadlift = safe_float("Max deadlift: ")
    if deadlift is None: return

    strength_index = (bench + squat + deadlift) / (body_weight * 3)
    print(f"Your Strength Index is: {strength_index:.2f}")


def bmi_calculator():
    height_cm = float(input("Enter your height in cm: "))
    weight_kg = float(input("Enter your weight in kg: "))
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    print(f"Your BMI is: {bmi:.1f}")
    return bmi


def vo2_max_test():
    print("How to do this test:")
    print("1. Find a space like a treadmill or an open area")
    print("2. Set a timer for 12 minutes")
    print("3. Run and try to keep a steady pace for 12 minutes")

    distanceran = safe_float("Enter distance ran in meters: ")
    if distanceran is None: return

    vo2_max = (distanceran - 504.9) / 44.73
    vo2_max = round(vo2_max, 1)

    print(f"Estimated VO2 Max: {vo2_max} mL/kg/min")

    if vo2_max < 35:
        category = "Below Average"
    elif vo2_max <= 45:
        category = "Average"
    elif vo2_max <= 55:
        category = "Good"
    elif vo2_max <= 65:
        category = "Excellent"
    else:
        category = "Superior"

    print(f"Fitness Level: {category}")


def bmr():
    age = safe_int("Enter your age: ")
    if age is None: return None

    weight = get_weight_kg("Enter your weight")
    if weight is None: return None

    height = get_height_cm("Enter your height")
    if height is None: return None

    gender = input("Enter your gender (M/F): ").strip().upper()

    if gender == "M":
        bmr_value = 10 * weight + 6.25 * height - 5 * age + 5
    elif gender == "F":
        bmr_value = 10 * weight + 6.25 * height - 5 * age - 161
    else:
        print("Invalid gender input")
        return None

    bmr_value = round(bmr_value, 1)
    print(f"Your BMR is: {bmr_value} calories per day")
    return bmr_value


def calculate_tdee():
    bmr_value = bmr()
    if bmr_value is None:
        return
    print("Select your activity level:")
    print("1. Sedentary (little/no exercise)")
    print("2. Lightly active (1 to 3 days/week)")
    print("3. Moderately active (3 to 5 days/week)")
    print("4. Very active (6 to 7 days/week)")
    print("5. Extra active (hard exercise + physical job)")

    activity_choice = input("Enter 1-5: ")
    activity_factors = {
        "1": 1.2,
        "2": 1.375,
        "3": 1.55,
        "4": 1.725,
        "5": 1.9
    }

    if activity_choice not in activity_factors:
        print("Invalid choice")
        return None

    tdee = bmr_value * activity_factors[activity_choice]
    tdee = round(tdee, 1)
    print(f"Your TDEE (total calories/day) is: {tdee}")
    return tdee


def bodyfat_percentage():
    weight = float(input("Enter your weight in kg: "))
    height_cm = float(input("Enter your height in cm: "))
    age = int(input("Enter your age in years: "))
    sex = input("Enter your sex (M/F): ").strip().upper()

    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    bmi = round(bmi, 1)

    gender_val = 1 if sex == "M" else 0
    bodyfat = (1.2 * bmi) + (0.23 * age) - (10.8 * gender_val) - 5.4
    bodyfat = round(bodyfat, 1,)

    if gender_val == 1:
        if bodyfat < 6:
            category = "Essential fat"
        elif bodyfat <= 24:
            category = "Healthy"
        elif bodyfat <= 31:
            category = "Overfat"
        else:
            category = "Obese"
    else:
        if bodyfat < 14:
            category = "Essential fat"
        elif bodyfat <= 31:
            category = "Healthy"
        elif bodyfat <= 36:
            category = "Overfat"
        else:
            category = "Obese"

    print(f"\nEstimated Body Fat: {bodyfat}%")
    print(f"Category: {category}")
    print(f"Based on BMI: {bmi}\n")

def onerm_estimator():
    weight_lifted = int(input("Enter the weight you lifted in kg's or lbs:"))
    reps = int(input("Enter how many reps you did:"))
    exercise = input("Optional: Type the exercise name:")
    if reps >= 10:
        print("Warning: 1RM estimation may not be as accurate with 10 or more reps:") 
        one_rm = weight_lifted * (1 + reps / 30)
    else:
        one_rm = weight_lifted * (1 + reps / 30)
    print(f"Estimated 1RM in {exercise}: {one_rm} kgs/lbs") 

def relative_strength():
    bodyweight = float(input("Enter your body weight in kilograms:"))
    print("Please count only reps with clean form for the next exercises listed")
    pushups = int(input("Enter how many clean push-ups you can do with no rest:"))
    pullups = int(input("Enter how many pull-ups you can do with no rest:"))
    situps = int(input("Enter how many situps you can do with no rest:"))
    squats = int(input("Enter how many squats you can do without any rest:"))
    pullup_coef = 1.5
    pushup_coef = 1.0
    situp_coef = 0.5
    squat_coef = 1.0
    total_score = (pullups * pullup_coef) + (pushups * pushup_coef) + (situps * situp_coef) + (squats * squat_coef)
    rss = total_score / bodyweight
    rss = round(rss, 2)

    if rss < 0.5:
        category = "Poor"
    elif rss < 1.0:
        category = "Below Average"
    elif rss < 1.5:
        category = "Average"
    elif rss < 2.0:
        category = "Above Average"
    elif rss < 2.5:
        category = "Excellent"
    else:
        category = "Elite" 
    print(f"Relative Strength Score: {rss}")
    print(f"Category:{category}") 

def waist_to_hip_ratio():
    sex = input("Enter your sex (M/F): ").strip().upper()
    waist = float(input("Enter your waist circumference (cm): "))
    hip = float(input("Enter your hip circumference (cm): "))

    whr = waist / hip
    whr = round(whr, 2)

    WHR_RISK = {
        "M": {
            "Low Risk": (0, 0.9),
            "Moderate Risk": (0.91, 0.99),
            "High Risk": (1.0, 5.0)
        },
        "F": {
            "Low Risk": (0, 0.8),
            "Moderate Risk": (0.81, 0.84),
            "High Risk": (0.85, 5.0)
        }
    }
    category = "Unknown"
    if sex in WHR_RISK:
        for cat, (low, high) in WHR_RISK[sex].items():
            if low <= whr <= high:
                category = cat
                break

    print(f"\nYour Waist-to-Hip Ratio (WHR) is: {whr}")
    print(f"Health Risk Category: {category}")


    print(f"\nYour Waist-to-Hip Ratio (WHR) is: {whr}")
    print(f"Health Risk Category: {category}")
    print("\nWelcome to the Health & Fitness Calculator!\n")
    

def resting_heart_rate():
    rhr = int(input("Enter your resting heart rate (bpm): "))
    
    if rhr < 60:
        category = "Excellent"
    elif rhr <= 70:
        category = "Good"
    elif rhr <= 80:
        category = "Average"
    else:
        category = "Poor"
    
    print(f"Resting Heart Rate: {rhr} bpm")
    print(f"Cardiovascular Fitness Category: {category}")
  
def activity_level_score():
    print("Select your activity level:")
    print("1. Sedentary (little/no exercise)")
    print("2. Lightly active (1â€“3 days/week)")
    print("3. Moderately active (3â€“5 days/week)")
    print("4. Very active (6â€“7 days/week)")
    print("5. Extra active (hard exercise + physical job)")

    choice = input("Enter 1-5: ")
    activity_points = {
        "1": 0,
        "2": 1,
        "3": 2,
        "4": 3,
        "5": 4
    }

    if choice not in activity_points:
        print("Invalid choice, assuming sedentary")
        choice = "1"

    print(f"Activity points: {activity_points[choice]}")
    return activity_points[choice]

def muscular_endurance_score():
    pushups = int(input("Maximum pushups in 1 minute:"))
    situps = int(input("Maximum situps in 1 minute:"))
    pullups = int(input("Maximum Pullups:"))
    score = (pushups + situps + pullups) / 3
    print(f"Muscular endurance score:{score:.1f}")

def flexibility_score():
    toe_touch = float(input("Distance from fingertips to toes (cm, 0 if touch, negative if can't reach): "))
    shoulder_reach = float(input("Distance between hands behind back (cm, 0 if touch, positive if gap): "))
    
    score = max(0, 50 - abs(toe_touch)) + max(0, 50 - abs(shoulder_reach))
    print(f"Flexibility Score: {score:.1f}")

def health_assessment(user_name):
    print(f"\n General Health Assessment for {user_name}")
    print("\n DISCLAIMER: This is not a true health assessment, just to get a general idea"
          "\n If you have any health questions, please ask your doctor\n")

    bmi = bmi_calculator()                    
    bodyfat = bodyfat_percentage()   
    whr = waist_to_hip_ratio()      
    vo2 = vo2_max_test()                      
    strength = strength_index_calculator()    
    rhr = resting_heart_rate()     
    activity = activity_level_score()        
    endurance = muscular_endurance_score()   
    flexibility = flexibility_score() 

    if bmi is None: bmi = 22
    if bodyfat is None: bodyfat = 18
    if whr is None: whr = 0.85
    if vo2 is None: vo2 = 40
    if strength is None: strength = 1
    if rhr is None: rhr = 70
    if activity is None: activity = 1
    if endurance is None: endurance = 30
    if flexibility is None: flexibility = 30


    bmi_score = max(0, min(10, 10 - abs(bmi - 22) / 2))
    bodyfat_score = max(0, min(10, 10 - abs(bodyfat - 18) / 3))
    whr_score = max(0, min(10, 10 - abs(whr - 0.85) * 20))
    vo2_score = min(10, vo2 / 10)
    strength_score = min(10, strength * 10)
    rhr_score = max(0, min(10, 10 - (rhr - 60) / 2))
    activity_score = min(activity * 2, 10)  
    endurance_score = min(endurance / 10, 10)
    flex_score = min(flexibility / 10, 10)

    total_score = (
        bmi_score + bodyfat_score + whr_score + vo2_score +
        strength_score + rhr_score + activity_score +
        endurance_score + flex_score
    )

    final_score = round(total_score / 9, 2)

    if final_score < 3:
        category = "Poor" 
    elif final_score < 4.5:
        category = "Below Average" 
    elif final_score < 6:
        category = "Average" 
    elif final_score < 7.5: 
        category = "Good"
    elif final_score < 9:
        category = "Excellent"
    else:
        category = "Superior"

    print(f"\nFinal Health Score: {final_score}/10")
    print(f"Health Category: {category}")


print("\nWelcome to the Health & Fitness Calculator!\n")
def print_menu():
    left = [
        "1. Future Height Prediction",
        "2. Strength Index Calculator",
        "3. Relative Strength Calculator",
        "4. BMI (Body Mass Index)",
        "5. VO2 Max Test",
    ]
    right = [
        "6. Basal Metabolic Rate (BMR)",
        "7. Total Daily Energy Expenditure(TDEE)",
        "8. Body Fat Percentage",
        "9. 1 Rep Max estimator",
        "10. Waist-Hip ratio",
        "11. Other Calculators(type 11 to see list)",
        "12. GENERAL HEALTH ASSESSMENT",
        "0. Quit"
    ]
    for i in range(max(len(left), len(right))):
        left_item = left[i] if i < len(left) else ""
        right_item = right[i] if i < len(right) else ""
        print(f"{left_item:<40}{right_item}")

def main():
    while True:
        print_menu()
        choice = input("\nChoose an option (enter number of option): ")

        if choice == "1":
            future_height_prediction()
        elif choice == "2":
            strength_index_calculator()
        elif choice == "3":
            relative_strength()
        elif choice == "4":
            bmi_calculator()
        elif choice == "5":
            vo2_max_test()
        elif choice == "6":
            bmr()
        elif choice == "7":
            calculate_tdee()
        elif choice == "8":
            bodyfat_percentage()
        elif choice == "9":
            onerm_estimator()
        elif choice == "10":
            waist_to_hip_ratio() 
        elif choice == "11":
            print("1. Muscular Endurance Score \n2. Flexibility Score \n3. Activity Level Score")
            tertiary_choice = input("Choose your Option:")
            if tertiary_choice == "1":
                muscular_endurance_score()
            elif tertiary_choice == "2":
                flexibility_score()
            elif tertiary_choice == "3": 
                activity_level_score()
        elif choice == "12":
            name = input("Enter your name:")
            health_assessment(name)
        elif choice == "0":
            print("Goodbye then. Stay Healthy and Fit!")
            break
        else:
            print("ERROR: Invalid choice")

if __name__ == "__main__":
    main()
