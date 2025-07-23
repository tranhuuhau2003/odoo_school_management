# -*- coding: utf-8 -*-
from odoo import models, fields

class SchoolSubject(models.Model):
    _name = 'school.subject'
    _description = 'Subject'

    name = fields.Char(string='Tên môn học', required=True)
    description = fields.Text(string='Mô tả')
    code = fields.Char(string='Mã môn học')
