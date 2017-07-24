# script to automate Or16 gate hdl
for i in range(16):
    print "Mux(a = a[" + str(i) + "], b = b[" + str(i) + "], sel = sel, out = out[" + str(i) + "]);"