#Exercise
count = 0
for number in range(1, 100):
    if number % 2 == 0 :
        count += 1
        print(number)
else:
    print(f"We have {count} even number!")
