from func import *
from getpass import getpass

print('                 Login to Admin Panel \n')

email = '123'
pwd = '123'

log_email = str(input('Enter your Email ID: '))
log_pwd = str(getpass('Enter your Password: '))

if __name__ == '__main__':
	if log_email == '123' and log_pwd == '123':
		admin_panel()
	else:
		while log_email != '123' or log_pwd != '123':
			print('Access Denied, Unauthorised User ! \n')
			speak('Access Denied, Unauthorised User !')
			log_email = str(input('Enter your Email ID: '))
			log_pwd = str(getpass('Enter your Password: '))