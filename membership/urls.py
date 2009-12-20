from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # XXX Would be nice to use just the name for redirect, but how to import from
    # urlconf that is not yet defined...
    url(r'pre-approval/', 'membership.views.membership_list_new', name='pre-approval'),

    url(r'new/person/', 'membership.views.new_person_application', name='new_person_application'),
    url(r'new/organization', 'membership.views.new_organization_application', name='new_organization_application'),
    url(r'new/', 'membership.views.new_application', name='new_application'),

    url(r'list/', 'membership.views.membership_list', name='membership_list'),
    url(r'edit_inline/(\d+)/', 'membership.views.membership_edit_inline', name='membership_edit_inline'),
    url(r'edit/(\d+)/', 'membership.views.membership_edit', name='membership_edit'),
    url(r'preapprove/(\d+)/', 'membership.views.membership_preapprove', name='membership_preapprove'),
    url(r'unpaid/', 'membership.views.unpaid_bill_list', name='unpaid_bill_list'),
    url(r'bills/', 'membership.views.bill_list', name='bill_list'),
    url(r'approve/(\d+)/', 'membership.views.membership_approve', name='membership_approve'),
)
