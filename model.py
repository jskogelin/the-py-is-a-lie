import random

class Faker:
    def __init__(self, lastnames, firstnames):
        self.types = {
            '__firstname__': firstnames,
            '__lastname__': lastnames
        }

    def reduce(self, config, id):
        data = {}
        for attr, value in config.items():
            if value == '__id__':
                data[attr] = id
            # this isnt exactly the best way to check this
            # todo: change this into something more robust
            elif '__' in value:
                rand_index = random.randint(0, len(self.types[value]) - 1)
                data[attr] = self.types[value][rand_index]
            # if this isnt something describing fake data
            # just it to whatever was in the config object
            else:
                data[attr] = value

        return data

# faker takes a config dict and returns a dict containing randomly generated
# strings, numbers, etc
faker = Faker(
    firstnames = [
        'Frank',
        'Dennis',
        'Dee',
        'Charlie',
        'Ronald',
        'Pamela',
        'Andrew'
    ],
    lastnames = [
        'Reynolds',
        'Kelly',
        'McDonald',
        'Beesly',
        'Malone',
        'Bernard'
    ]
)

# A ModelCollection takes a route config
# Randomly creates a number (n) based on the range specified in the config
# Creates n Models and stores them as a dict for easy access 
class ModelCollection:
    def __init__(self, config_range, data):
        num = random.randint(config_range[0], config_range[1])
        self.collection = {}
        for n in range(0, num):
            self.collection[n] = Model(config=data, id=n)
            
    def get_model_data(self):
        arr = []
        for attr, value in self.collection.items():
            arr.append(value.data)
        return arr


# Describes a model
class Model:
    def __init__(self, config, id):
        self.data = faker.reduce(config=config, id=id)
