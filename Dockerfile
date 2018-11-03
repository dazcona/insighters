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
RUN cd /insighters/dlib/build
RUN cmake /insighters/dlib -DDLIB_USE_CUDA=1 -DUSE_AVX_INSTRUCTIONS=1
RUN cmake --build .
RUN cd ..
RUN python setup.py install --yes USE_AVX_INSTRUCTIONS --yes DLIB_USE_CUDA

RUN pip install \
face_recognition \
imutils \
opencv-python