from __future__ import unicode_literals

from .models import Logs


def logger(ticket, user, action, destiny):
    log_destiny = (destiny[:190] + '..') if len(str(destiny)) > 75 else destiny
    new_log_row = Logs.objects.create(
        log_ticket=ticket, log_user=user, log_action=action, log_destiny=str(log_destiny))
    new_log_row.save()
    return new_log_row
