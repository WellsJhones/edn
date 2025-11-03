print("let's calculate your BMI now \n")

weight = float(input("type your weight in kg: \n"))
hight = float(input("type your hight now: \n"))

result = weight / ( hight ** 2)
print("\n")

if result <= 18.5:
    print("bellow the weight")
elif result <= 25:
    print("normal")
elif result <= 30:
    print("little overweight") 
else:
    print("you're overweight")