# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . .
EXPOSE 80
CMD [ "python","manage.py","runserver","0.0.0.0:80" ]
# making any changes
# now i will push those changes to new_brach
