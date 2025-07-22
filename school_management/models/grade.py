from odoo import models, fields

class Grade(models.Model):
    _name = 'student.grade'
    _description = 'Student Grade'

    student_id = fields.Many2one('student.student', string='Học sinh', required=True)
    subject = fields.Char(string='Môn học', required=True)
    score = fields.Float(string='Điểm số')
    note = fields.Text(string='Ghi chú')
