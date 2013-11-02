from django.http import HttpResponse
from django.utils import simplejson

def json_response(data):
    json_data = simplejson.dumps(data)
    return HttpResponse(json_data, content_type="application/json")

from django.db import transaction

@transaction.commit_manually
def flush_transaction():
    """
    Flush the current transaction so we don't read stale data

    Use in long running processes to make sure fresh data is read from
    the database.  This is a problem with MySQL and the default
    transaction mode.  You can fix it by setting
    "transaction-isolation = READ-COMMITTED" in my.cnf or by calling
    this function at the appropriate moment
    """
    transaction.commit()