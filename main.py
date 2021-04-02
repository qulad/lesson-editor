import composite_audio as ca
import seperate_audio as sa
import time
import ctypes

# github.com/qulad

def input_course(sleep_time=0.1):
	"""
EN: Asks what course user wants to edit, checks if the answer is according to criteria. With sleep_time parameter, the time (in seconds) between prints can be determinated.
TR: Kullanıcıya hangi dersi düzenlemek istediğini sorar, cevap kriterlere uygun mu kontrol eder. sleep_time-->uyku_zamanı parametresi ile yazıların ekrana kaç saniye aralıklarla yazılacağını belirler.
	"""
	ctypes.windll.kernel32.SetConsoleTitleW("DERS SEÇ")
	course = None
	course_list = ["BİL102", "BİL104", "BİL206", "BİL208", "TBB112", "TBB122", "TBB124", "ATA102", "TDL102", "YDL102"]
	cant_edit = ["TBB112", "ATA102", "TDL102", "YDL102"]

	while True:
		while course not in course_list:
			course = input("Hangi ders düzenlenecek? ")
			course = course.upper().replace("I", "İ")
			if course not in course_list:
				time.sleep(sleep_time)
				print("Lütfen aşağıdaki derslerden birini giriniz.")
				time.sleep(sleep_time)
				print(" ----------------------------------\n"
					f"|--{course_list[0]}--{course_list[1]}--{course_list[2]}--{course_list[3]}--|\n"
					f"|----{course_list[4]}----{course_list[5]}----{course_list[6]}----|\n"
					f"|----{course_list[7]}----{course_list[8]}----{course_list[9]}----|\n"
					" ----------------------------------")
		if course in cant_edit:
			time.sleep(sleep_time)
			print("Seçilen ders düzenlenemez, lütfen farklı bir ders seçiniz.")
			course = None
		elif course != cant_edit:
			break
	return course

def input_week(sleep_time=0.1):
	"""
EN: Asks what week user wants to edit, checks if the answer is according to criteria. With sleep_time parameter, the time (in seconds) between prints can be determinated.
TR: Kullanıcıya hangi haftayı düzenlemek istediğini sorar, cevap kriterlere uygun mu kontrol eder. sleep_time-->uyku_zamanı parametresi ile yazıların ekrana kaç saniye aralıklarla yazılacağını belirler.
	"""
	ctypes.windll.kernel32.SetConsoleTitleW("HAFTA SEÇ")
	week = None

	while True:
		try:
			time.sleep(sleep_time)
			week = input("Hangi hafta düzenlenecek? ")
			if "." in week:
				raise Exception
			week = int(week)
			if week <= 0 or week >= 17:
				raise Exception
			break
		except Exception:
			time.sleep(sleep_time)
			print("Lütfen 1 ve 16 arasında ([1,16]) bir tam sayı giriniz.")
	return week

def verify_details(course, week, sleep_time=0.1):
	"""
EN: Takes course and week parameters and asks user to verify these, return boolean values.
TR: course-->ders ve week-->hafta parametrelerini alır ve kullanıcıdan onaylamasını ister, geriye boolean değer döner.
	"""
	ctypes.windll.kernel32.SetConsoleTitleW("ONAYLA")
	positive = ["Y", "YES", "E", "EVET"]
	time.sleep(sleep_time)
	answer = input(f"{course} dersinin {week}. haftası seçildi, onaylamak için 'e' yazınız. ")
	if answer.upper() in positive:
		return True
	else:
		return False

def start(course, week):
	"""
EN: Starts the program. Takes two parameters, course and week.
TR: Programı başlatır. İki parametre alır, course-->ders ve week-->hafta.
	"""
	print(f"{course}H{week} düzenlenmeye başlanıyor...")
	audio = sa.seperate_audio(course, week)
	if audio == False:
		ctypes.windll.kernel32.SetConsoleTitleW("HATA")
		quit("webcam dosyası bulunamadı, program sonlandırılıyor...")
	merger = ca.merge(course, week)
	if merger == False:
		ctypes.windll.kernel32.SetConsoleTitleW("HATA")
		quit("deskshare veya audio dosyası bulunamadı, program sonlandırılıyor...")
	ctypes.windll.kernel32.SetConsoleTitleW(f"{course}, {week}. hafta")

if __name__ == "__main__":
	verify = False
	while verify == False:
		course = input_course()
		week = input_week()
		verify = verify_details(course, week)
	time.sleep(0.1)
	start(course, week)
