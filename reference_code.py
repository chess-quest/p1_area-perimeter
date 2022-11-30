import shapes.area
import shapes.perimeter


def selection():
    print('----------------------')
    print('SELECT SHAPE')
    print('----------------------')
    print('1 - Circle')
    print('2 - Rectangle')
    print('3 - Square')
    print('4 - Triangle')

    shape = int(input('Shape number: '))
    while shape < 1 or shape > 4:
        shape = int(input('Shape number (1-4): '))

    return shape


def main():
    while True:

        shape_num = selection()

        computation = input('Computation (Area = 1 or Perimeter = 2): ')
        while (computation != '1') and (computation != '2'):
            computation = input('Enter 1 or 2: ')
        shape_val_2 = 0
        if computation == '1':
            match shape_num:
                case 1:
                    shape_val_1 = float(input('Circle radius: '))
                    print(f'Circle Area = {shapes.area.area_func(shape_num, shape_val_1, shape_val_2)}')
                case 2:
                    shape_val_1 = float(input('Rectangle length: '))
                    shape_val_2 = float(input('Rectangle height: '))
                    print(f'Triangle Area = {shapes.area.area_func(shape_num, shape_val_1, shape_val_2)}')
                case 3:
                    shape_val_1 = float(input('Square length: '))
                    print(f'Square Area = {shapes.area.area_func(shape_num, shape_val_1, shape_val_2)}')
                case 4:
                    shape_val_1 = float(input('Triangle length: '))
                    shape_val_2 = float(input('Triangle height: '))
                    print(f'Rectangle Area = {shapes.area.area_func(shape_num, shape_val_1, shape_val_2)}')
        else:
            shape_val_3 = 0
            match shape_num:
                case 1:
                    shape_val_1 = float(input('Circle radius: '))
                    print(f'Circle Perimeter = {shapes.perimeter.perimeter_func(shape_num, shape_val_1, shape_val_2, shape_val_3)}')
                case 2:
                    shape_val_1 = float(input('Rectangle length: '))
                    shape_val_2 = float(input('Rectangle height: '))
                    print(f'Rectangle Perimeter = {shapes.perimeter.perimeter_func(shape_num, shape_val_1, shape_val_2, shape_val_3)}')
                case 3:
                    shape_val_1 = float(input('Square length: '))
                    print(f'Square Perimeter = {shapes.perimeter.perimeter_func(shape_num, shape_val_1, shape_val_2, shape_val_3)}')
                case 4:
                    shape_val_1 = float(input('Triangle side 1: '))
                    shape_val_2 = float(input('Triangle side 2: '))
                    shape_val_3 = float(input('Triangle side 3: '))
                    print(f'Triangle Perimeter = {shapes.perimeter.perimeter_func(shape_num, shape_val_1, shape_val_2, shape_val_3)}')

        yn = input('Continue (y/n): ')
        while (yn != 'y') and (yn != 'n'):
            yn = input('Enter y or n: ')
        if yn == 'n':
            print('PROGRAM DONE')
            return


if __name__ == '__main__':
    main()
