s = input().strip()
ch = ['dz=', 'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']

for c in ch:
    s = s.replace(c, '*')

print(len(s))