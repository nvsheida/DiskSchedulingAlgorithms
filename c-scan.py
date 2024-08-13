numbers = input("Enter requests with a space: ")
number_list = numbers.split()
number_list = [int(num) for num in number_list]



def max_numbers(number_list):
    new_list = []

    for number in number_list:
        if number > 54:
            new_list.append(number)
            new_list.sort()

    return new_list


result = max_numbers(number_list)
result.insert(0,54)
# print(result)


def min_numbers(number_list):
    next_list= []

    for i in number_list:
        if i < 54:
            next_list.append(i)
            next_list.sort()

    return next_list


answer = min_numbers(number_list)
answer.insert(0,0)
# print(answer)

final_list = result + answer
# print(final_list)

max_index = final_list.index(max(final_list))
final_list.insert(max_index + 1, 99)

mathmatic_opp = [abs(final_list[a]- final_list[a - 1])
                 for a in range(1, len(final_list))]

total_sum = sum(mathmatic_opp)

print(f"The request query is [{final_list}] and the total sum is [{total_sum}]")