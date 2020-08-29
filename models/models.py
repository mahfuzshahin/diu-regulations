# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class daffodil_diu_regulations(models.Model):
#     _name = 'daffodil_diu_regulations.daffodil_diu_regulations'
#     _description = 'daffodil_diu_regulations.daffodil_diu_regulations'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
