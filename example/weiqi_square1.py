#围棋棋盘由横纵19*19条线组成，这些线共组成多少个正方形？

def  horizontalVertical(hr,vl):
    num = 0
    if vl>=hr:
        i = 1
        while i < hr:
            num +=  (hr-i)*(vl-i)

    else:
        i = 1
        while i < vl:
            num += (hr - i) * (vl - i)
    print(num)
horizontalVertical(19,19)



