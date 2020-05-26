import json
import random
import timeit

# Setting up file for testing
with open('test.json', 'w') as f:
    data = {
        'depth1':
            [{
                'depth2':
                    [{
                        'depth3': [{}]
                    }]
            }]
    }

    json.dump(data, f)

start = timeit.default_timer()
for i in range(1000):
    with open('test.json') as f:
        data = json.load(f)

    n = {'number': i}
    rn = random.randint(1, 3)
    if rn == 1:
        data['depth1'].append(n)

    if rn == 2:
        data['depth1'][0]['depth2'].append(n)

    if rn == 3:
        data['depth1'][0]['depth2'][0]['depth3'].append(n)

    with open('test.json', 'w') as f:
        json.dump(data, f)

print('Write time: ', timeit.default_timer() - start)


print('Read time: ')
