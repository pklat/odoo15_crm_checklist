# -*- coding: utf-8 -*-

from odoo import models, fields, api
class crm_checkbox(models.Model):
    _name = 'crm_checklist.checkboxes'
    _description = 'Checklist Checkboxes'

    checkbox_id = fields.Many2one('crm.lead', string="Checkboxes", ondelete="cascade")
    checkbox = fields.Boolean(string="Checkbox", store=True, readonly=False, default=False, compute="_checkbox_on_change")
    name = fields.Char()
    description = fields.Text()

    #def save(self):
    #    print("Save")

    # @api.onchange('checkbox')
    # def _checkbox_on_change(self):
    #     for rec in self:
    #         print(rec.checkbox)
    #     print("Onchange")
    #     #self.write()