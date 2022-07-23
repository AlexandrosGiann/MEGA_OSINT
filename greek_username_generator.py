from greek_to_greeklish import to_greeklish

def generate_usernames(first_name, last_name):
    lst = []
    for x in to_greeklish(first_name):
        for y in to_greeklish(last_name):
            lst.append(x + y)
            lst.append(x + '.' + y)
            lst.append(x + '_' + y)
            lst.append(x + '_' + y + '_')
            lst.append(x + y + '_')
            lst.append(x[0] + y)
            lst.append(x[0] + '.' + y)
            lst.append(x[0] + '_' + y)
            lst.append(x[0] + '_' + y)
            lst.append(x[0] + '_' + y + '_')
            lst.append(x + y[0] + '_')
            lst.append(x + y[0])
            lst.append(x + '.' + y[0])
            lst.append(x + '_' + y[0])
            lst.append(x + '_' + y[0] + '_')
            lst.append(x + y[0] + '_')
    for x in to_greeklish(last_name):
        for y in to_greeklish(first_name):
            lst.append(x + y)
            lst.append(x + '.' + y)
            lst.append(x + '_' + y)
            lst.append(x + '_' + y + '_')
            lst.append(x + y + '_')
            lst.append(x[0] + y)
            lst.append(x[0] + '.' + y)
            lst.append(x[0] + '_' + y)
            lst.append(x[0] + '_' + y)
            lst.append(x[0] + '_' + y + '_')
            lst.append(x + y[0] + '_')
            lst.append(x + y[0])
            lst.append(x + '.' + y[0])
            lst.append(x + '_' + y[0])
            lst.append(x + '_' + y[0] + '_')
            lst.append(x + y[0] + '_')
    return lst

name = input("Εισάγετε ονοματεπώνυμο:")
print(name.split())
for username in generate_usernames(name.split()[0], name.split()[1]):
    print(username)
