
'''
ref: https://projecteuler.net/problem=18

Reduces to https://en.wikipedia.org/wiki/Widest_path_problem
which can be solved by inverting weights and using Dijkstra's algorithm

Answer: 1074
'''

Numstr = \
'''
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''

Nums = [[int(n) for n in line.split(' ')]
            for line in Numstr.strip().split('\n')]
# print(Nums)

def all_edges(Nums):
    edges = []
    for line in range(len(Nums) - 1):
        for x in range(line + 1):
            edges.append((Nums[line][x] + Nums[line + 1][x], (line, x, line + 1, x), (Nums[line][x], Nums[line + 1][x])))
            edges.append((Nums[line][x] + Nums[line + 1][x + 1], (line, x, line + 1, x + 1), (Nums[line][x], Nums[line + 1][x + 1])))
            # print(Nums[line][x], Nums[line + 1][x])
            # print(Nums[line][x], Nums[line + 1][x + 1])
    return edges


from pprint import pprint

pprint(sorted(all_edges(Nums), reverse=True))


def edge(G, Nums, line, x, offset):
    k1 = '{}-{}'.format(line, x)
    k2 = '{}-{}'.format(line + 1, x + offset)
    capacity = Nums[line][x] + Nums[line + 1][x + offset]
    G.add_node(k1)
    G.add_node(k2)
    G.add_edge(k1, k2, weight=1. / max(1, capacity), capacity=Nums[line + 1][x + offset])
    # print(k1, k2, capacity)


import networkx as nx
G = nx.DiGraph()


for line in range(len(Nums) - 1):
    for x in range(line + 1):
        edge(G, Nums, line, x, 0)
        edge(G, Nums, line, x, 1)
        # print(line, x, Nums[line][x], Nums[line + 1][x + 0])
        # print(line, x, Nums[line][x], Nums[line + 1][x + 1])
print('nodes:', sorted(G.nodes()))
print('edges:', sorted(G.edges()))
# print(nx.maximum_flow(G, '0-0', '1-0'))

last_row = len(Nums) - 1

from pprint import pprint
for n in range(len(Nums)):
    path = nx.dijkstra_path(G, '0-0', '{}-{}'.format(last_row, n))
    print(path)
    path_weight = ([G[x][y]['capacity'] for x, y in zip(path, path[1:])])
    print(sum(path_weight), path_weight)

