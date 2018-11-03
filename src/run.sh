
if [ $# -eq 0 ]
then
    echo "No arguments supplied"
    echo "Usage: $ sh run.sh <celebrity name>"
fi

name="$@"
echo "Running face recognizer for:" $name

# CRAWLER
output="../data/images/$name"
# rm -r "$output"
if [ ! -d "$output" ]; then
    echo "Calling CRAWLER"
    mkdir -p "$output"
    python search_bing_api.py --query "$name" --output "$output"
fi

# FACE ENCODER
encodings="../data/encodings/$name.pickle"
if [ ! -f "$encodings" ]; then
    echo "Developing ENCODINGS"
    python encode_faces.py --dataset "$output" --encodings "$encodings" --detection-method 'hog'
fi

# FACE DETECTOR
python main.py --video '../data/clip_01.mp4' --encodings "$encodings" --detection-method 'hog'
