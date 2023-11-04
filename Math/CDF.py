# function sampleFromDistribution(probabilities: array of float) -> int:
#     n = length(probabilities)
import random

# [0.8, 0.2]
def sampleFromDistribution(probabilities):
    cdf = [] # [0.8, 1.0]
    cdf.append(probabilities[0])

#   Compute the cumulative distribution
    for i in range(1, len(probabilities)):
        cdf.append(cdf[i - 1] + probabilities[i])
    
#   Generate a random number between 0 and 1
    random_value = random.uniform(0, 1)

#   Find the index in the cumulative distribution
    for i in range(len(cdf)):
        if random_value <= cdf[i]:
            return i

print(sampleFromDistribution([0.8, 0.2]))

# weights = {'a' => 0.4, 'b' => 0.4, 'c' => 0.2, 'd' => 0.0}
def cdf2(weighted_array):
    pass