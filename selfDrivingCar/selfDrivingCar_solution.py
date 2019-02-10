from copy import deepcopy
def prepare_ride(ride, i):
        startx, starty, endx, endy, startt, endt = ride.rstrip('\n').lstrip('\n').split(' ')
        distance = abs(int(endx) - int(startx)) + abs(int(endy) - int(starty))
        return (i, int(startx), int(starty), int(endx), int(endy), int(startt), int(endt), int(distance))

def calcDistance(vehicle, ride, b, s):
    distanceToStart = abs(vehicle[2][0]-ride[1]) + abs(vehicle[2][1] - ride[2])
    points = 0
    count = ride[6] if s > ride[6] else s
    print("vehicle: ", vehicle)
    print("ride: ", ride)
    print("distanceTostart: ", distanceToStart)
    if(distanceToStart + vehicle[1] < ride[5]):
        points = points + b + ride[7]
    elif((distanceToStart + vehicle[1]+ride[7])<ride[6]):
        points = points + ride[7]
    else:
        points = 0
    return (vehicle, ride, points, count)

with open("question.txt", "r") as q:
    r, c, v, ri, b, s = [int(item) for item in q.readline().rstrip('\n').lstrip('\n').split(' ')]
    print((r, c, v, ri, b, s))
    rides = [prepare_ride(line, ind) for ind, line in enumerate(q)]
    print(rides)
    rides = sorted(rides, key=lambda x: x[5])
    print(rides)

    vehicleMeta = [[0, 0, (0, 0), []] for _ in range(0,v)] #score, count, current/free pos for each vehicle
    print(vehicleMeta)

    minCount = 0
    infChech = 0
    while len(rides)>0:
        for index, ride in enumerate(rides):
            print("rides: ", rides)
            print("enumerate rides: ", enumerate(rides))
            print("index: ", index)
            print("ride: ", ride)
            vehicleIntermediate = [calcDistance(vehicle, ride, b, s) for vehicle in vehicleMeta]
            print("vehicleIntermediate: ", vehicleIntermediate)
            vehicleIntermediateSelected = sorted(vehicleIntermediate, key=lambda x: x[2])[-1]
            print("vehicleIntermediateSelected: ", vehicleIntermediateSelected)
            rides.pop(index)
            if(vehicleIntermediateSelected[2]>0):
                vehicleIntermediateSelected[0][1] = vehicleIntermediateSelected[0][1] + vehicleIntermediateSelected[1][7]
                vehicleIntermediateSelected[0][0] = vehicleIntermediateSelected[0][0] + vehicleIntermediateSelected[2]
                vehicleIntermediateSelected[0][2] = (ride[3], ride[4])
                vehicleIntermediateSelected[0][3].append(ride[0])
            # for vehicle in vehicleMeta:
            #     print("index: ", index)
                # if(ride[6]+vehicle[1]<=s):
                #     print("in")
                #     rides.pop(index)
                #     vehicle[1] = vehicle[1] + ride[6]
                #     vehicle[0] = vehicle[0] + ride[7]
                #     vehicle[2] = (ride[3], ride[4])
                #     break
                # print("ride[6]+vehicle[1]: ", ride[6]+vehicle[1])
    print("vehicles: ",vehicleMeta)
    print("rides: ", rides)

    with open("output.txt", "w") as o:
        for vehicle in vehicleMeta:
            stringToWrite = str(len(vehicle[3]))
            for ride in vehicle[3]:
                stringToWrite = stringToWrite + " " + str(ride)
            o.write(stringToWrite+"\n")
            print("writing to file: ", stringToWrite)