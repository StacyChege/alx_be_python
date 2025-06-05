#Empty list
#Function to add, remove & display the current list.
def display_menu():
    print("\nShoppping List Manager")
    print("1. Add Item")
    print("3. Viw List")
    print("4. Exit")


#Use loop to display menu .  
def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"'{item}' has been added to your shopping list.")
        elif choice == '2':
            item = input("Enter the item to remove:" ) ##Ask user for itm name to remove.
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' is not in the shopping list.") # If not found display that.
        elif choice == '3':
             if shopping_list:
                 print("Your Shopping List:")
                 for i, item in enumerate(shopping_list, 1):
                     print(f"{i}. {item}")  #To view list print each item
             else: 
                 print("Your shopping list is empty.")
        elif choice == '4':
            print("Goodbye!")
            break #Remember to break
        else:
            print("Invalid choice. Please try again.") #Ensure script can handle invalid menu choices

