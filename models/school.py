# -*- coding: utf-8 -*-
from odoo import models, fields

class School(models.Model):
    _name = 'school.school'
    _description = 'School'

    name = fields.Char(string='School Name', required=True)
