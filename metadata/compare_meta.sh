path="/mnt/d/csc5003data"
echo "" > diff.txt
for ((i=2005; i<=2015; i++)); do
    for ((j=i+1; j<=2015; j++)); do
        #echo "$i : $j"
        file1=$path/${i}_codes.json
        file2=$path/${j}_codes.json
        jd $file1 $file2 >> diff.txt
    done
done
