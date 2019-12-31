import hashlib

ALGORITHM_NAMES = list(hashlib.algorithms_guaranteed)
ALGORITHM_NAMES.sort()

def hash_data(data, algorithm):
    m = hashlib.new(algorithm)
    m.update(data.encode('utf-8'))
    try:
        return m.hexdigest()
    except:
        return m.hexdigest(len(data))
