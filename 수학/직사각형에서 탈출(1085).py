x, y, w, h = map(int, input().split())

dist1 = w - x
dist2 = h - y

dist_list = [x, y, dist1, dist2]

print(min(dist_list))
