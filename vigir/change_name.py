original_path = 'A1_cutvideo_expandzero_total_data.csv'
modified_path = 'A1_cutvideo_expandzero_total_data_modified.csv'
old_beginning = '/home1/SMATousi//A1_cut_video'
new_beginning = '/root/home/data/'

# Read the original file and modify the lines
modified_lines = []
with open(original_path, 'r') as file:
    for line in file:
        if line.startswith(old_beginning):
            modified_line = line.replace(old_beginning, new_beginning, 1)
            modified_lines.append(modified_line)
        else:
            modified_lines.append(line)

# Write the modified lines to a new file
with open(modified_path, 'w') as file:
    for line in modified_lines:
        file.write(line)

print(f'Modified file saved as {modified_path}')
