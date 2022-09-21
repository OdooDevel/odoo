from odoo import fields, models, api


class ScEmployee(models.Model):
    _name = 'sc.employee'
    _description = ''

    emp_name = fields.Char(required=True)
    emp_age = fields.Integer()
    emp_address = fields.Char(required=True)
    emp_sequence = fields.Char()
    emp_job_Position = fields.Char(required=True)
    emp_Salary = fields.Float(required=True)
    child = fields.Many2many('sc.employee.child')


class EmpChild(models.Model):
    _name = 'sc.employee.child'
    _description = ''
    child_name = fields.Char(required=True, string='child name')
    sequence = fields.Char(required=True, string='sequence')
    type = fields.Selection([
        ('parent_man', 'Parent_Man'),
        ('parent_wom', 'Parent_Wom'),
        ('woman', 'Woman'),
        ('child', 'Child'),
    ], string="type", default='parent_man')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ])

