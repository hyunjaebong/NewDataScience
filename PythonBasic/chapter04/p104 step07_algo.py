import  random
dataset = []
for i in range(10):
    r = random.randint(1,100)
    dataset.append(r)
print(dataset)

vmax = vmin = dataset[0]

for i in dataset:
    if vmax < i:
        vmax = i
    if vmin > i:
        vmin = i

print('max=', vmax, 'min=', vmin)