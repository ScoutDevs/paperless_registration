"""SponsoringOrganization classes"""
from . import Base
from . import Organization
from . import RecordNotFoundException


class SponsoringOrganization(Base.Object):
    """SponsoringOrganization class"""

    def __init__(self):
        super(self.__class__, self).__init__()
        self.type = Organization.ORG_TYPE_SPONSORING_ORGANIZATION
        self.parent_uuid = ''
        self.name = ''
        self.number = ''

    def get_validator(self):
        return Validator(self)

    @staticmethod
    def get_factory():
        return Factory()


class Validator(Base.Validator):
    """SponsoringOrganization validator"""

    def get_field_requirements(self):
        return {
            'uuid': Base.FIELD_REQUIRED,
            'type': Base.FIELD_REQUIRED,
            'parent_uuid': Base.FIELD_REQUIRED,
            'name': Base.FIELD_REQUIRED,
            'number': Base.FIELD_REQUIRED,
        }


class Factory(Base.Factory):
    """SponsoringOrganization Factory"""

    @staticmethod
    def get_uuid_prefix():
        return 'spo'

    @staticmethod
    def _get_object_class():
        return SponsoringOrganization

    @staticmethod
    def _get_persister():
        return Persister()

    def get_from_file_data(self, data, subdistrict):
        """Load or create object from file dict"""
        try:
            obj = self.load_from_database_query(
                {
                    '__index__': 'number',
                    'type': Organization.ORG_TYPE_SPONSORING_ORGANIZATION,
                    'number': data['Unit No'],
                }
            )
        except RecordNotFoundException:
            klass = self._get_object_class()
            obj = klass()
            obj.name = data['Ward/Sponsoring Org']
            obj.number = data['Unit No']
            obj.parent_uuid = subdistrict.uuid
            obj.validate()
        return obj


class Persister(Base.Persister):

    """Persists SponsoringOrganization objects"""

    @staticmethod
    def _get_table_name():
        return 'Organizations'
