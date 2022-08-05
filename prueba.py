
""" import wmi

w = wmi.WMI()
for p in w.Win32_Product():
	print (r"\newcommand*{\Title}", "{" + p.Version +"}")
	print (r"\newcommand*{\Title}", "{" + p.Vendor +"}")
	print (r"\newcommand*{\Title}", "{" + p.Caption +"}")
	print (r"\newcommand*{\Title}", "{%s}" % p.Caption)
	print("\n")
 """
""" 			try:
				software['version'] = winreg.QueryValueEx(sub_key, "DisplayVersion")[0]
			except EnvironmentError:
				software['version'] = 'undefined'
			try:
				software['publisher'] = winreg.QueryValueEx(sub_key, "Publisher")[0]
			except EnvironmentError: 
				software['publisher'] = 'undefined'"""

#	print('Name: %s, Version: %s, Publisher: %s' % (software['name'], software['version'], software['publisher']))

import winreg
import datetime

def transform_date(key_date):
	return key_date/10000000 - 11644473600


def sofware_instaled(hive, flag):
	Register = winreg.ConnectRegistry(None, hive)
	Key = winreg.OpenKey(Register, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall", 0, winreg.KEY_READ | flag)

	count_subkey = winreg.QueryInfoKey(Key)[0]
	subkey = transform_date(count_subkey)
	#dt = datetime.datetime.fromtimestamp(subkey)
	dt = datetime.datetime.fromtimestamp(count_subkey)
	print(dt)
	
	software_list = []

	for i in range(count_subkey):
		software = {}
		try:
			sub_key_name = winreg.EnumKey(Key, i)
			sub_key = winreg.OpenKey(Key, sub_key_name)
			software['name'] = winreg.QueryValueEx(sub_key, "DisplayName")[0]
			try:
				software['date'] = winreg.QueryValueEx(sub_key, "InstallDate")[0]
			except EnvironmentError:
				software['date'] = 'undefined'
			software_list.append(software)
		except EnvironmentError:
			continue
	print(sub_key)
	return software_list

software_list = sofware_instaled(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_32KEY) + sofware_instaled(winreg.HKEY_LOCAL_MACHINE, winreg.KEY_WOW64_64KEY) + sofware_instaled(winreg.HKEY_CURRENT_USER, 0)

for software in software_list:
	print('Name: %s, Date: %s' % (software['name'], software['date']))
print('Number of installed apps: %s' % len(software_list))