def add(a, b):
    try:
        c = a/b
        return a
    except:
        return 'division to zero'
print(add(1,1))