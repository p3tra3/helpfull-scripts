import os
import collections

def calculate_size(path):
    # Initialize a dictionary to store file extensions and their sizes
    extension_sizes = collections.defaultdict(int)

    # Traverse the directory
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            # Get the file extension
            _, extension = os.path.splitext(file)
            extension = extension.lower()

            # Get the file size
            file_path = os.path.join(dirpath, file)
            if os.path.isfile(file_path):
                file_size = os.path.getsize(file_path)

                # Add the file size to the total size of its extension
                extension_sizes[extension] += file_size

    # Convert sizes to megabytes and sort by size
    for extension in extension_sizes:
        extension_sizes[extension] /= (1024 * 1024)

    sorted_sizes = sorted(extension_sizes.items(), key=lambda item: item[1], reverse=True)

    return sorted_sizes

# Ask the user for a directory
directory = input("Please enter a directory: ")

# Calculate and print the sizes
sizes = calculate_size(directory)
for extension, size in sizes:
    print(f"Extension: {extension}, Size: {size:.2f} MB")
