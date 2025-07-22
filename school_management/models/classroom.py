from odoo import models, fields

class Classroom(models.Model):
    _name = 'student.classroom'
    _description = 'Classroom'

    name = fields.Char(string='Tên lớp', required=True)
    teacher_id = fields.Many2one('hr.employee', string='Giáo viên chủ nhiệm')
    student_ids = fields.One2many('student.student', 'classroom_id', string='Danh sách học sinh')
