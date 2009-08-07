# This file is part of Moksha
# Copyright (C) 2008-2009  Red Hat, Inc.
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
:mod:`fedoracommunity.widgets.expander` -- An Expander Widget
=============================================================

http://plugins.learningjquery.com/expander
"""

from tw.api import JSLink
from tw.jquery import jquery_js

expander_js = JSLink(filename='static/jquery.expander.js',
                     modname=__name__, javascript=[jquery_js])