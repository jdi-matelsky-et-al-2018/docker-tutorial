FROM pydicom/dicom
LABEL maintainer="Your Name <your@email.com>"

ADD ./normalize_scan.py .
ADD ./requirements.txt .
RUN pip install -r ./requirements.txt

CMD /bin/bash
ENTRYPOINT python3 ./normalize_scan.py /infile.dcm /mnt/vout/ 0 100
