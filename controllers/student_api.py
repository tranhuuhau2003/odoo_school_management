# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json


class StudentRestAPI(http.Controller):
    """
    RESTful API cho student.student
    Xác thực bằng Basic Auth (Odoo 16 API Key)
    """

    def _serialize(self, s):
        return {
            'id': s.id,
            'name': s.name,
            'email': s.email,
            'phone': s.phone,
            'gender': s.gender,
            'dob': str(s.dob) if s.dob else None,
            'student_code': s.student_code,
            'admission_date': str(s.admission_date) if s.admission_date else None,
            'status': s.status,
            'average_score': s.average_score,
        }

    # GET all
    @http.route('/api/students', type='http', auth='user', methods=['GET'], csrf=False)
    def get_students(self, **kwargs):
        students = request.env['student.student'].search([])
        data = [self._serialize(s) for s in students]
        return request.make_response(json.dumps(data),
                                     headers=[('Content-Type', 'application/json')])

    # GET by ID
    @http.route('/api/students/<int:student_id>', type='http', auth='user', methods=['GET'], csrf=False)
    def get_student(self, student_id, **kwargs):
        student = request.env['student.student'].browse(student_id)
        if not student.exists():
            return request.make_response(json.dumps({"error": "Not found"}), status=404,
                                         headers=[("Content-Type", "application/json")])
        return request.make_response(json.dumps(self._serialize(student)),
                                     headers=[("Content-Type", "application/json")])

    # POST (create)
    @http.route('/api/students', type='http', auth='user', methods=['POST'], csrf=False)
    def create_student(self, **kwargs):
        data = request.httprequest.get_json(force=True)
        student = request.env['student.student'].create(data)
        return request.make_response(json.dumps({"id": student.id, "message": "created"}), status=201,
                                     headers=[("Content-Type", "application/json")])

    # PUT (update)
    @http.route('/api/students/<int:student_id>', type='http', auth='user', methods=['PUT'], csrf=False)
    def update_student(self, student_id, **kwargs):
        student = request.env['student.student'].browse(student_id)
        if not student.exists():
            return request.make_response(json.dumps({"error": "Not found"}), status=404,
                                         headers=[("Content-Type", "application/json")])
        data = request.httprequest.get_json(force=True)
        student.write(data)
        return request.make_response(json.dumps({"message": "updated"}),
                                     headers=[("Content-Type", "application/json")])

    # DELETE
    @http.route('/api/students/<int:student_id>', type='http', auth='user', methods=['DELETE'], csrf=False)
    def delete_student(self, student_id, **kwargs):
        student = request.env['student.student'].browse(student_id)
        if not student.exists():
            return request.make_response(json.dumps({"error": "Not found"}), status=404,
                                         headers=[("Content-Type", "application/json")])
        student.unlink()
        return request.make_response(json.dumps({"message": "deleted"}),
                                     headers=[("Content-Type", "application/json")])
