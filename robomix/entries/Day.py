import json

class Day(object):

    def __init__(self, day_name: str, schedule: list):
        self.schedule = schedule
        self.day_name = day_name

    def __str__(self):
        return '{'+'"name":' + '"' + self.day_name + '"' + ', "schedule":' + json.dumps(self.schedule)+'}'


def make_json_from_list(jsons: list) -> str:
    result = '['
    for json in jsons:
        result = result + json + ","
    result = result[:-1]
    return result + ']'
