import nil.time, sys, string

from main_function import process_main_function
from generate_code import generate_code

def process_procedure(module_name, image_base, name, procedure_lines, lines, offsets):

	arguments = string.join(sys.argv)
	time_string = nil.time.timestamp()

	comment = """/*
Command line arguments: python %s
Time of generation: %s
*/

""" % (arguments, time_string)
	
	main_function_data = process_main_function(module_name, image_base, name, procedure_lines, offsets)
	if main_function_data == None:
		sys.exit(1)
	
	includes, variables, main_function, initialisation_function = main_function_data
		
	output_units = [
		comment,
		includes,
		variables,
		initialisation_function,
		main_function
	]
	
	output = string.join(output_units, '')
	
	hacks = [
		('_exit', 'custom_exit')
	]
	
	for target, replacement in hacks:
		output = output.replace(target, replacement)
	
	return output