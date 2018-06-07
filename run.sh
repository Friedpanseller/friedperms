#!/bin/sh
domain=`echo "$1" | sed 's/\./\\./g'`
for i in `ls splits`; do #i is the wordlist name
	cat $PWD/splits/$i | sed 's/$/\.'$domain'/g' | ../zdns A | grep "NOERROR" | jq '.["name"]' | sed 's/\"//g' > results/$i.txt&
done

