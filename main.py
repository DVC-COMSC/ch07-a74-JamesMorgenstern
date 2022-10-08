

numbers = [5, 20, 30, 30, 50]
delval = int(input('Enter the deletion value: '))
count = 0
j = 0
for i in range(len(numbers)):
    if(delval == numbers[j]):
        numbers.remove(delval)
        count += 1
        j -= 1
    j += 1

if (count == 0):
    numbers.clear()

print (numbers)
