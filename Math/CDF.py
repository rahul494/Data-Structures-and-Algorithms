# function sampleFromDistribution(probabilities: array of float) -> int:
#     n = length(probabilities)
import random

# [0.8, 0.2]
def sampleFromDistribution(probabilities):
    cdf = [] # [0.8, 1.0]
    cdf.append(probabilities[0])

#   Compute the cumulative distribution
    for i in range(1, len(probabilities)):
        cdf.append(cdf[i - 1] + cdf[i])

#   Generate a random number between 0 and 1
    random_value = random.uniform(0, 1) # 0.9

#   Find the index in the cumulative distribution
    for i in range(len(cdf)):
        if random_value <= cdf[i]:
            return i
