import base64
from itertools import cycle

message = 'NkYrAAINNAYSSUd3QX8SEwswAUZCR2oCNxkNCzASFAtAbVt4UgQdJRAEAwIpRnRVRgs3Ew4cEz5G\neE9BSTgbAhwCKQg6GQRJfVVGDwQlCD0DBAM0GxVJR3dBfwAPAj4WCgsDak14UhMPMxcIGhRqQWJV\nRh0wEwRJS21GPhoOSXFPQUkQJA95Uhw='

key = bytes("MaXuanQuang", "utf8")

print(bytes(a ^ b for a, b in zip(base64.b64decode(message), cycle(key))))
