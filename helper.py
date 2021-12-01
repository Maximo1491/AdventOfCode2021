import login_info
import requests

def get_daily_input(day):
    try:
        f = open("day{day}.txt".format(day=day), "r")
        return f.readlines()
    except FileNotFoundError:
        uri = 'http://adventofcode.com/2021/day/{day}/input'.format(day=day)
        response = requests.get(uri, cookies={'session': login_info.SESSION_ID}, headers={'User-Agent': login_info.USER_AGENT})
        f = open("day{day}.txt".format(day=day), "w")
        f.write(response.content.decode("utf-8"))
        f.close()
        f = open("day{day}.txt".format(day=day), "r")
        return f.readlines()

def get_daily_input_numbers(day):
    input = get_daily_input(day)
    return [int(i) for i in input]