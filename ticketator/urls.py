from django.conf.urls import include,url
from django.contrib import admin

#Import some modular views
from core import views
from core import views_users as vusers, views_company as vcompanies, views_queues as vqueues, \
    views_tickets as vtickets, views_group as vgroup, views_right as vright, views_auth as vauth

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^core/', include('core.urls')),

    #Dashboard, main screen spotted
    url(r'^$', views.index),

    #Settings & utilities
    url(r'^settings/$', views.settings, name='tickets-settings'),

    #Auth
    url(r'^login','django.contrib.auth.views.login',{'template_name': 'auth/login.html'}),
    url(r'^logoff', vauth.logout_v, name='logout'),

    #Users   
    url(r'^settings/user/$', vusers.list_users, name='user-list'),
    url(r'^settings/user/create', vusers.manage_user, name='user-create'),
    url(r'^settings/user/(?P<user_id>\d+)?$', vusers.manage_user, name='user-edit'),

    #Groups
    url(r'^settings/groups/$', vgroup.list_groups, name='group-list'),
    url(r'^settings/groups/create', vgroup.manage_group, name='group-create'),
    url(r'^settings/groups/(?P<group_id>\d+)?$', vgroup.manage_group, name='group-edit'),

    #Rights
    url(r'^settings/rights/$', vright.list_rights, name='right-list'),
    url(r'^settings/rights/create', vright.manage_right, name='right-create'),
    url(r'^settings/rights/(?P<right_id>\d+)?$', vright.manage_right, name='right-edit'),

    #Companys
    url(r'^settings/companies/$', vcompanies.list_companies, name='company-list'),
    url(r'^settings/companies/create', vcompanies.manage_company, name='company-create'),
    url(r'^settings/companies/(?P<company_id>\d+)?$', vcompanies.manage_company, name='company-edit'),

    #queues
    url(r'^settings/queue/$', vqueues.list_queues, name='queues-list'),
    url(r'^settings/queue/create', vqueues.manage_queue, name='queues-create'),
    url(r'^settings/queue/(?P<queue_id>\d+)?$', vqueues.manage_queue, name='queues-edit'),

    #Tickets
    url(r'^tickets/$', vtickets.list_tickets, name='tickets-list'),
    url(r'^tickets/create', vtickets.manage_ticket, name='tickets-create'),
    url(r'^tickets/(?P<ticket_id>\d+)?$', vtickets.manage_ticket, name='tickets-get'),
    
    #Filtering view
    url(r'^tickets/state/(?P<state_id>\d+)?$', vtickets.list_tickets, name='tickets-list-state'),

]

