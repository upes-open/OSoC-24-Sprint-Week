#!/bin/bash

# Configuration
LOG_SOURCE_DIR="./log"  
ARCHIVE_DIR="./archive/logs"  
DAYS_OLD=2  
SCRIPT_PATH=$(readlink -f "$0") 
LOCK_FILE="/tmp/log_archiver.lock"

# Function to perform log archiving
perform_archiving() {
   
    mkdir -p "$ARCHIVE_DIR"

    CURRENT_DATE=$(date +"%Y-%m-%d")


    ARCHIVE_FILE="logs_${CURRENT_DATE}.tar.gz"

    find "$LOG_SOURCE_DIR" -type f -mtime +$DAYS_OLD -print0 | tar czvf "$ARCHIVE_DIR/$ARCHIVE_FILE" --null -T -

    find "$LOG_SOURCE_DIR" -type f -mtime +$DAYS_OLD -delete

    echo "Log archiving completed. Archive saved as $ARCHIVE_DIR/$ARCHIVE_FILE"
}

if [ -e "$LOCK_FILE" ]; then
    echo "Script is already running. Exiting."
    exit 1
fi

touch "$LOCK_FILE"

perform_archiving

at now + 2 days &lt;&lt;EOF
$SCRIPT_PATH
EOF

rm "$LOCK_FILE"

echo "Next run scheduled in 2 days."