from unsilence import Unsilence

input_file = input("Enter the location of the input video file: ")
output_file = input("Enter the location for the output video file: ")

u = Unsilence(input_file)
u.detect_silence(min_silence_length=3, silence_threshold=-50)
u.render_media(output_file)
