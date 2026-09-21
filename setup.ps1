# =========================================
# AELC - Global Installation
# DATA-GLHF.exe
# =========================================

param(
    [Parameter(Mandatory = $true)]
    [ValidateSet("claude", "codex", "all")]
    [string]$Harness
)

$ErrorActionPreference = "Stop"

# =========================================
# Resolve repository directory
# =========================================

$ProjectRoot = $PSScriptRoot

# =========================================
# Check uv
# =========================================

if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
    Write-Error "uv is not installed."
    exit 1
}

# =========================================
# Check repository configuration
# =========================================

$Pyproject = Join-Path $ProjectRoot "pyproject.toml"

if (-not (Test-Path $Pyproject)) {
    Write-Error "pyproject.toml not found."
    exit 1
}

# =========================================
# Check installation prerequisites
# =========================================

Write-Host ""
Write-Host "Checking installation prerequisites..."
Write-Host ""

uv run --project "$ProjectRoot" aelc install-check --harness "$Harness"

if ($LASTEXITCODE -ne 0) {
    Write-Error "Installation prerequisites failed."
    exit 1
}

# =========================================
# Install AELC CLI globally
# =========================================
Write-Host ""
Write-Host "Installing AELC CLI..."
Write-Host ""

uv tool install "$ProjectRoot"

if ($LASTEXITCODE -ne 0) {
    Write-Error "AELC CLI installation failed."
    exit 1
}

# =========================================
# Deploy harness adapters
# =========================================

Write-Host "Installing AELC harness adapters..."

uv run --project $PSScriptRoot `
    aelc install-harness --harness $Harness

if ($LASTEXITCODE -ne 0) {
    Write-Error "Harness adapter installation failed."
    exit $LASTEXITCODE
}

Write-Host "AELC installation completed."

# =========================================
# Complete installation
# =========================================
Write-Host "Selected harness: $Harness"
Write-Host "Harness adapter deployment: not yet implemented."
Write-Host ""
Write-Host "Run 'aelc --version' to verify the CLI."
Write-Host ""

Write-Host "If the command is not found, run:"
Write-Host "  uv tool update-shell"