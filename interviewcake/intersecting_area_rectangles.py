# find the intersecting area of two rectanges.
# 1. First check if left_x of rect_2 is leass than the left_x + width of rect_1
# 2. Then check if left_y of rect_2 is less than the left_y + height of rect_1
# 3. If both stand correct means there is an intersection
#       a. if both doesn't stand correct call the find_rectabgular_intersection by replacing position of both rectangles.
#       b. IF still no intersection then return False that there is no such rectangle
#       c. or to avoid this swap you can check which left_x is closer to 0
# 4. Calculating intersection
# 5.    width = (left_x + width of rect_1) - left_x of rect_2
# 6.    height = (left_y + height of rect1) - left_y of rect_2
# 7.    left_x = left_x of rect_2

def find_rectangular_intersection(rect_1, rect_2):

    pass

def main():
    rect_1 = {
        'left_x'   : 1,
        'bottom_y' : 1,
        'width'    : 6,
        'height'   : 3,
    }

    rect_2 = {
        'left_x'   : 5,
        'bottom_y' : 2,
        'width'    : 3,
        'height'   : 6,
    }

    find_rectangular_intersection(rect_1, rect_2)

if __name__ == "__main__":
    main()
