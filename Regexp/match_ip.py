import re
pattern = re.compile(r'([0-9]|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])(\.(\d|[1-9]\d|1\d{2}|2[0-4]\d|25[0-5])){3}')

# input: a string containing only ip address
# output: boolean value
# return True if the string matches a valid ip adress from beginning to end
def match_ip(s):
    return bool(pattern.match(s))

# return True if a fraction of the string matches a valid ip adress
def search_ip(s):
    return bool(pattern.search(s))
