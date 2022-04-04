def group_anagrams(strings):
    dict = {}

    for str in strings:
        key = [0] * 26

        for letter in str:
            key[ord(letter) - ord('a')] += 1

        if tuple(key) in dict:
            dict[tuple(key)].append(str)
        else:
            dict[tuple(key)] = [str]

    return list(dict.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))