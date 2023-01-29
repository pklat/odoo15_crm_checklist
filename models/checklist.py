# -*- coding: utf-8 -*-

from odoo import models, fields, api


class crm_checklist(models.Model):
    _inherit = 'crm.lead'

    checkboxes_ids = fields.One2many("crm_checklist.checkboxes","checkbox_id",string="Checkboxes IDs")
    checkboxes = fields.One2many("crm_checklist.checkboxes","checkbox",string="Checkboxes")
    
    checkboxes_count = fields.Integer(string="Checkboxes Count", default=0, compute="_compute_checkbox_count")
    checkbox_done_count = fields.Integer(string="Checkboxes done", default=0)
    progress_rate = fields.Float(string="Progress", compute='_compute_progress', default=0,stored=True) #, stored=True
            
    @api.onchange('checkboxes_ids')
    def _compute_progress(self):
        for rec in self:
            #print(rec.name)
            #rec.progress_rate=0
            checkboxes_count = self.env['crm_checklist.checkboxes'].search([('checkbox_id','=',rec.id)])
            if len(checkboxes_count) > 0:            
                #print("Select checkboxes:",checkboxes_count, len(checkboxes_count))
                rec.checkboxes_count = len(checkboxes_count)
                count_progress = 0                
                for recc in checkboxes_count:
                    if recc.checkbox == True:
                        count_progress+=1
                if count_progress > 0:
                    self.checkbox_done_count = count_progress
                    try:
                        rec.progress_rate = 100/len(checkboxes_count)*count_progress
                        return 100/len(checkboxes_count)*count_progress
                    except Exception as a:
                        print(a)
            else:
                rec.progress_rate=0
    def save(self):
        print("Call SAVE!")
