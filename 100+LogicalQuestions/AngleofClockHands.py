# Calculate the angle between the hour hand and minute hand.
# Note: There can be two angles between hands; we need to print a minimum of two. 
# Also, we need to print the floor of the final result angle. 
# For example, if the final angle is 10.61, we need to print 10.

import math
#for every minute the minute hand move 6 degree 
#for every hour the hour hand makes 30 degrees and (360/12) and additional 0.5 degrees for 1 minutes (30degrees/60minutes)
#so , Hour hand angle = H*30 + M/2    


def getAngle(H, M):
    # Calculate angles for the hour and minute hands
    hour_angle = (H % 12) * 30 + (M * 0.5)
    minute_angle = M * 6

    # Calculate the absolute difference
    angle = abs(hour_angle - minute_angle)

    # Find the smaller of the two possible angles
    min_angle = min(angle, 360 - angle)

    # Return the floor of the angle
    return math.floor(min_angle)

H = int(input("Enter the hour (1-12): "))
M = int(input("Enter the minute (0-59): "))

#Output
print(f"The minimum angle between the hour and minute hands is: {getAngle(H, M)} degrees")