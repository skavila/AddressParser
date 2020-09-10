from service.address_parser import parse
import json

print('>>> testing...')
result = parse('3620 Vermont Ave, RM444, Los Angeles, CA 90089')

print(json.dumps(result.__dict__))