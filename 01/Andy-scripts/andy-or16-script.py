# script to automate Or16 gate hdl
for i in range(16):
    print "Or(a = a[" + str(i) + "], b = b[" + str(i) + "], out = out[" + str(i) + "]);"