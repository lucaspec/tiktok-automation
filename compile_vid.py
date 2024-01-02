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
overlay_image = ImageClip(image_path, duration=video_clip.duration)

# Set the position of the overlay image (you can adjust as needed)
overlay_position = ('center', 'center')

# Composite the video with the overlay image
composite_clip = CompositeVideoClip([video_clip, overlay_image.set_position(overlay_position)])

# Set the audio of the composite clip
composite_clip = composite_clip.set_audio(audio_clip)

# Write the final video to the output file
composite_clip.write_videofile(output_path, codec="libx264", audio_codec="aac", fps=24)