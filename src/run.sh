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
    python search_bing_api.py --query "\"$name\"" --output "$output"
fi

exit 1

# FACE ENCODER
encodings="../data/encodings/$name_dir.pickle"
if [ ! -f "$encodings" ]; then
    echo "Developing ENCODINGS"
    python encode_faces.py --dataset "$output" --encodings "$encodings" --detection-method 'hog'
fi

# FACE DETECTOR
python main.py --video '../data/clip_01.mp4' --encodings "$encodings" --detection-method 'hog'
