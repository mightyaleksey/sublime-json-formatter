#!/bin/sh

files='JsonFormatter.py JsonFormatter.sublime-commands'
packages_dir=~/Library/Application\ Support/Sublime\ Text\ 3/Packages

mkdir -p "$packages_dir/JsonFormatter"
for file in $files; do
  cp "$file" "$packages_dir/JsonFormatter/"
done
