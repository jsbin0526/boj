# import sys
# from collections import defaultdict
# input = sys.stdin.readline

# n, m = map(int, input().split())
# stops = [0] * n
# max_height = 0
# min_height = 0
# queries = []
# distances = defaultdict(dict)
# for i in range(n-1):
#     for j in range(i+1, n):
#         distances[stops[j]-stops[i]][i] = max(j-i, distances[stops[j]-stops[i]].get(i, 0))
#         distances[stops[j]-stops[i]][j] = max(j-i, distances[stops[j]-stops[i]].get(j, 0))

# for _ in range(m):  
#     target_distance = int(input())

#     max_key = max(distances[max_height - min_height], key=distances[max_height - min_height].get)
#     if distances[max_height - min_height][max_key] != target_distance:
#         max_height += 1
#         if target_distance < n//2 and max_height == 1 and min_height == 0:
#             min_height -= 1
#             stops[max_key] = min_height
#             queries.append(f"U {max_key+1} {min_height}")
#         distances[max_height - min_height][max_key] = target_distance
#         stops[max_key+target_distance] = max_height
#         queries.append(f"U {max_key+target_distance+1} {max_height}")
        
#     queries.append('P')
#     print(stops)
# print(len(queries), *queries, sep='\n')

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
stops = [0] * n
max_height = 0
targets = [(i, n-i-1) for i in range(n)]
target_index = 0
queries = []

for _ in range(m):
    target_distance = int(input())
    target = max(targets, key=lambda x: x[1])
    temp = []
    while target[1] != target_distance:
        max_height = max_height*-1 if max_height > 0 else max_height*-1+1
        if target_index - target_distance >= 0:
            target_index -= target_distance
            stops[target_index] = max_height
            queries.append(f"U {target_index + 1} {max_height}")
            for i, j in targets:
                pass
            temp.append((target_index - target_distance, target_distance))
        elif target_index + target_distance < n:
            target_index += target_distance
            stops[target_index] = max_height
            queries.append(f"U {target_index + 1} {max_height}")
            temp.append((target_index, target_distance))
        else:
            target_index = target_distance
            stops[target_index] = max_height
            queries.append(f"U {target_index + 1} {max_height}")
            temp.append((target_index, target_distance))
        target = max(temp, key=lambda x: x[1])
        targets = temp[:]
    print(stops)
            

    queries.append('p')

print(len(queries), *queries, sep="\n")