# Copyright 2015 ACSONE SA/NV
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    'name': "POS Analytic Config",
    'summary': """Use analytic account defined on
                  POS configuration for POS orders""",
    'author': 'ACSONE SA/NV,'
              'Odoo Community Association (OCA)',
    'website': "https://github.com/OCA/account-analytic",
    'category': 'Point Of Sale, Accounting',
    'version': '11.0.1.0.0',
    'license': 'AGPL-3',
    'depends': [
        'point_of_sale',
    ],
    'data': [
        'views/pos_config_view.xml',
    ],
}
