from Crypto.Util.number import long_to_bytes

with open("output.txt", "r") as f:
    data = f.readlines()

n = int(data[0].strip().split(" = ")[1])
e = int(data[1].strip().split(" = ")[1])
c = int(data[2].strip().split(" = ")[1])

phi = n - 1

d = pow(e, -1, phi)

m = pow(c, d, n)

print(long_to_bytes(m).decode())