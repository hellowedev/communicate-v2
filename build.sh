#!/usr/bin/env bash
set -o errexit  # Stop on any error
set -o pipefail # Propagate errors in pipelines
set -o nounset  # Treat unset variables as errors

echo "🔧 [1/5] Cleaning old static files and manifest..."
rm -rf staticfiles staticfiles.json

echo "🚀 [2/5] Upgrading setuptools and wheel..."
pip install --upgrade setuptools wheel

echo "📦 [3/5] Installing Python dependencies..."
pip install -r requirements.txt

echo "📂 [4/5] Collecting static files..."
python manage.py collectstatic --no-input --verbosity 2

# Confirm tailwindcss file present
if [ ! -f static/css/tailwind_style_output.css ]; then
  echo "❌ Tailwind CSS output missing! Exiting..."
  exit 1
else
  echo "✅ Tailwind CSS built successfully."
fi

# Confirm it's in the collected files
if [ ! -f staticfiles/css/tailwind_style_output.css ]; then
  echo "❌ File was not collected! Check STATICFILES_DIRS and naming!"
  exit 1
else
  echo "✅ File collected successfully."
fi

echo "🗃️ [5/5] Running database migrations..."
python manage.py migrate

echo "🎉 Build complete. All systems go!"
