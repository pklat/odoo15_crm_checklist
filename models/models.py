# -*- coding: utf-8 -*-

from odoo import models, fields, api


class crm_checklist(models.Model):
    _inherit = 'crm.lead'

    checkboxes_ids = fields.One2many("crm_checklist.checkboxes","checkbox_id",string="Checkboxes IDs",ondelete='cascade')
    checkboxes = fields.One2many("crm_checklist.checkboxes","checkbox",string="Checkboxes")
    checkboxes_count = fields.Integer(string="Checkboxes Count", default=0, compute="_compute_checkbox_count",stored=True)
    checkbox_done_count = fields.Integer(string="Checkboxes done")
    progress_rate = fields.Float(string="Progress", compute="_compute_progress", default=0, stored=True)

    #@api.depends('checkboxes_ids')
    @api.onchange('checkboxes')
    def _compute_checkbox_count(self):
        for rec in self:
            checkboxes_count = self.env['crm_checklist.checkboxes'].search([('checkbox_id','=',rec.id)])
            rec.checkboxes_count = len(checkboxes_count)
    
    #@api.depends('checkboxes_ids')
    @api.onchange('checkboxes_ids')
    def _compute_progress(self):
        for rec in self:
            #print(rec.progress_rate)
            checkboxes_count = self.env['crm_checklist.checkboxes'].search([('checkbox_id','=',rec.id)])
            count_progress = 0
            if len(checkboxes_count) >0:
                for recc in checkboxes_count:
                    print(recc)
                    if recc.checkbox == True:
                        count_progress+=1
                print("Count Progress:",count_progress)
                rec.checkbox_done_count = count_progress
                print("Compute Progress:",100/len(checkboxes_count)*count_progress)
                rec.progress_rate = 100/len(checkboxes_count)*count_progress
    
    
class crm_checkbox(models.Model):
    _name = 'crm_checklist.checkboxes'
    _description = 'Checklist Checkboxes'

    checkbox_id = fields.Many2one('crm.lead', string="Checkbox")
    name = fields.Char()
    checkbox = fields.Boolean(string="Checkbox", store=True, readonly=False, default=False, compute="_checkbox_on_change")
    description = fields.Text()
    
    @api.onchange('checkbox')
    def _checkbox_on_change(self):
        for rec in self:
            print(rec)
            print(rec.id, rec.checkbox)
            print("Onchange")
            return 
    



    #def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):


    # active = fields.Boolean(string='Active', default=True)

    
    # def toggle_active(self):
    #     print("save")
    #     self.active = not self.active

    #@api.onchange('checkbox')

    # @api.multi
    # def your_button(self):
    #     self.your_boolean_field = True