


sed -i  's/       <\/td>/,/g' cs
sed -n '/<td align="center">/{n;p}' cs > cs2
sed -i 's/<p align="center">//g' cs2
sed -i 's/&nbsp;<\/p>//g' cs2
sed -i s/[[:space:]]//g  cs2
cat cs2
