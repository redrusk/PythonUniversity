word = input()

vowels = {'a', 'e', 'i', 'o', 'u'}

total_vowels = 0
total_consonants = 0

vowel_counts = {vowel: 0 for vowel in vowels}

for letter in word:
    if letter in vowels:
        total_vowels += 1
        vowel_counts[letter] += 1
    else:
        if letter.isalpha():
            total_consonants += 1

print(f"Гласных букв: {total_vowels}")
print(f"Согласных букв: {total_consonants}")

print("Количество каждой гласной буквы:")
for vowel in sorted(vowels):
    count = vowel_counts[vowel]
    if count == 0:
        print(f"{vowel}: False")
    else:
        print(f"{vowel}: {count}")
