FROM python:alpine3.6

ADD main.py run.sh /root/Challenge/
RUN chmod u+x /root/Challenge/run.sh

# Add dependencies
RUN pip install pyparsing

# Run the program end exit
ENTRYPOINT ["sh", "-c", "/root/Challenge/run.sh"]

