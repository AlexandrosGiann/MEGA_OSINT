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

def to_greeklish(word):
    word = make_clear(word)
    word = word.lower()
    greek_list = ['α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'ι', 'κ', 'λ', 'μ', 'ν',
                  'ξ', 'ο', 'π', 'ρ', 'σ', 'ς', 'τ', 'υ', 'φ', 'χ', 'ψ', 'ω']
    greeklish_list = [['a'],['b', 'v'],['g'],['d', 'th'],['e'],['z'],['h', 'i', 'e'],['u', '8', 'th'],
['i'],['k'],['l'],['m'],['n'],['x', 'ks', 'j', '3'],['o'],['p'],['r'],
['s', 'c'],['s'],['t'],['y', 'u'],['f'],['x', 'h', 'ch'],['ps', '4'],['w', 'o']]
    v = word.find(max(word, key=lambda x: len(greeklish_list[greek_list.index(x)])))
    v1 = len(greeklish_list[greek_list.index(word[v])])
    lst = []
    c = 0
    while c < v1:
        for j in range(v1):
            word_lst = []
            for i in range(len(word)):
                if word[i] not in greek_list:
                    word_lst.append(word[i])
                elif i != v:
                    word_lst.append(greeklish_list[greek_list.index(word[i])][min(j, len(greeklish_list[greek_list.index(word[i])]) - 1)])
                else:
                    word_lst.append(greeklish_list[greek_list.index(word[v])][c])
            if ''.join(word_lst) not in lst:
                lst.append(''.join(word_lst))
        c += 1
    return lst

if __name__ == '__main__':
    word = input('>:')
    word = make_clear(word)
    print(to_greeklish(word))
