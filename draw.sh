#!/bin/bash

GIT_EMAIL="nisozakuto@gmail.com"
GIT_NAME="Niso Zakuto"
HOLIDAYS="skip_dates.txt"
START_DATE=$(date -v-52w -v-Sun +"%Y-%m-%d")
TODAY=$(date +"%Y-%m-%d")
CURRENT_DATE=$START_DATE

# Reset pixels.txt so commits are unique
> pixels.txt

while [[ "$CURRENT_DATE" < "$TODAY" ]]; do

    # Skip holidays/Saturdays
    if grep -qx "$CURRENT_DATE" "$HOLIDAYS"; then
        echo "Skipping $CURRENT_DATE"
    else
        # Add unique content
        echo "$(date +%s) pixel $CURRENT_DATE" >> pixels.txt

        # Commit with correct dates
        GIT_AUTHOR_DATE="$(date -j -f "%Y-%m-%d" "$CURRENT_DATE" +"%Y-%m-%dT12:00:00")" \
        GIT_COMMITTER_DATE="$(date -j -f "%Y-%m-%d" "$CURRENT_DATE" +"%Y-%m-%dT12:00:00")" \
        GIT_AUTHOR_NAME="$GIT_NAME" \
        GIT_AUTHOR_EMAIL="$GIT_EMAIL" \
        GIT_COMMITTER_NAME="$GIT_NAME" \
        GIT_COMMITTER_EMAIL="$GIT_EMAIL" \
        git add pixels.txt
        git commit -m "pixel $CURRENT_DATE"

        echo "Committed $CURRENT_DATE"
    fi

    # Next day
    CURRENT_DATE=$(date -j -v+1d -f "%Y-%m-%d" "$CURRENT_DATE" +"%Y-%m-%d")
done
