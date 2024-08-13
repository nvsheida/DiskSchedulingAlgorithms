while True:
    numbers = input("Enter the request query with space:")
    number_list = numbers.split()
    number_list.insert(0, 54)

    for num in number_list:
        if not (0 <= int(num) <= 99):
            print("Please enter numbers between 0 and 99.")
            break
    else:
        number_list = [int(num) for num in number_list]
        break

next_list = [abs(number_list[i] - number_list[i - 1])
             for i in range(1, len(number_list))]
total_sum = sum(next_list)

print(f"The query is {number_list[1:]} and the total sum is [{total_sum}]")
