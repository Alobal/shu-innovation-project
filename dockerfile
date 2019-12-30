FROM python:3.8
RUN mkdir /home/web && cd /home/web
WORKDIR /home/web
COPY ./backend/* /home/web/
RUN apt-get update \
    && apt-get install nodejs -y \
    && pip install -r ./requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/  \
    && pip install gunicorn -i https://pypi.tuna.tsinghua.edu.cn/simple/

EXPOSE 8080
CMD [ "gunicorn", "-w", "5", "-b", "0.0.0.0:8080", "api:app"]
