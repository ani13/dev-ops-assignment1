FROM ubuntu:latest
LABEL authors="ani"

ENTRYPOINT ["top", "-b"]