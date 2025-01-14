# -*- coding: utf-8 -*-
# Odoo, Open Source  Personalized All in One Reports.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).#

{
    'name': 'Personalized All in One Reports',
    'category': 'Reports',
    'author': 'Odoowikia',
    'description': """

""",
    'depends': [ 'base', 'web', 'sale', 'sale_management', 'product', 'account', 'purchase', 'stock'],
    'summary': ' To Generate Professional Reports ',

    'data': [ 'views/res_company_view.xml',
             'views/professional_widget_color_view.xml',
             'report/sale_fency_template.xml',
             'report/purchase_fency_template.xml',
             'report/purchase_quotation_fency_template.xml',
             'report/account_invoice_fency_template.xml',
             'report/stock_fency_template.xml',
             'report/stock_delivery_fency_template.xml',
             'report/sale_classic_template.xml',
             'report/purchase_classic_template.xml',
             'report/purchase_quotation_classic_template.xml',
             'report/account_invoice_classic_template.xml',
             'report/stock_classic_template.xml',
             'report/stock_delivery_classic_template.xml',
             'report/sale_vintage_template.xml',
             'report/purchase_vintage_template.xml',
             'report/purchase_quotation_vintage_template.xml',
             'report/account_invoice_vintage_template.xml',
             'report/stock_vintage_template.xml',
             'report/stock_delivery_vintage_template.xml',
             'report/sale_retro_template.xml',
             'report/purchase_retro_template.xml',
             'report/purchase_quotation_retro_template.xml',
             'report/account_invoice_retro_template.xml',
             'report/stock_retro_template.xml',
             'report/stock_delivery_retro_template.xml',
             'report/sale_modern_template.xml',
             'report/purchase_modern_template.xml',
             'report/purchase_quotation_modern_template.xml',
             'report/account_invoice_modern_template.xml',
             'report/stock_modern_template.xml',
             'report/stock_delivery_modern_template.xml',
             'report/sale_canva_template.xml',
             'report/purchase_canva_template.xml',
             'report/purchase_quotation_canva_template.xml',
             'report/account_invoice_canva_template.xml',
             'report/stock_canva_template.xml',
             'report/stock_delivery_canva_template.xml',
             'report/sale_elegant_template.xml',
             'report/purchase_elegant_template.xml',
             'report/purchase_quotation_elegant_template.xml',
             'report/account_invoice_elegant_template.xml',
             'report/stock_elegant_template.xml',
             'report/stock_delivery_elegant_template.xml',
             'report/sale_professional_template.xml',
             'report/purchase_professional_template.xml',
             'report/purchase_quotation_professional_template.xml',
             'report/account_invoice_professional_template.xml',
             'report/stock_professional_template.xml',
             'report/stock_delivery_professional_template.xml',
             'report/sale_western_template.xml',
             'report/purchase_western_template.xml',
             'report/purchase_quotation_western_template.xml',
             'report/account_invoice_western_template.xml',
             'report/stock_western_template.xml',
             'report/stock_delivery_western_template.xml',
             'report/sale_shine_template.xml',
             'report/purchase_shine_template.xml',
             'report/purchase_quotation_shine_template.xml',
             'report/account_invoice_shine_template.xml',
             'report/stock_shine_template.xml',
             'report/stock_delivery_shine_template.xml',
                         
                         ],
     'qweb': [
        'static/src/xml/widget.xml',
    ],
    'images':['static/description/Banner.png'],
    'installable': True,

}
