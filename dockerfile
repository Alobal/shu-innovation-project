FROM python:3.8
RUN mkdir /home/web && cd /home/web
WORKDIR /home/web
COPY ./backend/* /home/web/
RUN pip install -r ./requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/  \
    && pip install gunicorn

EXPOSE 5000
CMD [ "gunicorn", "-w", "5", "api:app"]
