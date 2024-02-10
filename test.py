class lak:
    a = []
    def __init__(self,x):
        self.x = x
        self.a.append(self.x)

    def update(self):
        self.x+=1

ab = lak(1)
while True:
    print(lak.a)
    print(ab.x)
    ab.update()