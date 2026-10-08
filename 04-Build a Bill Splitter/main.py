running_total = 0

num_of_friends = 4

appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

running_total += appetizers + main_courses + desserts + drinks
print('Total bill so far:', running_total)

tip = running_total * 0.25
print('Tip amount:', tip)

running_total += tip
print('Total with tip:', running_total)

final_bill = running_total / num_of_friends
print('Bill per person:', final_bill)

each_pays = round(final_bill, 2)
print('Each person pays:', each_pays)
# Output:
# Total bill so far: 198.82999999999998
# Tip amount: 49.707499999999996
# Total with tip: 248.53749999999998
# Bill per person: 62.13437499999999
# Each person pays: 62.13