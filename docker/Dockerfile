FROM tensorflow/tensorflow:latest-gpu
WORKDIR /insighters
RUN apt update -y; apt install -y \
git \
cmake \
libsm6 \
libxext6 \
libxrender-dev

RUN git clone https://github.com/davisking/dlib.git
RUN mkdir -p /insighters/dlib/build
RUN cd /insighters/dlib/build; cmake .. -DDLIB_USE_CUDA=1 -DUSE_AVX_INSTRUCTIONS=1; cmake --build .; cd ..; python setup.py install --yes USE_AVX_INSTRUCTIONS --yes DLIB_USE_CUDA

RUN pip install \
face_recognition \
imutils \
opencv-python

RUN pip install requests