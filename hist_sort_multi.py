import os
import cv2
import numpy as np
from glob import glob
from tqdm import tqdm
import concurrent.futures

def compute_histogram(image_path):
    """Compute the color histogram of an image."""
    img = cv2.imread(image_path)
    if img is None:
        print(f"Failed to load image at {image_path}")
        return None
    hist = cv2.calcHist([img], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    hist = cv2.normalize(hist, hist).flatten()
    return hist

def compute_similarity(hist1, hist2):
    """Compute similarity between two histograms using correlation method."""
    similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
    return similarity

def sort_images(directory):
    """Sort images in a directory based on histogram similarity."""
    image_paths = glob(os.path.join(directory, '*'))
    if not image_paths:
        raise ValueError(f"No images found in directory: {directory}")

    # Compute histograms of all images
    print("Computing image histograms...")
    histograms = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_path = {executor.submit(compute_histogram, path): path for path in image_paths}
        for future in tqdm(concurrent.futures.as_completed(future_to_path), total=len(future_to_path)):
            path = future_to_path[future]
            try:
                hist = future.result()
                if hist is not None:
                    histograms.append((path, hist))
            except Exception as exc:
                print('%r generated an exception: %s' % (path, exc))

    # Sort by similarity
    print("Sorting images based on histogram similarity...")
    sorted_paths = [histograms.pop(0)[0]]
    while histograms:
        last_hist = compute_histogram(sorted_paths[-1])
        similarities = [(i, compute_similarity(last_hist, hist)) for i, (_, hist) in enumerate(histograms)]
        similarities.sort(key=lambda x: x[1], reverse=True)
        sorted_paths.append(histograms.pop(similarities[0][0])[0])

    # Return sorted paths
    return sorted_paths

def rename_files(sorted_paths):
    """Rename files based on their order in sorted_paths."""
    for i, path in enumerate(sorted_paths):
        dir_name, file_name = os.path.split(path)
        base_name, ext = os.path.splitext(file_name)
        new_name = f"{i+1}_{base_name}{ext}"
        new_path = os.path.join(dir_name, new_name)
        os.rename(path, new_path)

def main():
    directory = input("Enter the directory of the images: ")
    sorted_images = sort_images(directory)
    rename_files(sorted_images)
    print("Images sorted and renamed based on histogram similarity.")

if __name__ == "__main__":
    main()
