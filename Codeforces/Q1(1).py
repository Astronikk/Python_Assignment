string = input()
txt = string.casefold()


def rm_vowel(txt):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    af_vowels = [letter for letter in txt if letter.lower() not in vowels]
    af_vowels = '.'.join(af_vowels)
    print('.' + af_vowels)


rm_vowel(txt)
