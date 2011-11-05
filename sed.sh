
sed -i '/<td align="center">/{n;p}' cs
sed -i 's/<p align="center">//g' cs
sed -i 's/&nbsp;<\/p>//g' cs
sed -i s/[[:space:]]//g  cs
cat cs
