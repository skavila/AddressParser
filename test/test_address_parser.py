import json
import os
import pkg_resources

from src.service.address_parser import parse

path = '/Users/saratkavila/Work/Projects/AddressParser/src/resources/logging.yaml'

fn = os.path.abspath(__file__ + "/../../" )
sn = os.path.join(fn, 'src/resources/logging.yaml')
print('...'+sn)

if os.path.exists(sn):
    print('Hurray !!')
else:
    print('naah !!')

print('>>> testing...')
result = parse('3620 Vermont Ave, RM444, Los Angeles, CA 90089')

print(json.dumps(result.__dict__))