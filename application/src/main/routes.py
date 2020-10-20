#!/usr/bin/env python
from main.app import api
from main.controller.healthcheck import Healthcheck
from main.controller.search import Search

api.add_resource(Healthcheck, '/')
api.add_resource(Search, '/search')