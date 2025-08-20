# -*- coding: utf-8 -*-
from odoo import models, fields
from odoo import api            


class Student(models.Model):
    _name = 'student.student'
    _description = 'Student'

    name = fields.Char(string='Họ tên', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Số điện thoại')
    gender = fields.Selection([
        ('male', 'Nam'),
        ('female', 'Nữ'),
        ('other', 'Khác')
    ], string='Giới tính')
    dob = fields.Date(string='Ngày sinh')
    image = fields.Binary(string='Ảnh đại diện')
    student_code = fields.Char(string='Mã học sinh')
    admission_date = fields.Date(string='Ngày nhập học')
    status = fields.Selection([
        ('studying', 'Đang học'),
        ('graduated', 'Đã tốt nghiệp'),
        ('reserve', 'Bảo lưu')
    ], string='Tình trạng', default='studying')
    parent_id = fields.Many2one('student.parent', string='Phụ huynh')  
    class_id = fields.Many2one('school.class', string='Lớp')
    
        # Danh sách kết quả kiểm tra
    exam_result_ids = fields.One2many('school.exam_result', 'student_id', string='Kết quả kiểm tra')

    # Điểm trung bình được tính tự động
    average_score = fields.Float(string='Điểm trung bình', compute='_compute_average_score', store=True)

    @api.depends('exam_result_ids.score')
    def _compute_average_score(self):
        for student in self:
            scores = student.exam_result_ids.mapped('score')
            student.average_score = sum(scores) / len(scores) if scores else 0.0
    @api.model
    def create(self, vals):
        if not vals.get('student_code'):
            vals['student_code'] = self.env['ir.sequence'].next_by_code('student.student.code') or '/'
        return super().create(vals)