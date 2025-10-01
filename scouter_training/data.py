import datetime
import pprint

class PersonOnePosition:
	def __init__(self, line = None):
		self.bsa_id = ''
		self.name = ''
		self.disp_name = ''
		self.email = ''
		self.unit = ''
		self.position = ''
		self.program = ''
		self.gender_accepted = ''
		self.program_position = ''
		self.direct_contact = ''
		self.trained = False
		self.expired = False
		self.missing = False

		self.course_codes = {"A90": "Wood Badge", "C31": "Den Chief Training", "C32": "BALOO (Basic Adult Ldr Outdoor Orient)", "C40": "Cubmaster and Assist Pos Specific Tng Classroom", "C42": "Cub Scout Den Ldr/Asst Pos Spec Tng Classroom", "C60": "Pack Committee Member Pos Spec Tng Classroom", "C62": "Pack Trainer Position Specific Tng", "CS02": "National Camp School:  Aquatics", "CS03": "National Camp Schl: Shooting Sports", "CS06": "National Camp School:  Commissioner", "CS07": "National Camp School:Outdoor Skills", "CS08": "National Camp School Ecology/Conserv", "CS09": "National Camp School:  Trek Leader", "CS10": "National Camp School:  Climbing", "CS11": "National Camp School C. O. P. E.", "CS12": "National Camp School:  Ranger", "CS13": "Cub/Webelos Sct Day Camp Admin/STEM", "CS15": "Shooting Sports Dir with Pistol", "CS31": "Cub Scout Archery Range Officer Tng", "CS32": "Cub Scout BB Gun Range Officer Training", "CS53": "NCAP Assessment Training", "CS54": "NCAP Authorization Training", "CS55": "National Camp Sch Resident Camp Admin", "CS56": "National Camp School Day Camp Mgmt", "CS58": "NCS COPE/Climbing Manager", "CS60": "NCS Ranger Rendezvous", "CS61": "Certified Angling Instructor Trng", "CS62": "NCS Cub Day Camp Online Prereq", "CS63": "NCS Cub Day Camp Council Prereq", "CS64": "Angling Educator Course", "CS66": "COPE Instructor in Training", "CS67": "COPE Level I Instructor", "CS68": "COPE Level II Instructor", "CS69": "Low COPE Level I Instructor", "CS70": "Low COPE Level II Instructor", "CS71": "Low COPE Director", "CS72": "Climbing Instructor in Training", "CS73": "Climbing Level I Instructor", "CS74": "Climbing Level II Instructor", "CS75": "Artificial Climbing Struc LI Inst", "CS76": "Artificial Climbing Struc LII Inst", "CS77": "Portable Climbing Wall Instructor", "CS78": "Bouldering Facilitator", "CS79": "COPE & Climbing Trng Pgrm Evaluator", "CS81": "BSA Safety and Marksmanship Program", "CS82": "NRA Rifle Instructor", "CS83": "NRA Pistol Instructor", "CS84": "NRA Shotgun Instructor", "CS85": "NRA Muzzleloader Instructor", "CS86": "NRA RSO", "CS87": "NRA CRSO", "CS88": "USA Archery Level 1 Instructor", "CS89": "USA Archery Level 2 Instructor", "CS90": "USA Archery Level 3 Instructor", "CS91": "NCS: Resident Camp Director", "CS92": "NCS: Resident Camp Program Director", "CS94": "CD Preventing Youth on Youth Abuse", "CS95": "CS Preventing Youth on Youth Abuse", "CS96": "NCAP Assessor Online Training", "CS97": "IOWLS", "CS98": "AOWLS", "CS99": "Short-Term Camp Administrator-STCAT", "D17": "Council Commissioner Position-Specific Training", "D18": "DC/ADC Commissioner Position-Specific Training", "D19": "Roundtable Commissioner Position-Specific Training", "D20": "Unit Commissioner Position-Specific Training", "D21": "Bachelor of Commissioner Science", "D22": "Master of Commissioner Science", "D23": "Doctor of Commissioner Science", "D25": "Advanced Commissioner Training", "D27": "CST Commissioner Position-Specific Training", "D61": "District Committee Basic Training", "D70": "Train-the-Trainer (Fundamentals)", "D71": "Council Officer Training", "D72": "Training the Chartered Org Rep Classroom", "D73": "Relationships Conference", "D74": "BSA Leave No Trace Basics", "D75": "Health and Safety Training", "D76": "Merit Badge Counselor Orientation Classroom", "D78": "Leave No Trace Level 1 Instructor", "D79": "Leave No Trace Level 2 Instructor", "D80": "Tread Lightly! Trainer", "D81": "Tread Lightly! Master Tread Trainer", "D82": "Supernova Mentor Training", "D83": "Nova Counselor Training", "D84": "Leave No Trace Skills Course", "D86": "Advanced Chaplain Training", "E00": "Exploring Orientation", "E05": "Exploring Certification", "E15": "Exploring Certification", "F12": "First Aid Instructor", "H101": "Philmont Training Center Conference", "H102": "Florida Sea Base Conference", "H105": "Cold Weather Leader Training", "H106": "Summit Conference", "H107": "Westlake Campus Conference", "H109": "Council President/Vice President Tr", "H110": "OA DYLC-Developing Youth Leadership Conf", "H112": "Commissioner Impact Session", "H113": "Commissioner College CED", "H114": "BSA DCSA Adviser/Committee Member", "H49": "Health and Safety/Risk Management", "H91": "Council Executive Board Training", "H96": "Trainer's EDGE", "H97": "Leadership Challenge", "L01": "Explorer Leader Adult Basic Training - Classroom", "L02": "Teacher Training for LFL School Pgm", "L03": "Career Seminar / Workshop Presentor", "L04": "Post Leader Workshop", "L05": "LFL Committee Workshop", "L06": "LFL Marketing Team Workshop", "L07": "LFL Program Team Workshop", "L08": "Finance Campaigns 'How To' in LFL", "L15": "LFL Curriculum Based Certification", "N01": "First Aid", "N02": "Wilderness First Aid", "N03": "Wilderness First Responder", "N04": "First Responder", "N05": "CPR", "N06": "CPR/AED", "N07": "Defensive Driving", "N08": "CPR Instructor", "N09": "CPR Instructor Trainer", "N10": "Wilderness First Aid Instructor", "N11": "WFA Instructor Trainer", "N12": "First Aid Instructor", "N13": "First Aid Instructor Trainer", "P21": "Venturing Leader Specific Training - Classroom", "P30": "Sea Scout Leader Specialized Tng", "P31": "Crew Officers' Seminar", "P33": "Kodiak Challenge", "P35": "ILSC-Intro Leadershp Skills-Crews", "P36": "Venturing Goal Setting/Time Mgmt", "P37": "Venturing Project Management", "P38": "Venturing Mentoring", "P39": "Sea Scout Leader Fast Start", "P40": "SEAL", "P41": "Sea Badge Underway", "P42": "Sea Badge Underway Instructor", "P43": "Sea Scout Adv Leader Training Inst", "P44": "Sea Scout Adult Ldr Basic Training - Classroom", "P45": "Sea Scout - Seamanship", "P46": "Sea Scout - Piloting", "P47": "Boating Safety", "P48": "ILSS-Intro Leadership Skills-Ships", "P50": "Powder Horn Training", "P51": "Powder Horn Course Directors Conference", "P60": "The Strategic Training Plan", "P61": "Mentoring", "P70": "Wood Badge Course Directors Conf", "P71": "NYLT Course Directors Conference", "P91": "Sea Badge (Sea Scouts)", "P92": "Sea Badge CDC", "P93": "Kodiak Course Directors Conference", "S09": "The Outdoor Program", "S100": "Multi-Gun Airsoft Training", "S102": "NYLT Leadership Academy", "S11": "Intro to Outdoor Leader Skills", "S110": "Outdoor Ethics Orientation (Youth)", "S111": "Outdoor Ethics Orientation (Adult)", "S112": "OA LLD Lodge Leadership Development", "S24": "Scoutmaster/Assistant Specific Training Classroom", "S35": "OA NLS National Leadership Seminar", "S36": "OA NLATS Lodge Adviser Training", "S54": "Certified Angling Instructor", "S55": "Certified Angling Educator", "S58": "COPE Program Manager", "S59": "Chain Saw Safety", "S74": "Climb on Safely Classroom", "S75": "Council Climbing Instructor", "S76": "Trek Safely Classroom", "S77": "Scouting Safety Begins With Ldrship", "S78": "National Youth Leadership Training", "S80": "Natl Adv Youth Ldrship Experience", "S81": "BSA Lifeguard", "S82": "Swimming and Water Rescue", "S83": "Paddle Craft Safety", "S84": "Swimming & Water Rescue Instructor", "S85": "Paddle Craft Safety Instructor", "S96": "NYLT to NAYLE Bridge", "S97": "ILST-Intro Leadership Skills-Troops", "S98": "BSA Lifeguard Instructor", "S99": "BS Pistol Safety/Marksmanship Trng", "SA": "Safety Afloat Classroom", "SCO_1000": "Aims and Methods", "SCO_1002": "BSA Organizational Structure Development", "SCO_1003": "What is Boy Scouting", "SCO_1004": "What is Cub Scouting", "SCO_1005": "What is Exploring", "SCO_1006": "What is Learning for Life", "SCO_1007": "What is Venturing", "SCO_101": "Venturing - Getting Started", "SCO_1012": "District Committee Structure", "SCO_1018": "Profile for a District Chair", "SCO_102": "Venturing - Officer Selection", "SCO_103": "Venturing - Crew Structure", "SCO_104": "Venturing - Membership Recruiting", "SCO_1042": "New Unit Application", "SCO_1047": "Selling Exploring to a CEO", "SCO_1048": "Develop an Explorer Post Program", "SCO_1049": "Conduct an Exploring Open House", "SCO_105": "Venturing - Fundraising and Budgeting", "SCO_106": "Venturing - Board of Review", "SCO_1061": "Community Campaign-Build I C 5 or Table Host Team", "SCO_1062": "District Fund Development Committee Guidebook", "SCO_1063": "Family Campaign - Family FOS Presenter Qualities", "SCO_1064": "Family Campaign Family FOS Presentation", "SCO_1066": "Family Campaign How to make a Family FOS Ask", "SCO_1067": "Fundraising Cycle", "SCO_1068": "Mechanics of a Campaign", "SCO_107": "Venturing - Event Planning", "SCO_1076": "Customizing Promotional Fliers for Units", "SCO_1077": "Membership Cycle", "SCO_1078": "New Unit Development Process", "SCO_108": "Venturing - Advising vs Leading", "SCO_109": "Venturing - Positive Youth Development", "SCO_110": "Venturing - Awards Program", "SCO_11000": "Strategic Training Plan Objectives and Goals", "SCO_11001": "Introduction to SMART Goals", "SCO_11002": "SWOT Analysis", "SCO_11003": "Introduction to Downloading Training Data", "SCO_11004": "Available Resources for Council & Dist Trng Teams", "SCO_11012": "District Committee Structure v2", "SCO_11013": "Four Functions of a District v2", "SCO_11016": "District Meetings - District Committee Meeting v2", "SCO_11017": "Meetings of the District - Key 3 Video v2", "SCO_11027": "Backdating v2", "SCO_11040": "Adult Applications v2", "SCO_11043": "Registration Fees v2", "SCO_11044": "Youth Applications v2", "SCO_11053": "Commissioner Structure v2", "SCO_11056": "What is Commissioner Service v2", "SCO_11059": "Council Budget v2", "SCO_11060": "Community Campaign Asking for a FOS Gift v2", "SCO_11065": "Family Campaign Followup Family FOS v2", "SCO_11080": "New Unit Organization Committee v2", "SCO_11083": "Recruiting Event Time Line and Roles v2", "SCO_1109": "What is Scouts BSA", "SCO_111": "Venturing - Officer Training", "SCO_11100": "Volunteer Recruitment Call v2", "SCO_11105": "Activities and Civic Service v2", "SCO_11106": "Advancement v2", "SCO_11107": "Scouting Safely v2", "SCO_11108": "BSA Insurance Coverage v2", "SCO_112": "Annual Program Planning for Venturing", "SCO_113": "Venturing - Selecting Advisors", "SCO_114": "Venturing - Interacting with Young Adults", "SCO_115": "Crew Officers Orientation", "SCO_1200": "Chaplain Roles and Responsibilities", "SCO_12000": "Welcome and Overview", "SCO_12001": "Quality Presentations", "SCO_12002": "Health and Safety in Wood Badge", "SCO_12003": "Day One Overview", "SCO_12004": "The Ticket", "SCO_12005": "Day Two Overview", "SCO_12006": "Day Three Overview", "SCO_12007": "Day Four Overview", "SCO_12008": "Youth in Wood Badge", "SCO_12009": "Day Five Overview", "SCO_1201": "Religious Emblems and Awards", "SCO_12010": "Time Management", "SCO_12011": "Course Connections / Leadership Connections", "SCO_12012": "Q/A Topics", "SCO_12013": "Culture Heart of a Servant", "SCO_12014": "WB Staff Recruiting and Development", "SCO_12015": "WB Team Based Learning", "SCO_12016": "WB Methods and Model", "SCO_12017": "Wood Badge Pre-course Orientation", "SCO_1202": "Interfaith Considerations", "SCO_1203": "Selling Exploring to Guidance Counselors", "SCO_1264": "Membership Ethics", "SCO_1265": "School Talks", "SCO_1266": "Council Market Analysis v2", "SCO_14000": "NCAP Assessor Training New", "SCO_14001": "Foundations of Cub Scout Day Camp New", "SCO_14002": "NCS Camp Health Officer", "SCO_1500": "District Key 3", "SCO_15000": "What is NYLT", "SCO_15001": "Course Consistency", "SCO_15002": "Course Staffing and Recruiting", "SCO_15003": "Diversity and Inclusion", "SCO_15004": "Health and Safety", "SCO_15005": "Youth on Youth Abuse", "SCO_15006": "Quality Presentation", "SCO_15007": "Communicating", "SCO_15008": "Coaching and Mentoring", "SCO_15009": "Course Directors Pledge", "SCO_1501": "Program Chair Overview", "SCO_1502": "District Resources", "SCO_1503": "Expectations and Accountability", "SCO_1504": "my.scouting Tools", "SCO_1505": "District Relationship to the Council", "SCO_1506": "District Evaluation and JTE", "SCO_1507": "Recruiting District People", "SCO_1508": "Planning for Success", "SCO_1509": "Camping and Outdoor Chair", "SCO_1510": "Training Chair", "SCO_1600": "ILST Introduction to Leadership Skills", "SCO_16001": "Specific Duties of the Board", "SCO_16002": "Council Functions", "SCO_16003": "Local Council Relationship to National Council", "SCO_16004": "More About the Local Council", "SCO_16005": "Board Governance Obedience, Care, and Loyalty", "SCO_16006": "Responsibilities of the Council Officers", "SCO_16007": "Strategic Planning", "SCO_16008": "The Local Council Funding Program", "SCO_16009": "Understanding the Council Financial Statement", "SCO_1601": "Creating a Vision", "SCO_16010": "President Guidelines in Leading Others", "SCO_16011": "President Guidelines in Leading the Organization", "SCO_1602": "Goal Setting", "SCO_1603": "Communication", "SCO_1604": "Planning and Delegation", "SCO_1605": "Stages of Team Development", "SCO_1606": "ILSC Introduction to Leadership Skills", "SCO_165": "School Talks", "SCO_1800": "Diversity, Equity, and Inclusion", "SCO_18000": "DCSA Introduction", "SCO_18001": "DCSA Role of the Adviser", "SCO_18002": "DCSA Projects", "SCO_18003": "DCSA Requirements", "SCO_18004": "DCSA Categories", "SCO_18005": "DCSA Workbook", "SCO_18006": "DCSA Field Trip", "SCO_18007": "DCSA Documentation", "SCO_19000": "The OWASP Top 10", "SCO_19001": "Secure Coding", "SCO_20001": "Lodge Leader Training Introduction", "SCO_20002": "Youth Led", "SCO_20003": "Lodge Leader Training - The Key 3", "SCO_20004": "Handbook for Officers and Advisers", "SCO_20005": "Lodge Leader Training Resources", "SCO_20006": "Lodge Communications", "SCO_20007": "Selecting Your Associates", "SCO_20008": "Lodge Elections", "SCO_20009": "Lodge Inductions", "SCO_20010": "Ceremonies", "SCO_20011": "What is the LEC?", "SCO_20012": "Roberts Rules of Order", "SCO_207": "Cub Scout Program Overview - June 2015 and Beyond", "SCO_231": "Working With Your Den Leader", "SCO_232": "Understanding Boys in the Den", "SCO_267": "What is a Charter?", "SCO_268": "Scouting Units", "SCO_269": "The COR Position", "SCO_270": "BSA Standards and Volunteers", "SCO_275": "Chartering to a Catholic Institution", "SCO_276": "Reaching Youth Through Scouting", "SCO_277": "Your Role as a Catholic COR", "SCO_278": "Catholic Scouting under BSA Standards", "SCO_280": "Introduction to the Cub Scout Outdoor Program v2", "SCO_281": "Pack Camping Program", "SCO_282": "Planning Your Cub Scout Outdoor Event v2", "SCO_283": "Planning Your Event", "SCO_3000": "Neglect Prevention", "SCO_3000S": "NEGLIGENCIA", "SCO_3001": "YPT Overview and Policies - Part 1 of 4", "SCO_3002": "Emotional Abuse Prevention", "SCO_3002S": "ABUSO EMOCIONAL", "SCO_3003": "YPT Sexual Abuse Prevention - Part 2 of 4", "SCO_3004": "YPT Bullying Prevention - Part 3 of 4", "SCO_3005": "Exposure to Violence Prevention", "SCO_3005S": "EXPOSICION A VIOLENCIA", "SCO_3006": "Physical Abuse Prevention", "SCO_3006S": "ABUSO FISICO", "SCO_3007": "YPT Certification Test - Part 4 of 4", "SCO_3008": "Overview and Policies", "SCO_3008S": "RESUMEN Y POLITICAS", "SCO_3009": "Sexual Abuse", "SCO_3009S": "ABUSO SEXUAL", "SCO_301": "Structure of an Exploring Program", "SCO_3010": "Bullying", "SCO_3010S": "INTIMIDACION", "SCO_3011": "YPT Certification Test", "SCO_3011S": "Prueba de certificacion de la capacitacion de Proteccion Juvenil", "SCO_302": "What Is Exploring?", "SCO_303": "Benefits of Exploring", "SCO_304": "Positive Youth Development for Exploring", "SCO_305": "Parts of a Meeting for Exploring", "SCO_306": "Marketing Your Exploring Program", "SCO_307": "Methods of Exploring", "SCO_308": "Registering and Renewing for Exploring", "SCO_309": "Safety Tips for Exploring", "SCO_310": "Developing SOPs and Bylaws for Exploring", "SCO_311": "Annual Program Planning for Exploring", "SCO_312": "Youth-Led Programs for Exploring", "SCO_313": "Youth Officer Elections for Exploring", "SCO_314": "Open House for Exploring", "SCO_315": "Program Fundraising for Exploring", "SCO_316": "Activity Planning for Exploring", "SCO_317": "Conducting an Officer Seminar for Exploring", "SCO_318": "Service Team Orientation for Exploring", "SCO_319": "Ride Along Safely", "SCO_350": "YE Introduction to Leadership", "SCO_351": "YE Planning", "SCO_352": "YE Time Management", "SCO_353": "YE Self Regulation and Goal Setting", "SCO_354": "YE Diversity and Culture", "SCO_355": "YE Ethics", "SCO_356": "YE Character of Leadership", "SCO_357": "YE Motivation", "SCO_358": "YE Communication", "SCO_359": "YE Meeting Management", "SCO_360": "YE Group Management", "SCO_361": "YE Managing Through Others", "SCO_362": "YE Decision Making", "SCO_419": "Chaplain Roles and Responsibilities Boy Scouting", "SCO_420": "Chaplain Emblems and Awards for Boy Scouting", "SCO_421": "Chaplain Interfaith Opportunities Boy Scouting", "SCO_450": "CS19 Welcome", "SCO_451": "CS19 Aims and Methods of Cub Scouting", "SCO_452": "CS19 Bobcat", "SCO_453": "CS19 Advancement", "SCO_454": "CS19 Cub Scout Uniforms", "SCO_455": "CS19 Conducting a Cub Scout Den Meeting", "SCO_456": "CS19 Resources", "SCO_457": "CS19 Den Management", "SCO_458": "CS19 Conducting a Cub Scout Pack Meeting", "SCO_459": "CS19 Conducting a Pack Committee Meeting", "SCO_460": "CS19 Preparing Families for Outdoor Adventures", "SCO_461": "CS19 Keeping Cub Scouting Safe", "SCO_462": "CS19 Involving Adults in Cub Scouting", "SCO_463": "CS19 Pack Structure", "SCO_464": "CS19 Denners and Den Chiefs", "SCO_465": "CS19 Childhood Development", "SCO_466": "CS19 Continue the Journey", "SCO_467": "CS19 Pack Finance", "SCO_468": "CS19 Annual Program Planning for Cub Scouting", "SCO_469": "CS19 Annual Charter Renewal Rechartering", "SCO_471": "Advancement", "SCO_472": "Aims and Methods of Scouts BSA", "SCO_473": "Annual Troop Program Planning", "SCO_474": "Introduction to Merit Badges", "SCO_475": "Outdoor Ethics", "SCO_476": "Outdoor Programs", "SCO_477": "Patrol Leaders Council Meeting", "SCO_478": "Patrol Method", "SCO_479": "Role of  the Unit Key 3", "SCO_480": "Roles of Scoutmaster and SPL", "SCO_481": "Scouting Organization", "SCO_482": "Troop Committee", "SCO_483": "Troop Committee Meetings", "SCO_484": "Troop Meeting", "SCO_485": "Scouts BSA Uniforms", "SCO_486": "What is a Merit Badge Counselor", "SCO_530": "Journey to Excellence", "SCO_535": "New Member Coordinator Welcome Course", "SCO_536": "Elements of the Job", "SCO_550": "What is STEM Scouts", "SCO_551": "The STEM Scouts Portal", "SCO_552": "STEM Lab Meeting and Structure", "SCO_553": "Lab Safety", "SCO_554": "Working with STEM Scouts", "SCO_555": "STEM Scouts Committee", "SCO_560": "BSA STEM Nova", "SCO_561": "Nova Counselor", "SCO_562": "Supernova Mentor", "SCO_570": "BSAA Creating the Committee", "SCO_571": "BSAA The Committee Chair's Role", "SCO_572": "BSAA The Scout Executive's Role", "SCO_573": "BSAA Affiliate & Affinity Group Relationships", "SCO_574": "BSAA Awards and Recognition", "SCO_575": "BSAA Communications", "SCO_576": "BSAA General User", "SCO_577": "BSAA Specialist", "SCO_600": "Sea Scout Getting Started", "SCO_601": "Starting and Reorganizing Your Ship", "SCO_602": "Planning Your Ships Program", "SCO_603": "Sea Scout Youth Leadership Development", "SCO_604": "Sea Scout Resources", "SCO_605": "Sea Scout Advancement", "SCO_606": "Sea Scout Uniforms", "SCO_607": "What is Sea Scouts", "SCO_620": "Planning a Long Cruise", "SCO_621": "Executing a Long Cruise", "SCO_700": "Why Build a Unit Service Plan", "SCO_701": "Collaborative Assessment and Key Concepts", "SCO_702": "Intermediate Assessment", "SCO_703": "Developing a Collaborative Unit Assessment", "SCO_704": "Developing a Unit Service Plan", "SCO_705": "Updating a Unit Service Plan", "SCO_720": "Accessing Commissioner Tools", "SCO_721": "The Units Tab in Commissioner Tools", "SCO_722": "Entering a Unit Contact in Commissioner Tools", "SCO_723": "Unit Assessment Scoring Matrix", "SCO_724": "Entering a Simple Assessment", "SCO_725": "The Detailed Assessment for Commissioners Tools", "SCO_726": "Collaborative Assessment for the Unit Key 3", "SCO_727": "The Reports Button for Commissioner Tools", "SCO_728": "Using the Discussion Tab in Commissioner Tools", "SCO_729": "The Roundtable Tab in Commissioner Tools", "SCO_730": "Using the Commissioner Tools Profile Tab", "SCO_731": "Commissioner Administration", "SCO_732": "Creative Pivot Tables - SCO_732", "SCO_733": "Commissioner Structure", "SCO_734": "Role of the Unit Commissioner", "SCO_735": "Contacting Units and Capturing Strengths/Need", "SCO_737": "The Roundtable Commissioner", "SCO_738": "The Six Ws of Roundtables", "SCO_739": "The Roundtable ADC and ACC", "SCO_740": "District Structure", "SCO_742": "The District Commissioner Role", "SCO_743": "The Assistant District Commissioner Role", "SCO_744": "Monthly Commissioner Staff Meeting", "SCO_746": "Journey to Excellence for Comm", "SCO_747": "Unit Service Plan", "SCO_748": "Support On Time Charter Renewal", "SCO_749": "Commissioners Training Continuum and Resources", "SCO_750": "LDS Commissioner Orientation", "SCO_751": "Using the Roundtable Planning Guides", "SCO_752": "Council Commissioner Roles and Responsibilities", "SCO_753": "The Council Commissioner Staff", "SCO_754": "Meetings of the Council Commissioner", "SCO_755": "Unit Comm Onboarding Worksheet Acknowledgement", "SCO_756": "Servicing Exploring Units", "SCO_757": "The Roundtable Team", "SCO_758": "Commissioner Service Foundation", "SCO_759": "DC/ADC Commissioner Onboarding Worksheet", "SCO_760": "Council Commissioner Onboarding Worksheet", "SCO_762": "RT Commissioner Onboarding Worksheet", "SCO_763": "Regional and Area Organization", "SCO_764": "Roles of the Regional and Area Commissioner", "SCO_765": "Tools Available to the Regional and Area Comm", "SCO_766": "Area Regional Comm Onboarding Worksheet", "SCO_770": "Unit Service Concepts-Unit Commissioner", "SCO_771": "District Level Unit Service", "SCO_772": "Unit Contacts", "SCO_773": "Unit Assessments", "SCO_774": "Commissioner Tools Navigation and Simple Assessments", "SCO_775": "Detailed Assessments and Unit Service Plan", "SCO_776": "Unit Service Plan V2", "SCO_777": "The District", "SCO_778": "Working with New Units", "SCO_779": "Youth Protection and Unit Resources", "SCO_780": "Charter Renewal", "SCO_781": "Commissioner Development", "SCO_782": "Roundtable Fundamentals", "SCO_783": "Roundtable Administration", "SCO_784": "Roundtable Organization", "SCO_785": "Roundtable Preparation", "SCO_786": "Components of Roundtable", "SCO_787": "Roundtable Tools", "SCO_788": "Roles of the Council Commissioner", "SCO_789": "Building the Team", "SCO_790": "Meetings of the Council Commissioner V2", "SCO_791": "Monitoring Unit Service", "SCO_792": "Commissioner Tools Reports", "SCO_793": "Commissioner Tools for AdministrativeCommissioners", "SCO_794": "Commissioner Tools for Roundtable Commissioners", "SCO_795": "Developing and Recognizing Commissioners", "SCO_796": "Council Support", "SCO_800": "Hazardous Weather Training", "SCO_801": "Safe Swim Defense", "SCO_802": "Safety Afloat", "SCO_803": "Trek Safely", "SCO_804": "Climb On Safely", "SCO_805": "Drive Safely", "SCO_806": "Volunteer Impact on Membership", "SCO_807": "Recruiting Unit Leaders", "SCO_808": "Volunteer Recruitment", "SCO_809": "Succession Planning", "SCO_900": "Unit Service in the District", "SCO_901": "Selecting & Assigning Unit Commissioners", "SCO_902": "Monitoring Unit Service in the District", "SCO_903": "Monthly District Commissioner Meeting", "SCO_904": "Unit Service Concepts-Roundtable Commissioner", "SCO_905": "Unit Service Concepts-Council Commissioner", "SCO_906": "Unit Service Concepts-District Commissioner", "SCO_907": "Charter Renewal in the District", "SCO_908": "Developing and Recognizing Commissioners District", "SPW": "Physical Wellness", "SSD": "Safe Swim Defense Classroom", "STEM": "STEM Scouts Adult Leader Training", "T00": "Tiger Adult Orientation", "V21": " Varsity Coach Leader Specific Tng", "WD77": "Staffing the District Committee", "WD80": "Generational Diversity", "WS10": "Troop Committee Challenge-Classroom", "WS11": "Team Committee Challenge-Classroom", "WS12": "Crew Committee Position Specific - Classroom", "Y01": "Youth Protection Training Certification"}

		if line:
			self.init_from_line(line)

	def __str__(self):
		retval = f"{self.disp_name}\n{self.bsa_id}\n{self.position}\nTrained: {self.trained}"
		if self.expired:
			retval += f"\nExpired: {self.expired}"
		if self.missing:
			retval += f"\nMissing:"
			for item in sorted(list(self.missing)):
				retval += '\n  %s - %s'%item
		retval += "\n"
		return retval

	def __repr__(self):
		return f"Person({self.disp_name}, {self.position}, {self.bsa_id}, trained={self.trained})"

	def init_from_line(self, line):
		Council,Service_Area,District,Sub_District,Unit,Gender_Accepted,Chartered_Org_Name,First_Name,Middle_Name,Last_Name,Zip_Code,MemberID,Program,Email,Position,Direct_Contact_Leader,Trained,Registration_Expiration_Date,Incomplete_Mandatory,Incomplete_Classroom,Incomplete_Online = line
		self.bsa_id = int(MemberID)
		self.name = '%s, %s'%(Last_Name, First_Name)
		if Middle_Name:
			self.name += ' %s'%(Middle_Name)
			self.disp_name = '%s %s %s'%(First_Name, Middle_Name, Last_Name)
		else:
			self.disp_name = '%s %s'%(First_Name, Last_Name)
		if Unit:
			self.unit = Unit
		else:
			self.unit = District
		if Program:
			self.program = Program
		else:
			self.program = "District"
		self.email = Email
		self.position = Position
		if self.program:
			self.program_position = '%s - %s'%(self.program, self.position)
		else:
			self.program_position = self.position
		self.gender_accepted = Gender_Accepted
		self.direct_contact = Direct_Contact_Leader == "YES"
		self.trained = Trained == "YES"
		self.missing = set([])

		for item in Incomplete_Mandatory.split():
			self.missing.add(self.get_course_code(item))
		for item in Incomplete_Online.split():
			self.missing.add(self.get_course_code(item))
		expiration = datetime.datetime.strptime(Registration_Expiration_Date, '%m/%d/%Y')
		self.expired = expiration < datetime.datetime.now()

	def get_course_code(self, item):
		course_code = item.strip(',')
		if course_code in self.course_codes.keys():
			return (course_code, self.course_codes[course_code])
		else:
			return (course_code, '')


