person = {
    'name': 'Nicolas',
    'lastName': 'Molina',
    'langs': ['python', 'javascript'],
    'age': 99
}

print(person)

person['name'] = 'Santi'
person['age'] -= 50
person['langs'].append('rust')
print(person)

del person['lastName']
person.pop('age')
print(person)

print('items')
print(person.items())

print('keys')
print(person.keys())

print('values')
print(person.values())
