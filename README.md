# PySize
Module for file representation. It behaves like an int or float.

## Usage:
``` 
from pysize import SIZE

size1 = SIZE(100)              # 100 Bytes
size2 = SIZE(100, SIZE.MB)     # 100 MByte

print size1 + size2            # 100MB 100B
print size1 * 256              # 25GB

``` 
