# def idx(arr):
#     mx = 0
#     mn = 0
#     for i in range(len(arr)):
#         if arr[i] > mx:
#             mx = arr[i]
#         elif arr[i] < mn:
#             mn = arr[i]
    
#     aux = [0]*(mx+1)
#     for i in range(len(arr)):
#         c = arr[i]
#         aux[c] += 1
#     for i in range(len(aux)):
#         for j in range(aux[i]):
#             print(i, end = " ")
    
# x = [1, 2, 5, 7, 6, 0, 2]
# idx(x)

class keyidx:
    def __init__(self, arr):
        mx = 0
        mn = 0
        for i in range(len(arr)):
            if arr[i] > mx:
                mx = arr[i]
            elif arr[i] < mn:
                mn = arr[i]
                self.posmn = abs(mn)
        self.aux = [0] * (mx + abs(mn) + 1)
        for i in range(len(arr)):
            c = arr[i]
            if c < 0:
                self.aux[c+self.posmn] += 1
            else:
                self.aux[c+self.posmn] += 1
        print(self.aux)
        # for  i in range(len(self.aux)):
        #     for j in range(self.aux[i]):
        #         print(i - self.posmn, end=" ")
                
    def search(self, val):
        for i in range(len(self.aux)):
            if val+self.posmn <= len(self.aux) and self.aux[val + self.posmn] >= 1 and val+self.posmn >= 0:
                return True
            else:
                return False
    def sort(self):
        for i in range(len(self.aux)):
            for j in range(self.aux[i]):
                print(i - self.posmn, end=" ")

x = [5, 7, -7, -5, -6, -3, -3]         
a = keyidx(x)
print(a.search(-7))
a.sort()