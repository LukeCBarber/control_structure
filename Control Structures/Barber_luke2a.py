#input
print('Your Screen Printing Quote')
print('')
shirt = int(input('How many T-shirts would you like to have printed? '))
color = int(input('How many colors will each shirt be printed with (1,2, or 3)? '))
print('')

#shirt price computation
if color ==1:
    if shirt >=250:
        cost = 5.0*shirt
    elif shirt >=100:
        cost = 6.0*shirt
    elif shirt <=99:
        cost = 8.0*shirt

if color ==2:
    if shirt >=250:
        cost = 6.0*shirt
    elif shirt >=100:
        cost = 7.0*shirt
    elif shirt <=99:
        cost = 9.0*shirt

if color ==3:
    if shirt >=250:
        cost = 7.0*shirt
    elif shirt >=100:
        cost = 8.0*shirt
    elif shirt <=99:
        cost = 10.0*shirt

total_cost = format(cost + (cost*.08875),',.2f')


#output
print(shirt,'shirts screen printed with',color,'colors:','$' + total_cost)
