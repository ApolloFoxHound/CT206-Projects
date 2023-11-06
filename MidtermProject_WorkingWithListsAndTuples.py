# Lists and Tuples
# https://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/05_ListsTuples/Pascal/
# Pascal's Triangle

# user input the height
while True:
    h = input("Please input the height of Pascal's Triangle: ")
    if h.isdigit() and int(h) > 0:
        h = int(h)
        break
    else:
        print("You should input a positive number. Try again.")

tri = [[1]]  # create a list representing the triangle

if h > 1:
    tri.append([1, 1])  # append the second row into the triangle
    for i in range(3, h + 1):
        new_row = []  # this is the new row we will generate
        last_row = tri[-1]  # the new row is based on the last row of current triangle

        new_row.append(1)  # the leftmost number is 1
        for j in range(i - 2):
            new_row.append(last_row[j] + last_row[j + 1])
        new_row.append(1)  # the rightmost number is 1

        tri.append(new_row)  # add the new row into the triangle

# output
last_line = ' '.join([str(j) for j in tri[-1]])
slots = len(last_line)
for i in range(h):
    line = ' '.join([str(j) for j in tri[i]])
    print(line.center(slots))
