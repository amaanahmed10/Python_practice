height_calibration = input('Estimated height(feet): ')

if int(height_calibration)>= 400:
    print("Reduce flight height and restart")
elif int(height_calibration)<=0:
    print("Wrong height value!")
else:
    print("Cleared to take-off")