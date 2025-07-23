# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SchoolExamResult(models.Model):
    _name = 'school.exam_result'
    _description = 'Exam Result'

    student_id = fields.Many2one('student.student', string='Học sinh')
    subject_id = fields.Many2one('school.subject', string='Môn học')
    exam_type = fields.Selection([
        ('oral', 'Miệng'),
        ('15min', '15 phút'),
        ('midterm', 'Giữa kỳ'),
        ('final', 'Cuối kỳ')
    ], string='Loại kiểm tra')
    score = fields.Float(string='Điểm')
    semester = fields.Char(string='Học kỳ')
    year = fields.Char(string='Năm học')

    @api.model
    def create(self, vals):
        res = super().create(vals)
        res.student_id._compute_average_score()
        return res

    def write(self, vals):
        res = super().write(vals)
        self.mapped('student_id')._compute_average_score()
        return res