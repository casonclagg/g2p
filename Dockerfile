FROM pytorch/pytorch:1.9.0-cuda11.1-cudnn8-runtime

WORKDIR /content

# Install python requirements
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["/bin/bash"]

# docker build -t ccc/g2p .
# docker run -it -v $(pwd):/content ccc/g2p /bin/bash
# docker run -it -v $(pwd):/content ccc/g2p python test.py