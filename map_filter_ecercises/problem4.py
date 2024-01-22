func=lambda x:-x if x>0 else 2
numbers=list(map(int,input().split()))
new=list(map(func,numbers))
print(new)