class PersonAllPositions:
	def __init__(self, person):
		self.bsa_id = person.bsa_id
		self.syt = True
		self.name = person.name
		self.disp_name = person.disp_name
		self.email = person.email
		self.positions = [person]
		self.trained_any = person.trained
		self.trained_all = person.trained
		self.direct_contact = person.direct_contact
		self.expired = person.expired
		self.missing = person.missing

	def __str__(self):
		return f"{self.disp_name}, {self.bsa_id}"

	def update(self, person):
		self.positions.append(person)
		self.trained_all &= person.trained
		self.trained_any |= person.trained
		self.direct_contact |= person.direct_contact
		self.expired |= person.expired
		self.missing |= person.missing

	def syt_update(self, sy_trained):
		self.syt = sy_trained
		if not sy_trained:
			self.trained_all = False
			self.trained_any = False
			for position in self.positions:
				position.trained = False

class Unit:
	def __init__(self, unit_name, program, gender_accepted):
		self.unit = unit_name
		self.program = program
		self.gender_accepted = gender_accepted
		self.adults = 0
		self.trained = 0
		self.expired = 0
		self.key3_trained = True
		self.people = []
		self.people_trained = []
		self.people_not_trained = []
		self.people_expired = []
		self.key3_positions = ['Chartered Organization Rep.', 'Committee Chair', 'Scoutmaster', 'Cubmaster', 'Skipper', 'Venturing Crew Advisor', 'District Chair', 'District Commissioner']

	def __str__(self):
		percent_trained = 100*self.trained/self.adults
		return f"{percent_trained:.2f}%\t{self.trained}\t{self.adults}\t{self.expired}\t{self.unit}"

	def update(self, person, use_expiration=False):
		if use_expiration and person.expired:
			self.people_expired.append(person)
			self.expired += 1
		else:
			self.people.append(person)
			self.adults += 1
			if person.trained:
				self.people_trained.append(person)
				self.trained += 1
			else:
				self.people_not_trained.append(person)
			if person.position in self.key3_positions:
				self.key3_trained &= person.trained

	def percent_trained(self):
		return(100.0*self.trained/self.adults)

	def need_training(self):
		self.print_list(self.people_not_trained)

	def all_people(self):
		self.print_list(self.people)

	def need_renewing(self):
		self.print_list(self.people_expired)

	def print_list(self, obj):
		for item in obj:
			print(item)
			print('')

