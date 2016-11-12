
from models.system_calls import *


def get_email_by_token(id):
    return db_pool.query("select email from public.users where unique_id={}".format(id, fetch_opts="single"))
