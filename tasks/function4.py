def count_vowels(text):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)
    
result = count_vowels("Hello, World!")
print(result)