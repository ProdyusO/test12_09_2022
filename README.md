First commit
The task wasn't completed, there are problems with writing to the database. The error is clear, I have to  rewrite the parser's code in another way. It seems to me, the parser works not bad. I'll continue to write this task but according agreement with Yana my time was end.

Second commit 
Task done without Postgres and Docker. 
    1) For run app in "src" directory you need to write "uvicorn main:app --reload" in terminal;
    2) Then go to 127.0.0.1/8000/n, where n = amount of pages (for example: 127.0.0.1:8000/1 - 1 page, 127.0.0.1:8000/3 - 3 pages) (Pagination)