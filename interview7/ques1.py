'''
Read a file
'''
baseFilename = 'names_list_00.txt'

cfile = open('c_'+baseFilename, 'a')
cppfile = open('cpp_'+baseFilename, 'a')
csfile = open('cs_'+baseFilename, 'a')
f = open(baseFilename, 'r')

for line in f:
    # print(line, end='')
    arr = line[0:len(line)-1].split('.')
    if arr[1] == 'c':
        cfile.write(line)
    elif arr[1] == 'cpp':
        cppfile.write(line)
    elif arr[1] == 'cs':
        csfile.write(line)

cfile.close()
cppfile.close()
csfile.close()