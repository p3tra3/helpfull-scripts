import os
from PIL import Image
from tqdm import tqdm
import shutil
import multiprocessing

def process_image(directory, filename, destination_folder):
    filepath = os.path.join(directory, filename)
    
    try:
        with Image.open(filepath) as image:
            width, height = image.size
            image.close()
            if width < 500 or height < 500:
                # Move the small image to the "2del" folder
                shutil.move(filepath, os.path.join(destination_folder, filename))
    except Exception as e:
        print(f"Failed to process {filename}: {e}")

def move_small_images(directory, num_parallel):
    # Create the "2del" folder if it doesn't exist
    destination_folder = os.path.join(directory, "2del")
    if not os.path.exists(destination_folder):
        os.mkdir(destination_folder)

    file_list = os.listdir(directory)

    with tqdm(total=len(file_list), desc="Moving Images") as pbar:
        pool = multiprocessing.Pool(processes=num_parallel)

        for filename in file_list:
            filepath = os.path.join(directory, filename)

            if os.path.isfile(filepath):
                locking_pid = None  # You may remove the locking check as it may not be necessary in parallel processing.

                if not locking_pid:
                    pool.apply_async(process_image, args=(directory, filename, destination_folder))

            pbar.update(1)

        pool.close()
        pool.join()

if __name__ == '__main__':
    directory = input("Please enter the location of the photos: ")
    num_parallel = int(input("Enter the number of images to process in parallel: "))

    move_small_images(directory, num_parallel)
