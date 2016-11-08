# -*- coding: utf-8 -*-
# Copyright (C) 2014-Today GRAP (http://www.grap.coop)
# Copyright (C) 2016-Today La Louve (http://www.lalouve.net)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Generate Barcodes (Abstract)',
    'summary': 'Generate Barcodes for Any Models',
    'version': '9.0.1.0.0',
    'category': 'Point Of Sale',
    'author':
        'GRAP,'
        'La Louve,'
        'Odoo Community Association (OCA)',
    'website': 'http://www.odoo-community.org',
    'license': 'AGPL-3',
    'depends': [
        'barcodes',
    ],
    'data': [
        'security/res_groups.xml',
        'views/view_barcode_rule.xml',
        'views/menu.xml',
    ],
    'demo': [
        'demo/res_users.xml',
    ],
}
