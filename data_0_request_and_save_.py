from urllib.request import urlopen


def request_data(data_url):
    ''' Obtain a key for accesing data and save it as response.
        Return the response
    '''
    try:
        response = urlopen(data_url)
    except Exception:
        raise Exception("Can not read url. " +
                "Verify Internet connection!")
    else:
        return response


def save_data(response, filename="0_requested_data_.txt"):
    ''' Reading line by line from Internet URL and 
        saving it into a text file.
    '''
    # Open text-file for writing.
    w_file = open(filename, 'w')
    for line_bin in response:
        # Convert a line from binary to text format.
        line_txt = line_bin.decode(encoding='utf8').strip() + '\n'
        # Write line to a text-file
        w_file.writelines(line_txt)
    w_file.close()
    print("Data is downloaded into file", filename)
    return filename


if __name__ == "__main__":
    # Test and example of usage code:

    data_url = ("https://archive.ics.uci.edu/ml/" +
            "machine-learning-databases/undocumented/" +
            "connectionist-bench/sonar/sonar.all-data")

    data_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/" +
            "00291/airfoil_self_noise.dat")

    response = request_data(data_url)
    if response is not None:
        file_name = save_data(response)

