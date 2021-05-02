print('Welcome to Unit Converter!\nDo you want to Convert?(yes/no)')
x = input()

def print_menu():
    print('1.   Meter to Kilometer')
    print('2.   Kilometer to Meter')
    print('3.   Meter to Centimeter')
    print('4.   Centimeter to Meter')
    print('5.   Meter to Millimeter')
    print('6.   Millimeter to Meter')
    print('7.   Meter to Micrometer')
    print('8.   Micrometer to Meter')
    print('9.   Meter to Nanometer')
    print('10.  Nanometer to Meter')


if x.upper() == 'YES':
    print_menu()
else:
    break

def m_km():
    m = float(input('Enter your value in meter: '))
    km = m/1000
    print('Your value in Kilometers: {0}'.format(km))

def km_m():
    km = float(input('Enter your value in kilometer: '))
    m = km*1000
    print('Your value in Meters: {0}'.format(m))

def m_cm():
    m = float(input('Enter your value in meter: '))
    cm = m*100
    print('You value in centimeters: {0}'.format(cm))

def cm_m():
    cm = float(input('Enter your value in centimeter: '))
    m = cm/100
    print('Your value in Meters: {0}'.format(m))

def m_mm():
    m = float(input('Enter your value in meter: '))
    mm = m*1000
    print('Your value in Millimeters: {0}'.format(mm))

def mm_m():
    mm = float(input('Enter your value in Millimeters: '))
    mm = m/1000
    print('Your value in Meters: {0}'.format(m))

def m_mcr():
    m = float(input('Enter your value in meter: '))
    mcr = m*1000000
    print('Your value in Micrometers: {0}'.format(mcr))

def mcr_m():
    mcr = float(input('Enter your value in Micrometer: '))
    m = mcr/1000000
    print('Your value in Meters: {0}'.format(m))


def m_nm():
    m = float(input('Enter your value in Meter: '))
    nm = m*1000000000
    print('You value in Nanometers: {0}'.format(nm))
def nm_m():
    nm = float(input('Enter your value in Nanometer: '))
    m = nm/1000000000
    print('You value in Meters: {0}'.format(m))

choice = int(input('Enter the number of conversion you want from the menu: '))

if choice == 1:
    m_km()
if choice == 2:
    km_m()
if choice == 3:
    m_cm()
if choice == 4:
    cm_m()
if choice == 5:
    m_mm()
if choice == 6:
    mm_m()
if choice == 7:
    m_mcr()
if choice == 8:
    mcr_m()
if choice == 9:
    m_nm()
if choice == 10:
    nm_m()
