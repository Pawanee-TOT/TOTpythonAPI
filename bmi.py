height = input("Enter your height: ")
height = float(height)
weight = input("Enter your weight: ")
weight = float(weight)

#คำนวน
bmi = weight/(height*height)
if(bmi < 18.50):
  print("Thin")
elif(bmi > 18.50 and bmi <= 22.90):
  print("Normal")
elif(bmi > 23.00 and bmi <= 24.90):
  print("fat1")
elif(bmi > 25.00 and bmi <= 29.90):
  print("fat2")
elif(bmi > 30.00):
  print("fat3")
print(bmi)


