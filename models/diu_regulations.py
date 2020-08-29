from odoo import models, fields, tools
from odoo.exceptions import ValidationError, except_orm, UserError
import calendar
import math
import re


class RegulationCategory(models.Model):
    _name = 'regulation.category'
    _description = 'Regulation Category'

    name = fields.Char('Category Name', required=True)


class DIURegulations(models.Model):
    _name = 'diu.regulations'
    _description = 'DIU Regulations'

    category_ids = fields.Many2one('regulation.category', string='Category Name', required=True)
    name = fields.Char('Title', required=True)
    effective_date = fields.Date('Effective Date', required=True)
    description = fields.Html(string='Description', sanitize=True, strip_style=False)
    attachment_ids = fields.Many2many('ir.attachment', string='Attachments')
    url = fields.Char('URL')