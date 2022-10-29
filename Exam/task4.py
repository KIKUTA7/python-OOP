""" Task 4 [8 points]"""

"""
'transport.txt' contains data about the city
transport lines. Each line from the file describes
one transport. The line has following format:
'Origin,Destination,Time,Type'. 
For example if file contains following information:
~~~
A,B,5,Tram
B,C,3,Metro
B,C,15,Tram
B,C,2,Boat
~~~
It means that the city has 4 transports: 2 Trams, 1 Boat
and 1 Metro. We also know where each transport starts, 
where it goes, how many minutes it takes to reach the 
destination and what type of transport it is.

There are several ways to travel in the city:
1. You can take only 1 Tram
2. You can take only 1 Metro
3. You can take 2 Trams. The second tram's origin should be
   equal to the first one's endpoint. Ex.: A,B,5,Tram and
   B,C,15,Tram can be used to reach C from A in 20 minutes.

Other type of transports or other combinations, except given
above, can not be used.

You should write a function, that finds a minimum time
needed to travel between every possible pair of places, based
on the data from 'transport.txt'. There are only 4 destination/origin
places: A, B, C and D. Write the result in the output file - 'commute.txt'.

Each line in output file should have following format: 'origin,destination,time'.

If there is no valid path between 2 places, time should be equal to None.

For example, for the data given above output file will be:
~~~
A,B,5
B,A,None
B,C,3
C,B,None
A,C,20
C,A,None
~~~
"""

def commuteTime(filename):
    pass
    