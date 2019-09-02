from pkg_resources import resource_stream

def get_schedule():
    with resource_stream("bar", "data/dataset.txt") as fin:
        return fin.readlines()
