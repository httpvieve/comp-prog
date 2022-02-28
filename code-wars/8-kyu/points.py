
def points(games):
        a = [x[0] for x in games]
        b = [x[2] for x in games]
        counter = 0
        for i in range(len(games)):
                if a[i] > b[i]:
                        counter += 3
                if a[i] == b[i]:
                        counter += 1
        return counter

print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))  