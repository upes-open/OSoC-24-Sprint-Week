#!/bin/bash

LOG_ARCHIVER_SCRIPT="./log_archiver.sh"

if [ ! -f "$LOG_ARCHIVER_SCRIPT" ]; then
    echo "Error: Log archiver script not found at $LOG_ARCHIVER_SCRIPT"
    exit 1
fi

chmod +x "$LOG_ARCHIVER_SCRIPT"

"$LOG_ARCHIVER_SCRIPT"

echo "Log archiver initiated. It will run every 2 days automatically."