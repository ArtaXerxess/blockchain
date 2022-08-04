import hashlib
def getSubString(msg,chunkLength):
    subStrings = []
    for i in range(0,len(msg),chunkLength):
        subStrings.append(msg[i:i+chunkLength])
    return subStrings
def getHash(subStrings):
    hashes = []
    for subString in subStrings:
        subStrHash = hashlib.sha256(str(subString).encode()).hexdigest()
        print("Hash value of ",subString," is ",subStrHash)
        hashes.append(subStrHash[:4])
    return hashes
def getMerkleRoot(merkleLeaves,level):
    if len(merkleLeaves)==1:
        return merkleLeaves
    root = []
    for i in range(0,len(merkleLeaves),2):
        if i == len(merkleLeaves) -1:
            root.append(merkleLeaves[i])
        else:
            root.append(merkleLeaves[i]+merkleLeaves[i+1])
            print("At level ",level," hashes are ",root)
    leaf = getMerkleRoot(root,level+1)
    return leaf
msg = input("Enter the input string: ")
chunkLength = int(input("Enter the chunk length: "))
subStrings = getSubString(msg,chunkLength)
print("Substrings generated: ",subStrings)
print()
merkleLeaves = getHash(subStrings)
print()
print("Merkle leaves(of length 4): ",merkleLeaves)
print("Merkle root: ",getMerkleRoot(merkleLeaves,2))