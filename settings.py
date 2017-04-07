#!/usr/bin/env python
"""
Aircraft Communications Addressing and Reporting System API for Flight Simulation
Copyright (C) 2017  Pedro Rodrigues <prodrigues1990@gmail.com>

This file is part of ACARS API.

ACARS API is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 2 of the License.

ACARS API is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with ACARS API.  If not, see <http://www.gnu.org/licenses/>.
"""

import os

transponders_schema = {
	'callsign': {
		'type': 'string'
	}
}
transponders = {
	'schema': transponders_schema,
	'resource_methods': ['GET', 'POST']
}

position_reports_schema = {
	'timestamp': {
		'type': 'datetime',
		'required': True
	},
	'location': {
		'type': 'point',
		'required': True
	},
	'altitude': {
		'type': 'number',
		'required': True
	},
	'transponder': {
		'type': 'ObjectId',
		'required': True
	},
	'flight': {
		'type': 'ObjectId'
	}
}
position_reports = {
	'schema': position_reports_schema,
	'resource_methods': ['POST']
}

flights_schema = {
	'origin': {
		'type': 'string',
		'minlength': 4,
		'maxlength': 4,
		'required': True
	},
	'destination': {
		'type': 'string',
		'minlength': 4,
		'maxlength': 4,
		'required': True
	},
	'alternate': {
		'type': 'string',
		'minlength': 4,
		'maxlength': 4,
		'required': True
	},
	'route': {
		'type': 'string',
		'required': True
	},
	'cruise_altitude': {
		'type': 'number',
		'required': True
	}
}
flights = {
	'schema': flights_schema,
	'resource_methods': ['POST', 'GET']
}

# live_flights = {
# 	'datasource': {
# 		'source': 'position_reports',
# 		'filter': { '' }
# 	}
# }

DOMAIN = {
	'transponders': transponders,
	'position_reports': position_reports,
	'flights': flights
}

# We want to seamlessy run our API both locally and on Heroku. If running on
# Heroku, sensible DB connection settings are stored in environment variables.
MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
MONGO_PORT = os.environ.get('MONGO_PORT', 27017)
MONGO_USERNAME = os.environ.get('MONGO_USERNAME', '')
MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD', '')
MONGO_DBNAME = os.environ.get('MONGO_DBNAME', 'acars-api')

#X_DOMAINS = '*'