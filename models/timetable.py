# -*- coding: utf-8 -*-
from odoo import models, fields

class SchoolTimetable(models.Model):
    _name = 'school.timetable'
    _description = 'Timetable'

    class_id = fields.Many2one('school.class', string='Lớp')
    subject_id = fields.Many2one('school.subject', string='Môn học')
    teacher_id = fields.Many2one('res.users', string='Giáo viên')
    weekday = fields.Selection([
        ('mon', 'Thứ 2'),
        ('tue', 'Thứ 3'),
        ('wed', 'Thứ 4'),
        ('thu', 'Thứ 5'),
        ('fri', 'Thứ 6'),
        ('sat', 'Thứ 7'),
        ('sun', 'Chủ nhật')
    ], string='Thứ')
    time_start = fields.Float(string='Giờ bắt đầu')
    time_end = fields.Float(string='Giờ kết thúc')
