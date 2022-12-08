from subroutines import *
audio_filename='electric-feel' #should be G# major, 103bpm, 6/4
# audio_filename='sweet-home-alabama' #should be G major, 98bpm, 4/4

audio_format = '.mp3' #.wav or .mp3

audio_path = './songs/' + audio_filename + audio_format

song = Song(audio_path) #loads song, finds key and tempo

start_octave = 3 #keep it kind of high to not clash as much
n_octaves = 3
    
freqs = get_scale_freqs(start_note=song.root + str(start_octave), octaves=n_octaves, scale=song.scale)

image_index = 0 

image_catalog = ImageCatalog('WebbDemo.csv')
image_path = image_catalog.get_image_path(image_index) 

beats_per_bar = 4 #assume 4/4, doesn't matter much
time_per_bar = beats_per_bar*60/song.tempo
n_bars = 16
sonif_duration = n_bars*time_per_bar #seconds, need to set with tempo, key signature and # of bars

print('sonification duration: ',round(sonif_duration,2),'seconds')
print('song duration: ',round(len(song.y)/song.sr,2),'seconds')

sonification = Sonification(image_path, song, freqs, sonif_duration) 
plt.imshow(sonification.pixels,aspect='auto',cmap='gray')

# sonification.save_sonification('./sonifications/' + image_catalog.get_image_name(image_index) + '.wav')
sonification.wave.make_audio()

spec = sonification.wave.make_spectrogram(seg_length=1000)
spec.plot()
plt.ylim(min(freqs),max(freqs))

print("mid")

sonification.mix_audio(mix=0.6) #mix sonfication with audio,  mix is fraction of sonification

sonification.mix.make_audio()

spec = sonification.mix.make_spectrogram(seg_length=1000)
spec.plot()
plt.ylim(min(freqs),max(freqs))

sonification.mix.write('./mixes/' + audio_filename + ' + ' +image_catalog.get_image_name(image_index) + '.wav')

print('end')
