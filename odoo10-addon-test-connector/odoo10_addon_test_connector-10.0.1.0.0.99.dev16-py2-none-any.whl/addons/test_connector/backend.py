# -*- coding: utf-8 -*-
# Copyright 2017 Camptocamp SA
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html)

from odoo.addons.connector.backend import Backend

test_backend = Backend('test_connector')

test_backend_1 = Backend(parent=test_backend, version='1')
