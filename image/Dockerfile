FROM python:latest

RUN pip3 install PyGithub requests

COPY get_public_repo.py /home/

CMD ["python /home/get_public_repo.py"]