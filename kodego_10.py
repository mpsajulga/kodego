print("What is the angle betwen the hands of a clock at 10.30?")

full_rotation = 360

deg_per_hour = 360/12
hours_inbetween = 4.5
degrees_inbetwen = (360/12)*hours_inbetween

print(f"A full rotation is 360 degrees and there are 12 hours in a clock-face.")
print(f"We'd get {deg_per_hour} degrees for every hour if we divide the degrees per hour: '360/12'.")
print("There are 4 and a half hours if we manually count clockwise from 10pm to 10:30pm wherein the short hand rests inbetween 10 and 11 while the long hand rests on 6pm.")
print(f"The degrees from the shorthand to longhand for 10:30pm is {degrees_inbetwen} degrees: (360/12)*{hours_inbetween}.")