weather = input("What's the weather like today? (sunny/rainy/cold): ")

#Provide clothig advice based on the weather
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")

elif weather == "rainy":
    print("Don't forget to take an umbrella and wear a raincoat.")

elif weather == "cold":
    print("Make sure to wear a warm coat and scarf.")

else:
    print("Sorry, I don't have recommendations for this weather.")