from glom import glom, Coalesce

data = {'a': {'b': {'c': 'd'}}}
data['a']['b']['c']
data.get('a').get('b').get('c')
data.get('a', {}).get('b', {}).get('c')

glom(data, 'a.b.c')

target = {'system': {'planets': [{'name': 'earth', 'moons': 1},
                                 {'name': 'jupiter', 'moons': 69}]}}

# 自定义的格式
spec = {'names': ('system.planets', ['name']),
        'moons': ('system.planets', ['moons'])}
print(glom(target, spec))
# {'moons': [1, 69], 'names': ['earth', 'jupiter']}


# Coalesce 合并
spec = {'names': (Coalesce('system.planets', 'system.dwarf_planets'), ['name']),
        'moons': (Coalesce('system.planets', 'system.dwarf_planets'), ['moons'])}
print(glom(target, spec))

# 求和
print(glom(target, {'moon_count': ('system.planets', ['moons'], sum)}))


target = {
    'data': {
        'name': 'just_test',
        'likes': [{'ball': 'basketball'},
                  {'ball': 'football'},
                  {'water': 'swim'}]
    }
}

# 希望 {'name': 'just_for_test', 'likes': ['basketball', 'football', 'water']}


spec = {
    'name': ('data.name'),
    'likes': ('data.likes', [lambda x: x.values()[0] if 'ball' or 'water' in x.keys() else '']),
}

print(glom(target, spec))