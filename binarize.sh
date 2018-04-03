cd output_files
for f in *.png; do
  echo "$f"
  convert "$f" -threshold 50% "$f"
done
