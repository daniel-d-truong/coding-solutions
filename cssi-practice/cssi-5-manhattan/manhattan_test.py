from random import randint
from manhattan import find_meeting_point
import sys
import time

def test_meeting_point(coordinates, best_candidate):
    xs = [x for (x,y) in coordinates]
    ys = [y for (x,y) in coordinates]
    xs.sort()
    ys.sort()
    # x1 and x2 will be the same if we have an odd
    # number of points, they will be the two points
    # at the center of the array otherwise
    best_x1 = xs[(len(xs)-1)/2]
    best_x2 = xs[(len(xs))/2]
    best_y1 = ys[(len(ys)-1)/2]
    best_y2 = ys[(len(ys))/2]

    if (best_x2 >= best_candidate[0] >= best_x1 and
        best_y2 >= best_candidate[1] >= best_y1):
        return True
    else:
        return False

def create_random_coords(people_count, grid_size = (10000, 10000)):
    size_x = grid_size[0]
    size_y = grid_size[1]
    coords = [(randint(0,size_x), randint(0,size_y))
                for i in range(people_count)]
    return coords

def main(hugemode = False):
    fail = False;
    for size in [1, 2, 3, 5, 10]:
        print "Testing with: %d people." % size
        coords = create_random_coords(size, (50, 50))
        start = time.time()
        student_solution = find_meeting_point(coords)
        end = time.time()
        if not test_meeting_point(coords, student_solution):
            print ("\t\tYour solution: %s is not a valid one for coordinates: %s." %
                    (student_solution, coords))
            fail = True
            break
        else:
            print "\tOK, time to compute the solution: %fs" % (end - start)
    if hugemode:
        groups = [(10, 100), (100, 1000), (1000, 10000)]
    else:
        groups = [(10, 30), (30, 50), (50, 100)]
    for group in groups:
        if fail:
            break
        sizes = [randint(group[0],group[1]) for i in range(5)]
        sizes.sort()
        for size in sizes:
            print "Testing with: %d people." % size
            if hugemode:
                grid_size = (10000, 10000)
            else:
                grid_size = (500, 500)
            coords = create_random_coords(size, grid_size)
            start = time.time()
            student_solution = find_meeting_point(coords)
            end = time.time()
            if not test_meeting_point(coords, student_solution):
                print "\tYour solution: %s is not a valid one." % (student_solution,)
                fail = True
                break
            else:
                print "\tOK, time to compute the solution: %fs" % (end - start)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print sys.argv[1]
        main(sys.argv[1] == "huge")
    else:
        main()
