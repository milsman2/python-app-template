
# Python App Template

A modern, modular Python application template with robust CI/CD, best practices, and synthwave terminal UI. This project demonstrates clean architecture, packaging, and workflow automation for professional Python development.

## Features
- **Modular Structure**: src layout, clear separation of core, UI, models, and tests
- **Synthwave Terminal UI**: Rich + pyfiglet for beautiful astronomical data display
- **Robust CI/CD**: GitHub Actions for linting, testing, Docker multi-arch builds, Trivy scanning, and releases
- **Best Practices**: Type hints, logging, config management, reusable workflows, DRY code
- **Packaging**: pyproject.toml, src layout, testable modules, versioned releases

## Architecture

```
python-app-template/
├── src/sample_python_app/
│   ├── core/         # Core logic: config, logging, display (thin wrappers)
│   ├── models/       # Data models (Pydantic)
│   ├── ui/           # Terminal UI (synthwave)
│   ├── data_loader/  # Data loader module (API logic)
│   ├── services/     # Service layer (business logic, imports data loader)
│   └── main.py       # Entry point
├── tests/            # Unit tests
├── data/             # Sample data
├── Dockerfile        # Containerization
├── pyproject.toml    # Packaging
├── .github/workflows # CI/CD workflows
```

## Frameworks & Libraries
- **rich**: Terminal formatting and color
- **pyfiglet**: ASCII art for synthwave look
- **pydantic**: Data validation and settings
- **httpx**: HTTP requests
- **pytest**: Testing
- **ruff, black, isort**: Linting and formatting

## CI/CD & Workflows

- **cache-uv-build.yaml**: Caches Python dependencies for fast builds
- **ruff.yaml**: Lints code for style and quality
- **pytest.yaml**: Runs unit tests
- **docker-build-and-scan.yaml**: Multi-arch Docker builds, Trivy vulnerability scan
- **ci-cd.yaml**: Orchestrates all jobs, triggers on push, PR, release, manual
- **release.yaml**: Publishes releases on main/tags

### Docker Build Safety Features
- **Multi-arch builds**: Uses Docker Buildx and QEMU for isolated, reproducible builds across amd64 and arm64
- **Trivy vulnerability scan**: Automated scan for critical/high OS and library vulnerabilities before release
- **Buildx isolation**: Ensures builds are run in a clean environment, reducing risk of contamination
- **Secrets management**: DockerHub credentials and other secrets are handled securely via GitHub Actions
- **Minimal base image**: Dockerfile uses slim Python base for reduced attack surface
- **No root user**: (Recommended) Run containers as non-root for extra safety (customize Dockerfile as needed)

## Python Best Practices
- **src layout**: Prevents import shadowing, enables clean packaging
- **pyproject.toml**: Modern build system, dependency management
- **Type hints**: Static analysis, clarity
- **Logging**: Traceability for inputs, API calls, UI rendering
- **Modularization**: UI logic in dedicated module, core as thin wrappers, data loader and service layer separated for clarity and maintainability
- **Testing**: pytest for unit and integration tests
- **CI/CD**: Automated lint, test, build, scan, release
- **Multi-arch Docker**: Builds for amd64 and arm64

## Getting Started
1. Clone the repo
2. Install dependencies: `uv sync`
3. Run tests: `uv run pytest`
4. Run app: `uv run src/sample_python_app/main.py`
	- Data loading and business logic are now handled via the service layer and data_loader module
5. Build Docker: `docker build -t python-app-template .`

## Contributing
- Follow PEP8 and use ruff, black, isort
- Write tests for new features
- Use modular, reusable workflows

## License
MIT

---
This template is ideal for modern Python apps with clean architecture, robust automation, and beautiful terminal UI.
