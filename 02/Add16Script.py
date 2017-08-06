# automates tedious code repetition in Add16.hdl
# Andy Davies 01/08/17

for i in range(16):
    print "FullAdder(a = a[" + str(i) + "], b = b[" + str(i) + "], c = c" + str(i) + ", sum = out[" + str(i) + "], carry = c" + str(i + 1) + ");"

    