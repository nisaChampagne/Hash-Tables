
import hashlib

## hashtables will not be full

## change key = changing hash

key = b"str"

key2 = b"mom"
#bit string / bit-like object
# b strips the string object away and makes it a bit-like object

my_string = 'This is a normal string. Nothing to see here'
#string object

# my_string = 'This is a normal string. Nothing to see here'.encode()

# for i in range(10):
    # print(hashlib.sha256(key))
    # hashed = hashlib.sha256(key)
    # breakpoint()
    # gave a hash location ten times with ^

    # in terminal use ex: hashed.hexdigest() to get hash
    ### built in method! invoke when using

    # hashed = hashlib.sha256(key).hexdigest()
    # print(hashed)


for i in range(10):
    hashed = hash(key)
    # every time you use hash and run the code, the hash will change! hard for debugging
    print(hashed)

for i in range(10):
    hashed = hash(key2)
    # every time you use hash and run the code, the hash will change! hard for debugging
    print(hashed % 8) # give us an index
    # 8 is just for 8 spaces in storage btw

