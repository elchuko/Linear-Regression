''' The goal of this module is to load data from file to RAM.
    The structure used in RAM is a list of rows, 
    where each row is a list of strings.
    Individual items, identified by row and column,
    may be stripped of prefix and suffix empty space and lowercased.

    Then header and footer lines are eliminated.
    Finally empty lines are eliminated.
'''


def make_2D_list(filename, header_lines=0, footer_lines=0,
        strip=True, lower=True):
    ''' Move data from file into a list of rows,
        where each row is a list of items of type string.
        Also eliminates empty rows.
    '''
    in_file = open(filename, 'r')
    # Input-output (xz) list of rows starts empty
    rows = []
    # For each line (string) in a data file
    for line in in_file:
        # Create row by splitting line into list of items (strings)
        row_list = line.split(",")
        if strip:
            # Eliminate prefix and suffix whitespace in each item
            row_list = [item.strip() for item in row_list]
        if lower:
            # Convert all letters into lowercase
            row_list = [item.lower() for item in row_list]
        # Add row_list into a list of lists
        rows.append(row_list)

    # Calculate number of lines stored in "rows" list
    R = len(rows)

    # Eliminate header lines and footer lines
    xz = rows[header_lines:R - footer_lines]
    print("Eliminated header rows = ", format(header_lines, '3d'))
    print("Eliminated footer rows = ", format(footer_lines, '3d'))
    
    # Calculate number of lines stored in "xz" list
    R = len(xz)

    # Eliminate empty rows from bottom to top
    eliminated = 0
    for Ri in range(R - 1, -1, -1):
        # If a row Ri s an empty string,
        if xz[Ri] == ['']:
            # delete it
            del xz[Ri]
            eliminated += 1
    print("Eliminated empty  rows = ", format(eliminated, '3d'),
          format(eliminated / R, '7.2%'), "\n")

    # Return 2D list of data items. 
    return xz


def get_row_sizes(xz):
    ''' Count frequencies (items per row) of the 2D list of data.
        Desired distribution is: all rows with same amount of items.
    '''
    
    # Start with empty frequency list
    frequencies = []
    # Count the number of rows
    R = len(xz)
    # and if there are no rows (empty 2D list) exit the function
    if R == 0: 
        return None

    # For each row i
    for i in range(R):
        # count the number of items in this row
        Ci = len(xz[i])
        # Check in the list of frequencies 
        for list_ in frequencies:
            # If there is an entry with number of items == Ci
            if Ci == list_[1]:
                # increase frequency of such rows by 1
                list_[0] += 1
                # Exit checking the list of frequencies
                break
        # If list of frequencies has no entry with Ci
        else:
            # Add new entry into list of frequencies.
            frequencies.append([1, Ci])

    # Sort the list of frequencies from highest to lowest.
    frequencies = sorted(frequencies, reverse=True)
    # Print the report
    print(" ROWS: ITEMS:")
    for line_ in frequencies:
        print(format(line_[0], '6d'), format(line_[1], '6d'))

    return frequencies


if __name__ == "__main__":
    pass
