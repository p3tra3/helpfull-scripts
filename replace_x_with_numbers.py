def replace_x_with_numbers(text, start_number, end_number):
    replaced_text = ""
    number = start_number
    for _ in range(start_number, end_number + 1):
        replaced_line = text.replace('x', str(number), 1)
        replaced_text += replaced_line + '\n'
        number += 1
    return replaced_text

text = input("Enter the text: ")
start_number = int(input("Enter the start number: "))
end_number = int(input("Enter the end number: "))

replaced_text = replace_x_with_numbers(text, start_number, end_number)
print(replaced_text)

output_file = input("Enter the output file name: ")

with open(output_file, 'w') as file:
    file.write(replaced_text)

print("Output saved to", output_file)
