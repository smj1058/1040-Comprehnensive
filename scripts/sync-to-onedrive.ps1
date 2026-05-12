# Sync dossier .html files from this repo to the OneDrive shared folder.
# Run this once on your Windows laptop after pulling the latest changes.
# It will:
#   1. Verify you're in the repo root
#   2. Copy every dossiers/<Client>/dossier.html to the OneDrive Dossier Files folder
#   3. Preserve per-client subfolder structure
#   4. Copy docs/PROJECT_OVERVIEW.md and docs/HANDOFF_2026-04-22.md too
#   5. Report what was copied

# === CONFIG ===
$ONEDRIVE_TARGET = "C:\Users\SethJohnson\OneDrive - Subledge\_Client Review\Dossier Files"
$REPO_DOSSIERS = ".\dossiers"
$REPO_DOCS = ".\docs"

# === SAFETY ===
if (-not (Test-Path -Path $REPO_DOSSIERS)) {
    Write-Host "ERROR: '$REPO_DOSSIERS' not found." -ForegroundColor Red
    Write-Host "Please run this script from the root of the 1040-Comprehnensive repo." -ForegroundColor Red
    Write-Host "Current directory: $(Get-Location)" -ForegroundColor Yellow
    exit 1
}

if (-not (Test-Path -Path $ONEDRIVE_TARGET)) {
    Write-Host "Target folder does not exist. Creating: $ONEDRIVE_TARGET" -ForegroundColor Yellow
    New-Item -ItemType Directory -Path $ONEDRIVE_TARGET -Force | Out-Null
}

Write-Host ""
Write-Host "=== Syncing dossier HTML files to OneDrive ===" -ForegroundColor Cyan
Write-Host "Source: $REPO_DOSSIERS"
Write-Host "Target: $ONEDRIVE_TARGET"
Write-Host ""

$count = 0
$skipped = 0

# Copy each client's dossier.html into a matching subfolder
Get-ChildItem -Path $REPO_DOSSIERS -Directory | ForEach-Object {
    $clientName = $_.Name
    $sourceHtml = Join-Path $_.FullName "dossier.html"
    $sourceMd = Join-Path $_.FullName "dossier.md"
    $sourceState = Join-Path $_.FullName "state.json"

    if (Test-Path $sourceHtml) {
        $targetDir = Join-Path $ONEDRIVE_TARGET $clientName
        if (-not (Test-Path $targetDir)) {
            New-Item -ItemType Directory -Path $targetDir -Force | Out-Null
        }

        # Copy HTML (primary deliverable for team viewing)
        Copy-Item -Path $sourceHtml -Destination (Join-Path $targetDir "dossier.html") -Force
        # Copy markdown source for archival
        if (Test-Path $sourceMd) { Copy-Item -Path $sourceMd -Destination (Join-Path $targetDir "dossier.md") -Force }
        # Copy state.json
        if (Test-Path $sourceState) { Copy-Item -Path $sourceState -Destination (Join-Path $targetDir "state.json") -Force }

        Write-Host "  ✓ $clientName" -ForegroundColor Green
        $count++
    } else {
        Write-Host "  - $clientName (no dossier.html)" -ForegroundColor Gray
        $skipped++
    }
}

# Copy project-level docs to OneDrive root
Write-Host ""
Write-Host "=== Copying project-level docs to OneDrive root ===" -ForegroundColor Cyan
$projectDocs = @("PROJECT_OVERVIEW.md", "HANDOFF_2026-04-22.md", "BATCH_REFRESH_PROMPT.md")
foreach ($doc in $projectDocs) {
    $sourceDoc = Join-Path $REPO_DOCS $doc
    if (Test-Path $sourceDoc) {
        Copy-Item -Path $sourceDoc -Destination (Join-Path $ONEDRIVE_TARGET $doc) -Force
        Write-Host "  ✓ $doc" -ForegroundColor Green
    }
}

Write-Host ""
Write-Host "=== Done ===" -ForegroundColor Cyan
Write-Host "Copied dossiers for $count clients." -ForegroundColor Green
if ($skipped -gt 0) {
    Write-Host "Skipped $skipped folders (no dossier.html present)." -ForegroundColor Yellow
}
Write-Host ""
Write-Host "OneDrive will sync these to the cloud automatically." -ForegroundColor Cyan
Write-Host "Right-click the 'Dossier Files' folder in OneDrive → Share → set team permissions." -ForegroundColor Cyan
Write-Host ""
Read-Host "Press Enter to close"
