def myhash(data):
    blocksize = 16
    digest = [0]*blocksize
    # digest = [0,0,0,0], blocksize = 4
    dataIndex = 0
    end = False
    for i in range(blocksize):
        while dataIndex < len(data) and not end:
        #    print(digest)
            for i in range(blocksize):
                if dataIndex == len(data):
                    dataIndex = 0
                    end = True
                digest[i] = digest[i]^ord(data[dataIndex])
                dataIndex += 1
        return digest
    
data = input("Data: ")
h = (myhash(data))
for i in range(len(h)):
    print('{:02x}'.format(h[i]),end='')
print()
