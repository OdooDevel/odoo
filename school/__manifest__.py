{
	"name": "School Management",
	"summary": "To Manage School and Students",
	"description": """ 
		Odoo Course:
		- Python.
		- create module.
		- views
	""",
	"sequence": -100,
	"website": "http://frasstech2.net",
	"author": "Frasstech2",
	"data": [
		"security/security.xml",
		"security/ir.model.access.csv",
		"views/views.xml",
		"reports/student_report.xml"
	],
	"depends": ["hr"],
	"category": "Education",
	"version" : "1.0",
}