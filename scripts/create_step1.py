from pathlib import Path

# =====================================================
# Step 1 - Create Project Root Structure
# =====================================================

PROJECT_NAME = "secgenie-ai"

ROOT_FOLDERS = [
    "app",
    "docs",
    "tests",
    "deployment",
    "scripts",
    "data",
    "logs",
    "tmp",
]

root = Path(PROJECT_NAME)

print(f"Creating project: {PROJECT_NAME}")

root.mkdir(exist_ok=True)

for folder in ROOT_FOLDERS:
    path = root / folder
    path.mkdir(parents=True, exist_ok=True)
    print(f"Created: {path}")

print("\n✅ Step 1 completed successfully.")