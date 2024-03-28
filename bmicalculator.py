h = float(input("Enter your height in meters: "))
w = float(input("Enter your weight in kg: "))

BMI= w /(h*h)

print("BMI calculated is:",BMI)

if BMI > 0:
    if BMI <= 16:
        print("You are very underweight")
    
    elif BMI <= 18:
        print("You are underweight")
        
    elif BMI <= 25:
        print("Congrats! you are Healthy")
    
    elif BMI <= 35:
        print("You are overweight")
    
    else:
        print("You are very overweight")

else:
    print("Enter valid details!...")