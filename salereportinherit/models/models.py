from odoo import models, fields, api

class SaleReportHerit(models.Model):
    _inherit = 'sale.report'
    sale_marge_report  = fields.Float(string="Marge commerciale", readonly=True)


    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        fields['sale_marge_report'] = ", SUM(s.x_studio_marge_commerciale) AS sale_marge_report"
        return super(SaleReportHerit, self)._query(with_clause, fields, groupby, from_clause)



