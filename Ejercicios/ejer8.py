#!/usr/bin/env python
import re
texto=raw_input("introduzca un texto :  ")
palabra=re.split("/([A-z])\w+ ([A-Z])\W/g",texto)
print palabra