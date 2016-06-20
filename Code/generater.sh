filename=$1
convert filename -compress none ${filename:0:-4}.ppm
python findEdges.py ${filename:0:-4}.ppm
convert ${filename:0:-4}Edges.jpg -compress none ${filename:0:-4}Edges.ppm
python3 instructionGenerater.py ${filename:0:-4}Edges.ppm