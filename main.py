#Import python labs
import os
import os.path as osp
import hashlib
import sys


# --- helpers ---

#Create write function
def write(text):
    """ helper for writing output, as a single point for replacement """
    print(text)

#Create file hash function
def filehash(filepath):
    blocksize = 64*1024 #Define blocksize
    sha = hashlib.sha256() #Create sha256
    with open(filepath, 'rb') as fp:
        while True:
            data = fp.read(blocksize)
            if not data:
                break
            sha.update(data)
    return sha.hexdigest() #return values

# --- /helpers ---

#Print output
write("""\n## Agent Hunt ##\n""")

ROOT = '.'
for root, dirs, files in os.walk(ROOT):
    for fpath in [osp.join(root, f) for f in files]:
        size = osp.getsize(fpath)#Get file values
        sha = filehash(fpath)#Create hash values for files using sha256
        name = osp.relpath(fpath, ROOT)#Get file names
        write('%s,%s,%s' % (size, sha, name))#Print output

#Create function to save output in a file
def writeToFile(path, content):
    file = open(path, "w")#Write path
    file.write(content)
    file.close()


PATH_TO_MY_FILE = './log.txt'#Save output in log.txt file
writeToFile(PATH_TO_MY_FILE, sha)#Save hash values only
