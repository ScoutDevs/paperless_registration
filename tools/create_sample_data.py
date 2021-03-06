#!/usr/bin/python

# pylint: disable=no-member
"""Creates sample data to prime the pump"""

from . import AdultApplications
from . import CharterApplications
from . import District
from . import Guardian
from . import SponsoringOrganization
from . import Subdistrict
from . import Unit
from . import User
from . import Volunteer
from . import Youth
from . import YouthApplications
from . import sample_data


def create_objects(module, source_data):
    """Create and persist objects"""
    factory = module.Factory()
    persister = module.Persister()

    for data in source_data:
        obj = factory.construct(data)
        persister.save(obj)


def main():
    """Create all the objects from the sample data"""
    create_objects(User, sample_data.USER_DATA)
    create_objects(Youth, sample_data.YOUTH_DATA)
    create_objects(Volunteer, sample_data.VOLUNTEERS_DATA)
    create_objects(Guardian, sample_data.GUARDIANS_DATA)
    create_objects(District, sample_data.DISTRICTS_DATA)
    create_objects(Subdistrict, sample_data.SUBDISTRICTS_DATA)
    create_objects(SponsoringOrganization, sample_data.SPONSORING_ORGANIZATIONS_DATA)
    create_objects(Unit, sample_data.UNITS_DATA)
    create_objects(YouthApplications, sample_data.YOUTH_APPLICATIONS_DATA)
    create_objects(AdultApplications, sample_data.ADULT_APPLICATIONS_DATA)
    create_objects(CharterApplications, sample_data.CHARTER_APPLICATIONS_DATA)

if __name__ == '__main__':
    main()
