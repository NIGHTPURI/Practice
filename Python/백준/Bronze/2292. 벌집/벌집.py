n = int(input())

layer = 1
end = 1
while n > end :
    end += layer*6
    layer += 1
    
print(layer)