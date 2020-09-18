from src.model.address import Address
import usaddress
import src.controller.app_logging

logger = src.controller.app_logging.logger('src.service.address_parser')


def parse(address_str):
    try:
        if address_str:
            logger.debug('>>> paring address...')
            us_address = usaddress.tag(address_str)[0]
            # country = us_address['Country']
            building_number = us_address['AddressNumber']
            street_type = us_address['StreetNamePostType']
            street_name = us_address['StreetName']
            city = us_address['PlaceName']
            state = us_address['StateName']
            postal_code = us_address['ZipCode']

            address = Address(building_number, street_name, street_type, city, state, postal_code, 'USA')

            return address
        else:
            logger.error('Invalid Input Address...')
            raise Exception('Invalid Input Address')
    except:
        logger.error('>>> error parsing...')
