# -*- coding: utf-8 -*-
from odoo import models, fields

class SchoolAttendance(models.Model):
    _name = 'school.attendance'
    _description = 'Attendance'

    student_id = fields.Many2one('student.student', string='Học sinh')
    class_id = fields.Many2one('school.class', string='Lớp')
    date = fields.Date(string='Ngày')
    status = fields.Selection([
        ('present', 'Có mặt'),
        ('absent', 'Vắng'),
        ('leave', 'Có phép'),
        ('late', 'Muộn')
    ], string='Trạng thái')
    note = fields.Char(string='Ghi chú')
