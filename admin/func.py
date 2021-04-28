import os

class Opt:
		def info():
			print('        PERSONAL PREFERENCE')
			print('  -> Change your name\n  -> Change salutation\n  -> Intro\n  -> Run on Startup')
		def acc():
			print('        USER ACCOUNT')
			print('  -> Change Email ID\n  -> Change Password')
		def media():
			print('         MEDIA TAB')
			print('  -> Change Video Directory\n  -> Change Music Directory\n  -> Change Picture Directory.')
		def weather():
			print('         WEATHER OPTIONS')
			print('  -> Change temperature unit\n  -> Speak on Startup')
		def web():
			print('         WEB SETTINGS')
			print('  -> Default search engine\n  -> Default keywords')
		def ai():
			print('         A.I. CUSTOMIZATIONS')
			print('  -> A.I. Name\n  -> Font color while typing\n  -> Font color while speaking')
		def bkp():
			print('         BACK UP AND RESTORE')
			print('  -> Back Up and Restore')
		def speech():
			print('         EMULATE SPEECH')
			print('Type below to emulate speech (type \'exit\' to end emulation.)')


def admin_panel():
	os.system('cls')
	print('                 Welcome to Admin Panel \n')
	print('1.) PERSONAL PREFERENCE\n2.) USER ACCOUNT\n3.) MEDIA TAB\n4.) WEATHER OPTIONS\n5.) WEB SETTINGS\n6.) A.I. CUSTOMIZATIONS\n7.) BACK UP AND RESTORE\n8.) EMULATE SPEECH\n')

	while True:
		opt = int(input('Choose one of the above : '))
		print('')
		if opt == 1:
			Opt.info()
		elif opt == 2:
			Opt.acc()
		elif opt == 3:
			Opt.media()
		elif opt == 4:
			Opt.weather()
		elif opt == 5:
			Opt.web()
		elif opt == 6:
			Opt.ai()
		elif opt == 7:
			Opt.bkp()
		elif opt == 8:
			Opt.speech()
		else:
			x = {1, 2, 3, 4, 5, 6, 7, 8}	
			print('Invalid input !')

		print('')
