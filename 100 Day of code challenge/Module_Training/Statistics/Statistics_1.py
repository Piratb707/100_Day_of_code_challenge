import statistics
import math

ages_data = [10, 13, 14, 12, 11, 10, 11, 10, 15]

print(statistics.mean(ages_data))
print(statistics.mode(ages_data))
print(statistics.median(ages_data))
print(sorted(ages_data))

print(statistics.variance(ages_data))
print(statistics.stdev(ages_data))
print(math.sqrt(statistics.variance(ages_data)))

