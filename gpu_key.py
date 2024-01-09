import os
import subprocess

# Supported video file extensions
SUPPORTED_EXTENSIONS = (".mp4", ".mov", ".mkv", ".wmv")

def convert_video(video_file, output_directory):
    try:
        # Get the base name of the video file
        base_name = os.path.splitext(os.path.basename(video_file))[0]
        output_file = os.path.join(output_directory, f"{base_name}_converted.mp4")

        # Use ffmpeg to convert the video
        cmd = [
    "ffmpeg",
    "-y",
    "-hwaccel_output_format", "cuda",
    "-hwaccel", "cuda",
    "-i", video_file,
    "-c:v", "h264_nvenc",
    "-qp", "20",
    "-preset", "slow",
    "-rc", "vbr",
    "-rc-lookahead", "32",
    "-bf", "3",
    "-b_ref_mode", "middle",
    "-b_strategy", "1",
    "-c:a", "copy",
    output_file
]
        subprocess.run(cmd, check=True)

        print(f"Converted {video_file} to {output_file}")
    except Exception as e:
        print(f"Error converting {video_file}: {str(e)}")

def convert_files_in_directory(input_directory, output_directory):
    for root, _, files in os.walk(input_directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file.lower().endswith(SUPPORTED_EXTENSIONS):
                convert_video(file_path, output_directory)

if __name__ == "__main__":
    input_directory = input("Enter the input directory path containing video files: ")
    output_directory = os.path.join(input_directory, "out")

    if os.path.isdir(input_directory):
        os.makedirs(output_directory, exist_ok=True)
        convert_files_in_directory(input_directory, output_directory)
    else:
        print("The specified input directory does not exist.")