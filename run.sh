#!/bin/sh

for i in `ls splits`; do #i is the wordlist name
	python2 $1 -d ns.agency -w "$PWD/splits/$i" -t 64 -o "$PWD/results/$i.txt"&
done
