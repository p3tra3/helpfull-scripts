import os
import subprocess

def convert_png_sequence_to_mp4(png_directory, output_video_path, frame_rate=30):
    # Get a list of PNG files in the directory
    png_files = [os.path.join(png_directory, f) for f in os.listdir(png_directory) if f.endswith('.png')]
    png_files.sort()  # Sort the files in alphanumeric order

    # Build the ffmpeg command
    cmd = [
        'ffmpeg',
        '-hwaccel', 'auto',
        '-framerate', str(frame_rate),
        '-i', os.path.join(png_directory, '%d.png'),  # Input PNG files
        '-c:v', 'h264_nvenc',  # Video codec
        '-qp', '20',
        '-r', str(frame_rate),  # Output frame rate
        '-pix_fmt', 'yuv420p',  # Pixel format
        output_video_path,
    ]

    # Run the ffmpeg command
    subprocess.run(cmd)

if __name__ == "__main__":
    png_directory = input("Enter the path to the directory containing PNG images: ")
    output_video_path = "output_video.mp4"  # You can change the output video name if needed
    frame_rate = 30  # You can adjust the frame rate as needed

    convert_png_sequence_to_mp4(png_directory, output_video_path, frame_rate)
