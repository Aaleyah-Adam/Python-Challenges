errors = 0 

while True:
    MyNumber = input("Please enter a number: ")
    try:
        valid_number = int(MyNumber)
        break
    except ValueError:
        print("Seriously, don't you read the instructions. \nI asked for a number...")
        errors += 1 
 
print(valid_number)
print("you made so many errors, ", errors)
