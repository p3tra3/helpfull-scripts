#!/bin/bash
for i in *.mp4; do
	ffmpeg -skip_frame nokey -threads 1 -i "$i" -vsync vfr -threads 1 -frame_pts true -max_muxing_queue_size 1024 -map 0:v -y "${i%.*}.mkv"
done
