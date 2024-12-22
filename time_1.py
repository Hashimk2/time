while (True):
    time = int(input('Please enter the time in 24 hours: '))
    convert = time - 1200
    if (time > 1259 and time < 2400):
        print ('The time in 12 hour format is: ', convert, 'PM')
    elif (time > 1159 and time < 1300):
        print('The time in 12 hour format is: ', time, 'PM' )
    elif (time >= 0 and time < 100):
        print('The time in 12 hour format is: ', time + 1200, 'AM')
    elif (time > 59 and time < 1201):
        print('The time in 12 hour format is: ', time, 'AM' )
    