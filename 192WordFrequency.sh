awk '{words[$1]+=1} END{for(word in words){print word,words[word]}}' RS="[ \n]+" words.txt  | sort -nrk2