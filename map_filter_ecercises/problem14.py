x,y,z=map(int,input().split())
max_of_three = lambda x, y, z: x if x > y and x > z else y if y > z else z


