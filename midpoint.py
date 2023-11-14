import json

in_filename = 'original.geojson'

with open(in_filename) as f:
    data = json.load(f)

num_iterations = 3

for _ in range(num_iterations):
    for feature in data['features']:
        for j in range(len(feature['geometry']['coordinates'])):
            ring = feature['geometry']['coordinates'][j]
            new_ring = []
            if len(ring) < 3:
                print('error polygon ring length less than 3')
                exit()
            for i in range(len(ring) - 1):
                p0 = ring[i]
                p1 = ring[i + 1]
                new_ring.append([0.5 * (p0[0] + p1[0]), 0.5 * (p0[1] + p1[1])])
            feature['geometry']['coordinates'][j] = new_ring

out_filename = f'midpoint-{num_iterations}.geojson'

with open(out_filename, 'w') as f:
    json.dump(data, f)

