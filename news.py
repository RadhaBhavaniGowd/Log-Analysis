#!/usr/bin/env python
import psycopg2

DBName = "news"


def db_connect():
    """Return a connection to the news database and cursor."""
    db = psycopg2.connect(database=DBName)
    c = db.cursor()
    return db, c


def execute_query(query):
    """execute_query takes an SQL query as a parameter.
	Executes the query and returns the results as a list of tuples."""
    db, cursor = db_connect()
    cursor.execute(query)
    return cursor.fetchall()
    db.close()


def popular_articles():
    """Return 3 most popular articles of all time."""
    print("1. What are the most popular three articles of all time?")
    query = """select title, views from articles
    inner join (select path, count(path) as views from log group by log.path)
    as log on log.path = '/article/' || articles.slug order by views
    desc limit 3;"""
    results = execute_query(query)
    for article, view in results:
        print('."{}" - {} views'.format(article, view))
    print("\n")


def popular_authors():
    """Return most popular article authors of all time."""
    print("2. Who are the most popular article authors of all time?")
    query = """select authors.name, count(*) as views from authors,
    articles, log where authors.id = articles.author and
    concat('/article/', articles.slug) = log.path group by name
    order by views desc;"""
    results = execute_query(query)
    for author, view in results:
        print('. {} - {} views'.format(author, view))
    print("\n")


def request_errors():
    """Return the day when more than 1% of requests lead to error."""
    print("3. On which days did more than 1% of requests lead to errors?")
    query = """select * from (select to_char(date(time), 'Mon DD, YYYY'),
    round(100.0*sum(case log.status when '200 OK'  then 0 else 1 end)
    /count(log.status),2) as error from log group by date(time)
    order by error desc) as subq where error > 1;"""
    results = execute_query(query)
    for day, percent in results:
        print('. {} - {}%%errors'.format(day, percent))
    print("\n")


def database_operations():
    popular_articles()
    popular_authors()
    request_errors()


if __name__ == '__main__':
    database_operations()
