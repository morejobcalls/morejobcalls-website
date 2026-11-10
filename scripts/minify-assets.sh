#!/bin/sh
# Rebuild minified CSS from the readable sources. Edit assets/*.src.css, then run this.
# Needs Node (uses npx esbuild). Commit both the .src.css and the generated .css.
set -e
cd "$(dirname "$0")/.."
npx --yes esbuild assets/mjc.src.css --minify --outfile=assets/mjc.css
npx --yes esbuild assets/wins.src.css --minify --outfile=assets/wins.css
