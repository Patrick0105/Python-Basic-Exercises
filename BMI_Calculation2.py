if __name__ == "main":
   height = 160
   weight = 60
   BMI = round(weight / (height / 100) ** 2, 2)
   
   print(f'身高為{height}cm,體重為{weight}kg,您的BMI為{BMI}')