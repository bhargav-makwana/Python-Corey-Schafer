print('Imported my_module...')

test = 'Test String'

def find_index(source, target_value):
	""" Find an index of the value in target """
	for i, value in enumerate(source):
		if value == target_value:
			return i

	return -1
