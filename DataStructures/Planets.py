def main(planets):
    # A spaceship is approaching some planets that are arranged in a line. It needs to pass through the line of the planets, but can't get too close to any planet, otherwise it would get caught in that planet's gravitational field.
    # Given a list of planets, where each planet is specified by its position along the line and the range of its gravitational field, compute the list of gaps in [0, 1000] through which the spaceship can fly.
    # This is best illustrated by a few examples:
    # input               output                               reasoning
    # [3,2],[5,1]         [0,1],[6,1000]                        The fields cover [1,5] and [6,6].
    # [2,1],[5,1],[0,4]   [6,1000]                             The fields cover [0,6].
    # [2,7],[0,4],[5,4]   [6.5,7.5],[3,5]                      The fields cover [0,4], [6.5,7.5], and [3,5].

    # Sort list
    # Merge overlapping planets
    # Find any empty space from 0 - 1000
    
    interval = []
    
    for planet in planets:
        interval.append([planet[0] - planet[1], planet[0] + planet[1]])
        
    interval.sort(key=lambda x: x[0])
    
    merged = []
    merged.append(interval[0])
    
    for i in range(1, len(interval)):
        if interval[i][0] <= merged[-1][1]:
            prevmax = merged[-1][1]
            merged[-1] = [merged[-1][0], max(interval[i][1], prevmax)]
        else:
            merged.append(interval[i])
    
    print(merged)
    
    maxi = 0
    mini = 0
    res = []
    
    for inter in merged:
        maxi = inter[0]
        if maxi == 0:
            mini = inter[1]
            continue
        else:
            res.append([mini, maxi])
        mini = inter[1]
    
    if mini < 1000:
        res.append([mini, 1000])
    
    print(res)
    return res

planets1 = [[3, 2], [5, 1]]
planets2 = [[2, 1], [6, 3]]
planets3 = [[2, 7], [0, 4], [5, 4], [4, 1]]

main(planets3)
