import re

command_recognition={
    "select":r"^SELECT\s+(?P<columns>\*|[\w,\s]+)\s+FROM\s+(?P<table>\w+);$",
    "insert":r"^INSERT\s+INTO\s+(?P<table>\w+)\s+VALUES\s+(?P<value>.+);$"
}



def query_checker(regex,query):
    return re.match(
        regex,
        query,
        re.IGNORECASE
    )

while True:
    query=input(">>>")
    for command in command_recognition:
        if command in query:
            result=query_checker(command_recognition[command],query)
            if result:
                for element in result.groupdict():
                    print(element,result[element])