# -*- coding: utf-8 -*-
from odoo import http

# class OdooMautic(http.Controller):
#     @http.route('/odoo_mautic/odoo_mautic/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_mautic/odoo_mautic/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_mautic.listing', {
#             'root': '/odoo_mautic/odoo_mautic',
#             'objects': http.request.env['odoo_mautic.odoo_mautic'].search([]),
#         })

#     @http.route('/odoo_mautic/odoo_mautic/objects/<model("odoo_mautic.odoo_mautic"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_mautic.object', {
#             'object': obj
#         })