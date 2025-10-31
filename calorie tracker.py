#project : Daily Calorie Tracker CLI
#Author : Lucky Pannu
#Date : 25 October 2025
#Description :  A asimple Python app to record meals, calculate total and average calories, compare with daily limit.

print ("=================================")
print ("Welcome to Daily Calorie Tracker!")
print ("==================================")
print ("This tool helps you track what you eat and check")
print ("whether you are within your daily calorie goal. \n")

meals_no = int(input("How many meals would you like to enter today?"))
meals = []
calories = []

for i in range(meals_no) : 
 print(f"\n--- Enter details for meal {i+1} ---")
 meal_name = input("Meal name:")
 meal_calories = float(input(f"Calories for {meal_name} :" ))
 meals.append(meal_name)
 calories.append(meal_calories)

total_calories = sum(calories)
average_calories = total_calories / meals_no

daily_limit =  float(input("\Enter your daily calorie limit:"))

if total_calories > daily_limit:
    print("\n You have exceeded your daily calorie limit")
elif total_calories < daily_limit :
    print ("\n You are within your daily calorie limit.")
else :
    print("\n Perfect! You met your goal exactly")


print("\n ==================================")
print("              Calorie Summary")
print("======================================")

print (f"{'Meal Name':<15} {'Calories' :>12}")
print("-----------------------------------------")

for i in range(meals_no) :
    print(f"{meals[i]:<15} {calories[i]:>12.2f}")

print("-------------------------------------------")

print(f"{'Total:':<15} {total_calories:>12.2f}")
print(f"{'Average:':<15} {average_calories:>12.2f}")

print("==============================================")

save = input("would you like to save this report? (yes/no:)"). lower()

if save == "yes" :
   with open ("calorie_log.text" , "w") as file:
      file.write ("Calorie Tracker Report\n")

      file.write ("================================= \n")

      for i in range(meals_no) :
         file.write(f"{meals[i]} - {calories[i]} calories\n")
         file.write(f"Average: {average_calories: .2f}\n")
         file.write(f"Daily Limit: {daily_limit}\n")
         print("Report saved as'calorie_log.txt'")
      else :
         print("Report not saved. Goodbye!")