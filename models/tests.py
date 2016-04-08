# pylint: disable=no-member
""" Tests models package """

import unittest
from . import Base
from . import User
from . import Youth
from . import Volunteers
from . import Guardians
from . import Districts
from . import Subdistricts
from . import SponsoringOrganizations
from . import Units
from . import YouthApplications
from . import AdultApplications
from . import CharterApplications


class ModelTestCase(unittest.TestCase):

    """ Parent for all model tests """

    def _test_persistence(self):
        """ Test persistance of object """
        self.persister.save(self.obj)

        new_obj = self.factory.load_by_uuid(self.obj.uuid)
        self.assertEquals(new_obj.uuid, self.obj.uuid)

        self.persister.delete(self.obj)
        with self.assertRaises(Base.RecordNotFoundException):
            self.factory.load_by_uuid(self.obj.uuid)


class TestUser(ModelTestCase):

    """ Tests User module """

    def setUp(self):
        """ Init """
        obj_data = {
            'username': 'foo',
            'password': 'bar',
        }
        self.obj = User.User(obj_data)
        self.factory = User.Factory()
        self.persister = User.Persister()

    def test_uuid(self):
        """ Validate the UUID prefix """
        self.assertEquals('usr', self.obj.uuid[0:3])

    def test_persistence(self):
        """ Test persistence in parent """
        self._test_persistence()


class TestYouth(ModelTestCase):

    """ Tests Youth module """

    def setUp(self):
        """ Init """
        obj_data = {
            'duplicate_hash': 'foo',
            'units': [123, 456],
        }
        self.obj = Youth.Youth(obj_data)
        self.factory = Youth.Factory()
        self.persister = Youth.Persister()

    def test_uuid(self):
        """ Validate the UUID prefix """
        self.assertEquals('yth', self.obj.uuid[0:3])

    def test_persistence(self):
        """ Test persistence in parent """
        self._test_persistence()


class TestVolunteers(ModelTestCase):

    """ Tests Volunteers module """

    def setUp(self):
        """ Init """
        obj_data = {
            'scoutnet_id': 123,
            'unit_id': 1455,
            'duplicate_hash': '123123123',
            'YPT_completion_date': '2015-01-01',
            'data': {},
        }
        self.obj = Volunteers.Volunteers(obj_data)
        self.factory = Volunteers.Factory()
        self.persister = Volunteers.Persister()

    def test_uuid(self):
        """ Validate the UUID prefix """
        self.assertEquals('vol', self.obj.uuid[0:3])

    def test_persistence(self):
        """ Test persistence in parent """
        self._test_persistence()


class TestGuardians(ModelTestCase):

    """ Tests Guardians module """

    def setUp(self):
        """ Init """
        obj_data = {
            'youth': [123, 456],
        }
        self.obj = Guardians.Guardians(obj_data)
        self.factory = Guardians.Factory()
        self.persister = Guardians.Persister()

    def test_uuid(self):
        """ Validate the UUID prefix """
        self.assertEquals('gdn', self.obj.uuid[0:3])

    def test_persistence(self):
        """ Test persistence in parent """
        self._test_persistence()


class TestDistricts(ModelTestCase):

    """ Tests Districts module """

    def setUp(self):
        """ Init """
        obj_data = {
            'number': '05',
            'name': 'Provo Peak',
        }
        self.obj = Districts.Districts(obj_data)
        self.factory = Districts.Factory()
        self.persister = Districts.Persister()

    def test_uuid(self):
        """ Validate the UUID prefix """
        self.assertEquals('dst', self.obj.uuid[0:3])

    def test_persistence(self):
        """ Test persistence in parent """
        self._test_persistence()


class TestSubdistricts(ModelTestCase):

    """ Tests Subdistricts module """

    def setUp(self):
        """ Init """
        obj_data = {
            'district_id': '123123',
            'number': '05-9',
            'name': 'Provo North Park Stake',
        }
        self.obj = Subdistricts.Subdistricts(obj_data)
        self.factory = Subdistricts.Factory()
        self.persister = Subdistricts.Persister()

    def test_uuid(self):
        """ Validate the UUID prefix """
        self.assertEquals('sbd', self.obj.uuid[0:3])

    def test_persistence(self):
        """ Test persistence in parent """
        self._test_persistence()


class TestSponsoringOrganizations(ModelTestCase):

    """ Tests SponsoringOrganizations module """

    def setUp(self):
        """ Init """
        obj_data = {
            'subdistrict_id': '123123',
            'name': 'North Park 3rd Ward',
        }
        self.obj = SponsoringOrganizations.SponsoringOrganizations(obj_data)
        self.factory = SponsoringOrganizations.Factory()
        self.persister = SponsoringOrganizations.Persister()

    def test_uuid(self):
        """ Validate the UUID prefix """
        self.assertEquals('spo', self.obj.uuid[0:3])

    def test_persistence(self):
        """ Test persistence in parent """
        self._test_persistence()


class TestUnits(ModelTestCase):

    """ Tests Units module """

    def setUp(self):
        """ Init """
        obj_data = {
            'sponsoring_organization_id': '123123',
            'type': 'Troop',
            'number': 1455,
        }
        self.obj = Units.Units(obj_data)
        self.factory = Units.Factory()
        self.persister = Units.Persister()

    def test_uuid(self):
        """ Validate the UUID prefix """
        self.assertEquals('unt', self.obj.uuid[0:3])

    def test_persistence(self):
        """ Test persistence in parent """
        self._test_persistence()


class TestYouthApplications(ModelTestCase):

    """ Tests YouthApplications module """

    def setUp(self):
        """ Init """
        obj_data = {
            'status': 'Completed',
            'unit_id': 1455,
            'scoutnet_id': 123,
            'data': {}
        }
        self.obj = YouthApplications.YouthApplications(obj_data)
        self.factory = YouthApplications.Factory()
        self.persister = YouthApplications.Persister()

    def test_uuid(self):
        """ Validate the UUID prefix """
        self.assertEquals('yap', self.obj.uuid[0:3])

    def test_persistence(self):
        """ Test persistence in parent """
        self._test_persistence()


class TestAdultApplications(ModelTestCase):

    """ Tests AdultApplications module """

    def setUp(self):
        """ Init """
        obj_data = {
            'status': 'Completed',
            'org_id': '123123',
            'data': {},
        }
        self.obj = AdultApplications.AdultApplications(obj_data)
        self.factory = AdultApplications.Factory()
        self.persister = AdultApplications.Persister()

    def test_uuid(self):
        """ Validate the UUID prefix """
        self.assertEquals('aap', self.obj.uuid[0:3])

    def test_persistence(self):
        """ Test persistence in parent """
        self._test_persistence()


class TestCharterApplications(ModelTestCase):

    """ Tests CharterApplications module """

    def setUp(self):
        """ Init """
        obj_data = {
            'sponsoring_organization_id': '123123',
            'year': 2015,
            'status': 'Completed',
        }
        self.obj = CharterApplications.CharterApplications(obj_data)
        self.factory = CharterApplications.Factory()
        self.persister = CharterApplications.Persister()

    def test_uuid(self):
        """ Validate the UUID prefix """
        self.assertEquals('cap', self.obj.uuid[0:3])

    def test_persistence(self):
        """ Test persistence in parent """
        self._test_persistence()


if __name__ == '__main__':
    unittest.main()