#! /bin/bash

for file in $*
do
	echo "Type a TODO or type 'exit': "
	read -r option 
	
	if [ "${option,,}" == "exit" ]
	then
		echo "Exit successfull!"
		break
	else
		if [ -f ./$file ]
		then 
			echo "$file already exists. Do you want to overwrite it? "
			read -r option2
			if [ "${option2,,}" == 'yes' ] || [ "${option2,,}" == "y" ]
			then
				echo "# $option" > ./$file
				echo "$file overwrited successfully!"
				nvim "./$file"
			fi
		else
			echo "# $option" > ./$file
			echo "$file created successfully!"
			nvim "./$file"
		fi
		#clear
	fi
done
