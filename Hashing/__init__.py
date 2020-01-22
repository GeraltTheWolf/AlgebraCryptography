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


def get_file_hash(file_path):
    block_size = 65536  # 64kb
    file_hash = hashlib.sha256()
    with open(file_path, 'rb') as f:
        fb = f.read(block_size)
        while len(fb) > 0:
            file_hash.update(fb)
            fb = f.read(block_size)
    return file_hash.hexdigest()