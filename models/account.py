# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

from datetime import date
from datetime import datetime
from datetime import datetime, timedelta
from odoo.exceptions import UserError, ValidationError
import calendar
import re
import json
from dateutil.relativedelta import relativedelta
import pgeocode
import qrcode
from PIL import Image
from random import choice
from string import digits

import math
import re
from odoo import api, models


class EstimateOrders(models.Model):
    _inherit = 'estimate.orders'
    _order = 'id desc'


    inv_status = fields.Selection([
        ('draft', 'Draft'),
        ('posted', 'Posted'),
        ('paid', 'paid'),
        ('cancel', 'Cancel'),
    ], default='draft')


    def _compute_total_amount(self):
        for rec in self:
            rec.total_amount = 0.0
            for line in rec.order_lines:
                rec.total_amount += line.price* line.quantity
