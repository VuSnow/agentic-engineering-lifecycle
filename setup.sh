#!/usr/bin/env bash
# =========================================
# AELC - Global Installation
# DATA-GLHF.exe
# =========================================
set -euo pipefail

# =========================================
# Resolve repository directory
# =========================================
SCRIPT_DIR="$(
    cd "$(dirname "${BASH_SOURCE[0]}")" && pwd
)"

# =========================================
# Display usage information
# =========================================

print_usage() {
    cat <<EOF
AELC - Agentic Engineering Lifecycle

Usage:
  ./setup.sh --harness <name>

Supported harnesses:
  claude
  codex
  all

Examples:
  ./setup.sh --harness claude
  ./setup.sh --harness codex
  ./setup.sh --harness all
EOF
}

# =========================================
# Parse command-line arguments
# =========================================

HARNESS=""

while [[ $# -gt 0 ]]; do
    case "$1" in

        --harness)
            if [[ $# -lt 2 ]]; then
                echo "Error: Missing harness value." >&2
                print_usage
                exit 1
            fi

            HARNESS="$2"
            shift 2
            ;;

        -h|--help)
            print_usage
            exit 0
            ;;

        *)
            echo "Error: Unknown argument: $1" >&2
            print_usage
            exit 1
            ;;

    esac
done

# =========================================
# Validate harness selection
# =========================================

case "$HARNESS" in
    claude|codex|all)
        ;;
    *)
        echo "Error: Invalid harness selection." >&2
        print_usage
        exit 1
        ;;
esac

# =========================================
# Check uv
# =========================================

if ! command -v uv >/dev/null 2>&1; then
    echo "Error: uv is not installed." >&2
    echo "Please install uv before continuing." >&2
    exit 1
fi

# =========================================
# Check repository configuration
# =========================================

if [[ ! -f "$SCRIPT_DIR/pyproject.toml" ]]; then
    echo "Error: pyproject.toml not found." >&2
    exit 1
fi

# =========================================
# Check installation prerequisites
# =========================================

echo ""
echo "Checking installation prerequisites..."
echo ""
uv run \
    --project "$SCRIPT_DIR" \
    aelc install-check \
    --harness "$HARNESS"


# =========================================
# Install AELC CLI globally
# =========================================

echo ""
echo "Installing AELC CLI..."
echo ""
uv tool install "$SCRIPT_DIR"

# =========================================
# Complete installation
# =========================================

echo ""
echo "AELC CLI installation completed."
echo ""

echo "Selected harness: $HARNESS"
echo "Harness adapter deployment: not yet implemented."
echo ""

echo "Run 'aelc --version' to verify the CLI."
echo ""

echo "If the command is not found, run:"
echo "  uv tool update-shell"
echo ""