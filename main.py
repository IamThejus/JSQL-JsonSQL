from query_handler import QueryHandler

qh=QueryHandler()


while True:
    query=input(">>>")
    print(qh.query_parser(query))