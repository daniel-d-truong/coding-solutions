#coords is a list of tuples, representing coords of each location
def find_meeting_point(coords):
    x_max = coords[0][0]
    for coord in coords:
        if coord[0] > x_max:
            x_max = coord[0]

    y_max = coords[0][1]
    for coord in coords:
        if coord[1] > y_max:
            y_max = coord[1]

    best_meeting = (0,0)

    if len(coords) == 1:
        return coords[0]

    x_list = [coords[i][0] for i in range(len(coords))]
    y_list = [coords[i][1] for i in range(len(coords))]

    x_list.sort()
    y_list.sort()

    print x_list
    print y_list

    x_best_1 = x_list[len(coords)/2 - 1]
    x_best_2 = x_list[len(coords)/2]

    y_best_1 = y_list[len(coords)/2 - 1]
    y_best_2 = y_list[len(coords)/2]

    best = (0,0)

    coordinate_options = [
      (x_best_1, y_best_1),
      (x_best_1, y_best_2),
      (x_best_2, y_best_1),
      (x_best_2, y_best_2)
    ]

    results = [
      calculate_total_steps(coords, (x_best_1, y_best_1)),
      calculate_total_steps(coords, (x_best_1, y_best_2)),
      calculate_total_steps(coords, (x_best_2, y_best_1)),
      calculate_total_steps(coords, (x_best_2, y_best_2))
    ]

    min = results[0]
    best = (x_best_1, y_best_1)
    for i in range(len(results)):
        if results[i] < min:
            min = results[i]
            best = coordinate_options[i]


    return best

    # for i in range(len(coords)):
    #     for j in range(len(coords)):
    #         temp = calculate_total_steps(coords, (coords[i][0], coords[j][1]))
    #         if (temp < min_steps):
    #             min_steps = temp
    #             best_meeting = (coords[i][0], coords[j][1])


    # for x in range(x_max):
    #     for y in range(y_max):
    #       temp = calculate_total_steps(coords, (x+1, y+1))
    #       if (temp < min_steps):
    #           min_steps = temp
    #           best_meeting = (x+1,y+1)

    return best_meeting

def calculate_total_steps(coords, (x,y), type = False):
    x_total = 0
    for coord in coords:
        x_total += (abs(coord[0]) - x)
    y_total = 0
    for coord in coords:
        y_total += (abs(coord[1]) - y)
    if (type == False):
        return x_total + y_total
    else:
        return (x,y)
