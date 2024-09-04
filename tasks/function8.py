def merge_dicts(dict1, dict2):
    merged = dict1.copy()
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value
        else:
            merged[key] = value
    return merged
dict_a = {'a':1, 'b':2, 'c':3}
dict_b = {'b': 3, 'c':4, 'd':5}

merged_results = merge_dicts(dict_a, dict_b)
print(merged_results)