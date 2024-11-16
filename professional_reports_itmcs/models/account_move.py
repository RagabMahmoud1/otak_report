from odoo import api, fields, models, tools

class AccountMoveInherit(models.Model):
    _inherit = 'account.invoice'

    payments_ids = fields.One2many('account.payment', 'invoice_ids', string='Payments', copy=False, store=False, compute='_compute_payments_ids')

    def _compute_payments_ids(self):
        for rec in self:
            rec.payments_ids = self.env['account.payment'].search([('communication', '=', rec.number)])