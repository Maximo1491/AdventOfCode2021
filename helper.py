import login_info
import requests

current_day = 0

def get_daily_input():
    try:
        f = open("day{day}.txt".format(day=current_day), "r")
        return f.readlines()
    except FileNotFoundError:
        uri = 'http://adventofcode.com/2021/day/{day}/input'.format(day=current_day)
        response = requests.get(uri, cookies={'session': login_info.SESSION_ID}, headers={'User-Agent': login_info.USER_AGENT})
        f = open("day{day}.txt".format(day=current_day), "w")
        f.write(response.content.decode("utf-8"))
        f.close()
        f = open("day{day}.txt".format(day=current_day), "r")
        return f.readlines()

def get_daily_input_numbers():
    input = get_daily_input()
    return [int(i) for i in input]

def get_daily_input_strings():
    input = get_daily_input()
    return [str(i).strip() for i in input]