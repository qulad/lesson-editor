import moviepy.editor as mp
import os
import pathlib

# github.com/qulad

course = "BİL208"
week = 5

def seperate_audio(course, week, source_dir="SOURCE", export_dir="SOURCE"):
	"""
EN: Takes course and week parameters. Seperates audio and deskshare of the course on the week.
TR: course-->ders ve week-->hafta parametrelerini alır. audio ve deskshare dosyalarını ayırır.
	"""
	week = str(week)
	try:
		clip = mp.VideoFileClip(f"{source_dir}/webcams - {course}H{week}.mp4")
	except Exception:
		try:
			clip = mp.VideoFileClip(f"{source_dir}/webcams - {course}H{week}.webm")
		except Exception:
			if __name__ == "__main__":
				quit(f"{source_dir}/webcams - {course}H{week}.mp4/webm dosyası bulunamıyor.")
			elif __name__ != "__main__":
				return False
	if not os.path.exists(export_dir):
		os.makedirs(export_dir)
	clip.audio.write_audiofile(f"{export_dir}/audio - {course}H{week}.mp3")
	return pathlib.Path(__file__).parent.absolute() + f"{export_dir}/audio - {course}H{week}.mp3"

if __name__ == "__main__":
	seperate_audio(course, week)
