# -*- coding: utf-8 -*-
from odoo import models, fields

class Parent(models.Model):
    _name = 'student.parent'
    _description = 'Parent'

    name = fields.Char(string='Họ tên', required=True)
    phone = fields.Char(string='Số điện thoại')
    email = fields.Char(string='Email')
    job = fields.Char(string='Nghề nghiệp')
    address = fields.Char(string='Địa chỉ liên hệ')
    child_ids = fields.One2many('student.student', 'parent_id', string='Học sinh')  # Tham chiếu lại đúng tên field
