import math

class Solution:
    def findRestaurant(self, list1, list2):
        frequencies = {}
        result = []
        curr_smallest  = math.inf
        
        for index, val in enumerate(list1):
            frequencies[val] = index
        
        for index, val in enumerate(list2):
            if val in frequencies.keys():
                if index + frequencies[val] < curr_smallest:
                    curr_smallest = index + frequencies[val]
                    result = [val]
                elif index + frequencies[val] == curr_smallest:
                    result.append(val)
            
        return result

s = Solution()
print(s.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], 
                        ["KFC","Shogun","Burger King"]))