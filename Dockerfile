FROM alpine:3.12

COPY requirements.txt /
RUN apk add --update --no-cache python3 \
 && rm -rf /var/cache/* \
 && mkdir /var/cache/apk \
 && ln -sf python3 /usr/bin/python \
 && python -m ensurepip \
 && pip3 install --no-cache-dir --upgrade pip \
 && pip3 install --no-cache-dir -r requirements.txt

COPY root/ /

ENTRYPOINT ["/app/rename.py"]
CMD ["-h"]
