def largest_unique_character_count_of_k_size_subtring(str, k):
    history = {}
    largest_unique_count = 0
    
    # maintains the indexes of the window boundries
    low = high = 0
    
    while high < len(str):

        if str[high] not in history:
            history[str[high]] = 1
            largest_unique_count += 1
        else:
            history[str[high]] += 1

        # if window size is greater than k, remove characters of the left
        if high - low + 1 > k:
            if history[str[low]] >= 2:
                history[str[low]] -= 1
            else:
                del history[str[low]]
                largest_unique_count -= 1

            low += 1

        high += 1

    return largest_unique_count

print(largest_unique_character_count_of_k_size_subtring("aassssddff", 2))