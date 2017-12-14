my_variable = "Hello"
grades = [88, 53, 95]
tuple_grades = (88, 53, 95)
set_grades = {88, 53, 95}

set_grades.add(67)
set_grades.add(56)
print(set_grades)

your_lottery_number = {1, 2, 3, 4, 5}
winning_number = {1, 3, 5, 7, 9, 11}

print(your_lottery_number.intersection(winning_number))
print(your_lottery_number.union(winning_number))
print(your_lottery_number.difference(winning_number))
