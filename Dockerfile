FROM python:3

WORKDIR /fila-com-prioridade

COPY requirements.txt ./
RUN pip install requirements.txt

CMD python fila.py