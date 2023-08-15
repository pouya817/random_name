FROM python:3.10.1
COPY randomname1.py /app/
WORKDIR /app
RUN pip install requests
CMD ["python" , "./randomname1.py"]