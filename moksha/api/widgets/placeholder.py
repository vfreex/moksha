# This file is part of Moksha.
# Copyright (C) 2008-2010  Red Hat, Inc.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from tg import config
from paste.deploy.converters import asbool

from tw.api import Widget

class TW1Placeholder(Widget):
    engine_name = 'mako'
    hidden = True
    template = """
<p class='placeholder'>
    Moksha application <strong>${appname}</strong> is not registered yet.  This is a placeholder
    for testing purposes.  When the app is registered it will appear in the
    layout once the server is restarted.
</p>
"""

if asbool(config.get('moksha.use_tw2', False)):
    raise NotImplementedError(__name__ + " not ready for tw2.")
else:
    Placeholder = TW1Placeholder
