# -*- coding: utf-8 -*-
# from odoo import http


# class Educacion-2(http.Controller):
#     @http.route('/educacion-2/educacion-2', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/educacion-2/educacion-2/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('educacion-2.listing', {
#             'root': '/educacion-2/educacion-2',
#             'objects': http.request.env['educacion-2.educacion-2'].search([]),
#         })

#     @http.route('/educacion-2/educacion-2/objects/<model("educacion-2.educacion-2"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('educacion-2.object', {
#             'object': obj
#         })

