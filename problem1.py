'''Problem Description:

You are given a positive integer r denoting the radius of a sphere as a parameter. Write a program to calculate the volume of the sphere. The volume of a sphere having
radius R is given by (4 * π * R3) / 3.

NOTE: Return the volume of the sphere up to two decimal places. You can use round().

NOTE2: Use pi as 22/7 (not math.pi).

Input Format:

The first line indicates the number of the test cases. For each testcase there will be one line of input:
The one line contains r in integer format.
Output Format:

The volume of the sphere in float format is printed for each testcase in a new line.
Sample Input:

1
8
Sample Output:

2145.52'''
def shape_of_sphere(r):
    pi=22/7
    volume=(4*pi*(r**3))/3
    return round(volume,2)

t=int(input("enter test cases:"))
for _ in range(t):
   r=int(input("enter r value"))
   print(shape_of_sphere(r))


