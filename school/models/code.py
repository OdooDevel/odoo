from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import date, datetime


# student
class Student(models.Model):
    _name = "school.student"

    _sql_constraints = [
        ('name_uniq', 'unique (name)', _('The name must be unique !')),
    ]

    name = fields.Char(string="Student Name", required=True)
    number = fields.Integer()
    description = fields.Text()
    year = fields.Date()
    register_date = fields.Datetime()
    image = fields.Binary()
    birthdate = fields.Date()
    age = fields.Integer(compute="_cal_age", store=True)
    age2 = fields.Integer()
    cv = fields.Html()
    is_register = fields.Boolean(readonly=True)
    degree = fields.Float()
    state = fields.Selection(selection=[("draft", "Draft"), ("studying", "Studying"), ("graudate", "Graudate")],
                             default="draft")
    fees = fields.Float(help="Enter the money that must paid by student", digits=(2, 6))
    gender = fields.Selection(selection=[("male", "Male"), ("female", "Female")], default="male")
    room_id = fields.Many2one("school.room")
    subjects = fields.Many2many("school.subject")

    def studying(self):
        for rec in self:
            rec.state = "studying"

    def graudate(self):
        for rec in self:
            rec.state = "graudate"

    @api.depends("birthdate")
    def _cal_age(self):
        for rec in self:
            today = datetime.today()
            if self.birthdate:
                rec.age = today.year - rec.birthdate.year
            # 12	 =	2022 - 2010
            else:
                rec.age = 0

    @api.onchange("birthdate")
    def _onchange_cal_age(self):
        for rec in self:
            today = datetime.today()
            if self.birthdate:
                rec.age2 = today.year - rec.birthdate.year
            # 12	 =	2022 - 2010
            else:
                rec.age2 = 0

    # @api.constrains("number")
    # def _check_number(self):

    # ORM Search Enviroument
    # result = self.env["school.student"].search([
    # 	('number','=',1)
    # 	# ('field','operater','value')
    # ])

    # ORM Delete Enviroument
    # result.unlink()

    # ORM Custom Method Enviroument
    # result._cal_age()

    # ORM Update Enviroument
    # result.write({
    # 	"number":2
    # })

    # ORM Create Enviroument
    # student = self.env["account.move"].create({
    # 	"name":"Omer Abdallah"
    # })

    # for rec in self:
    # 	if result:
    # 		raise UserError("This number is already registered!")

    @api.model
    def create(self, vals):
        # before the database (raw)
        # raise UserError(vals["register_date"])
        # vals["name"] = "Osman ,Omer"
        rec = super(Student, self).create(vals)
        # after the database (python datatypes)
        # raise UserError(rec.register_date.year)
        return rec

    def write(self, vals):

        if "state" in vals:
            if vals["state"] == "studying":
                vals["description"] = "dshfhskf"

        return super(Student, self).write(vals)

    def unlink(self):
        if self.is_register:
            raise UserError("Is student is already registred.")
        return super(Student, self).unlink()


# lesson
class Lesson(models.Model):
    _name = "school.lesson"
    name = fields.Char()
    number = fields.Integer()
    subject_id = fields.Many2one("school.subject")
    time = fields.Datetime()


class Subject(models.Model):
    _name = "school.subject"
    name = fields.Char()
    number = fields.Integer()
    description = fields.Text()
    lessons = fields.One2many("school.lesson", "subject_id")


class Teacher(models.Model):
    _name = "school.teacher"
    name = fields.Char()
    phone = fields.Char()
    cv = fields.Html()
    description = fields.Text()
    image = fields.Binary()


class TeacherHR(models.Model):
    _inherit = "hr.employee"

    subjects = fields.Many2many("school.subject")
    supervisor_room = fields.Many2one("school.room")


class Room(models.Model):
    _name = "school.room"
    # _rec_name = "title"
    name = fields.Char()
    students = fields.One2many("school.student", "room_id")
