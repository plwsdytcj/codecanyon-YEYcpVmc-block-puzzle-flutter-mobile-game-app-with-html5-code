#!/usr/bin/env bash
set -euo pipefail

# Root dir = repo root (script is in store_assets/scripts)
ROOT_DIR="$(cd "$(dirname "$0")"/../.. && pwd)"
SRC_ICON="$ROOT_DIR/app_icons/ios/Icon-App-1024x1024@1x.png"
OUT_DIR="$ROOT_DIR/store_assets/google_play"
APP_DIR="$ROOT_DIR/store_assets/app_store"

mkdir -p "$OUT_DIR" "$APP_DIR"

if [ ! -f "$SRC_ICON" ]; then
  echo "Source icon not found: $SRC_ICON" >&2
  exit 1
fi

echo "Exporting Google Play icon (512×512)…"
sips -Z 512 "$SRC_ICON" --out "$OUT_DIR/icon-512.png" >/dev/null

echo "Copying App Store icon (1024×1024)…"
cp -f "$SRC_ICON" "$APP_DIR/app-icon-1024.png"

echo "Done. Output:"
echo " - $OUT_DIR/icon-512.png"
echo " - $APP_DIR/app-icon-1024.png"

