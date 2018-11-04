#!/bin/sh

if [ $# -eq 0 ]
then
    echo "No arguments supplied"
    echo "Usage: $ sh run.sh <celebrity name>"
    exit 1
fi

name="$@"
name_dir=$( echo "$name" | tr -s ' ' | tr ' ' '_' )
echo "Running face recognizer for:" $name

# CRAWLER
output="../data/images/$name_dir"
# rm -r "$output"
if [ ! -d "$output" ]; then
    echo "Calling CRAWLER"
    mkdir -p "$output"
    # Run!
    python3 crawl.py --query "\"$name\"" --output "$output"
fi

# FACE ENCODER
encodings="../data/encodings/$name_dir.pickle"
if [ ! -f "$encodings" ]; then
    echo "Developing ENCODINGS"
    python3 encode_faces.py --dataset "$output" --encodings "$encodings" --detection-method 'hog'
fi
# python3 encode_faces.py --dataset '../data/images/tom_cruise' --encodings '../data/encodings/tom_cruise.pickle' --detection-method 'hog'

# FACE DETECTOR
echo "Face Detector on a Video"
python3 main.py --video '../data/video1.mp4' --encodings "$encodings" --detection-method 'hog'
# python3 main.py --video '../data/video1.mp4' --encodings ../data/encodings/tom_cruise.pickle --detection-method 'hog'
