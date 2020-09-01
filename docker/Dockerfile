#publicly available docker image "python" on docker hub will be pulled

FROM python:3.8

#creating directory myscript in container (linux machine)

RUN mkdir ./twittermonitor

#copying requirements.txt from local directory to container's myscript folder
COPY requirements.txt ./twittermonitor/requirements.txt
CMD pip install -r ./requirements.txt

#copying twittermonitor.py from local directory to container's myscript folder
COPY twittermonitor.py ./twittermonitor/twittermonitor.py

#running twittermonitor.py in container
CMD python3 ./twittermonitor/twittermonitor.py NSWEducation

#EXPOSE 8000

#CMD twittermonitor --port 8000