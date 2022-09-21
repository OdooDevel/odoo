from odoo import models, fields


class Airlines(models.Model):
    _name = "agency.airline"

    number = fields.Integer()
    name = fields.Char()

    services = fields.Many2many("product.template")
    flights = fields.One2many("product.template", "airline")


class Locations(models.Model):
    _name = "agency.location"

    name = fields.Char(required=True)
    lat = fields.Float()
    lng = fields.Float()


class Flight(models.Model):
    _inherit = "product.template"

    from_loc = fields.Many2one("agency.location")
    to_loc = fields.Many2one("agency.location")

    dep_time = fields.Datetime()
    ari_time = fields.Datetime()
    total_time = fields.Float()

    airline = fields.Many2one("agency.airline")


class Passenger(models.Model):
    _inherit = "res.partner"

    number = fields.Integer()
    passport_no = fields.Integer()
    flight = fields.Many2one("product.template")
    bookings = fields.One2many("sale.order", "partner_id")


class Booking(models.Model):
    _inherit = "sale.order"

    airline = fields.Many2one("agency.airline")
