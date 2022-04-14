# -*- coding: utf-8 -*-
# Copyright 2017 Camptocamp SA
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html)

from odoo.addons.component.core import WorkContext, ComponentRegistry
from .common import TransactionComponentCase


class TestWorkOn(TransactionComponentCase):
    """ Test on WorkContext

    This model is mostly a container, so we check the access
    to the attributes and properties.

    """

    def setUp(self):
        super(TestWorkOn, self).setUp()
        self.collection = self.env['collection.base']

    def test_collection_work_on(self):
        """ Create a new instance and test attributes access """
        collection_record = self.collection.new()
        with collection_record.work_on('res.partner') as work:
            self.assertEquals(collection_record, work.collection)
            self.assertEquals('collection.base', work.collection._name)
            self.assertEquals('res.partner', work.model_name)
            self.assertEquals(self.env['res.partner'], work.model)
            self.assertEquals(self.env, work.env)

    def test_propagate_work_on(self):
        """ Check custom attributes and their propagation """
        registry = ComponentRegistry()
        work = WorkContext(
            model_name='res.partner',
            collection=self.collection,
            # we can customize the lookup registry, but used mostly for tests
            components_registry=registry,
            # we can pass our own keyword args that will set as attributes
            test_keyword='value',
        )
        self.assertIs(registry, work.components_registry)
        # check that our custom keyword is set as attribute
        self.assertEquals('value', work.test_keyword)

        # when we want to work on another model, work_on() create
        # another instance and propagate the attributes to it
        work2 = work.work_on('res.users')
        self.assertNotEquals(work, work2)
        self.assertEquals(self.env, work2.env)
        self.assertEquals(self.collection, work2.collection)
        self.assertEquals('res.users', work2.model_name)
        self.assertIs(registry, work2.components_registry)
        # test_keyword has been propagated to the new WorkContext instance
        self.assertEquals('value', work2.test_keyword)
