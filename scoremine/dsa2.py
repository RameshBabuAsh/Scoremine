def schedule_maker(schedule, court):
    out = {}
    for i in range(court):
        out[i] = []
    while(len(schedule)!=0):
        y = []
        for i in range(court):
            for j in range(len(schedule)):
                t = 0
                x = []
                x.append(schedule[j][0][0])
                x.append(schedule[j][0][1])
                x.append(schedule[j][1][0])
                x.append(schedule[j][1][1])
                if x[0] not in y and x[1] not in y and x[2] not in y and x[3] not in y:
                    t = 1
                    for k in range(len(x)):
                        y.append(x[k])
                    out[i].append(schedule[j])
                    schedule.pop(j)
                    break
            if t==0:
                out[i].append([0,0])
    z = 0
    for i in range(court):
        z = max(z, len(out[i]))
    for i in range(court):
        if len(out[i])!=z:
            for k in range(z-len(out[i])):
                out[i].append([0,0])
    return out


schedule=[]

no_of_courts=0

print(schedule_maker(schedule, no_of_courts))