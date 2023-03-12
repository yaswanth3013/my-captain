def most_frequent(string):
    freq_dict = {}
    for char in string:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    sorted_dict = dict(sorted(freq_dict.items(), key=lambda x: x[1], reverse=True))
    for key, value in sorted_dict.items():
        print(key, "=", '{:02d}'.format(value), end=" ")
most_frequent("Mississippi")
"""
output:i = 04 s = 04 p = 02 M = 01
"""
