# Copyright (c) 2018 SMHI, Swedish Meteorological and Hydrological Institute
# License: MIT License (see LICENSE.txt or http://opensource.org/licenses/mit).

from . import gui
from .app import App


INFO = dict(title='Tavastland',
            users_directory='users',
            description='Plugin to handle CO2 merge of Tavastland data.',
            sub_pages=[dict(name='PageTavastland',
                            title='Start')],
            user_page_class='PageUser')  # Must match name in ALL_PAGES in main app

USER_SETTINGS = [('basic', 'tavastland'),
                 ('basic', 'layout')]