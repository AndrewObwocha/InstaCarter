set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

cd "$PROJECT_ROOT"

if [[ ! -d "venv" ]]; then
	echo "Virtual environment not found. Run: make setup"
	exit 1
fi

. venv/bin/activate 

cat >> logs/test_instacart.log << EOF

================================================================================
TEST RUN: $(date '+%Y-%m-%d %H:%M:%S')
================================================================================

EOF

python tests/config_test.py >> logs/test_instacart.log 2>&1