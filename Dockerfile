FROM python:3.9

WORKDIR /application

COPY requirement.txt ./

RUN pip install -r requirement.txt 

COPY ./src ./src

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]