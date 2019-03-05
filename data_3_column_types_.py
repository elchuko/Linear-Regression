# Types searched for:
_TYPES = ("COLUMN:", "   float", "     inf", "     nan", "     int", 
           "    bool", "     str", "   empty")

# List of columns, containing counts of data types
_xz_cdt = []


def column_types(xz):
    # For each column of the 2D list (list of lists)
    for cr in range(len(xz[-1])):
        # Create a list of data type counters set to zeros
        _xz_cdt.append([0] * len(_TYPES))
        # See "_TYPES" global tuple above.

        # Set the number of the column
        _xz_cdt[cr][0] = cr

        # For each row in 2D list
        for row in xz:
            # Pick item in the column cr
            item = row[cr]

            # Standardize the representation of infinity 
            # to positive or negtive 'inf'
            if 'infinity' in item:
                if '-' in item:
                    item = '-inf'
                else:
                    item = 'inf'

            # Check if the item is of boolean type
            if item == "false" or item == "true":
                _xz_cdt[cr][5] += 1   # Count one more boole item
                # Start cycle for the next item
                continue

            # Check if the item is of integer type
            try:
                # Try converting item (string) to integer data type
                int(item)
            except ValueError:
                # If conversion fails, do nothing
                pass
            else:
                # If conversion is succesful, count the item
                _xz_cdt[cr][4] += 1     # Count one more integer
                # Start cycle for the next item
                continue

            # Check if the item is "not a number"
            if item == 'nan':
                # If it is
                _xz_cdt[cr][3] += 1     # Count one more nan
                # Start cycle for the next item
                continue

            # Check if the item is "infinity"
            if (item == "inf" or item == "-inf"):
                # If it is
                _xz_cdt[cr][2] += 1     # Count one more infinity
                # Start cycle for the next item
                continue

            # Check if the item is of float type
            try:
                # Try converting item (string) to float data type
                float(item)
            except ValueError:
                # If conversion fails, do nothing
                pass
            else:
                # If conversion is succesful, count the item
                _xz_cdt[cr][1] += 1     # Count one more float
                # Start cycle for the next item
                continue

            # If item (string) is not empty
            if len(item) > 0:
                _xz_cdt[cr][6] += 1     # Count one more string
                continue
            # If item (string) is empty
            else:
                _xz_cdt[cr][7] += 1     # Count one more empty item

    return _xz_cdt


# Print data types of columns, first z then xz
def print_column_types():
    ''' Prints each column number with
        frequencies of column's data types.
    '''
    # The "dt" is a row of the global "_xz_cdt" list
    def print_cr(dt):
        # Printing column number then frequencies one by one.
        print(format(dt[0], '7d'), end=" ")
        # Avoid printing frequency 0,
        if dt[1] > 0:
            print(format(dt[1], '7d'), end=" ")
        # instead print empty space.
        else:
            print(" " * 7, end=" ")
        if dt[2] > 0:
            print(format(dt[2], '7d'), end=" ")
        else:
            print(" " * 7, end=" ")
        if dt[3] > 0:
            print(format(dt[3], '7d'), end=" ")
        else:
            print(" " * 7, end=" ")
        if dt[4] > 0:
            print(format(dt[4], '7d'), end=" ")
        else:
            print(" " * 7, end=" ")
        if dt[5] > 0:
            print(format(dt[5], '7d'), end=" ")
        else:
            print(" " * 7, end=" ")
        if dt[6] > 0:
            print(format(dt[6], '7d'), end=" ")
        else:
            print(" " * 7, end=" ")
        if dt[7] > 0:
            print(format(dt[7], '7d'), end=" ")
        else:
            print(" " * 7, end=" ")
        # Move to new line.
        print()

    # Printing data type frequency for each column of "xz"
    # which is represented by a row in "_xz_cdt"
    for row in range(len(_xz_cdt)):
        # Repeat header every 10 printed lines
        if row % 10 == 0:
            # To print header join _TYPES in one string.
            print("".join(_TYPES))
        # Print the row by calling the above inner function.
        print_cr(_xz_cdt[row])


def xz_str_to_type(xz, c_types):
    types = ("float", "inf", "nan", "int", "bool", "str", "empty")
    # Identify number of rows and columns of the 2D data list
    R = len(xz)
    C = len(c_types)

    # For each column
    for Cj in range(C):
        # Extract frequency information (items from 1 onward)
        frequencies = c_types[Cj][1:]
        # Find the highers frequency
        max_value = max(frequencies)
        # Find index of data type with highest frequency
        index = frequencies.index(max_value)
        # Convert strings to appropriate data type
        if index == 0:
            _set_to_float(xz, R, Cj)
        elif index == 3:
            _set_to_int(xz, R, Cj)
        elif index == 4: 
            _set_to_bool(xz, R, Cj)
        elif index == 5:
            # Do nothing because colum already contains strings
            pass
        else:
            raise Exception("Invalid conversion to type \"" +
                    types[index] + "\" was requested!") 
    return xz


def _set_to_bool(xz, R, Cj):
    ''' Convert the column Cj into boole data type,
        represented as 0 for False and 1 for True.
        Count the number of failed conversions.
    '''
    failed = 0
    for Ri in range(R):
        if xz[Ri][Cj] == 'false':
            xz[Ri][Cj] = 0          # 0 == False
        elif xz[Ri][Cj] == 'true':
            xz[Ri][Cj] = 1          # 1 == True
        else:
            failed += 1
    if failed:
        print("\nConversion failed in column ", Cj, ".\nFailures:  ",
                failed, ", ", format(failed / R, '7.2%'), sep="")
    return failed, round(failed / R, 4)
    

def _set_to_int(xz, R, Cj):
    ''' Convert the column Cj into integer data type,
        Count the number of failed conversions.
    '''
    failed = 0
    for Ri in range(R):
        try:
            xz[Ri][Cj] = int(xz[Ri][Cj])
        except:
            failed += 1
    if failed:
        print("\nConversion failed in column ", Cj, ".\nFailures:  ",
                failed, ", ", format(failed / R, '7.2%'), sep="")
    return failed, round(failed / R, 4)


def _set_to_float(xz, R, Cj):
    ''' Convert the column Cj into floating-point data type,
        Count the number of failed conversions.
    '''
    failed = 0
    for Ri in range(R):
        try:
            xz[Ri][Cj] = float(xz[Ri][Cj])
        except:
            failed += 1
    if failed:
        print("\nConversion failed in column ", Cj, ".\nFailures:  ",
                failed, ", ", format(failed / R, '7.2%'), sep="")
    return failed, round(failed / R, 4)


if __name__ == "__main__":
    pass
