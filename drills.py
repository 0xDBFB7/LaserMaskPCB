safe_z = 5
low_z = -0.9
feedrate = 300
output = open('output_files/drills.ngc','w+')
output.write('%\n')
output.write('M03 S24000;\n')
holes_dict = []
for line in open('input_files/drills.drd'):
	if('X' in line and 'Y' in line):
		coords = line.replace('\n','').replace('X',' ').replace('Y',' ').split(' ')
		coords = [x for x in coords if x]
		holes_dict.append(coords)
print(holes_dict)
output.write('G00 Z{};\n'.format(safe_z))
output.write('G00 X{} Y{};\n'.format(0,0))
print(len(holes_dict))
for i in holes_dict:
	output.write('G00 Z{};\n'.format(safe_z))
	output.write('G00 X{} Y{};\n'.format(float(i[0])/1000.0,float(i[1])/1000.0))
	output.write('G01 Z{} F{};\n'.format(low_z,feedrate))
	output.write('G00 Z{};\n'.format(safe_z))
output.write('M05;\n')
output.write('%\n')
output.close()
