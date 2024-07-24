#!/bin/bash

# Configuration
LOG_SOURCE_DIR="./log"  
ARCHIVE_DIR="./archive/logs"  
DAYS_OLD=1
SCRIPT_PATH=$(readlink -f "$0") 
LOCK_FILE="/tmp/log_archiver.lock"

# Function to perform log archiving
perform_archiving() {
    echo "Starting archiving process..."
    echo "LOG_SOURCE_DIR: $LOG_SOURCE_DIR"
    echo "ARCHIVE_DIR: $ARCHIVE_DIR"
    echo "DAYS_OLD: $DAYS_OLD"
    
    mkdir -p "$ARCHIVE_DIR"
    CURRENT_DATE=$(date +"%Y-%m-%d")
    ARCHIVE_FILE="logs_${CURRENT_DATE}.tar.gz"
    
    echo "Files to be archived:"
    find "$LOG_SOURCE_DIR" -type f -not -newermt "-${DAYS_OLD} days" -print
    
    echo "Creating archive..."
    find "$LOG_SOURCE_DIR" -type f -not -newermt "-${DAYS_OLD} days" -print0 | 
    tar czvf "$ARCHIVE_DIR/$ARCHIVE_FILE" --null -T - --verbose
    
    echo "Deleting archived files..."
    find "$LOG_SOURCE_DIR" -type f -not -newermt "-${DAYS_OLD} days" -delete
    
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