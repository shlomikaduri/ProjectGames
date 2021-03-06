FROM python:3-alpine
COPY GuessGame.py /
COPY Live.py /
COPY MainGame.py /
COPY MainScores.py /
COPY MemoryGame.py /
COPY Score.py /
COPY Scores.txt /
COPY Utils.py /

RUN pip install flask

CMD ["python3", "./MainScores.py"]
