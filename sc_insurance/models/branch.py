from odoo import fields, models, api


class ScBranch(models.Model):
    _name = 'sc.branch'
    _description = ''

    branch_name = fields.Char(required=True, string='branch name')
    branch_state = fields.Char(required=True, string='branch state')
    country_id = fields.Many2one("res.country", required=True, string='country name')
