# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import fields,models

class resPartner(models.Model):
    _inherit = 'res.partner'

    first_name = fields.Char('First Name')
    middle_name = fields.Char('Middle Name')
    surname = fields.Char('Surname')
    last_surname = fields.Char('Last surname')
    age = fields.Integer('Partner Age')
    type_id = fields.Selection([
					('CC','CEDULA DE CIUDADANIA'),
					('NI','NIT'),
					('RC','REGISTRO CIVIL'),
					('PA','PASAPORTE')
    			],string='Type ID',default='CC')
    arl = fields.Many2one('res.partner',string='ARL Company', 
                            domain=[('is_arl','=',True)])
    is_arl = fields.Boolean('Is ARL Company?', default=False)