# -*- coding: utf-8 -*-
# from odoo import http


# class CrmProgress(http.Controller):
#     @http.route('/crm_progress/crm_progress', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/crm_progress/crm_progress/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('crm_progress.listing', {
#             'root': '/crm_progress/crm_progress',
#             'objects': http.request.env['crm_progress.crm_progress'].search([]),
#         })

#     @http.route('/crm_progress/crm_progress/objects/<model("crm_progress.crm_progress"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('crm_progress.object', {
#             'object': obj
#         })
