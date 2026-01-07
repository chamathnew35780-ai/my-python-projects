shopping_list = [ "grapes","honey", "ice cream", "jelly"]
administer_password = "dark_knight"

while True:
    password = input("Enter the admin password to access the shopping list: ")
    if password == administer_password:
        print("Access granted. You can now manage the shopping list.")
        break
    else:
        print("Incorrect password. Please try again.")
        continue

while True:
  item_to_find = input("Enter the item you want to find in the shopping list.('exit' to quit) ")
  if item_to_find.lower() == 'exit':
     break

  elif item_to_find in shopping_list:
     print("################################################################################")
     print(f"{item_to_find} is in the shopping list.")
     print("################################################################################")

  else:
     print("################################################################################")
     print(f"{item_to_find} is not in the shopping list.")
     print("################################################################################")
     continue_prompt = input("Do you want to add it to the shopping list? (y/n): ")
     print("################################################################################")

     if continue_prompt.lower() == "y":
      shopping_list.append(item_to_find)
      print(f"{item_to_find} has been added to the shopping list.")
      print("################################################################################")
     else:
      print("No changes made to the shopping list.")
      print("################################################################################")
  shopping_list.sort()
  print("Current shopping list:")    
  for item in shopping_list:
     print(f"- {item}")
  print("################################################################################")  