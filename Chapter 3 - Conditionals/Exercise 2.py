try:
    
    hours = float(input("Enter Hours: "))
    
    try:

        rate = float(input("Enter Rate: "))


        if hours > 40:
            pay = (40 * rate) + (hours - 40) * (rate * 1.5)
        else:
            pay = rate * hours
            
        print("Pay: " + str(pay))

    except:
            
        print("Error, please enter numeric input")

except:

    print("Error, please enter numeric input")
