import re


class QueryHandler:
    command_map={
        "select":[r"^SELECT\s+(?P<columns>\*|[\w,\s]+)\s+FROM\s+(?P<table>\w+)\s*;$"],
        "insert":[r"^INSERT\s+INTO\s+(?P<table>\w+)\s+VALUES\s+(?P<value>.+)\s*;$"],
        "create":{
            "db":[r"CREATE\s+DB\s+(?P<database>\w+)\s*;$"],
            "tb":[r"CREATE\s+TB\s+(?P<tabale>\w+)\s+(?P<value>.+)\s*;$"],
        },
    }


    def regax_query_parser(self,regex,query):
        return re.match(
            regex,
            query,
            re.IGNORECASE
        )

    def query_command_identifier(self,query,command_mapper=command_map):
        query=query.lower()
        if query.startswith("exit"):
            exit(0)
        for command in command_mapper:
            if len(command_mapper[command])==1:
                if command in query:
                    return command_mapper[command][0]

            else:
                return self.query_command_identifier(query,command_mapper[command])
        return None
    
    def query_parser(self,query):
        result=self.query_command_identifier(query)
        if result:
            regax_val=self.regax_query_parser(result,query)
            if regax_val:
                return regax_val.groupdict()
        return None
    
    
