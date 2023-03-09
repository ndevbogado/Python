#! /bin/bash 

DIR=./scriptDir
URL_FILE=$DIR/url.txt
INFO_FILE=$DIR/info.txt
LIST_FILE=$DIR/list.txt

if [ ! -d "$DIR" ]
#Checks if the directory is not created and creates it
then 
	mkdir $DIR

	echo "https://www.google.com" > $URL_FILE 
	echo "no INFO passed" > $INFO_FILE
fi

printf "(1) - Continue reading\n(2) - Save info\n(3) - View list\n(4) - Edit List\nType an option:  "
read -r option

case $option in
	1)
	info=`cat $INFO_FILE`
	url=`cat $URL_FILE`
	echo "INFO: $info"
	xdg-open "$url"
	;;

	2)
	printf "Write the url: "
	read -r url
	echo $url > $URL_FILE	

	printf "Write a description: "
	read -r info
	echo $info > $INFO_FILE
	;;

	3)
		if [ -f $LIST_FILE ]
		then	
			while read line
			do
				i=1
				echo "Line $i: $line"
				i=$((i+1))
			done < $LIST_FILE
		else
			echo "List file not found! Choose option '4' to create one."
		fi
	;;
	*)
	printf "Write something: "
	read -r info
	echo "$info" >> $LIST_FILE
	;;
esac
