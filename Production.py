import os
import Color
from Extractor import Extract_Table
from Table import Display_Table
from Query import Create_Table_Query, Fill_Table_Query

print('Launching Application')
os.system('cls')

while True:
    print(Color.green, 'Welcome to SQL Vision', Color.reset, sep='')
    print('1) About\n2) Start Application')
    choice = int(input('Enter : '))

    if choice == 1:
        os.system('cls')
        print(f'{Color.green}SQL Vision{Color.reset}')
        print('Harnessing the power of image analysis and data processing, SQL Vision translates images into SQL queries.')
        print('By meticulously extracting key details and conducting thorough data processing, it generates SQL queries for seamless table creation.\n')
        print(f'Developer: {Color.yellow}Valerian Coelho{Color.reset}')
        print(f'Github:{Color.blue} https://github.com/ValerianCoelho{Color.reset}')
        print(f'Linked in:{Color.blue} https://www.linkedin.com/in/valerian-coelho-835193258/{Color.reset}')
        input()

    else:
        os.system('cls')
        path = input('Enter the Path of the Image : ')
        data = Extract_Table(path)

        try:
            column_names = data[0]
        except:
            print(Color.red, 'Extraction Failed', Color.reset, sep='')
            os.system('pause')
            exit(0)
            
        data_types = []
        constraints = []

        table_name = input('Enter the table name : ')
        os.system('cls')

        print('Fill in the column Data-Type and column constraints:-')

        for column in column_names:
            print(Color.green, f'{column}:-', Color.reset, sep='')
            data_type = input('Data Type : ')
            constraint = input('Constraint : ')

            data_types.append(data_type)
            constraints.append(constraint)

        while True:
            os.system('cls')
            Display_Table(data)
            print("If you are satisfied with the table click 'Enter'")
            print('If not enter the cell coord you wish to alter')
            cell = input('Coordinates (seperated by a comma) : ').replace(' ', '')
            if not cell:
                break
            else:
                try:
                    cell_x, cell_y = cell.split(',')
                except:
                    print(Color.red, 'Invalid Coordinates, Press Enter', Color.reset, sep='', end=' ')
                    input()
                    continue
                new_entry = input(f'Enter the Cell data for cell ({cell_x}, {cell_y}) : ')
                try:
                    data[int(cell_x)][int(cell_y)] = new_entry
                except:
                    print(Color.red, 'Table index out of Bounds, Press Enter', Color.reset, sep='', end=' ')
                    input()

        os.system('cls')

        print(Color.green, 'CREATE TABLE QUERY:-', Color.reset, sep='')
        print(Create_Table_Query(table_name, column_names, data_types, constraints))

        print(Color.green, '\nFILL TABLE QUERY:-', Color.reset, sep='')
        print(Fill_Table_Query(table_name, data))

        os.system('pause')
    os.system('cls')