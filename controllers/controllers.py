# -*- coding: utf-8 -*-
# from odoo import http


# class ReportBanqueAtlantique(http.Controller):
#     @http.route('/report_banque_atlantique/report_banque_atlantique/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/report_banque_atlantique/report_banque_atlantique/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('report_banque_atlantique.listing', {
#             'root': '/report_banque_atlantique/report_banque_atlantique',
#             'objects': http.request.env['report_banque_atlantique.report_banque_atlantique'].search([]),
#         })

#     @http.route('/report_banque_atlantique/report_banque_atlantique/objects/<model("report_banque_atlantique.report_banque_atlantique"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('report_banque_atlantique.object', {
#             'object': obj
#         })
