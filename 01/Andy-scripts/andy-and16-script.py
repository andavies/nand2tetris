# script to automate And16 gate hdl
for i in range(16):
    print "And(a = a[" + str(i) + "], b = b[" + str(i) + "], out = out[" + str(i) + "]);"