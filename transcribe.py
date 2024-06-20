from moviepy.editor import VideoFileClip
import os
import mimetypes
import whisper
from whisper.utils import get_writer

# full_filename = "test_file.mp4"
# mimetype = mimetypes.guess_type(full_filename)[0]

# filename = os.path.splitext(full_filename)[0]

# if mimetype is not None:
#     if mimetype.startswith('video'):
#         print("This is a video file, extracting audio...")
#         video_clip = VideoFileClip(full_filename)
#         audio_clip = video_clip.audio
#         audio_filename = f"{filename}.mp3"
#         audio_clip.write_audiofile(audio_filename)
#     elif mimetype.startswith('audio'):
#         print("This is an audio file, no need to extract audio.")
#         audio_filename = full_filename
#     else:
#         print("This is not a video or audio file")



# model = whisper.load_model("base")
# result = model.transcribe(audio_filename)

# # Save as a TXT file with hard line breaks
# txt_writer = get_writer("txt", './')
# txt_writer(result, audio_filename)


def generate_transcript(full_filename):
    print(full_filename)
    mimetype = mimetypes.guess_type(full_filename)[0]
    print(mimetype)
    # get the filename without the path
    filename = os.path.basename(full_filename)
    filename = os.path.splitext(filename)[0]
    print(filename)
    if mimetype is not None:
        if mimetype.startswith('video'):
            print("This is a video file, extracting audio...")
            video_clip = VideoFileClip(full_filename)
            audio_clip = video_clip.audio
            audio_filename = f"{filename}.mp3"
            audio_clip.write_audiofile(audio_filename)
        elif mimetype.startswith('audio'):
            print("This is an audio file, no need to extract audio.")
            audio_filename = full_filename
        else:
            print("This is not a video or audio file")

    model = whisper.load_model("base")
    result = model.transcribe(audio_filename)

    # Save as a TXT file with hard line breaks
    txt_writer = get_writer("txt", './uploads')
    txt_writer(result, audio_filename)
    return  f"{filename}.txt"