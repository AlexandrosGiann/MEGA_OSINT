file = open('post_codes.txt', 'r').readlines()

lst = []

lst1 = []

for f in file:
    f = f.replace('\n', '')
    f1 = f
    counter = 1
    lst.append([])
    string = ''
    while f1[-counter].isnumeric() or f1[-counter] == ',' or f1[-counter] == ' ':
        if f1[-counter] != ',':
            string += f1[-counter]
        else:
            string = string.replace(' ', '')
            lst[-1].append(string[::-1])
            string = ''
        counter += 1
    string = string.replace(' ', '')
    lst[-1].append(string[::-1])
    lst1.append(f[: -counter + 1])


def get_postcode_info(postcode):
    results = []
    for i in range(len(lst)):
        for j in lst[i]:
            if postcode == j:
                results.append([lst1[i], lst[i]])
    return results


def get_post_code_by_area(area_name):
    results = []
    for i in range(len(lst1)):
        if area_name.lower() == lst1[i].lower():
            results.append([lst1[i], lst[i]])
    return results


def contains_postcode(the_string):
    return len(the_string.split()[-1]) == 5 and the_string.split()[-1].isnumeric()
