from tkinter import filedialog, messagebox
import imageio
import os

video_path = os.path.abspath("vid.mp4")

print("\n\nClip:", clip, "\n\n")

def convert_to_gif(video_path, target_format):
    gif_path = os.path.splitext(video_path)[0] + target_format
    print(f'Converting: {video_path} \n to \n {gif_path}')
    reader = imageio.get_reader(video_path)
    fps = reader.get_meta_data()['fps']

    writer = imageio.get_writer(gif_path, fps=fps)

    for frames in reader:
        writer.append_data(frames)
        print(f'Frame: {frames}')
    
    print("Done")
    writer.close()

convert_to_gif(video_path, ".gif")