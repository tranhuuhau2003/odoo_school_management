# -*- coding: utf-8 -*-
from odoo import models, fields

class SchoolClass(models.Model):
    _name = 'school.class'
    _description = 'Classroom'

    name = fields.Char(string='Tên lớp', required=True)
    school_year = fields.Char(string='Năm học')
    homeroom_teacher = fields.Many2one('res.users', string='Giáo viên chủ nhiệm')
    student_ids = fields.One2many('student.student', 'class_id', string='Học sinh')
