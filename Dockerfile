# Openfaas JSON Wrapper
FROM python:3.4-alpine
LABEL maintainer="simone.zabberoni@gmail.com"
LABEL version="0.2"

# Python wrapper
COPY entrypoint.py   .
RUN chmod +x entrypoint.py

# Openfaas watchdog
ADD https://github.com/openfaas/faas/releases/download/0.7.9/fwatchdog /usr/bin
RUN chmod +x /usr/bin/fwatchdog

# Startup
ENV fprocess="./entrypoint.py"
CMD ["fwatchdog"]
EXPOSE 8080

#--------------------------------------------------#
# Additional setup here - examples                 #
#--------------------------------------------------#

# COPY requirements.txt . 
# RUN pip install -r requirements.txt
 
# RUN apk add --update bind-tools

# RUN pip install requests



