
FROM python:latest

COPY requirements.txt .

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable 
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN apt-get install -yqq unzip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

RUN pip install -r requirements.txt


RUN mkdir /mydirectory

WORKDIR /mydirectory

COPY scraper.py .
COPY retrieve_data.py .
COPY book.py .
COPY driver.py .
COPY file_system_manager.py .
COPY requirements.txt .

ENTRYPOINT ["python", "scraper.py"]