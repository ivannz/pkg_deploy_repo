from pkg_resources import resource_stream

def get_schedule():
    with resource_stream("bar", "schedule") as fin:
        return fin.readlines()
