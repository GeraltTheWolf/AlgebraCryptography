import hashlib

algNames = list(hashlib.algorithms_guaranteed)

string_to_hash = b"Hello world"

m = hashlib.new(algNames[0])

m.update(string_to_hash)

try:
    hash = m.hexdigest()
except:
    hash = m.hexdigest(len(string_to_hash))


print(hash)











