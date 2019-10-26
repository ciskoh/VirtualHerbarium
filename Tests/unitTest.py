
"""Test for VirtualHerbarium"""

from Modules.classes import Plant

kali = Plant("Parthenium", "eeeee")
print(kali.type)
print(kali.__dict__)
kali.wikipedia = "eeeee"
print(kali.__doc__)
