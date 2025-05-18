import os
import glob
current_directory = os.path.dirname(os.path.abspath(__file__))
extensions = ['mp3', 'wav']
pastai = 0

for ext in extensions:
    file_data = glob.glob(os.path.join(current_directory, f'*.{ext}'))
    for file in file_data:
        from pydub import AudioSegment
        audio = AudioSegment.from_file(file, format=ext)
        from pydub.silence import split_on_silence
        chunks = split_on_silence(audio, min_silence_len=25, silence_thresh=-35)
        pastai += 1
        for i, chunk in enumerate(chunks):
            if not os.path.exists(f"output{pastai}"):
                os.mkdir(f"output{pastai}")
            chunk.export(f"output{pastai}/part_{i}.{ext}".format(i), format=ext)
