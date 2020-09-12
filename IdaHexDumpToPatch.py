def inputget():
    try:
        print("IDA Hex Dump to Patch by Haxxie")
        a = int(input("Offset: "), 16)
        print("Hex Dump: ")
        inp = input()
        b = ''
        while inp != "":
            b+=inp
            inp = input()
        convert(a, b)
    except:
        print("Error, check the input data.")
        inputget()
def convert(a, b):
    output = [[(str(format(a, 'x')).rjust(8, "0")).upper(), ' ']]
    outlen = 1
    outarrlen = [0]
    for i in b:
        if i != " ":
            if outarrlen[outlen - 1] >= 16:
                outarrlen+=[0]
                output+=[[(str(format(a + (8 * outlen), 'x')).rjust(8, "0")).upper(), ' ']]
                outlen+=1
            output[outlen - 1] += i
            outarrlen[outlen - 1] += 1
    for i in output:
        print(*i, sep = '')
    inputget()
inputget()
