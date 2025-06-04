#User Weather Input
weather = input("What's the weather like today? (sunny/rainy/cold): ")

#Using if provide clothing Recommendations
if weather == "sunny":
   print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
#Use an else statement for unrecognized input
else:
    print("Sorry, I don't have recommendations for this weather.")
#Print the Output