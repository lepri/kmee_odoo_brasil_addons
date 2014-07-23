# -*- encoding: utf-8 -*-
##############################################################################
#
#    KMEE XML to ZIP module for OpenERP
#    Copyright (C) 2014 KMEE (http://www.kmee.com.br)
#    @author Matheus Lima Felix <matheus.felix@kmee.com.br>
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
{
    'name': 'KMEE XML to Zip Month',
    'version': '0.1',
    'category': 'Generic Modules',
    'description': """KMEE XML to Zip Month""",
    'author': 'KMEE',
    'license': 'AGPL-3',
    'website': 'http://www.kmee.com.br',
    'depends': [
                'account',
    ],
    'data': ['wizard/validate_xml_to_zip_invoice.xml',
             'wizard/validate_xml_to_zip.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'active': False,
}
