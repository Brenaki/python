print('===== Challenge 02 =====')

day = input ('What day were you born?\n')
month = input ('What month were you born?\n')
year = input ('What year were you born?\n')

for m in month:
    
    if month == '1':
        m = 'January'
        break
    
    elif month == '2':
        m = 'February'
        break
    
    elif month == '3':
        m = 'March'
        break
    
    elif month == '4':
        m = 'April'
        break

    elif month == '5':
        m = 'May'
        break

    elif month == '6':
        m = 'June'
        break

    elif month == '7':
        m = 'July'
        break

    elif month == '8':
        m = 'August'
        break

    elif month == '9':
        m = 'September'
        break

    elif month == '10':
        m = 'October'
        break

    elif month == '11':
        m = 'November'
        break

    elif month == '12':
        m = 'December'
        break
    else:
        m = 'Write one number, please!'




print('Your date of birth is', day, 'of', m, 'of', year+',', 'right?')
