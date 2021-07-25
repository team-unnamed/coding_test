real_answer = []
while(1):

    w, h = map(int, input().split())

    if w==0 and h==0:
        for a in real_answer:
            print(a)
        break

    Map = []

    for i in range(h):
        Map.append(list(map(int, input().split())))

    answer = 0
    for y in range(h):
        for x in range(w):
            if Map[y][x]==1:
                temp = [(x,y)]
                answer += 1
                Map[y][x]=0

                while temp:
                    a,b = temp[-1]
                    series = [(a-1,b-1), (a-1,b), (a-1, b+1), (a, b-1), (a, b+1), (a+1, b-1), (a+1, b), (a+1, b+1)]

                    for c,d in series:
                        if c>=0 and c<w and d>=0 and d<h and Map[d][c]==1:
                            temp.append((c,d))
                            Map[d][c]=0
                            break
                    else:
                        temp.pop(-1)

    real_answer.append(answer)