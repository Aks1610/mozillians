from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from cities_light.models import Country
from mozillians.users.views import (AccessGroupInvitationAutocomplete,
                                    BaseProfileAdminAutocomplete, CityAutocomplete,
                                    CountryAutocomplete, NDAGroupInvitationAutocomplete,
                                    RegionAutocomplete, StaffProfilesAutocomplete,
                                    TimeZoneAutocomplete, UsersAdminAutocomplete,
                                    VouchedAutocomplete, VoucherAutocomplete)


urlpatterns = patterns(
    '',
    # Admin urls for django-autocomplete-light.
    url('users-autocomplete/$', login_required(UsersAdminAutocomplete.as_view()),
        name='users-autocomplete'),
    url('vouchee-autocomplete/$', login_required(BaseProfileAdminAutocomplete.as_view()),
        name='vouchee-autocomplete'),
    url('voucher-autocomplete/$', login_required(VoucherAutocomplete.as_view()),
        name='voucher-autocomplete'),
    url('vouched-autocomplete/$', login_required(VouchedAutocomplete.as_view()),
        name='vouched-autocomplete'),
    url('country-autocomplete/$', login_required(CountryAutocomplete.as_view(model=Country)),
        name='country-autocomplete'),
    url('region-autocomplete/$', login_required(RegionAutocomplete.as_view()),
        name='region-autocomplete'),
    url('city-autocomplete/$', login_required(CityAutocomplete.as_view()),
        name='city-autocomplete'),
    url('timezone-autocomplete/$', login_required(TimeZoneAutocomplete.as_view()),
        name='timezone-autocomplete'),
    url('staff-autocomplete/$', login_required(StaffProfilesAutocomplete.as_view()),
        name='staff-autocomplete'),
    url('access-group-invitation-autocomplete/$',
        login_required(AccessGroupInvitationAutocomplete.as_view()),
        name='access-group-invitation-autocomplete'),
    url('nda-group-invitation-autocomplete/$',
        login_required(NDAGroupInvitationAutocomplete.as_view()),
        name='nda-group-invitation-autocomplete'),
)
