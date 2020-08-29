# -*- coding: utf-8 -*-
# from odoo import http


# class DaffodilDiuRegulations(http.Controller):
#     @http.route('/daffodil_diu_regulations/daffodil_diu_regulations/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/daffodil_diu_regulations/daffodil_diu_regulations/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('daffodil_diu_regulations.listing', {
#             'root': '/daffodil_diu_regulations/daffodil_diu_regulations',
#             'objects': http.request.env['daffodil_diu_regulations.daffodil_diu_regulations'].search([]),
#         })

#     @http.route('/daffodil_diu_regulations/daffodil_diu_regulations/objects/<model("daffodil_diu_regulations.daffodil_diu_regulations"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('daffodil_diu_regulations.object', {
#             'object': obj
#         })
