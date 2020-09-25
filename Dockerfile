FROM python:3.8
RUN pip install --upgrade pip
WORKDIR /
COPY ./src /src
COPY ./requirements.txt /
COPY ./gunicorn.py /
RUN pip install -r requirements.txt
EXPOSE 5000

USER root

RUN mkdir /usr/share/applogs
RUN chown -R root /usr/share/applogs/
RUN chmod -R go-w /usr/share/applogs/

#CMD python ./rest_api.py
CMD ["gunicorn", "--config", "gunicorn.py", "src.controller.rest_api:app"]