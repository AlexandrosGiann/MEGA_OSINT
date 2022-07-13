def make_clear(word):
    word = word.replace('ΐ', 'ι')
    word = word.replace('ς', 'σ')
    word = word.upper()
    word = word.replace('Ά', 'Α')
    word = word.replace('Έ', 'Ε')
    word = word.replace('Ή', 'Η')
    word = word.replace('Ί', 'Ι')
    word = word.replace('Ό', 'Ο')
    word = word.replace('Ύ', 'Υ')
    word = word.replace('Ώ', 'Ω')
    word = word.replace('Ϊ', 'Ι')
    word = word.replace('Ϋ', 'Υ')
    return word

def has_no_greek_letters(word):
    letters_gr = [chr(x) for x in range(ord('α'), ord('ω') + 1)]
    for letter in word:
        if letter in letters_gr:
            return False
    return True

def to_greeklish(word):
    word = make_clear(word)
    word = word.lower()
    greeklish_dict = {'α': ['a'],
                      'β': ['b', 'v'],
                      'γ': ['g'],
                      'δ': ['d', 'th'],
                      'ε': ['e'],
                      'ζ': ['z'],
                      'η': ['h', 'i', 'e'],
                      'θ': ['u', '8', 'th'],
                      'ι': ['i'],
                      'κ': ['k'],
                      'λ': ['l'],
                      'μ': ['m'],
                      'ν': ['n'],
                      'ξ': ['x', 'ks', 'j', '3'],
                      'ο': ['o'],
                      'π': ['p'],
                      'ρ': ['r'],
                      'σ': ['s', 'c'],
                      'ς': ['s'],
                      'τ': ['t'],
                      'υ': ['y', 'u'],
                      'φ': ['f'],
                      'χ': ['x', 'h', 'ch'],
                      'ψ': ['ps', '4'],
                      'ω': ['w', 'o'],
                      }
    lst = []
    mt = 0
    for letter in word:
        if not has_no_greek_letters(letter):
            mt = max(mt, len(greeklish_dict[letter]))
    print(mt)
    print(lst)

if __name__ == '__main__':
    word = input('>:')
    print(make_clear(word))
    print(to_greeklish(word))
