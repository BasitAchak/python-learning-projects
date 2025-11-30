numbers = input("Enter the numbers separated by spaces:").split()
numbers = [int(num) for num in numbers]

total_numbers = len(numbers)
biggest = max(numbers)
smallest = min(numbers)
avg = sum(numbers)/total_numbers

sorted_numbers = sorted(numbers)
unique_numbers = list(set(numbers))


print("Total numbers:", total_numbers)
print("Biggest number:", biggest)
print("Smallest number:", smallest)
print("Average:", avg)
print("Sorted numbers:", sorted_numbers)
print("Unique numbers:", unique_numbers)