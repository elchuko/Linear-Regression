import data_0_request_and_save_ as d0rs
import data_1_into_2D_list_ as d1il
import data_2_row_types_ as d2rt
import data_3_column_types_ as d3ct
import data_4_column_stats_ as d4cs

import numpy as np


def data_0_request_and_save(data_url):
    response = d0rs.request_data(data_url)
    if response is not None:
        file_name = d0rs.save_data(response, "Mis_datos.txt")


def data_1_into_2D_list():
    print("-" * 80)
    print("DATA TABLE SIZE: ")
    xz = d1il.make_2D_list(file_name, header_lines=0,
            footer_lines=0, strip=True, lower=True)
    frequencies = d1il.get_row_sizes(xz)
    return xz
    

def data_2_row_types(xz):
    print("-" * 80)
    print("ROW DATA TYPES:")
    d2rt.row_types(xz)
    d2rt.print_row_types()

    d2rt.filter_bad_rows(xz)
    d2rt.row_types(xz)
    d2rt.print_row_types()


def data_3_column_types(xz):
    print("-" * 80)
    print("COLUMN DATA TYPES: ")
    xz_c_types = d3ct.column_types(xz)
    d3ct.print_column_types()
    xzv = d3ct.xz_str_to_type(xz, xz_c_types)


def data_4_column_stats(xz):
    print("-" * 80)
    print("COLUMN STATISTICS:")

    # For each column (according to the last row of 2D list)
    for c in range(len(xz[-1])):
        # If it is a float data type
        if isinstance(xz[-1][c], float):
            # Create the column of interest
            column = []
            for row in xz:
                column.append(row[c])
            print("-" * 30)
            ca = np.array(column)
            mean, std = d4cs.mean_std(ca)
            print("COLUMN", c)
            print("    mean =", format(mean, '12.6f'))
            print("     std =", format(std, '12.6f'))
            percentile_boundaries = d4cs.percentiles(ca, 4)
            print("    percentile boundaries:")
            print("       ", percentile_boundaries)
        else:
            # Create the column of interest
            column = []
            for row in xz:
                column.append(row[c])
            print("-" * 30)
            print("COLUMN", c)
            base_size, frequencies = d4cs.discrete_analysis(column)
            d4cs.print_frequencies(frequencies)


if __name__ == "__main__":
    print()
    data_url = ("https://archive.ics.uci.edu/ml/machine-learning-" +
            "databases/undocumented/connectionist-bench/" +
            "sonar/sonar.all-data")
    # data_0_request_and_save(data_url)
    print("Data is already downloaded.")
    input("\nPress [Enter] to continue! ")

    file_name = "my_data/my_try_.csv"
    #file_name = "my_float_char_.csv"
    #file_name = "my_missing_.csv"
    print("\nFilename:  ", file_name)

    xz = data_1_into_2D_list()
    input("\nPress [Enter] to continue! ")

    data_2_row_types(xz)
    input("\nPress [Enter] to continue! ")

    data_3_column_types(xz)
    input("\nPress [Enter] to continue! ")

    data_4_column_stats(xz)
    input("\nPress [Enter] to continue! ")

