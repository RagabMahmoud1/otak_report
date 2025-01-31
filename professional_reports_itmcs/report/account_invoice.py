# -*- coding: utf-8 -*-
# Odoo, Open Source Personalized All in One Reports.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).#
                                          
from odoo import api, models




#  account invoice reports 

class ReportAccountReport(models.AbstractModel):
    _name = 'report.account.report_invoice'
 
    @api.multi
    def get_report_values(self, docids, data=None):
        sale_obj = self.env['account.invoice'].browse(docids[0])
        self.model = self.env.context.get('active_model')
        user = self.env["res.users"].browse(self._uid)
        company_data = user.company_id
        data = {'sale_header_footer':user.company_id.sale_header_footer ,
                'primary_color': company_data.primary_color ,
                'secondary_color':  company_data.secondary_color,
                'sale_font_color': company_data.sale_font_color}
        docargs = {
            'doc_ids': self.ids,
            'doc_model': self.model,
            'docs': sale_obj,
            'data': data,
            'doc' :user,
        }
        
        return docargs





class ReportAccountDupReport(models.AbstractModel):
    _name = 'report.account.report_invoice_with_payments'
 
    @api.multi
    def get_report_values(self, docids, data=None):
        sale_obj = self.env['account.invoice'].browse(docids[0])
        self.model = self.env.context.get('active_model')
        user = self.env["res.users"].browse(self._uid)
        company_data = user.company_id
        data = {'sale_header_footer':user.company_id.sale_header_footer ,
                'primary_color': company_data.primary_color ,
                'secondary_color':  company_data.secondary_color,
                'sale_font_color': company_data.sale_font_color}
        docargs = {
            'doc_ids': self.ids,
            'doc_model': self.model,
            'docs': sale_obj,
            'data': data,
            'doc' :user,
        }
        
        return docargs



