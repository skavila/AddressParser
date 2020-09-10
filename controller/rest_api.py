from flask import Flask, jsonify, request
from service.address_parser import parse
import json
import controller.app_logging

# create a flask app
app = Flask(__name__)

logger = controller.app_logging.logger('controller.rest_api')


@app.route('/ping', methods=['GET', 'POST'])
def ping():
    logger.debug('ping success....')
    response = 'SUCCESS'
    return jsonify(response)


@app.route('/address_parser', methods=['GET', 'POST'])
def address_parser():
    addr_str = request.args.get('address')
    logger.debug('In address_parser....' + addr_str)
    p_address = parse(addr_str)
    response = {'input_address': addr_str, 'parsed_address': json.dumps(p_address.__dict__)}
    logger.debug(response)
    return jsonify(response)


# driver function
if __name__ == '__main__':
    app.run(debug=True)
