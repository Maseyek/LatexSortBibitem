def parse_bib_items(file_path):
    bib_dict = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        current_key = None
        current_value = ""
        for line in file:
            if line.strip().startswith(r'\bibitem'):
                # If a new \bibitem is encountered, save the previous key and value
                if current_key is not None:
                    bib_dict[current_key] = current_value.strip()
                # Extract the new key
                current_key = line.strip()
                # Reset the value
                current_value = ""
            else:
                # Append the current line to the current value
                current_value += line
        # Add the last entry to the dictionary
        if current_key is not None:
            bib_dict[current_key] = current_value.strip()
    return bib_dict


input_file_path = 'test.txt'
output_file_path = "sorted_out.txt"

bib_dictionary = parse_bib_items(input_file_path)

sorted_bib = dict(sorted(bib_dictionary.items(), key=lambda item: item[1].lower()))

for key, value in sorted_bib.items():
    print(f"Key: {key}")
    print(f"Value: {value}")
    print("--------------")

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for key, value in sorted_bib.items():
        output_file.write(f"{key}\n")
        output_file.write(f"{value}\n")

print(f"Sorted items saved to {output_file_path}.")
