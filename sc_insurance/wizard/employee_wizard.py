from odoo import fields, models, api


class EmployeeWizard(models.TransientModel):
    _name = 'employee.wizard'
    emp_name = fields.Char(required=True)
    emp_age = fields.Integer()
    emp_address = fields.Char(required=True)
    emp_sequence = fields.Char()
    emp_job_Position = fields.Char(required=True)
    emp_Salary = fields.Float(required=True)

    def send_to_accept(self):
        for rec in self:
            self.env['sc.employee'].create(rec)
