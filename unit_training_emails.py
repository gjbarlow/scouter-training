import scouter_training
import os
import sys
import datetime

training_file = "TrainedLeader_Lackawanna_01.csv"
syt_file = "SYT_Lackawanna_01.csv"

if not os.path.isfile(training_file):
	print('Trained leader file is missing', training_file)
	exit()
elif not os.path.isfile(syt_file):
	print('Safeguarding Youth Training file is missing', syt_file)
	exit()
else:
	t = scouter_training.Training(training_file, syt_file)

s = scouter_training.sendemail.SendEmail(EMAIL_ADDRESS, APP_PASSWORD)

if len(sys.argv) > 1:
	unit = ' '.join(sys.argv[1:])
	if unit not in t.units:
		print('Unit not found')
		exit()
else:
	exit()

unit_type, unit_number = unit.split()
disp_unit = '%s %d'%(unit_type, int(unit_number))

unitobj = t.units[unit]

people = unitobj.people_not_trained

percent_trained = unitobj.percent_trained()

month = datetime.datetime.now().strftime('%B')

for person in people:
	addr = person.email
	subject = '%s - Registered Leader Training'%(disp_unit)
	body = '''Hello %s,

This is a reminder for %s to complete your position-specific training for your role as %s in %s. Our goal is for 100%% of our registered leaders to be trained. Trained adults deliver a better Scouting program for our youth and are more effective volunteers. Currently, %.2f%% of our adult leaders are position-trained. You can help us get to 100%% by completing the training courses listed below. Online course modules can be found through your account on https://my.scouting.org.

'''%(person.disp_name, month, person.position, disp_unit, percent_trained)

	if not t.people[person.bsa_id].syt:
		body += 'Your Safeguarding Youth Training (SYT/YPT) is EXPIRED. You cannot serve as a registered leader in Scouting America until you renew this training. Please complete this training as soon as possible.\n\n'

	for course in sorted(list(person.missing)):
		body += '    %s - %s\n'%course

	body += '''
If you need help or you have questions, please let me know. Thank you for your commitment to youth and the Scouting movement!

Yours in Scouting,
NAME
CONTACT INFO'''

	print(addr, "\n", subject, "\n", body)
	# s.send(addr, subject, body)