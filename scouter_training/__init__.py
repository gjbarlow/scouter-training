from . import data
from . import files
from . import sendemail

class Training:
	def __init__(self, training_file = None, syt_file = None):
		self.people = {}
		self.units = {}
		self.names = {}
		self.courses = {}

		# Need to add check for input files

		training_data = files.readfile(training_file)
		syt_data = files.readfile(syt_file)

		# Read all positions
		all_positions = [data.PersonOnePosition(line) for line in training_data]

		# Create dictionary of all people
		# self.people = data.AllPeople(all_positions)
		for person in all_positions:
			if person.bsa_id not in self.people:
				self.people[person.bsa_id] = data.PersonAllPositions(person)
			else:
				self.people[person.bsa_id].update(person)

		for person in self.people:
			self.names[self.people[person].name] = self.people[person].bsa_id

		# Add SAFEguarding Youth Training information to all people
		for person in syt_data:
			district,unittype,unitnumber,genderaccepted,chartedorganization,firstname,middlename,lastname,memberid,positionname,isyptcurrent2,yptexpirationdatec,y01coursecode,y01completiondatec,y01expirationdatec,streetaddress,city,statecode,zip,emailaddress,phonenumber,registrationdatec,cregistrationexpirydate,stronlinecourses = person
			bsa_id = int(memberid)
			syt_trained = isyptcurrent2 == "YES"
			if bsa_id in self.people:
				self.people[bsa_id].syt_update(syt_trained)
			else:
				pass

		# Create unit data
		for bsa_id in self.people:
			for position in self.people[bsa_id].positions:
				if position.unit not in self.units:
					self.units[position.unit] = data.Unit(position.unit, position.program, position.gender_accepted)
				self.units[position.unit].update(position)

		# Create course data
		for bsa_id in self.people:
			person = self.people[bsa_id]
			if person.missing:
				for course_code,course_name in person.missing:
					if course_code not in self.courses:
						self.courses[course_code] = data.Course(course_code, course_name)
					self.courses[course_code].update(person)

	def ranking(self):
		units_by_percent_trained = sorted([(self.units[unit].trained/self.units[unit].adults, unit) for unit in self.units], reverse=True)
		print("% Trnd\tDC Trnd\tTrained\tAdults\tDC\tExpired\tNo SYT\tUnit")
		for unit in units_by_percent_trained:
			print(self.units[unit[1]])

	def ranking_direct_contact(self):
		units_by_percent_trained = sorted([(self.units[unit].trained_direct_contact/self.units[unit].adults_direct_contact if self.units[unit].adults_direct_contact>0 else 0, self.units[unit].trained/self.units[unit].adults, unit) for unit in self.units], reverse=True)
		print("% Trnd\tDC Trnd\tTrained\tAdults\tDC\tExpired\tNo SYT\tUnit")
		for unit in units_by_percent_trained:
			print(self.units[unit[2]])

	def listed(self):
		unit_keys = sorted(self.units.keys())
		print("% Trnd\tTrained\tAdults\tDC\tExpired\tUnit")
		for unit in unit_keys:
			print(self.units[unit])

	def summary(self):
		total = 0
		trained_any = 0
		trained_all = 0
		for person in self.people.keys():
			total += 1
			if self.people[person].trained_any:
				trained_any += 1
				if self.people[person].trained_all:
					trained_all += 1
		try:
			percent_any = 100.0*trained_any/total
			percent_all = 100.0*trained_all/total
			print('\t\t    Total:\t%d\n Trained for any position:\t%d\t%.2f%%\nTrained for all positions:\t%d\t%.2f%%\n'%(total, trained_any, percent_any, trained_all, percent_all))
		except:
			print(data)

	def direct_contact(self):
		total = 0
		trained = 0
		for person in self.people.keys():
			for position in self.people[person].positions:
				if position.direct_contact:
					total += 1
					if position.trained:
						trained += 1
		try:
			percent_dc = 100.0*trained/total
			print('Direct contact positions:\t%d\n\tPosition trained:\t%d\t%.2f%%\n'%(total, trained, percent_dc))
		except:
			print(data)


	def course_ranking(self):
		courses_by_needed = sorted([(self.courses[course_code].needed(), course_code) for course_code in self.courses], reverse=True)
		print("Needed\tCode\tCourse")
		for course in courses_by_needed:
			print(self.courses[course[1]])

	def person(self, name):
		ids = []
		if name in self.names.keys():
			ids.append(self.names[name])
		else:
			for n in self.names.keys():
				if name in n:
					id = self.names[n]
					ids.append(id)
		for id in ids:
			print(self.people[id])


	def not_trained(self, unit):
		for p in self.units[unit].people_not_trained:
			print(p)

	def expired(self, unit):
		for p in self.units[unit].people_expired:
			print(p)
