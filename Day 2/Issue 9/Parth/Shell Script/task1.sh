#!/bin/bash

read -e -p "Log Directory: " log_directory
read -e -p "File Extension: " extension
read -e -p "Backup Directory: " backup_directory

# Add the cron job to run every two days at midnight
(crontab -l 2>/dev/null; echo "0 0 */2 * * /bin/bash $(realpath "$0")") | crontab -

echo "Cron job added"

tar czf archive.tar.gz $(find "$log_directory" -name "*.$extension")
mv archive.tar.gz "$backup_directory"/$(date +%F).tar.gz
rm $(find "$log_directory" -name "*.$extension")

exit 0