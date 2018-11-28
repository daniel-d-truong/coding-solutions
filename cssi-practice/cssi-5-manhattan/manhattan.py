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
    min_steps = x_max*y_max

    for x in range(x_max):
        for y in range(y_max):
          temp = calculate_total_steps(coords, (x+1, y+1))
          if (temp < min_steps):
              min_steps = temp
              best_meeting = (x+1,y+1)

    return best_meeting

def calculate_total_steps(coords, (x,y)):
    x_total = 0
    for i in range(len(coords)):
        x_total += (abs(coords[i][0]) - x)

    y_total = 0
    for i in range(len(coords)):
        y_total += (abs(coords[i][1]) - y)

    return x_total + y_total
