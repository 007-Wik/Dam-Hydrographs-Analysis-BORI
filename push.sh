#!/usr/bin/env bash
# =============================================================================
# push.sh
# Kurnur (BORI) Dam – Git Commit & Push to GitHub
#
# Usage:
#   cd /workspaces/Dam-Hydrographs-Analysis-BORI
#   bash push.sh
#
# Optional – pass a custom commit message:
#   bash push.sh "feat: add overtopping interactive figure"
#
# Requirements:
#   • git must be configured (name + email)
#   • Remote 'origin' must point to your GitHub repo
#   • You must be authenticated (gh auth login, or SSH key set up)
# =============================================================================

set -euo pipefail

GREEN='\033[0;32m'; BLUE='\033[0;34m'; YELLOW='\033[1;33m'; RED='\033[0;31m'; BOLD='\033[1m'; NC='\033[0m'
info()    { echo -e "${BLUE}[INFO]${NC}  $*"; }
success() { echo -e "${GREEN}[OK]${NC}    $*"; }
warn()    { echo -e "${YELLOW}[WARN]${NC}  $*"; }
error()   { echo -e "${RED}[ERROR]${NC} $*"; exit 1; }
banner()  { echo -e "\n${BOLD}$*${NC}\n"; }

# ── Resolve repo root ─────────────────────────────────────────────────────────
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO_ROOT"

banner "================================================================="
banner "  BORI DAM – Git Commit & Push"
banner "  Kurnur (BORI) Dam · Solapur · Maharashtra"
banner "================================================================="

# ── Custom commit message (optional arg) ──────────────────────────────────────
COMMIT_MSG="${1:-"feat: world-class repository – CWC/GOV submission ready (v2.0.0)"}"
info "Commit message: \"$COMMIT_MSG\""

# ── Preflight checks ──────────────────────────────────────────────────────────
banner "STEP 1 – Preflight checks"

# Git installed?
command -v git &>/dev/null || error "git not found. Install git first."
success "git found: $(git --version)"

# Inside a git repo?
git rev-parse --git-dir &>/dev/null || error "Not inside a git repository. Run: git init"
success "Git repository detected."

# Remote set?
if ! git remote get-url origin &>/dev/null; then
    error "No remote 'origin' configured. Run:\n  git remote add origin https://github.com/<your-username>/Dam-Hydrographs-Analysis-BORI.git"
fi
REMOTE_URL=$(git remote get-url origin)
success "Remote origin: $REMOTE_URL"

# Git user configured?
GIT_USER=$(git config user.name  2>/dev/null || echo "")
GIT_EMAIL=$(git config user.email 2>/dev/null || echo "")
if [[ -z "$GIT_USER" || -z "$GIT_EMAIL" ]]; then
    warn "Git user not fully configured. Setting defaults..."
    git config user.name  "${GIT_USER:-"Satwik Udupi"}"
    git config user.email "${GIT_EMAIL:-"your@email.com"}"
    warn "Update these with:  git config user.name 'Your Name'"
fi
success "Git user: $(git config user.name) <$(git config user.email)>"

# ── Checksums: regenerate if data changed ─────────────────────────────────────
banner "STEP 2 – Data integrity"
if ls data/raw/*.xlsx 1>/dev/null 2>&1; then
    sha256sum data/raw/*.xlsx > data/metadata/checksums.sha256
    success "SHA-256 checksums refreshed."
    cat data/metadata/checksums.sha256
else
    warn "No .xlsx files in data/raw/ — checksums not generated."
fi

# ── Show what will be committed ───────────────────────────────────────────────
banner "STEP 3 – Staging all files"
git add -A
echo ""
info "Files staged for commit:"
git status --short
echo ""

# Count staged files
N_STAGED=$(git diff --cached --name-only | wc -l | tr -d ' ')
if [[ "$N_STAGED" -eq 0 ]]; then
    warn "Nothing to commit — working tree is clean."
    exit 0
fi
info "$N_STAGED file(s) staged."

# ── Commit ────────────────────────────────────────────────────────────────────
banner "STEP 4 – Committing"
git commit -m "$COMMIT_MSG"
success "Committed: $COMMIT_MSG"

# ── Determine branch ──────────────────────────────────────────────────────────
BRANCH=$(git rev-parse --abbrev-ref HEAD)
info "Branch: $BRANCH"

# ── Push ──────────────────────────────────────────────────────────────────────
banner "STEP 5 – Pushing to origin/$BRANCH"
git push -u origin "$BRANCH"
success "Pushed to origin/$BRANCH"

# ── Summary ───────────────────────────────────────────────────────────────────
echo ""
echo -e "${GREEN}=================================================================${NC}"
echo -e "${GREEN}  PUSH COMPLETE${NC}"
echo -e "${GREEN}=================================================================${NC}"
echo ""
info "Repository: $REMOTE_URL"
info "Branch:     $BRANCH"
info "Commit:     $(git log -1 --pretty='%h – %s')"
echo ""
echo -e "${BOLD}Next steps:${NC}"
echo "  1. Visit your GitHub repo and verify all files are present"
echo "  2. Check the Actions tab — CI workflow will run automatically"
echo "  3. Add a release tag when ready for GOV submission:"
echo "     git tag -a v2.0.0 -m 'GOV/CWC submission release'"
echo "     git push origin v2.0.0"
echo ""
