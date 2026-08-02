from pathlib import Path

APP_DIR = Path("app")

MODULES = [
    "api",
    "agents",
    "core",
    "database",
    "domain",
    "services",
    "workflow",
    "providers",
    "integrations",
    "schemas",
    "models",
    "middleware",
    "security",
    "events",
    "utils",
    "prompts",
]

for module in MODULES:
    path = APP_DIR / module
    path.mkdir(parents=True, exist_ok=True)
    (path / "__init__.py").touch(exist_ok=True)
    print(f"✅ Created: {path}")

print("\n🎉 Step 2 completed successfully!")
