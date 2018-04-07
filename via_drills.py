safe_z = 5
low_z = -0.9
feedrate = 300 #feedrate for via hits
current_drill_size = 0.66  #in tool list, tools with a diameter of 0.66 are for vias.

output = open('output_files/via_drills.ngc','w+')
output.write('%\n')
output.write('M03 S24000;\n')

input_file = open('input_files/drills.drd')

#Split into tool section, split per line, make sure the line's a tool, split tool into ID and diameter.

input_data = [x for x in input_file.read().split('%') if x] #split into sections

tool_section = input_data[0]
tool_list = [float(x.split('C')[1]) for x in tool_section.split('\n') if 'T0' in x]#split into tool lines
current_tool_id = tool_list.index(current_drill_size)
print(current_tool_id)

path_section = [x.split('\n') for x in [x for x in input_data[1].split('T0')]]
path_section = [tool for tool in [[line for line in tool if 'X' in line and 'Y' in line] for tool in path_section] if tool]

current_path_section = path_section[current_tool_id]

holes_dict = []

for line in current_path_section:
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
