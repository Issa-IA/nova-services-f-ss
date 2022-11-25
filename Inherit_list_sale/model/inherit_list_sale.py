from odoo import models, fields, api


class StockHerit(models.Model):
    _inherit = 'sale.order'

    etiquette_maintenance = fields.Selection([('maintenance', 'Maintenance'), ('autres', 'Autres'),('cvi','CVI')], compute='_maintenance_etiquette', store=True)


    @api.depends('sale_maintnance','sale_dossier')
    def _maintenance_etiquette(self):
        for rec in self:
            if rec.sale_maintnance :
                rec.etiquette_maintenance = 'maintenance'
            elif rec.sale_dossier:
                rec.etiquette_maintenance = 'cvi'
            else:
                rec.etiquette_maintenance = False

