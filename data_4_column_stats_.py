import numpy as np


def discrete_analysis(a):
    ''' For categorical data type (factors)
        create a frequency table.
    '''
    categories = set(a)
    base_size = len(categories)
    frequencies = [0] * base_size
    frequencies = dict(zip(categories, frequencies))
    for category in a:
        frequencies[category] += 1
    return base_size, frequencies


def print_frequencies(frequencies):
    ''' Print frequency table.
    '''
    for key in frequencies:
        print(format(str(key), '>15s'), ": ", 
                format(str(frequencies[key]), '>7s'))


def mean_std(a):
    ''' Calculate mean and standard deviation
        of the received numeric data collection.
    '''
    a_arithmetic_mean = np.mean(a)
    a_standard_deviation = np.std(a)
    return a_arithmetic_mean, a_standard_deviation

    
def percentiles(a, n_tiles=4):
    ''' Calculate percentiles that divide the data
        into n groups with same percent of data.
    '''
    a_percentile_boundaries = []
    for i in range(n_tiles + 1):
        a_percentile_boundaries.append(round(
                np.percentile(a, i * 100 / n_tiles), 6))
    return a_percentile_boundaries


if __name__ == "__main__":
    pass
