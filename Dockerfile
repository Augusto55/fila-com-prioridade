FROM python:3

WORKDIR /fila-com-prioridade

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY fila.py ./fila.py
CMD python fila.py