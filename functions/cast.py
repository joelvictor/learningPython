# Casts to another type
# Only numbers can be converted to number types

number123 = 123
print("Cast str to ",type(number123), number123)

str = str(number123)
print( "Cast int to ",type(str), str)

fl = float(str)
print("Cast str to ",type(fl), fl)

fl = float(234234)
print("Cast int to ",type(fl), fl)

