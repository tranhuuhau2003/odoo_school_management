from odoo import models, fields

class Student(models.Model):
    _name = 'student.student'
    _description = 'Student'

    name = fields.Char(string='Họ và tên', required=True)
    birthday = fields.Date(string='Ngày sinh')
    gender = fields.Selection([
        ('male', 'Nam'),
        ('female', 'Nữ'),
        ('other', 'Khác')
    ], string='Giới tính')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Số điện thoại')
    classroom_id = fields.Many2one('student.classroom', string='Lớp học')
