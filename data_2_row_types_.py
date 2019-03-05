# Types searched for:
_TYPES = ("   ROWS:", "   float", "     inf", "     nan", "     int", 
           "    bool", "     str", "   empty", "  ITEMS:")


# Frequency list of row types
_xz_rdt = []
# List of bad row indexes
_xz_bad_rows = []
# Bad rows have "not-a-number", "infinity", or empty string items.


def row_types(xz, strip_lower=True):
    ''' Report the frequency of row types 
        with respect to data types contained.
        Return the frequency list and list of bad rows.
    '''
    # Start with empty global lists
    global _xz_rdt
    global _xz_bad_rows
    _xz_rdt = []
    _xz_bad_rows = []

    # Count the number of rows in 2D list of data
    rows = len(xz)

    # For each row
    for r in range(len(xz)):
        # Create a list of data type counters set to zeros
        rdt = [0] * len(_TYPES)
        # See "_TYPES" global tuple above.

        # For each item (column) of the row
        for c in range(len(xz[r])):
            # Strip whitespaces and convert letters to lowercase.
            item = xz[r][c].strip().lower()
            # If modification is to be permanent
            if strip_lower:
                # modify the datum in the 2D list
                xz[r][c] = item

            # Standardize the representation of infinity 
            # to positive or negtive 'inf'
            if 'infinity' in item:
                if item[0] == '-':
                    item = '-inf'
                else:
                    item = 'inf'
            
            # Check if the item is of boolean type
            if item == "false" or item == "true":
                rdt[5] += 1         # Count one more boole item
                rdt[-1] += 1        # Count one more item in total
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
                rdt[4] += 1         # Count one more integer
                rdt[-1] += 1        # Count one more item in total
                # Start cycle for the next item
                continue

            # Check if the item is "not a number"
            if item == 'nan':
                # If it is
                rdt[3] += 1         # Count one more nan
                rdt[-1] += 1        # Count one more item in total
                # If this row is not in the list of bad rows
                if r not in _xz_bad_rows:
                    # Append its index to the list of bad rows
                    _xz_bad_rows.append(r)
                # Start cycle for the next item
                continue

            # Check if the item is "infinity"
            if (item == "inf" or item == "-inf"):
                # If it is
                rdt[2] += 1         # Count one more infinity
                rdt[-1] += 1        # Count one more item in total
                # If this row is not in the list of bad rows
                if r not in _xz_bad_rows:
                    # Append its index to the list of bad rows
                    _xz_bad_rows.append(r)
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
                rdt[1] += 1         # Count one more float
                rdt[-1] += 1        # Count one more item in total
                # Start cycle for the next item
                continue

            # If item (string) is not empty
            if len(item) > 0:
                rdt[6] += 1         # Count one more string
                rdt[-1] += 1        # Count one more item in total
            # If item (string) is empty
            else:
                rdt[7] += 1         # Count one more empty item
                rdt[-1] += 1        # Count one more item in total
                # If this row is not in the list of bad rows
                if r not in _xz_bad_rows:
                    # Append its index to the list of bad rows
                    _xz_bad_rows.append(r)
                # Start cycle for the next item

        # For each row in the list of row types
        for i in range(len(_xz_rdt)):
            # Check if row with same structure as this one exists
            if rdt[1:] == _xz_rdt[i][1:]:
                # If it does, increase frequency of such rows by 1
                _xz_rdt[i][0] += 1
                # Exit further search
                break
        else:
            # If no row as this one already exists, set frequency = 1
            rdt[0] = 1
            # Add row to the frequency list          
            _xz_rdt.append(rdt)
        # Continue with the next row

    # Sort list of lists by given column number
    column = 0
    _xz_rdt = sorted(_xz_rdt, key=lambda x: x[column], reverse=True)

    return _xz_rdt, _xz_bad_rows


def filter_bad_rows(xz):
    ''' Eliminate bad rows. Bad rows have:
        "not-a-number", "infinity", or empty string items.
        Returns number of eliminated bad rows
    '''
    # Count the number of rows in 2D list.
    total_rows = len(xz)
    # If there are no rows,
    if total_rows == 0:
        # exit the function.
        return 0

    # Count number of bad rows.
    bad_rows = len(_xz_bad_rows)
    # If there are bad rows
    if bad_rows > 0:
        # For each of the bad roes
        for row in range(bad_rows - 1, -1, -1):
            # Delete the bad row from 2D list.
            del xz[_xz_bad_rows[row]]

    # Calculate percentage of bad rows in 2D list
    percentage = bad_rows / total_rows
    print("\nEliminated bad rows = " + format(bad_rows, '6d'),
          format(percentage, '8.2%'), end="   ")
    if percentage > 0.10:
        print("WARNING: High Percentage of eliminated rows!\n")
    else:
        print()

    return bad_rows


def print_row_types():
    ''' Prints frequency of rows with a certain 
        frequencies of row data types.
    '''
    # The "dt" is a row of the global "_xz_rdt" list
    def print_row(dt):
        # Printing items of row, one by one.
        print(format(dt[0], '8d'), end=" ")
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
        if dt[8] > 0:
            print(format(dt[8], '7d'), end=" ")
        else:
            print(" " * 7, end=" ")
        # Move to new line.
        print()

    # Printing data type frequency for each row frequency
    for row in range(len(_xz_rdt)):
        # Repeat header every 10 printed lines
        if row % 10 == 0:
            # To print header join _TYPES in one string.
            print("".join(_TYPES))
        # Print the row by calling the above inner function.
        print_row(_xz_rdt[row])


if __name__ == "__main__":
    pass
