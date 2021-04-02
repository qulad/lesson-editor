import moviepy.editor as mp
import os
import pathlib

# github.com/qulad

course = "BİL208"
week = 5

def merge(course, week, source_dir="SOURCE", export_dir="OUT"):
	"""
EN: Takes course and week parameters. Merges audio and deskshare of the course on the week.
TR: course-->ders ve week-->hafta parametrelerini alır. audio ve deskshare dosyalarını birleştirir.
	"""
	week = str(week)
	try:
		clip = mp.VideoFileClip(f"{source_dir}/deskshare - {course}H{week}.mp4")
	except Exception:
		try:
			clip = mp.VideoFileClip(f"{source_dir}/deskshare - {course}H{week}.webm")
		except Exception:
			if __name__ == "__main__":
				quit(f"{source_dir}/deskshare - {course}H{week}.mp4/webm dosyası bulunamıyor.")
			elif __name__ != "__main__":
				return False
	try:
		audio = mp.AudioFileClip(f"{source_dir}/audio - {course}H{week}.mp3")
	except:
		if __name__ == "__main__":
			quit(f"{source_dir}/deskshare - {course}H{week}.mp4/webm dosyası bulunamıyor.")
		elif __name__ != "__main__":
			return False
	final_audio = mp.CompositeAudioClip([audio])
	final_clip = clip.set_audio(final_audio)
	if not os.path.exists(export_dir):
		os.makedirs(export_dir)
	final_clip.write_videofile(f"{export_dir}/{course}H{week}.mp4", codec= "libx264", audio=True, audio_codec="libmp3lame", audio_bitrate="64k")
	return pathlib.Path(__file__).parent.absolute() + f"{export_dir}/{course}H{week}.mp4"

if __name__ == "__main__":
	merge(course, week)
