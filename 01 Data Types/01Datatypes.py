





# Complex Types
d = 3+5j
print(d)
# type(d) do not works in IDE but works in Google Colab
print(type(d))


# Binary to Decimal
e = 0B1010
print(type(e))   # cause already converted e from binary to decimal
print(e)
print(type(e))   # cause already converted e from binary to decimal

# Hexadecimal to Decimal
f = 0XFF
print(f)
print(type(f))   # cause already converted f from hexadecimal to decimal

# Octal to Decimal
g = 0O111
print(g)
print(type(g))


# Boolean Datatypes
h = True
print(h)
print(type(h))
i = 9>8
print(i)
print(type(i))
j = 9<8
print(j)
print(type(j))


# Type Conversion Functions

# float to int
x = 33.5
print(type(x))
i = int(x)
print(i)
print(type(i))

# String to float
j = float("22.5")
print(j)
print(type(j))

# Decimal to Binary
k = 10          # int type
l=bin(k)        # string type
print(l)
print(type(l))
# and if
k = 10
print(bin(k))
print(type(k))          # int type
print(type(bin(k)))     # string type


# Decimal to Hexadecimal
m = 27
print(hex(m))
print(type(hex(m)))


# Decimal to Octal
n = 35
print(oct(n))
print(type(oct(n)))

