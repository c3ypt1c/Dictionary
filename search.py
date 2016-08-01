words = "words.txt"
custo = "cwords.txt"

def read(loc):
    errorLog = []
    try:
        ##print ( "Reading" )
        f = open ( loc, "rb" )
        fdd = f.read()
        f.close()
        del f                                                       #saves a byte of memory or so...
        ##print ( "Success!" )
        try:
            ##print ( "Decoding" )
            fdd = fdd.decode().lower().split("\r\n")                  #decoding from UTF-8 to string.lower() and splitting into actual words
            ##print ( "Success" )
        except Exception as e:
            print ( "Fail" )
            errorLog.append([e])
    except Exception as e:
        print ( "Fail" )
        errorLog.append([e])

    a = [fdd, errorLog]

    return a

fd = read(words)
additional = read(custo)

for y in range (0,2):
    for x in additional[y]:
        fd[y].append(x)

ww = fd[0][:]

del additional

def write(words, loc):
    strr = ""
    for x in words:
        strr += str ( x ) + "\n\r"
    f = open ( loc, "wb" )
    f.write(strr.encode())
    f.close()

while True:
    word = input ( "Is the word in the dictionary?> " ).lower()
    auth = False
    for x in ww:
        auth = auth or x == word
        if auth:
            break

    if auth:
        print ( "Yes,", word, "is in the file" )
    else:
        print ( "No! Automatically adding:", word )
        ww.append( word )
        ww.sort()
        afd = read( custo )
        afd[0].append(word)
        write( afd[0], custo )
        fd[1].append(afd[1])
        del afd
