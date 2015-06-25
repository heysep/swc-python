def fahr_to_kelvin(temp):
	"""
	Returns the conversion of fahrenheit to kelvin.
	Arguement passed to the function's parameter must be int or float.
	"""
	return ((temp - 32) * (5.0/9)) + 273.15

def kelvin_to_celsius(temp):
	"""
	Return the conversion of kelvin to celcius.
	Argument passed to the parameter must be int or float.
	"""
	return temp - 273.15

def fahr_to_celsius(temp):
	"""
	Return the conversion of fahrenheit to celsius.
	Argument passed to the parameter must be int or float.
	"""
	temp_k = fahr_to_kelvin(temp)
	result = kelvin_to_celsius(temp_k)
	return result

print "freezing point of water:", fahr_to_kelvin(32.0)
print "boiling point of water:", fahr_to_kelvin(212.0)

print "zero kelvin to celcius is:", kelvin_to_celsius(0.0)
print "freezing point of water in celsius is:", fahr_to_celsius(32.0)
