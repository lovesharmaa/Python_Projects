






dict1 = {"Harsh sharma":{"maths":11,"Science":78,"Sst":53,"Hindi":65,"English":75},
		"Shantanu":{"maths":67,"Science":58,"Sst":63,"Hindi":34,"English":23},
		"Sachin singh":{"maths":34,"Science":62,"Sst":46,"Hindi":75,"English":48},
		"Rahul yadav":{"maths":11,"Science":23,"Sst":19,"Hindi":21,"English":22},
		"Simran":{"maths":87,"Science":73,"Sst":87,"Hindi":32,"English":43},
		"Neerav jain":{"maths":90,"Science":54,"Sst":89,"Hindi":56,"English":45},
		"Angel sharma":{"maths":90,"Science":56,"Sst":70,"Hindi":65,"English":91},
		"Anant aggarwal":{"maths":78,"Science":89,"Sst":45,"Hindi":78,"English":59},
		"Manaya gupta":{"maths":67,"Science":40,"Sst":50,"Hindi":89,"English":39},
		"Kavya bansal":{"maths":23,"Science":29,"Sst":15,"Hindi":25,"English":11},
		"Monika sharma":{"maths":63,"Science":61,"Sst":46,"Hindi":73,"English":81},
		"Arnav malik":{"maths":64,"Science":53,"Sst":80,"Hindi":46,"English":49},
		"Ritika rajput":{"maths":43,"Science":56,"Sst":47,"Hindi":38,"English":49},
		"Raghav verma":{"maths":93,"Science":89,"Sst":86,"Hindi":99,"English":93},
		"Lucky rajput":{"maths":64,"Science":73,"Sst":40,"Hindi":76,"English":68},
		"Punit malhotra":{"maths":84,"Science":73,"Sst":65,"Hindi":85,"English":73},
		"Nitin rawat":{"maths":78,"Science":64,"Sst":84,"Hindi":85,"English":79},
		"Aditi gupta":{"maths":81,"Science":87,"Sst":94,"Hindi":99,"English":98},
		"Om sinha":{"maths":94,"Science":74,"Sst":64,"Hindi":74,"English":74},
		"Shiva kumar":{"maths":27,"Science":38,"Sst":30,"Hindi":46,"English":43},
		"Saloni goyal":{"maths":29,"Science":27,"Sst":25,"Hindi":35,"English":20},
		"Nitish jha":{"maths":65,"Science":85,"Sst":89,"Hindi":74,"English":23},
		"Ajeet kumar":{"maths":62,"Science":60,"Sst":65,"Hindi":65,"English":61},
		"Neha pathak":{"maths":78,"Science":45,"Sst":67,"Hindi":53,"English":48},
		"Raj kumar":{"maths":34,"Science":62,"Sst":46,"Hindi":75,"English":48},
		"Aryan rana":{"maths":19,"Science":23,"Sst":26,"Hindi":40,"English":32},
		"Dhruv rathee":{"maths":89,"Science":82,"Sst":91,"Hindi":81,"English":98},
		"Akansha viyogi":{"maths":53,"Science":64,"Sst":65,"Hindi":76,"English":67},
		"Vinay singh":{"maths":61,"Science":91,"Sst":39,"Hindi":65,"English":87},
		"Divya kumari":{"maths":67,"Science":52,"Sst":46,"Hindi":75,"English":58},
		"Ankit hooda":{"maths":74,"Science":62,"Sst":61,"Hindi":51,"English":89},
		"Bhanu patel":{"maths":34,"Science":62,"Sst":80,"Hindi":95,"English":48},
		"Tarun vats":{"maths":67,"Science":62,"Sst":70,"Hindi":81,"English":78},
		"Mohit mittal":{"maths":34,"Science":62,"Sst":46,"Hindi":75,"English":48},
		"Nisha singh":{"maths":87,"Science":53,"Sst":73,"Hindi":42,"English":48},
		"Rajat dubey":{"maths":34,"Science":62,"Sst":46,"Hindi":57,"English":73},

}
	


# print(dict1)


dict2 = {1:"Harsh sharma",
		2:"Shantanu",
		3:"Sachin singh",
		4:"Rahul yadav",
		5:"Simran",
		6:"Neerav jain",
		7:"Angle sharma",
		8:"Anant aggarwal",
		9:"Manaya gupta",
		10:"Kavya bansal",
		11:"Monika sharma",
		12:"Arnav malik",
		13:"Ritika rajput",
		14:"Raghav verma",
		15:"Lucky rajput",
		16:"Punit malhotra",
		17:"Nitin rawat",
		18:"Aditi gupta",
		19:"Om sinha",
		20:"Shiva kumar",
		21:"Saloni goyal",
		22:"Nitish jha",
		23:"Ajeet kumar",
		24:"Neha pathak",
		25:"Raj kumar",
		26:"Aryan rana",
		27:"Dhruv rathee",
		28:"Akansha viyogi",
		29:"Vinay singh",
		30:"Divya kumari",
		31:"Ankit hooda",
		32:"Bhanu patel",
		33:"Tarun vats",
		34:"Mohit mittal",
		35:"Nisha singh",
		36:"Rajat dubey",

	
}

# print(dict2)

print("__"*30)

while True:


	roll = int(input("Enter the roll number:- "))
	y = dict2[roll]
	z = dict1[y]

	marks = sum(z.values())

	per = marks/5

	if per>=60:
		div="First division"
	elif per>=45:
		div="Second division"
	elif per>=33:
		div="Third division"
	else:
		div="Fail"


	print("---------------- ⭐REPORT CARD⭐ --------------------")

	print("Name of student:-",y)

	print("-"*50)

	print("Total marks:      ",500)
	print("Marks obtained:   ",marks)
	print("Percentage:       ",per,"%")
	print("Division:         ",div)



	if per>=33:
		print("[CONGRATULATIONS ! ☀ Have a bright future]")
	else:
		print("Better luck next time...")


	print("-"*50)


	W = str(input("To check the result of another student press 2----->"))
	if W=="2":
		continue
	else:
		break

