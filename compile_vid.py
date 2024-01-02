from moviepy.editor import VideoFileClip, CompositeVideoClip, ImageClip, AudioFileClip

# Paths to input video, image, and audio files
video_path = "videos/exp.mp4"
image_path = "texts/exp1.PNG"
audio_path = "tts/exp1.mp3"

# Output video file path
output_path = "output/final.mp4"


# Load the video clip, image and audio
audio_clip = AudioFileClip(audio_path, fps=44100) 
video_clip = VideoFileClip(video_path).subclip(0, audio_clip.duration)
overlay_image = ImageClip(image_path, duration=audio_clip.duration)

# Crop the video to a 16:9 vertical format
print("video size before:", video_clip.size[0],  video_clip.size[1])
video_height = video_clip.size[1]
video_width = int(video_clip.size[0] * 9/16 * 9/16)
cropped_clip = video_clip.crop(x1=(video_clip.size[0] - video_width)/2, y1=0, x2=(video_clip.size[0] + video_width)/2, y2=video_height)
print("video size after:", cropped_clip.size[0], cropped_clip.size[1])

# Resize the overlay image
print("image size before:", overlay_image.size[0],  overlay_image.size[1])
image_width = int(video_width * 0.7)
image_height = int((image_width / overlay_image.size[0]) * overlay_image.size[1])
resized_overlay = overlay_image.resize(width=image_width, height=image_height)
print("image size after:", resized_overlay.size[0],  resized_overlay.size[1])

# Composite the video with the overlay image
overlay_position = ('center', 'center')
composite_clip = CompositeVideoClip([cropped_clip, resized_overlay.set_position(overlay_position)])

# Set the audio of the composite clip
composite_clip = composite_clip.set_audio(audio_clip)

# Write the final video to the output file
composite_clip.write_videofile(output_path, codec="libx264", audio_codec="aac", fps=24)