# assert that there are 2 arguments
if [ $# -ne 2 ]; then
    echo "Usage: $0 <path_to_dir> <output>"
    exit 1
fi

convert -resize 70% -delay 200 -loop 0 $1/*.png $2