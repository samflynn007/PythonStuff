year = int(input("Which year do you want to check? "))
if year % 4 == 0 or year % 400 == 0:
    print("Leap year.")
else:
    print("Not leap year.")
    
    
    
    # Method -2 
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap Year")
            else:
                print("Not leap year")
        else:
            print("Leap year")
    else:
        print("Not leap year")