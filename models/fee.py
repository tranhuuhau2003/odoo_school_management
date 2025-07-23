# -*- coding: utf-8 -*-
from odoo import models, fields

class SchoolFee(models.Model):
    _name = 'school.fee'
    _description = 'School Fee'

    student_id = fields.Many2one('student.student', string='Học sinh')
    class_id = fields.Many2one('school.class', string='Lớp')
    amount = fields.Float(string='Số tiền')
    due_date = fields.Date(string='Hạn nộp')
    state = fields.Selection([
        ('draft', 'Nháp'),
        ('open', 'Chưa thu'),
        ('paid', 'Đã thu')
    ], string='Trạng thái', default='draft')
    invoice_id = fields.Many2one('account.move', string='Hóa đơn')
