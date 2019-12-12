FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /src
WORKDIR /src
ADD requirements.txt /src/
RUN pip install -r requirements.txt
RUN pip install mysqlclient 
ADD . /src/
EXPOSE 8000
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
