#!/usr/bin/env bash
# ---------------------------------------------------------------------------
# install_hooks.sh — Install Braze Docs git hooks from .github/hooks/
#
# Run once from the repo root after cloning:
#   bash scripts/install_hooks.sh
#
# What it does:
#   Symlinks .github/hooks/pre-commit → .git/hooks/pre-commit
#   so the accessibility pre-commit check runs automatically on every commit.
#
# To uninstall:
#   rm .git/hooks/pre-commit
# ---------------------------------------------------------------------------

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
HOOKS_SRC="$REPO_ROOT/.github/hooks"
HOOKS_DEST="$REPO_ROOT/.git/hooks"

if [[ ! -d "$HOOKS_SRC" ]]; then
  echo "❌  .github/hooks/ not found. Run this script from the repo root."
  exit 1
fi

mkdir -p "$HOOKS_DEST"

installed=0
skipped=0

for src in "$HOOKS_SRC"/*; do
  hook_name="$(basename "$src")"
  dest="$HOOKS_DEST/$hook_name"

  if [[ -e "$dest" && ! -L "$dest" ]]; then
    echo "⚠️  $dest already exists and is not a symlink — skipping (remove it manually if you want to replace it)"
    ((skipped++)) || true
    continue
  fi

  ln -sf "$src" "$dest"
  echo "✅  Installed $hook_name → $dest"
  ((installed++)) || true
done

echo ""
if [[ $installed -gt 0 ]]; then
  echo "Installed $installed hook(s). They will run automatically on every commit."
fi
if [[ $skipped -gt 0 ]]; then
  echo "Skipped $skipped hook(s) that already exist as non-symlinks."
fi
echo ""
echo "To skip a check in an emergency:  SKIP_A11Y=1 git commit"
echo "To uninstall:                      rm .git/hooks/pre-commit"
