# With modifications from
# https://github.com/lincolnloop/django-salmonella/blob/master/salmonella/views.py

from django.urls import reverse
from django.conf import settings
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseBadRequest, HttpResponseForbidden
from django.shortcuts import render
from django.apps import apps


@user_passes_test(lambda u: u.is_staff)
def label_view(request, app_name, model_name):

    template_object_name = 'object'
    template_name = 'dj_ajax_raw_id_fields/label.html'

    # The list of to obtained objects is in GET.id. No need to resume if we
    # didnt get it.
    if not request.GET.get('id'):
        msg = 'No list of objects given'
        return HttpResponseBadRequest(settings.DEBUG and msg or '')

    # Given objects are either an integer or a comma-separted list of
    # integers. Validate them and ignore invalid values. Also strip them
    # in case the user entered values by hand, such as '1, 2,3'.
    object_list = []
    for pk in request.GET['id'].split(","):
        object_list.append(pk.strip())

    # Check if at least one value survived this cleanup.
    if len(object_list) == 0:
        msg = 'No list or only invalid ids of objects given'
        return HttpResponseBadRequest(settings.DEBUG and msg or '')

    # Make sure this model exists and the user has 'change' permission for it.
    # If he doesnt have this permission, Django would not display the
    # change_list in the popup and the user were never able to select objects.
    try:
        model = apps.get_model(app_name, model_name)
    except LookupError:
        msg = 'Model %s.%s does not exist.' % (app_name, model_name)
        return HttpResponseBadRequest(settings.DEBUG and msg or '')

    if not request.user.has_perm('%s.change_%s' % (app_name, model_name)):
        return HttpResponseForbidden()

    try:
        model_template = "dj_ajax_raw_id_fields/%s/%s.html" % (
            app_name, model_name)
        obj = model.objects.get(pk=object_list[0])
        change_url = reverse("admin:%s_%s_change" % (app_name, model_name),
                             args=[obj.pk])
        extra_context = {
            template_object_name: (obj, change_url),
        }
    # most likely the pk wasn't convertable
    except ValueError:
        msg = 'ValueError during lookup'
        return HttpResponseBadRequest(settings.DEBUG and msg or '')
    except model.DoesNotExist:
        msg = 'Model instance does not exist'
        return HttpResponseBadRequest(settings.DEBUG and msg or '')

    return render(request, (model_template, template_name), extra_context)
