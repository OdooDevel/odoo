from odoo import fields, models, api
from odoo.exceptions import UserError


class ScCompany(models.Model):
    _name = 'sc.company'
    _description = ''
    _rec_name = 'company_name'

    company_name = fields.Char(required=True)
    company_index = fields.Char(required=True)
    company_no = fields.Char(required=True)
    position = fields.Char(required=True, string='position name')
    date = fields.Date(rquired=True)
    manager = fields.Char(required=True)
    location = fields.Char(string='location name')
    branch_ids = fields.Many2many('sc.branch')
    emp_ids = fields.Many2many('sc.employee', string='emp_ids')

    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirm'),
                              ('set_to_draft', 'Set Draft')
                              ], string='State', default='draft')

    # total_sum = fields.Float(string='Sum Total', compute='_compute_total_salary', store=True)
    # total_dec = fields.Float(compute='_compute_dec', string='Total Dec', store=True)
    # tax = fields.Float(string='Tax')

    def action_confirm(self):
        self.state = 'confirm'

    def action_draft(self):
        self.state = 'draft'

    def unlink(self):
        for rec in self:
            if rec.state == 'confirm':
                raise UserError(('Sorry you can not delete Emp in confirm state'))
            rtn = super(ScCompany, self).unlink()
            return rtn

    # @api.depends('emp_ids')
    # def _compute_total_salary(self):
    #     for rec in self:
    #         total_sum = 0.0
    #         for line in rec.emp_ids:
    #             total_sum += line.emp_Salary
    #             rec.update({
    #                 'total_sum': total_sum
    #             })
    #
    # @api.depends('total_sum', 'tax')
    # def _compute_dec(self):
    #     for rec in self:
    #         rec.total_dec = rec.total_sum - rec.tax
