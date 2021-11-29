FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /afisha
COPY req.txt /afisha/req.txt
RUN pip install  -r/afisha/req.txt
COPY . /afisha

EXPOSE 8000
CMD ["python","manage.py","runserver","127.0.0.1:8000"]