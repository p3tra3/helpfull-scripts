import os
import subprocess
import shlex  # For splitting command string into arguments
from fuzzywuzzy import fuzz  # For fuzzy string matching
from fuzzywuzzy import process

def merge_video_and_subtitle(video_path, subtitle_path):
    # Generate output MKV file path
    output_path = os.path.splitext(video_path)[0] + ".mkv"

    # Run mkvmerge command to merge video and subtitle
    command = f'mkvmerge -o "{output_path}" "{video_path}" --language 0:eng "{subtitle_path}"'
    subprocess.run(shlex.split(command), check=True)

    print("Merged successfully. Output file:", output_path)

def find_matching_subtitle(video_file, subtitle_files):
    video_filename_no_ext = os.path.splitext(video_file)[0]
    best_match = process.extractOne(video_filename_no_ext, subtitle_files, scorer=fuzz.partial_ratio)
    if best_match[1] > 70:  # Adjust the threshold according to your naming convention
        return best_match[0]
    else:
        return None

if __name__ == "__main__":
    # Input directory
    directory = input("Enter the directory containing video and subtitle files: ")

    # Check if the directory exists
    if not os.path.exists(directory):
        print("Error: Directory not found.")
        exit()

    # Get all video and subtitle files in the directory
    video_files = [f for f in os.listdir(directory) if f.endswith('.webm')]
    subtitle_files = [f for f in os.listdir(directory) if f.endswith('.srt')]

    # Merge each video with its corresponding subtitle
    for video_file in video_files:
        subtitle_file = find_matching_subtitle(video_file, subtitle_files)
        if subtitle_file:
            video_path = os.path.join(directory, video_file)
            subtitle_path = os.path.join(directory, subtitle_file)
            merge_video_and_subtitle(video_path, subtitle_path)
        else:
            print(f"No matching subtitle found for {video_file}. Skipping.")
