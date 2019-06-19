#!/bin/bash
IFS='
'
for file in $(locate -e DS_Store)
do
	echo "Removing: $file"
	# Use double quotation to handle the space in folder/file path
	# Single quotation doesn't work
	sudo rm -rf "$file"
done

for dir in $(locate -e Network\ Trash\ Folder)
do
	echo "Removing: $dir"
	sudo rm -rf "$dir"
done

for dir in $(locate -e AppleDouble)
do
	echo "Removing: $dir"
	sudo rm -rf "$dir"
done

for dir in $(locate -e Temporary\ Items)
do
	echo "Removing: $dir"
	sudo rm -rf "$dir"
done

for dir in $(locate -e AppleDB)
do
	echo "Removing: $dir"
	sudo rm -rf "$dir"
done

for dir in $(locate -e AppleDesktop)
do
	echo "Removing: $dir"
	sudo rm -rf "$dir"
done
