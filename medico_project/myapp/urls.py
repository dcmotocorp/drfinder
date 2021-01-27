"""medico_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,include
from . import views
urlpatterns = [
    path("index_page/",views.index_page,name="index_page"),

path("patient_profile/", views.patient_profile, name="patient_profile"),
path("add_patient/", views.add_patient, name="add_patient"),
path("all_patients/", views.all_patients, name="all_patients"),
path("doctors/", views.doctors, name="doctors"),
path("addoctors/", views.addoctors, name="addoctors"),
path("drprofile/<int:ck>", views.drprofile, name="drprofile"),
path("event/", views.event, name="event"),

# app
path("chat/", views.chat, name="chat"),
path("compose/", views.compose, name="compose"),
path("contact_list/", views.contact_list, name="contact_list"),
path("inbox/", views.inbox, name="inbox"),
path("single/", views.single, name="single"),

# book_appoitment
path("book_appoitment/", views.book_appoitment, name="book_appoitment"),
path("appointment/", views.appointment, name="appointment"),

# authentication

path("register-page/",views.register_page,name="register-page"),
path("login-page/", views.login_page, name="login-page"),
path("register/", views.register, name="register"),
path("login_evalute/", views.login_evalute, name="login_evalute"),
path("logout/", views.logout, name="logout"),
path("forgot_password/", views.forgot_password, name="forgot_password"),
path("SEND_OTP/", views.SEND_OTP, name="SEND_OTP"),
path("reset_password/", views.reset_password, name="reset_password"),
path("page404/", views.page404, name="page404"),
path("page500/", views.page500, name="page500"),
path("page_offline/", views.page_offline, name="page_offline"),



# blog

path("dashboard/", views.dashboard, name="dashboard"),
path("detail/", views.detail, name="detail"),
path("grid/", views.grid, name="grid"),
path("list/", views.list, name="list"),
path("new_post/", views.new_post, name="new_post"),


# department

path("add_department/", views.add_department, name="add_department"),
path("all_department/", views.all_department, name="all_department"),
path("more_department/", views.more_department, name="more_department"),

#doctors

#file-manager


path("dashboard/", views.dashboard, name="dashboard"),
path("document/", views.document, name="document"),
path("image/", views.image, name="image"),
path("media/", views.media, name="media"),

#page

path("blank_pages/", views.blank_pages, name="blank_pages"),
path("image_gallery/", views.image_gallery, name="image_gallery"),
path("profile/", views.profile, name="profile"),
path("rtl/", views.rtl, name="rtl"),
path("search_result/", views.search_result, name="search_result"),
path("timeline/", views.timeline, name="timeline"),

#patient
path("invoice/", views.invoice, name="invoice"),

#payment

path("add_payment/", views.add_payment, name="add_payment"),
path("all_payment/", views.all_payment, name="all_payment"),

#ui


path("alerts/", views.alerts, name="alerts"),
path("collapse/", views.collapse, name="collapse"),
path("colors/", views.colors, name="colors"),
path("dialogs/", views.dialogs, name="dialogs"),
path("icons/", views.icons, name="icons"),
path("list_group/", views.list_group, name="list_group"),
path("media_objects/", views.media_objects, name="media_objects"),
path("models/", views.models, name="models"),
path("notifications/", views.notifications, name="notifications"),
path("progressbar/", views.progressbar, name="progressbar"),
path("range_slider/", views.range_slider, name="range_slider"),
path("sortable_nestable/", views.sortable_nestable, name="sortable_nestable"),
path("tabs/", views.tabs, name="tabs"),
path("ui_ki/", views.ui_ki, name="ui_ki"),
path("waves/", views.waves, name="waves"),

#widgets

path("apps/", views.apps, name="apps"),
path("data/", views.data, name="data"),


#edit patient detail
path("edit_patient/", views.edit_patient, name="edit_patient"),
path("edit_patient_detail/", views.edit_patient_detail, name="edit_patient_detail"),

    ]
