number = 0
total = 0
count = 0
average = 0

while True:
    
    number = input("Enter a number: ")

    try:
        number = float(number)
        total += number
        count += 1
        average = total / count
    except:
        if number == "done":
            print(total, count, average)
            break
        else:
            print("Invalid input")