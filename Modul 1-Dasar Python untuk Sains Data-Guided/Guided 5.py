start = 1
end = 10
sum_odds = sum(i for i in range(start, end + 1) if i % 2 != 0)
print(f"Sum of odd numbers between {start} and {end} is {sum_odds}")