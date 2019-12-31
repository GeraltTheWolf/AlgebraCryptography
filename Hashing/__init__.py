import hashlib

ALGORITHM_NAMES = list(hashlib.algorithms_guaranteed)
ALGORITHM_NAMES.sort()


def hash_data(data, algorithm):
    m = hashlib.new(algorithm)
    try:
        # for text files
        m.update(data.encode('utf-8'))
    except:
        # for binary files
        m.update(data)
    try:
        return m.hexdigest()
    except:
        return m.hexdigest(len(data))
