#!/bin/bash
set -euo pipefail

# Only needed in Claude Code on the web containers
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

# Install the Codex CLI if it isn't already present
if ! command -v codex >/dev/null 2>&1; then
  npm install -g @openai/codex
fi

# Restore the Codex login from the CODEX_AUTH_JSON_B64 environment secret.
# The secret is the base64-encoded contents of ~/.codex/auth.json.
if [ -n "${CODEX_AUTH_JSON_B64:-}" ] && [ ! -s "$HOME/.codex/auth.json" ]; then
  mkdir -p "$HOME/.codex"
  # Decode into a private temp file and rename into place only on success,
  # so a failed decode can never leave a partial or world-readable auth.json
  tmp="$(mktemp "$HOME/.codex/.auth.json.XXXXXX")"
  chmod 600 "$tmp"
  # A decode can succeed on a truncated secret, so also verify the result
  # is valid JSON with the credential fields Codex expects
  if printf '%s' "$CODEX_AUTH_JSON_B64" | base64 -d > "$tmp" 2>/dev/null \
    && node -e '
      const a = JSON.parse(require("fs").readFileSync(process.argv[1], "utf8"));
      if (!(a.tokens && a.tokens.refresh_token) && !a.OPENAI_API_KEY) process.exit(1);
    ' "$tmp" 2>/dev/null; then
    mv "$tmp" "$HOME/.codex/auth.json"
    echo "Codex login restored from CODEX_AUTH_JSON_B64"
  else
    rm -f "$tmp"
    echo "Warning: CODEX_AUTH_JSON_B64 is not a valid Codex auth file; run /codex:setup to log in" >&2
  fi
fi
