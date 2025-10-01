import scouter_training
import os

training_file = "TrainedLeader_Lackawanna_01.csv"
syt_file = "SYT_Lackawanna_01.csv"

if not os.path.isfile(training_file):
	print('Trained leader file is missing', training_file)
elif not os.path.isfile(syt_file):
	print('Safeguarding Youth Training file is missing', syt_file)
else:
	t = scouter_training.Training(training_file, syt_file)
	t.summary()
	t.ranking()