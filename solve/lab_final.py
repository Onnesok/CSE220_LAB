def array(n):
    i = 1
    arr = ["-1"]*n
    while i <= n:
        arr[i-1] = i
        i+= 1
    return arr

def game(n, k, start = 0):
    if type(n) == int:
        temp = array(n)
        n = temp
    if len(n) == 1:
        return n[0]
    
    start = (start + (k-1))%len(n)
    n.pop(start)
    return game(n, k, start = start)
    

print(game(5, 2))

#lab_final