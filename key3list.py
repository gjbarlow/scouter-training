import scouter_training
import os
import csv

training_file = "TrainedLeader_Lackawanna_01.csv"
syt_file = "SYT_Lackawanna_01.csv"

key3_file = "Lackawanna_Key3.csv"

if not os.path.isfile(training_file):
	print('Trained leader file is missing', training_file)
elif not os.path.isfile(syt_file):
	print('Safeguarding Youth Training file is missing', syt_file)
else:
	t = scouter_training.Training(training_file, syt_file)
	key3_list = sorted([ person for unit in t.units for person in t.units[unit].key3 ])
	# for x in key3_list:
	# 	print(",".join(x))

	with open(key3_file, "w", newline="") as fh:
		writer = csv.writer(fh)
		writer.writerows(key3_list)


