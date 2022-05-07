
# słowniki

kraje = {'Litwa': 'Wilno', 'Białoruś': 'Mińsk', 'Ukraina': 'Kijów', 'Rosja': 'Moskwa', 'Niemcy': 'Berlin', 'Czechy': 'Praga', 'Słowacja': 'Bratysława'}


# sortowanie słownika wg klucza i wartości -> w domu

kraje.update({'Hiszpania':'Madryt'})

print(kraje.keys())
print(kraje.values())

print('----------------------------------------')

print(bool(''))
print(bool(' '))
print(bool(0))
print(bool(1))
print(bool('0'))
print(bool('1'))
print(bool([]))
print(bool([","]))

print('----------------------------------------')

napis = "Metody Inżynierii Wiedzy"
print(napis)

if "i" in napis:
    print("tak")
else:
    print("nie")

print('----------------------------------------')

for x in range(21):
    print(x)

print('----------------------------------------')
# split without using split()

def my_own_split(str):

    list = []
    tmp = ''
    for c in napis:
        if c == ' ':
            list.append(tmp)
            tmp = ''
        else:
            tmp += c
    if tmp:
        list.append(tmp)

    return list

print(my_own_split(napis))


print('----------------------------------------')

def pass_validate(passw):
    strength = [0, 0]

    if len(passw) < 10:
        return False
    elif '!' not in passw:
        return False

    for i in passw:
        if i.islower():
            strength[0] = 1
        elif i.isupper():
            strength[1] = 1

    if 0 in strength:
        return False

    return True

pass1 = 'HasLLLo123456!'
pass2 = 'haslosdsdsdsdds!'

print(pass_validate(pass1))
print(pass_validate(pass2))