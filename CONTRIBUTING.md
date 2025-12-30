# Contributing to UnicodeHexMono

Thank you for your interest in contributing to UnicodeHexMono! This document provides guidelines for contributing to the project.

## 🌟 Ways to Contribute

- **Report Bugs**: Found an issue? Open a [GitHub Issue](https://github.com/Pratnomenis/unicode-hex-mono/issues)
- **Suggest Features**: Have an idea? Share it via Issues
- **Improve Documentation**: Fix typos, clarify instructions, add examples
- **Optimize Code**: Improve font generation performance or code quality
- **Add Tests**: Help expand test coverage

## 🐛 Reporting Bugs

When reporting bugs, please include:

1. **Clear description** of the issue
2. **Steps to reproduce** the problem
3. **Expected behavior** vs actual behavior
4. **Environment details**:
   - OS (macOS, Linux, Windows)
   - FontForge version (`fontforge --version`)
   - Python version (`python3 --version`)
5. **Screenshots** if applicable

## 💡 Suggesting Features

For feature requests, please:

1. Check if it's already been suggested in [Issues](https://github.com/Pratnomenis/unicode-hex-mono/issues)
2. Explain the **use case** - why is this needed?
3. Provide **examples** of how it would work
4. Consider **implementation complexity**

## 🔧 Development Setup

### Prerequisites

```bash
# Install FontForge
brew install fontforge  # macOS
# or see https://fontforge.org/en-US/downloads/ for other platforms

# Install Python dependencies for WOFF2 generation
pip3 install --break-system-packages fonttools brotli
```

### Troubleshooting

#### "fonttools not installed" warning despite installation

**Problem**: FontForge shows "⚠ fonttools not installed" even after running `pip3 install fonttools brotli`.

**Cause**: FontForge uses its own embedded Python interpreter (often different from system Python). When you install packages with `pip3`, they go to your system Python, not FontForge's Python.

**Solution**: Check FontForge's Python version and install for that specific version:

```bash
# 1. Check which Python version FontForge uses
fontforge -script -c "import sys; print(sys.version)"
# Example output: 3.14.2 (main, Dec  5 2025, ...)

# 2. Install fonttools for that specific Python version
python3.14 -m pip install --break-system-packages fonttools brotli

# If the python3.X command doesn't exist, try:
# /opt/homebrew/bin/python3.14 -m pip install --break-system-packages fonttools brotli
```

**Verification**: Run generation again - WOFF2 files should now be created without warnings.

### Clone and Build

```bash
# Fork the repository on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/unicode-hex-mono.git
cd unicode-hex-mono

# Generate fonts
fontforge -script main.py

# Test in browser
python3 -m http.server 8080
# Visit http://localhost:8080/index.html
```

## 📝 Code Style

- **Python**: Follow PEP 8 conventions
- **Comments**: Add docstrings to functions explaining purpose and parameters
- **Configuration**: Use `config.py` constants, avoid magic numbers
- **Modularity**: Keep functions focused and reusable

## 🧪 Testing

Before submitting changes:

```bash
# Quick test with sample glyphs
fontforge -script test.py

# Full generation (5-10 minutes)
fontforge -script main.py

# Verify fonts load in browser
python3 -m http.server 8080
```

Check the browser console for any OTS parsing errors or font loading issues.

## 📤 Submitting Changes

1. **Fork** the repository
2. **Create a branch** for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes** with clear, descriptive commits:
   ```bash
   git commit -m "feat: add support for custom glyph styling"
   ```
4. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Open a Pull Request** on GitHub with:
   - Clear description of changes
   - Reference any related issues
   - Screenshots/examples if applicable

## 🎯 Commit Message Convention

We use conventional commits for clarity:

- `feat:` - New feature
- `fix:` - Bug fix
- `docs:` - Documentation changes
- `style:` - Code style changes (formatting, no logic change)
- `refactor:` - Code refactoring
- `perf:` - Performance improvements
- `test:` - Adding or updating tests
- `chore:` - Maintenance tasks

Examples:
```
feat: add support for custom corner radius per plane
fix: correct hex digit 'A' rendering issue
docs: update installation instructions for Linux
```

## 📋 Project Structure

Understanding the codebase:

```
unicode-hex-mono/
├── main.py              # Entry point
├── generator.py         # Font generation engine
├── config.py           # Configuration constants
├── utils.py            # Drawing primitives
├── glyphs.py           # Glyph creation logic
├── css_generator.py    # CSS generation
├── test.py             # Quick testing script
├── index.html          # Browser demo
└── dist/               # Generated fonts (git tracked)
```

## 🤝 Code Review Process

1. Maintainers will review your PR
2. Address any feedback or requested changes
3. Once approved, changes will be merged
4. Your contribution will be credited in the release notes

## 📜 License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).

## 💬 Questions?

- Open a [GitHub Discussion](https://github.com/Pratnomenis/unicode-hex-mono/discussions)
- Or create an [Issue](https://github.com/Pratnomenis/unicode-hex-mono/issues) with the "question" label

---

**Thank you for contributing to UnicodeHexMono!** 🎉
