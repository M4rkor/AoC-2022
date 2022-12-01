file1 = open('elve_inventory')
calorie_lines = file1.readlines()
calorie_sums = []
sum = 0
for line in calorie_lines:
    if line.strip() == '':
        calorie_sums.append(sum)
        sum = 0
    else:
        sum = sum + int(line.replace("\n", ""))

print(sum)

top_three = 0

for i in range(3):
    top_three = top_three + max(calorie_sums)
    calorie_sums.remove(max(calorie_sums))

print(top_three)