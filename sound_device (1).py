import sounddevice
import  wavio

sample_per_sec=44100  #  for recording audio / music standrd  sample per second.
sound_rec_sec=int(input("please enter sound duration in seconds."))
import pdb; pdb.set_trace()
start_rec_audio = sounddevice.rec(sample_per_sec * sound_rec_sec, samplerate=sample_per_sec, channels=2)
sounddevice.wait() 
file_name = "record3.wav"

wavio.write(file_name, start_rec_audio, sample_per_sec, sampwidth=2)

play_audio = wavio.read(file_name)
sounddevice.play(play_audio.data, samplerate=play_audio.rate)
sounddevice.wait()