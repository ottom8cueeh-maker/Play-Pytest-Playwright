def convert_cm_to_feet_inches(cm):
    feet = cm / 30.48
    inches = (feet % 1) * 12
    return int(feet), round(inches, 1)

if __name__ == "__main__":
    length_in_cm = float(input("Enter length in cm: "))
    feet, inches = convert_cm_to_feet_inches(length_in_cm)
    print(f">> {length_in_cm} cm is equal to \033[38;5;208m{feet} feet and {inches} inches\033[0m.")