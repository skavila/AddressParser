FROM python:3.8
RUN pip install --upgrade pip
WORKDIR /
COPY ./src /src
COPY ./requirements.txt /
COPY ./gunicorn.py /
RUN pip install -r requirements.txt
EXPOSE 5000
#CMD python ./rest_api.py
CMD ["gunicorn", "--config", "gunicorn.py", "src.controller.rest_api:app"]