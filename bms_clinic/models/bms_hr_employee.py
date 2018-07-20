# -*- coding: utf-8 -*-

from odoo import fields, models

class BMSEmployee(models.Model):
    _inherit = 'hr.employee'

    barcode = fields.Char(string='ID nhân viên')
    wage = fields.Float(string='Lương cơ bản')
    a = fields.Date(string='Ngày bắt đầu làm việc')
