""""
Common definitions for functions.
Authors: Amanda Gomez Gomez, Oussama El Azizi
"""

from collections import Counter
import urllib


def get_file_words(file_name, http_server, reducer):
    """
    Download file via HTTP and normalize its words.

    :param file_name: file to be downloaded
    :param http_server: HTTP server URL
    :param reducer: reducer instance to start the timing
    :return: Map with all words
    """
    punc = ',.:;!?-_\'\"+=/*&^%$#@[]()'
    mapped_words = Counter()
    # Assuming the file already exists
    print "Downloading " + file_name
    file_name, _ = urllib.urlretrieve(http_server + '/parted/' + file_name, filename=file_name)
    print "Download done"
    reducer.set_init_time()
    print "Processing Starts"
    with open(file_name) as contents:
        for line in contents:
            mapped_words.update([val for val in [x.strip(punc).lower() for x in line.split()] if val != ''])
    print "Processing Done"
    return mapped_words


def word_count(data, values_list):
    """
    Creates a Map with frequencies of every word in a list.

    :param data: Map that contains frequencies
    :param values_list: list of words to be added
    :return: Updated Map
    """
    data.update(values_list)
    print '.'
    return data


def counting_words(data, values_list):
    """
    Adds the number of a list to a accumulator.

    :param data: accumulator
    :param values_list: list containing words
    :return: accumulator
    """
    data['total'] = data['total'] + sum(values_list.values())
    print '.'
    return data


def outputFormat(data, func):
    """
    Standard output format.

    :param data: result data
    :param func: function executed
    :return: the string with the result in output format
    """
    if func.__name__ == 'word_count':
        return 'Results for word_count\n---------------------------\nFrequencies are:\n' + str(data)
    return 'Results for counting words\n---------------------------\nTotal count of words: ' + str(data['total'])
