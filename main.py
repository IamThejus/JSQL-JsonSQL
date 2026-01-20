import re

command_mapper={
    "select":[r"^SELECT\s+(?P<columns>\*|[\w,\s]+)\s+FROM\s+(?P<table>\w+);$"],
    "insert":[r"^INSERT\s+INTO\s+(?P<table>\w+)\s+VALUES\s+(?P<value>.+);$"],
    "create":{
        "db":[r"CREATE\s+DB\s+(?P<database>\w+)\s*;$"],
        "tb":[r"CREATE\s+TB\s+(?P<tabale>\w+)\s+(?P<value>.+);$"],
    }
}


def query_parser(regex,query):
    return re.match(
        regex,
        query,
        re.IGNORECASE
    )
# this function works but only for "select" check it
def query_command_identifier(query,command_mapper):
    for command in command_mapper:
        if len(command_mapper[command])==1:
            if command in query:
                return command_mapper[command][0]

        else:
            return query_command_identifier(query,command_mapper[command])
    return False

while True:
    query=input(">>>")
    cmd=query_command_identifier(query,command_mapper)
    if cmd:
        result=query_parser(cmd,query)
        if result:
            print(result.groupdict())
            