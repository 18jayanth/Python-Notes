a=3+5j
b=5j
print(a)
print(type(a))
print(a.real) # 3.0
print(a.imag) # 5.0
print(complex()) #0j
#int to complex
print(complex(0)) #0j
print(complex(5)) #5+0j
print(complex(5,2)) # 5+2j
#float to complex
print(complex(3.2)) # 3.2+0j
print(complex(0.0)) # 0j
print(complex(3.2,5.4)) # 3.2+5.4j
print(complex(0,5.3)) # 5.3j
#boolean to complex
print(complex(True)) #1+0j
print(complex(False,True)) #1j
print(complex(False)) #0j
#complex to complex
print(complex(3+2j)) # 3+2j
print(complex(3+2j,4+5j)) #-2+6j
print(complex(0,2+3j)) # -3+2j

# string to complex
print(complex('5')) # 5+0j
print(complex('a')) # malformed string
print(complex('3','a')) # malformed
print(complex('3','2')) # malformed




