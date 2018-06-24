# "Reporting tool" for the News Forum queries.
import psycopg2

DBName = "news"


def popular_articles(cursor):
    """Return 3 most popular articles of all time."""
    title = ("1. What are the most popular three articles of all time?")
    cursor.execute("select title, count(path) as views from articles, \
    log where concat('/article/', articles.slug) = log.path \
    group by title order by views desc limit 3;")
    results = cursor.fetchall()
    print(title)
    for article in results:
        print ". %s - %s views" % (article[0], article[1])
    print("\n")


def popular_authors(cursor):
    """Return most popular article authors of all time."""
    title = ("2. Who are the most popular article authors of all time?")
    cursor.execute("select authors.name, count(*) as views from authors, \
    articles, log where authors.id = articles.author and \
    concat('/article/', articles.slug) = log.path group by \
    name order by views desc;")
    results = cursor.fetchall()
    print(title)
    for article in results:
        print ". %s - %s views" % (article[0], article[1])
    print("\n")


def request_errors(cursor):
    """Returns the day when more than 1% of requests lead to error."""
    title = ("3. On which days did more than 1% of requests lead to errors?")
    cursor.execute("select * from (select to_char(date(time), 'Mon DD, YYYY'),\
    round(100.0*sum(case log.status when '200 OK'  then 0 \
    else 1 end)/count(log.status),2) as error from log group \
    by date(time) order by error desc) as subq where error > 1;")
    results = cursor.fetchall()
    print(title)
    for article in results:
        print ". %s - %s%%errors" % (article[0], article[1])
    print("\n")


def database_operations():
    db = psycopg2.connect(database=DBName)
    cursor = db.cursor()
    popular_articles(cursor)
    popular_authors(cursor)
    request_errors(cursor)
    db.close()


if __name__ == '__main__':
    database_operations()
