
#!/bin/bash

# Get the directory where the script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Loop through all MKV files in the script's directory
for file in "$SCRIPT_DIR"/*.mkv; do
  if [ -f "$file" ]; then
    curl -T "$file" -u :145846d5-4210-4103-a18b-9dbf9e25429d https://pixeldrain.com/api/file/
  fi
done

echo "Upload complete."

