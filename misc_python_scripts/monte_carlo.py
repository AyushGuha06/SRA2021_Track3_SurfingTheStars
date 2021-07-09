import numpy
number_that_landed_in_circle = 0
total = 0

while True:
    try:
        coords = numpy.random.random((1,2))
        total+=1
        if (coords[0][0]**2+coords[0][1]**2) < 1:
            number_that_landed_in_circle+=1
    except KeyboardInterrupt:
        break
print(4*number_that_landed_in_circle/total)
print(total)