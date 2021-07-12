#!/bin/sh
python readme_update.py
git add README.md
git commit -m "Update README.md"
git push
