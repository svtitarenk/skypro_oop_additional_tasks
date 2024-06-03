"""
fp = None
try:
    fp = open("myfile.txt")
    for t in fp:
        print(t)

except Exception as e:
    print(e)
finally:
    if fp is not None:
        fp.close()
"""

"""
fp = None
try:
    with open("myfile.txt") as f:
        for t in fp:
            print(t)
except Exception as e:
    print(e)
"""


class DefenedVector:
    def __init__(self, v):
        self.__v = v

    def __enter__(self):
        self.__temp = self.__v[:]
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:  # если никаких ошибок не было
            self.__v[:] = self.__temp

        return False


v1 = [1, 2, 3]
# v2 = [2, 3]  # пробуем, чтобы вызвать ошибку на строкe с перебором enumerate
v2 = [2, 3, 4]  # в это случае ошибки не возникает и копия меняет v1

try:
    with DefenedVector(v1) as dv:
        for i, a in enumerate(dv):
            dv[i] += v2[i]
except:
    print("Ошибка")

print(v1)
