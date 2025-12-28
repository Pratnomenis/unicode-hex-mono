# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-12-28

### 🎉 Initial Release

Complete Unicode font with hexadecimal codepoint display for debugging and fallback purposes.

### Added

#### Core Features
- **Complete Unicode coverage** - All 1,111,998 valid codepoints (U+0000 to U+10FFFD)
- **Hexadecimal display** - Each glyph shows its codepoint in hex format
- **Multi-format support** - Both OTF and WOFF2 formats generated
- **19 font files** - Split architecture to handle OpenType's 65,535 glyph limit
- **Automatic CSS generation** - `font.css` with optimized `@font-face` rules

#### Visual Design
- **2×2 grid layout** for BMP characters (U+0000-U+FFFF)
- **Split layout** for Supplementary Planes 1-15 (U+10000-U+FFFFF) with large plane digit
- **Filled squares** for Plane 16 (U+100000-U+10FFFD) with vertical separator
- **Diagonal X** for replacement character (U+FFFD) and NULL (U+0000)
- **Rounded corners** - 70 units for most planes, 120 units for Plane 16
- **Monospaced design** - 1000 EM unit width for consistent alignment

#### Technical Implementation
- **Modular Python architecture**:
  - `main.py` - Entry point
  - `generator.py` - Font generation engine
  - `config.py` - Configuration constants
  - `utils.py` - Drawing primitives
  - `glyphs.py` - Glyph creation logic
  - `css_generator.py` - CSS generation
- **3×5 pixel grid rendering** for hex digits (0-9, A-F)
- **Proper codepoint exclusions**:
  - Surrogate pairs (U+D800-U+DFFF)
  - Non-characters ending in FFFE/FFFF
  - Reserved non-characters (U+FDD0-U+FDEF)

#### Performance Optimizations
- **WOFF2 compression** - 97.6% smaller than OTF (10 MB vs 414 MB)
- **Unicode-range optimization** - Browser loads only needed fonts
- **Font-display swap** - Immediate text visibility with fallback
- **Lazy loading** - On-demand font file loading

#### Distribution
- **NPM package** published as `unicode-hex-mono`
- **GitHub repository** at https://github.com/Pratnomenis/unicode-hex-mono
- **MIT License** for open source use
- **38 font files included** (19 ranges × 2 formats)

#### Documentation
- **Comprehensive README.md** with installation and usage instructions
- **Visual examples** showing glyph formats and debugging use cases
- **HISTORY.md** with detailed development log
- **CONTRIBUTING.md** with contribution guidelines
- **Interactive demo** (`index.html`) with 4 tabbed screens:
  - Info tab with documentation
  - Text testing with configurable display
  - Virtual scrolling glyph list
  - Test cases for all hex digit combinations

### Technical Specifications

- **Package size**: 24.6 MB compressed, 416.1 MB unpacked
- **Total coverage**: 1,111,998 valid Unicode codepoints
- **Generation time**: ~5-10 minutes for all fonts
- **Browser compatibility**: All modern browsers supporting WOFF2/OTF

---

## Version History

### Planned for Future Releases

**v1.1.0** (Future)
- Potential customization options for glyph styling
- Additional font weight variants
- Performance optimizations for generation speed

**Suggestions welcome!** Open an [issue](https://github.com/Pratnomenis/unicode-hex-mono/issues) with ideas.

---

[1.0.0]: https://github.com/Pratnomenis/unicode-hex-mono/releases/tag/v1.0.0
