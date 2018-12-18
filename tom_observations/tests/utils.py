from django.core.files.uploadedfile import SimpleUploadedFile

from tom_observations.facility import GenericObservationFacility
from tom_dataproducts.models import DataProduct

# Site data matches built-in pyephem observer data for Los Angeles
SITES = {
    'Los Angeles': {
        'latitude': 34.052222,
        'longitude': -117.756306,
        'elevation': 86.847092
    }
}


class FakeFacility(GenericObservationFacility):
    name = 'FakeFacility'

    @classmethod
    def get_observing_sites(clz):
        return SITES

    @classmethod
    def get_observation_url(clzz, observation_id):
        return ''

    @classmethod
    def data_products(clz, observation_record):
        return [{'id': 'testdpid'}]

    @classmethod
    def save_data_products(clz, observation_record, product_id=None):
        return([DataProduct(product_id=product_id, data=SimpleUploadedFile('afile.fits', b'afile'))])

    @classmethod
    def get_observation_status(clz, observation_id):
        return 'COMPLETED'

    @classmethod
    def get_terminal_observing_states(clz):
        return ['COMPLETED', 'FAILED']
