FROM python:3

ADD main.py /

RUN pip install requests
RUN pip install PyYAML
RUN pip install pytest
RUN pip install requests-mock

CMD [ "python", "./main.py" ]