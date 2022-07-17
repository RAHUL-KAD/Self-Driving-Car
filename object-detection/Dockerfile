# Since yolov5 is built using pytorch we will use pytorch image
FROM pytorch/pytorch:latest

RUN apt-get update

RUN pip install --upgrade pip

RUN pip install -r https://raw.githubusercontent.com/ultralytics/yolov5/master/requirements.txt streamlit

RUN apt-get install ffmpeg libsm6 libxext6  -y

WORKDIR /app

COPY . /app

EXPOSE 8000

CMD ["streamlit", "run", "app.py"]