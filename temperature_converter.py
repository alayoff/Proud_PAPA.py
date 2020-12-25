# 1st ever project, a degrees converter with a letter change.

str_temperature = input('''\t\t\t  Enter a degree number.
Add \"F\" if it's Fahrenheit, Add \"C\" if it's Celsius.
 \t\t\t  example: 50F\n:''').upper()
kind = str_temperature[-1]

if kind == 'F' and len(str_temperature) == 3:
    fahrenheit_above_9 = float(str(str_temperature[:2]))
    print(((fahrenheit_above_9*5-160) / 9),
          (kind.replace('F', 'C')))
elif kind == 'F' and len(str_temperature) == 2:
    fahrenheit_below_10 = float(str(str_temperature[:1]))
    print(((fahrenheit_below_10*5-160) / 9),
          (kind.replace('F', 'C')))
elif kind == 'C' and len(str_temperature) == 3:
    celsius_above_9 = float(str(str_temperature[:2]))
    print(((celsius_above_9*9 + 32*5) / 5),
          (kind.replace('C', 'F')))
elif kind == 'C' and len(str_temperature) == 2:
    celsius_below_9 = float(str(str_temperature[:1]))
    print(((celsius_below_9*9 + 32*5) / 5),
          (kind.replace('C', 'F')))
else:
    print('Oops, something is wrong, please try again!\nexample: 50F ')
