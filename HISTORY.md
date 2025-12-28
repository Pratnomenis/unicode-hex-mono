# UnicodeHexMono - Full Unicode Support

## Overview

The UnicodeHexMono font generator creates a complete monospaced font covering **all Unicode characters** (U+0000 to U+10FFFD) by generating **19 separate font files in both OTF and WOFF2 formats**, each covering a specific Unicode range. Each glyph displays its hexadecimal codepoint in a 2x2 grid inside a rounded square.

## Quick Start

```bash
# Generate fonts (requires FontForge)
# This will create 19 font files in two formats (OTF + WOFF2) AND font.css automatically
fontforge -script main.py

# Test in browser
python3 -m http.server 8080
# Then open http://localhost:8080/index.html
```

## NPM Package Usage

### Installation

```bash
# Using npm
npm install unicode-hex-mono

# Using yarn
yarn add unicode-hex-mono

# Using pnpm
pnpm add unicode-hex-mono
```

### Usage

The font is designed to be used as a **fallback font** in your CSS font stack. When your primary font doesn't have a glyph for a character, UnicodeHexMono will display the character's hexadecimal codepoint.

#### Option 1: CSS Import (Recommended)

```css
/* Import the pre-generated CSS with all @font-face declarations */
@import 'unicode-hex-mono/dist/font.css';

/* Use as a backup font in your CSS */
body {
  font-family: 'Your Primary Font', 'UnicodeHexMono', monospace;
}
```

#### Option 2: HTML Link Tag

```html
<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="node_modules/unicode-hex-mono/dist/font.css">
  <style>
    body {
      font-family: 'Inter', 'UnicodeHexMono', monospace;
    }
  </style>
</head>
<body>
  <!-- Your content here -->
</body>
</html>
```

#### Option 3: Modern Bundlers (Webpack, Vite, Parcel)

```javascript
// Import CSS in your JavaScript entry point
import 'unicode-hex-mono/dist/font.css';
```

```css
/* Then use in your CSS */
.debug-text {
  font-family: 'UnicodeHexMono', monospace;
}
```

### Package Contents

- **38 font files**: 19 ranges × 2 formats (`.otf` + `.woff2`)
- **1 CSS file**: `font.css` with all `@font-face` declarations
- **Total size**: ~414 MB OTF + ~10 MB WOFF2 unpacked (WOFF2 97.6% smaller!)

**Note**: The browser will automatically load only the font files needed for the characters displayed on your page, thanks to CSS `unicode-range` optimization. WOFF2 format is prioritized for dramatically better compression (40× smaller) and faster loading.

### When to Use

- **Debugging**: Identify mystery characters by their codepoint
- **Development**: See invisible characters (zero-width spaces, RTL marks, etc.)
- **Internationalization**: Detect missing glyphs in your primary font
- **Code editors**: Fallback for rare Unicode symbols


## Current Status: ✅ COMPLETE

**Architecture**: Modular design with 5 specialized Python files for maintainability

**Latest Updates**:
- ✅ **NEW (Dec 28, 2025)**: **WOFF2 format support** - All fonts now generated in both OTF and WOFF2 formats
  - WOFF2 provides incredible 97.6% compression (414MB → 10MB!)
  - Uses `fonttools` library for WOFF2 conversion (FontForge's WOFF2 generation was broken)
  - CSS automatically uses WOFF2 with OTF fallback for maximum browser compatibility
  - Dramatically faster page loads thanks to 40× smaller file sizes
  - Generator creates both formats automatically: 38 total files (19 ranges × 2 formats)
  - **Requires**: `pip3 install --break-system-packages fonttools brotli`
- ✅ **NEW (Dec 28, 2025)**: **NPM package ready for distribution** 🎉
  - Created `package.json` with best practices for font distribution
  - Package name: `unicode-hex-mono` (24.6 MB compressed, 416.1 MB unpacked)
  - Includes 38 production font files (19 ranges × 2 formats: OTF + WOFF2), excludes development/test files
  - MIT License added
  - Comprehensive npm usage documentation in README
  - Local installation verified successfully
  - Ready to publish with `npm publish`
- ✅ **NEW (Dec 28, 2025)**: **Automatic CSS generation + index.html refactoring** - Production-ready npm distribution
  - New `css_generator.py` module scans dist/ folder and creates font.css automatically
  - Runs automatically after font generation (integrated into `main.py`)
  - Includes all 19 @font-face rules with proper unicode-range selectors
  - Uses font-display: swap for optimal performance
  - **index.html refactored**: Now uses standard `<link rel="stylesheet" href="dist/font.css">` instead of JavaScript-based font loading
  - Eliminated 47 lines of complex JavaScript (removed `loadMainFonts()` function)
  - Better performance, easier debugging, follows web standards
  - Ready for npm package distribution
- ✅ **NEW (Dec 27, 2025)**: **Code grooming completed** - production-ready codebase
  - Removed 2 dead code functions from `glyphs.py`
  - Added 5 configuration constants to eliminate all hardcoded magic numbers
  - Added comprehensive module docstrings to all 5 modules
  - Created `create_notdef_glyph()` helper function for cleaner API
  - Removed sys.path hack from `test.py`
  - Added section comments for better code organization
  - Result: Clean, professional, maintainable codebase with no magic numbers
- ✅ **NEW (Dec 27, 2025)**: **Plane 16 more rounded corners** - increased corner radius from 70 to 120 units (71% increase)
  - **Critical bug fix**: Fixed `draw_rounded_square()` in `utils.py` that was ignoring radius parameter
  - Added cache busting for instant font reload during development
- ✅ **NEW (Dec 27, 2025)**: **Plane 16 vertical line** - changed from horizontal to vertical line in middle for better visual distinction
- ✅ **NEW (Dec 27, 2025)**: **Solid hex digits** - removed gaps between pixels for better readability (no longer pixelated)
- ✅ **NEW (Dec 27, 2025)**: **Increased hex digit sizes 37%** (190→260 units) - much better visibility, recommended minimum 20px+
- ✅ **NEW (Dec 27, 2025)**: U+FFFD (replacement character) displays with **diagonal X** - solves U+0000 distinction (browser forces NULL→U+FFFD)
- ✅ **NEW (Dec 27, 2025)**: Simplified implementation - removed empty square logic, only U+FFFD gets special rendering
- ✅ **NEW (Dec 27, 2025)**: Fixed broken hex digits '2' and 'A' - all digits now render correctly with proper shapes
- ✅ **NEW (Dec 27, 2025)**: Hex digits now use 3x5 pixel grid rendering for cleaner, more consistent appearance
- ✅ Unified rendering: All hex digits (0-9, A-F) rendered as bitmap-style 3×5 grid patterns
- ✅ 5-digit split layout for supplementary planes (U+10000-U+FFFFF) with larger plane digit indicator (290 units)
- ✅ Modular refactoring: Split `generate.py` into `main.py`, `generator.py`, `config.py`, `utils.py`, `glyphs.py`
- ✅ Full Unicode coverage with proper glyph rendering
- ✅ Hex code display for BMP (2x2 grid) and supplementary planes (split layout)
- ✅ Multi-file OTF generation (19 files)

**Issue Resolved**: The test page was showing a console error: `OTS parsing error: cmap: Out of order end range (65535 <= 65535)`

**Root Cause**: The font generator was including Unicode non-characters (U+FFFE, U+FFFF, and similar codepoints ending in FFFE/FFFF for each plane) which caused invalid cmap table entries.

**Solution**: Updated `utils.py` (called by `main.py`) to exclude all Unicode non-characters:
- Codepoints ending in FFFE or FFFF (e.g., U+FFFF, U+1FFFF, U+2FFFF, etc.)
- Arabic Presentation Forms-B non-characters (U+FDD0 to U+FDEF)

**Result**: 
- ✅ OTS parsing error is resolved
- ✅ All 19 font files successfully generated
- ✅ Fonts load properly in the browser
- ✅ Total valid codepoints: 1,111,998

### Generation Complete
- **Files Generated**: 38 files (19 ranges × 2 formats: OTF + WOFF2) ✅
  - OTF files: ~414 MB total (full compatibility)
  - WOFF2 files: ~10 MB total (97.6% compression!)
  - Browsers automatically use WOFF2 when available
- **Coverage**: Full Unicode (U+00000 to U+10FFFD, excluding non-characters)

---

## Why Multiple Files?

The OpenType/TrueType format has a **hard limit of 65,535 glyphs** per file. Since the full Unicode range contains over 1 million codepoints, we need to split them across multiple font files.

**Solution**: Generate 19 separate `.otf` files, each containing ~60,000 glyphs

---

## Generated Files

Each font file is named with its Unicode range:

```
dist/UnicodeHexMono_00000_0F25F.otf     (U+00000 - U+0F25F)  
dist/UnicodeHexMono_00000_0F25F.woff2   (U+00000 - U+0F25F)  
dist/UnicodeHexMono_0F260_1DCE1.otf     (U+0F260 - U+1DCE1)
dist/UnicodeHexMono_0F260_1DCE1.woff2   (U+0F260 - U+1DCE1)
...
dist/UnicodeHexMono_108302_10FFFD.otf   (U+108302 - U+10FFFD)
dist/UnicodeHexMono_108302_10FFFD.woff2 (U+108302 - U+10FFFD)
```

> **Note**: Ranges exclude Unicode non-characters (codepoints ending in FFFE/FFFF and U+FDD0-U+FDEF) to ensure valid OpenType cmap tables.

---

## Project Structure

The project is organized into multiple Python modules for better maintainability:

**Core Files:**
- **`main.py`**: Entry point script that initiates font generation and CSS generation
- **`generator.py`**: Core font generation logic and multi-file handling
- **`config.py`**: Configuration constants (font metrics, Unicode ranges, etc.)
- **`utils.py`**: Utility functions (codepoint validation, drawing primitives for rounded squares, hex digit rendering with 7-segment and custom outlines)
- **`glyphs.py`**: Glyph creation and rendering logic (2x2 grid layouts, 5-digit split layouts, filled/outlined squares)
- **`css_generator.py`**: Automatic CSS generation for npm distribution (scans .otf files, creates font.css with @font-face declarations)

**Testing & Demo Files:**
- **`test.py`**: Quick test script for generating small sample fonts with comprehensive hex digit testing
- **`index.html`**: Production-ready font showcase application with four tabbed screens:
  - Info tab with comprehensive font documentation
  - Text testing with font mode switcher and size controls
  - Virtual scrolling glyph list viewer (U+0000 - U+10FFFF)
  - Test Cases tab with examples covering all hex digit combinations (0-9, A-F)
  - Dark/light mode theming with system detection
  - **Uses standard CSS loading**: Loads fonts via `<link rel="stylesheet" href="dist/font.css">` (no JavaScript font loading)

**Output:**
- **`dist/`**: Directory containing generated `.otf` font files (19 files for full generation) and `font.css` for npm usage

## How It Works

### 1. Font Generation Pipeline

The font generation follows a modular pipeline:

1. **`main.py`**: Calls `generator.generate_multi_file()` to start the process
2. **`generator.py`**: 
   - Collects all valid Unicode codepoints using `utils.is_valid_codepoint()`
   - Excludes surrogates and non-characters
   - Splits codepoints into chunks of 60,000 glyphs each
   - Creates a separate `.otf` file for each chunk
   - Names each file with its Unicode range (e.g., `UnicodeHexMono_00000_0F25F.otf`)
3. **`glyphs.py`**: 
   - Creates individual glyphs with appropriate rendering based on Unicode range
   - Draws 4-digit hex codes in 2x2 grid for BMP characters (U+0000-U+FFFF)
   - Draws 5-digit hex codes in split layout for supplementary planes 1-15 (U+10000-U+FFFFF)
   - Draws 4-digit hex codes in 2x2 grid inside filled squares for plane 16 (U+100000-U+10FFFD)
4. **`utils.py`**: 
   - Provides drawing primitives for rounded squares
   - Implements vector paths for all hex digits (0-9, A-F)
5. **`css_generator.py`**: 
   - Scans `dist/` folder for all generated `.otf` files
   - Parses Unicode ranges from filenames
   - Generates `font.css` with @font-face declarations for each font file
   - Includes unicode-range selectors for browser optimization
   - Uses `font-display: swap` for better performance

### 2. Font Loading (`index.html`)

The HTML page uses standard CSS loading for optimal performance:

1. **CSS Link in `<head>`**: Loads `dist/font.css` with a simple `<link>` element
   ```html
   <link rel="stylesheet" href="dist/font.css">
   ```

2. **Automatic Browser Optimization**: The CSS file contains 19 `@font-face` declarations with `unicode-range` selectors
   - Browser automatically loads only the font files needed for displayed characters
   - Better performance - no need to load all ~405MB upfront
   - Uses `font-display: swap` for better performance (text visible immediately with fallback fonts)
   - Standard CSS caching applies

3. **No JavaScript Required**: Font loading is handled entirely by the browser via CSS (simpler, faster, more reliable)

### Example of Auto-Generated CSS (`dist/font.css`):

```css
@font-face {
    font-family: 'UnicodeHexMono';
    src: url('./UnicodeHexMono_00000_0F25F.woff2') format('woff2'),
         url('./UnicodeHexMono_00000_0F25F.otf') format('opentype');
    unicode-range: U+00000-0F25F;
    font-display: swap;
}

@font-face {
    font-family: 'UnicodeHexMono';
    src: url('./UnicodeHexMono_0F260_1DCE1.woff2') format('woff2'),
         url('./UnicodeHexMono_0F260_1DCE1.otf') format('opentype');
    unicode-range: U+0F260-1DCE1;
    font-display: swap;
}
/* ... 17 more @font-face rules ... */
```

The browser intelligently loads only the font files needed for the characters actually displayed on the page, automatically preferring WOFF2 for smaller file sizes!

---

## Configuration

Edit [`config.py`](file:///Users/denis.ivanov108/Developer-private/mono-pfont/config.py) to customize font generation parameters:

```python
# Font metadata
FONT_NAME = "UnicodeHexMono"
FONT_FAMILY = "UnicodeHexMono"
FONT_VERSION = "1.0"

# Font metrics
EM_SIZE = 1000
ASCENT = 800
DESCENT = 200

# Glyph design parameters
GLYPH_WIDTH = 1000          # Monospaced width
BOX_SIZE = 700              # Square box dimensions
BOX_STROKE_WIDTH = 40       # Border thickness
CORNER_RADIUS = 70          # Rounded corner radius

# Hex digit display parameters
DIGIT_SIZE = 260            # Size of each hex digit (increased from 190, 37% larger for visibility)
GRID_SPACING = 30           # Spacing between digits in BMP 2x2 grid (increased from 20)
DIGIT_STROKE_WIDTH = 25     # Stroke width for digit paths (Note: actual implementation in utils.py uses calculated proportions, not this constant)

# Unicode ranges
UNICODE_MIN = 0x0000
UNICODE_MAX = 0x10FFFD

# Multi-file configuration
GLYPHS_PER_FILE = 60000     # Glyphs per font file (max 65,535)
OUTPUT_FORMAT = 'otf'       # Output format (only OTF supported)
```

---

## Usage

### Generate Fonts

```bash
fontforge -script main.py
```

This will create 19 `.otf` files in the `dist/` directory.

### Test in Browser

```bash
# Start local server
python3 -m http.server 8080

# Open in browser
open http://localhost:8080/index.html
```

#### NEW: Production-Ready Index.html

The `index.html` file has been completely rebuilt as a comprehensive, enterprise-like single-page application featuring:

**Four Tabbed Screens:**

1. **ℹ️ Info** (Default tab): Comprehensive documentation including:
   - What is UnicodeHexMono and its purpose as a backup font
   - Primary use case: Adding to CSS font-family stack
   - Glyph display formats by Unicode range (BMP, Supplementary Planes, Plane 16, U+FFFD)
   - Edge cases & special behaviors (control characters, excluded codepoints, rendering contexts)
   - Font size recommendations
   - Technical specifications
   - This tab opens by default to immediately educate users about the font's purpose

2. **📝 Text Testing**: Interactive textarea with:
   - Font mode switcher ("Only Font" vs "As Backup")
   - Font size slider (0.5rem - 20rem, step 0.5rem)
   - Real-time preview updates
   - Debugging-focused placeholder with examples of problematic Unicode (zero-width spaces, RTL marks, ancient scripts)

3. **🔤 Glyph List** (Unicode Glyph Explorer):
   - **Full-width design** - Breaks out of container to maximize screen space
   - **Optimized card display** - Shows only one large (4rem) glyph per card
   - **Thin cards (140px min-width)** - Allows 8-12+ cards per row depending on screen size
   - All Unicode symbols from U+0000 to U+10FFFF
   - Performance optimized for 1,112,064 codepoints
   - **Virtual scrolling** - Only renders visible glyphs (~50-100 at a time)
   - **Dynamic warning system** - Shows alert when screen is too narrow to reach all glyphs
   - Smooth 60fps scrolling performance

4. **✅ Test Cases**: Comprehensive test display:
   - Control characters
   - BMP characters (2x2 grid layout)
   - Supplementary planes 1-15 (split layout)
   - Plane 16 (filled squares)
   - Visual verification of all hex digit combinations

**Features:**
- 🎨 **Dark/light mode** - System detection + manual toggle with localStorage persistence
- 📱 **Responsive design** - Mobile-first approach
- ⚡ **Virtual scrolling** - Smooth performance with row-based calculations
- 🎭 **Premium aesthetics** - Vibrant colors and micro-animations
- 🎯 **Zero dependencies** - Pure HTML/CSS/vanilla JavaScript
- 💾 **Single self-contained file** - Everything in one ~78 KB file
- ⚠️ **Smart warnings** - Dynamic feedback when browser limitations prevent full range access
- 🖥️ **Selective full-width** - Only glyph explorer spans full screen width
- 📖 **Info-first design** - Default tab educates users about font purpose and usage

**Technical Highlights:**
- Debounced resize handler (150ms) prevents layout breakage
- Row-aligned virtual scroll positioning eliminates jumping
- Dynamic column calculation adapts to any screen width
- Browser scroll limit detection (~33M pixels)
- Color-scheme support for native scrollbars in dark mode

The browser will automatically load the appropriate font files based on what characters are displayed.

### Quick Testing (Rapid Iteration)

For testing hex digit rendering without regenerating all 19 font files:

```bash
# Generate comprehensive test font (46 test glyphs covering all hex digit combinations)
fontforge -script test.py

# View in browser Test Cases tab
open http://localhost:8080/index.html  # Click on "✅ Test Cases" tab
```

**Test Files:**
- [`test.py`](file:///Users/denis.ivanov108/Developer-private/mono-pfont/test.py) - Generates test font with 46 glyphs for comprehensive hex digit testing
- Test Cases tab in [`index.html`](file:///Users/denis.ivanov108/Developer-private/mono-pfont/index.html) - Visual test page displaying all hex digit combinations in grid layout

**Test Coverage:**

*BMP Characters (19 test cases):*
- Sequential combinations: U+0123, U+1234, U+2345, U+3456, U+4567, U+5678, U+6789
- Mixed digits/letters: U+789A, U+89AB, U+9ABC
- All letters: U+ABCD, U+BCDE, U+CDEF, U+DEF0, U+EF01, U+F012
- Edge cases: U+0000 (all zeros), U+FFFD (high F's), U+0041 (Basic Latin 'A')

*Supplementary Planes 1-15 (15 test cases):*
- Tests all plane digits 1-F with various 4-digit combinations
- Examples: U+10000, U+23456, U+3789A, U+E12AB, U+FFFFD

*Plane 16 (5 test cases):*
- Filled squares with different digit combinations
- Examples: U+100000, U+101234, U+10ABCD, U+10F012

**Benefits:**
- ⚡ Fast generation (~8 seconds vs 5-10 minutes)
- 🎯 Complete coverage of all hex digits (0-9, A-F) in various positions
- 🔄 Quick iteration for fixing rendering issues
- 👀 Visual verification in browser with grid layout

---

## Technical Details

### Project Architecture

The codebase is split into five specialized modules:

#### [`main.py`](file:///Users/denis.ivanov108/Developer-private/mono-pfont/main.py) - Entry Point
- Simple entry point that calls `generator.generate_multi_file()`
- Imports configuration from `config.py`
- 24 lines total

#### [`generator.py`](file:///Users/denis.ivanov108/Developer-private/mono-pfont/generator.py) - Font Generation Engine
- **`create_font_object()`**: Creates and configures FontForge font objects with proper metadata
- **`generate_multi_file()`**: Main generation pipeline that:
  1. Collects all valid codepoints using `utils.is_valid_codepoint()`
  2. Splits them into 60,000-glyph chunks
  3. Creates font objects for each chunk
  4. Calls `glyphs.create_glyph()` for each codepoint
  5. Adds `.notdef` glyph
  6. Validates and generates OTF files to `dist/` directory
- 127 lines total

#### [`config.py`](file:///Users/denis.ivanov108/Developer-private/mono-pfont/config.py) - Configuration Constants
- Font metadata (name, family, version, copyright)
- Font metrics (EM size, ascent, descent)
- Glyph design parameters (box size, stroke width, corner radius)
- Hex digit display parameters (digit size, grid spacing, stroke width)
- Unicode ranges and multi-file configuration
- 43 lines total

#### [`utils.py`](file:///Users/denis.ivanov108/Developer-private/mono-pfont/utils.py) - Drawing Utilities
- **`is_valid_codepoint(cp)`**: Validates Unicode codepoints, excluding:
  - Surrogate pairs (U+D800-U+DFFF)
  - Non-characters ending in FFFE/FFFF
  - Arabic Presentation Forms-B non-characters (U+FDD0-U+FDEF)
- **`draw_rounded_filled_square(pen, x, y, size, radius)`**: Draws filled rounded squares using Bézier curves
- **`draw_rounded_square(pen, x, y, size, radius)`**: Draws filled rounded squares using passed parameters (bug fixed Dec 27, 2025: was ignoring radius parameter)
- **`draw_thick_line(pen, x1, y1, x2, y2, width)`**: Draws thick lines as filled rectangles (used for U+FFFD X and Plane 16 vertical line)
- **`draw_hex_digit(pen, digit, x, y, size, reverse_winding=False)`**: Solid 3x5 pixel grid hex digit renderer:
  - **Unified approach**: All hex digits (0-9, A-F) rendered as solid bitmap-style 3×5 grid patterns
  - **Grid format**: Each digit defined as a list of (col, row) coordinates where col is 0-2 and row is 0-4
  - **Cell-based rendering**: Each filled cell in the pattern becomes a solid rectangle
  - **Aspect ratio**: 60% width-to-height (3:5 grid)
  - **Benefits**: Clean shapes, good readability at 20px+ font sizes
  - Optional reverse winding for creating holes in filled backgrounds
  - **Important**: Digit '2' uses S-curve pattern; Digit 'A' has pixels at both bottom corners
- 105 lines total (cleaned up from 230 lines)

#### [`glyphs.py`](file:///Users/denis.ivanov108/Developer-private/mono-pfont/glyphs.py) - Glyph Creation Logic
- **`draw_replacement_character(glyph)`**: For U+FFFD, draws diagonal X inside outlined rounded square using `draw_thick_line`
- **`draw_hex_code_2x2(glyph, codepoint)`**: For U+0000-U+FFFF, draws 4-digit hex code in 2x2 grid inside filled rounded square
- **`draw_hex_code_5digit_split(glyph, codepoint)`**: For U+10000-U+FFFFF, draws 5-digit hex with large plane digit + 2x2 grid
- **`draw_hex_code_2x2_filled(glyph, codepoint)`**: For U+100000-U+10FFFF, draws last 4 digits in 2x2 grid with vertical line separator
- **`create_rounded_square_glyph(glyph)`**: Creates outlined rounded square frame (legacy, not used)
- **`create_filled_rounded_square_glyph(glyph)`**: Creates filled rounded square (legacy, not used)
- **`create_glyph(font, codepoint)`**: Main glyph creation dispatcher that routes to appropriate drawing function based on codepoint range
- **`validate_font_glyphs(font)`**: Validates and removes empty or invalid glyphs
- 258 lines total

### Unicode Coverage

- **Total valid codepoints**: 1,111,998 codepoints
- **Excluded codepoints**: 
  - Surrogate pairs (U+D800-U+DFFF) - 2,048 codepoints
  - Non-characters ending in FFFE/FFFF - 34 codepoints
  - Arabic Presentation Forms-B non-characters (U+FDD0-U+FDEF) - 32 codepoints
- **Files generated**: 19 OTF files (in multi-file mode)
- **Glyphs per file**: ~60,000 (last file may have fewer)

### Font Features by Unicode Range

Each glyph displays differently based on its Unicode range:

**U+0000 to U+FFFF (Basic Multilingual Plane):**

*Replacement Character (U+FFFD):*
- **Diagonal cross (X)** inside outlined rounded square
- Visually distinct from normal characters (which show hex codes)
- Line thickness: 40 units (matches border thickness)
- **Note**: U+0000 (NULL) also displays as X because browsers force NULL→U+FFFD replacement

*All Other BMP Characters (U+0000-U+FFFC, excluding U+FFFD):*
- Outlined rounded square with 40-unit stroke width
- **2x2 grid of hexadecimal digits** showing the character's 4-digit code
- Example: U+12AB displays as:
  ```
  1 2
  A B
  ```
- Transparent interior (except for hex digits)
- Recommended minimum font size: 20px+
- **Note**: Some characters (U+000A line feed, U+0009 tab) may show as whitespace due to browser handling

**U+10000 to U+FFFFF (Supplementary Planes 1-15):**
- Outlined rounded square with 40-unit stroke width
- **Split layout with 5-digit hex code display:**
  - **Left section**: First hex digit (plane digit) shown **larger** at 290 units (increased from 220)
  - **Right section**: Remaining 4 hex digits in **2x2 grid** at 260 units (increased from 140)
  - **Grid spacing**: 40 units (between grid cells, doubled from BMP's 30 units)
  - **Consistent padding**: ~75 units on all sides (left, right, top, bottom)
- Example: U+E12AB displays as:
  ```
       E  │  1  2
          │  A  B
  ```
  (Large 'E' on left, '12AB' in 2x2 grid on right)
- Transparent interior (except for hex digits)
- **Plane digit 57% larger** than grid digits for immediate plane identification (290 vs 260 units)
- Visually distinguishes supplementary planes from BMP with split layout

**U+100000 to U+10FFFD (Plane 16):**
- **Filled (solid) rounded square** with white background
- **More rounded corners** (120-unit radius vs 70 units for other planes) for enhanced visual distinction
- **Vertical line through the middle** for visual distinction
- **2x2 grid displaying the last 4 hexadecimal digits** of the 6-digit code
- Example: U+10ABCD displays digits from positions 2-5 as:
  ```
  A │ B
  C │ D
  ```
- Visually distinguishes the highest Unicode plane from others

**Common Properties:**
- Outer dimensions: 700×700 units
- Corner radius: 70 units for BMP and Supplementary Planes 1-15, 120 units for Plane 16 (uses Bézier curves)
- Monospaced: All glyphs have uniform width (1000 EM units)
- Hex digits: Vector-based, 140-unit height with 25-unit stroke width

### Browser Optimization

Using `unicode-range` in CSS means:
- Only relevant font files are downloaded
- Better performance - no need to load all ~405MB upfront
- Automatic fallback if a range file is missing

---

## File Sizes

File sizes are approximate and optimized per Unicode range:

- **OTF Format**: ~414 MB total (19 files)
  - Average: ~22 MB per file
  - Range: 16 MB to 24 MB depending on glyph complexity
- **WOFF2 Format**: ~10 MB total (19 files)
  - Average: ~500 KB per file
  - **97.6% compression ratio** compared to OTF
  - Dramatically faster loading for web use
- **npm package**: Will include both formats for maximum compatibility
- **Browser loads**: Only what's needed per page (WOFF2 preferred for speed)

---

## Dependencies

### Required Software

- **FontForge** with Python scripting support
  - Install on macOS: `brew install fontforge`
  - Verify installation: `fontforge --version`
- **Python 3.x** for running the local test server
- **fonttools + brotli** for WOFF2 generation (required)
  - Install: `pip3 install --break-system-packages fonttools brotli`
  - Why needed: FontForge's built-in WOFF2 generation produces corrupted fonts (black squares)
  - fonttools properly handles PostScript outline conversion to WOFF2

### Python Imports

The project uses only FontForge's built-in Python modules:
- `fontforge` - Font creation and manipulation
- Standard library only (no external dependencies)

---

## Development Notes

### Generation Performance

- **Time**: ~5-10 minutes to generate all 19 font files (depends on machine)
- **Memory**: Peak usage ~2-3 GB during generation
- **Disk Space**: Final output ~405 MB total (19 files)
- **Per File**: Each file generation takes ~20-30 seconds

### Design Decisions

#### Why OTF Instead of TTF?

- **PostScript outlines** (CFF format) handle complex Bézier curves better
- **Smaller file sizes** for vector-heavy fonts
- **Better rendering** of rounded corners at small sizes
- TTF support was removed due to compatibility issues with FontForge's TrueType instructions

#### Why Multi-File Generation?

- **Hard limit**: OpenType supports maximum 65,535 glyphs per file
- **Unicode coverage**: 1,111,998 valid codepoints require 19 files
- **Browser optimization**: CSS `unicode-range` loads only needed files
- **Chunk size**: 60,000 glyphs per file leaves room for `.notdef` and safety margin

#### Why Exclude Non-Characters?

- **U+FFFE, U+FFFF** and plane variants are permanent non-characters per Unicode standard
- **U+FDD0-U+FDEF** are reserved non-characters
- Including them causes **OTS parsing errors** in browsers
- Total excluded: 66 codepoints (2048 surrogates + 34 plane non-chars + 32 reserved)

#### Glyph Rendering Strategy

- **BMP (U+0000-U+FFFF)**: 4-digit hex in 2x2 grid inside outlined square
  - Most commonly used range, needs quick visual identification
  - Transparent background for readability
- **Supplementary Planes 1-15 (U+10000-U+FFFFF)**: Outlined square only
  - Less frequently used, visual distinction from BMP
- **Plane 16 (U+100000-U+10FFFD)**: Filled square with last 4 hex digits
  - Rarest range, needs strong visual distinction
  - Filled background makes it immediately recognizable

### Code Organization Rationale

The 5-file modular structure emerged from refactoring on **2025-12-26**:

- **`config.py`**: Single source of truth for all constants
  - Change font size, stroke width, Unicode ranges globally
  - No magic numbers scattered across codebase
- **`utils.py`**: Reusable drawing primitives
  - `is_valid_codepoint()` used by generator
  - `draw_hex_digit()` used by both BMP and Plane 16 rendering
  - `draw_rounded_square()` variations for outlined/filled
- **`glyphs.py`**: Glyph-specific logic isolated
  - Different rendering strategies for different Unicode ranges
  - Easy to add new glyph types without touching generator
- **`generator.py`**: Orchestration only
  - File chunking, font object creation, OTF generation
  - Delegates actual drawing to `glyphs.py`
- **`main.py`**: Minimal entry point
  - Makes testing and alternative entry points easy

---

## Publishing to NPM

For maintainers who want to publish updates to npm:

### Prerequisites

1. **npm account**: Create one at [npmjs.com](https://www.npmjs.com/)
2. **Login locally**: `npm login`
3. **Fonts generated**: Ensure `dist/` folder contains all 19 .otf files

### Publishing Steps

```bash
# 1. Ensure fonts are up-to-date
fontforge -script main.py

# 2. Update version in package.json (following semver)
# Patch: 1.0.0 → 1.0.1 (bug fixes)
# Minor: 1.0.0 → 1.1.0 (new features)
# Major: 1.0.0 → 2.0.0 (breaking changes)
npm version patch  # or 'minor' or 'major'

# 3. Preview what will be published (dry run)
npm pack --dry-run

# 4. Create a tarball to verify package contents
npm pack
tar -tzf unicode-hex-mono-*.tgz | head -20

# 5. Publish to npm (first time)
npm publish

# Or for updates
npm publish

# 6. Verify publication
npm view unicode-hex-mono
```

### Package Size Warning

The published package is **24.6 MB compressed** (416.1 MB unpacked) due to 38 font files (19 ranges × 2 formats). This is expected and acceptable for a development/debugging tool. Users will only download fonts for characters they actually display (thanks to `unicode-range` optimization, and browsers prefer smaller WOFF2 format).

### What Gets Published

Based on `.npmignore` and `package.json` files array:
- ✅ `dist/` directory (38 font files: 19 .otf + 19 .woff2 + font.css)
- ✅ `package.json`
- ✅ `LICENSE`
- ✅ `README.md`
- ❌ Python source files (*.py, __pycache__)
- ❌ Development files (index.html, test.py)
- ❌ Git and IDE files

### First-Time NPM Package Setup

If this is the first time publishing:

```bash
# Update repository URLs in package.json
# Replace 'yourusername' with your actual GitHub username
"repository": {
  "type": "git",
  "url": "https://github.com/yourusername/unicode-hex-mono.git"
}
```

---

## Troubleshooting


### Font Generation Issues

**Problem**: `fontforge: command not found`
```bash
# Solution: Install FontForge
brew install fontforge
```

**Problem**: `ImportError: No module named fontforge`
```bash
# Solution: Use FontForge's Python, not system Python
fontforge -script main.py  # ✅ Correct
python main.py             # ❌ Wrong
```

**Problem**: Glyphs appear as tiny dots or nothing renders
- **Cause**: Path winding order incorrect (clockwise vs counter-clockwise)
- **Check**: `utils.draw_rounded_square()` for proper outer/inner path directions
- **Fix**: Outer path must be clockwise, inner hole must be counter-clockwise

**Problem**: Hex digits erased by rounded square
- **Cause**: Inner counter-clockwise hole cuts through digit paths
- **Solution**: Use `draw_hex_code_2x2()` which draws border WITHOUT inner hole first

### Browser Testing Issues

**Problem**: Fonts not loading in browser
```bash
# Check local server is running
python3 -m http.server 8080

# Check console for errors (F12 → Console)
# Look for CORS or 404 errors
```

**Problem**: `OTS parsing error: cmap: Out of order end range`
- **Cause**: Non-characters (U+FFFE, U+FFFF variants) included in font
- **Solution**: Verify `utils.is_valid_codepoint()` excludes them
- **Test**: Check that `(cp & 0xFFFF) >= 0xFFFE` returns False

**Problem**: Wrong characters display
- **Cause**: `unicode-range` in `index.html` doesn't match actual font files
- **Solution**: Regenerate fonts, verify range names match files in `dist/`

### Development Workflow

**Making Changes**:
1. Edit configuration in `config.py`
2. Modify drawing logic in `utils.py` or `glyphs.py`
3. Test with small range first:
   ```python
   # In generator.py, temporarily limit range
   all_codepoints = [cp for cp in range(0x0000, 0x0100)]  # Test with ASCII only
   ```
4. Generate fonts: `fontforge -script main.py`
5. Refresh browser test page (Cmd+Shift+R for hard refresh)
6. Check console for errors
7. Restore full range and generate production fonts

**Testing Specific Glyphs**:
```python
# In index.html, add specific test cases
<p class="test">
    &#x0041;  <!-- Test U+0041 (A) -->
    &#x10FFFD; <!-- Test highest valid codepoint -->
</p>
```

**Debugging Glyph Paths**:
- Open generated `.otf` in FontForge GUI: `fontforge dist/UnicodeHexMono_00000_0F25F.otf`
- Navigate to specific glyph to inspect paths visually
- Check path direction: Element → Correct Direction

---

## Known Limitations

- **No hinting**: Fonts don't include TrueType instructions for pixel-grid alignment
- **Large file sizes**: Vector-heavy design results in ~2-3 MB per file
- **Generation time**: Full regeneration takes 5-10 minutes
- **No TTF support**: Only OTF (PostScript outlines) format supported
- **Fixed design**: Stroke width, corner radius are set at generation time
- **Monospace only**: All glyphs have same width (not suitable for proportional text)

---

## Development History

This section documents major issues encountered during development and their solutions, useful for future troubleshooting.

### Session Timeline

#### 2025-12-28 (Latest Session)
- **Task**: Automatic CSS generation and index.html refactoring for npm distribution
- **Actions**:
  - Created new `css_generator.py` module (195 lines) for automatic font.css generation
  - Scans `dist/` folder for `.otf` files and parses Unicode ranges from filenames
  - Generates production-ready CSS with 19 @font-face declarations
  - Integrated into `main.py` to run automatically after font generation
  - Refactored `index.html`: Replaced JavaScript-based font loading with standard `<link>` element
  - Removed `loadMainFonts()` function, eliminating 47 lines of complex JavaScript
- **Benefits**:
  - Simpler codebase with standard web practices
  - Better performance (native CSS loading vs custom JavaScript)
  - Ready for npm package distribution
  - Easier debugging and maintenance
- **Result**: Production-ready workflow with automatic CSS generation and clean HTML implementation

#### 2025-12-27 (Previous Session)
- **Task**: Make Plane 16 squares more rounded
- **Action**: Increased corner radius from 70 to 120 units for Plane 16 glyphs
- **Critical Bug Found**: `draw_rounded_square()` in `utils.py` was ignoring the `radius` parameter and always using hardcoded `config.CORNER_RADIUS`
- **Bug Fix**: Modified function to use passed parameters instead of hardcoded values
- **Additional**: Added cache busting for instant font reload during development
- **Result**: Plane 16 glyphs now have 71% rounder corners, significantly improving visual distinction

#### 2025-12-26 (Previous Session)
- **Task**: Modular refactoring
- **Action**: Split monolithic `generate.py` into 5 specialized modules
- **Result**: Better code organization, easier maintenance

#### 2025-12-26 (Earlier Sessions)

**Issue #1: Font Cmap Error**
- **Problem**: `OTS parsing error: cmap: Out of order end range`
- **Root Cause**: Including Unicode non-characters (U+FFFE, U+FFFF, U+FDD0-U+FDEF)
- **Solution**: Enhanced `is_valid_codepoint()` to exclude non-characters
- **Files Modified**: `utils.py`

**Issue #2: Missing Hex Digits**
- **Problem**: Hex digits disappeared when rounded square border was drawn
- **Root Cause**: Inner counter-clockwise hole created a "hole" that erased digit paths
- **Solution**: Modified `draw_hex_code_2x2()` to use border-only for BMP glyphs
- **Files Modified**: `glyphs.py`

**Issue #3: Font Rendering as Tiny Marks**
- **Problem**: Glyphs appeared as tiny dots instead of proper shapes
- **Root Cause**: Incorrect path winding order (both outer and inner clockwise)
- **Solution**: Inner path must be counter-clockwise to create transparent hole
- **Files Modified**: `utils.py` (`draw_rounded_square()`)

**Issue #4: Font Not Installable on macOS**
- **Problem**: "Contains no installable fonts" error message
- **Root Cause**: Missing OS/2 table metadata and PostScript name entries
- **Solution**: Added complete font naming table in `create_font_object()`
- **Files Modified**: `generator.py`

#### 2025-12-26 (Initial Sessions)

**Milestone**: Initial implementation of full Unicode coverage
- Created multi-file generation system (19 OTF files)
- Implemented 2x2 hex digit grid for BMP characters
- Added filled squares for Plane 16 characters
- Set up `index.html` test page with dynamic font loading

### Key Learnings

1. **Path Winding Matters**: FontForge requires strict clockwise (fill) vs counter-clockwise (hole) winding
2. **Unicode Non-Characters**: Always exclude U+FFFE, U+FFFF variants - browsers reject them
3. **Bézier Constant**: Use `0.448` as the control point offset for 90° circular arc approximation
4. **Font Metadata**: macOS requires complete name table entries or font won't install
5. **Chunk Size**: 60,000 glyphs per file is safe; leaves margin below 65,535 limit
6. **Drawing Order**: Draw border first, THEN hex digits (digits must be on top layer)
7. **Function Parameters**: Always use passed parameters, never hardcode config values inside utility functions (learned from `draw_rounded_square()` bug)
8. **Browser Font Caching**: Add cache busting to test pages - browsers aggressively cache font files
9. **CSS Loading Best Practice**: Use standard `<link>` elements for font loading instead of JavaScript - simpler, faster, and follows web standards

---

## Recent Updates

### ✅ December 27, 2025 - Info Tab & Debugging-Focused Interface

**Implemented**: Added comprehensive Info tab to `index.html` as the default landing page, with improved debugging-focused interface.

- **New Info Tab** (ℹ️):
  - Opens by default to immediately educate users about the font's purpose
  - Comprehensive documentation of font usage as a backup font in CSS font stacks
  - Visual examples of all glyph display formats (BMP, Supplementary Planes, Plane 16, U+FFFD)
  - Detailed edge cases documentation (control characters, excluded codepoints, browser behaviors)
  - Rendering context examples (code editors, web development, i18n work)
  - Font size recommendations and technical specifications
- **Improved Text Testing Tab**:
  - Updated placeholder with debugging-focused examples
  - Demonstrates problematic Unicode: zero-width spaces (U+200B), RTL marks (U+200F), em spaces, ancient scripts
  - Emphasizes "As Backup" mode for practical usage
- **Tab Reordering**: Info → Text Testing → Glyph List → Test Cases
- **Benefits**:
  - New users immediately understand the font's purpose
  - Reduces learning curve with comprehensive built-in documentation
  - Practical debugging examples ready to copy/paste
  - Single source of truth for font capabilities and edge cases

### ✅ December 26, 2025 - Modular Refactoring

**Implemented**: Split the monolithic `generate.py` into five specialized modules for better maintainability and code organization.

- **New File Structure**:
  - `main.py` - Entry point (24 lines)
  - `generator.py` - Font generation engine (127 lines)
  - `config.py` - Configuration constants (43 lines)
  - `utils.py` - Drawing utilities and hex digit paths (574 lines)
  - `glyphs.py` - Glyph creation logic (279 lines)
- **Benefits**:
  - Clear separation of concerns
  - Easier to maintain and debug
  - Better code reusability
  - Simplified testing
- **No Functionality Changes**: The overall font generation process remains identical, just better organized

### ✅ December 26, 2025 - Hex Code Display in 2x2 Grid

**Implemented**: Characters from U+0000 to U+FFFF now display their hexadecimal codes inside rounded squares in a 2x2 grid layout.

- **2x2 Grid Layout**: Each 4-digit hex code is split into a grid (top row: digits 1-2, bottom row: digits 3-4)
- **Example**: U+12AB displays as "1 2" in the top row and "A B" in the bottom row
- **Vector-Based Digits**: All hex digits (0-9, A-F) are drawn as vector paths for scalability
- **Optimized Readability**: Digit size and positioning optimized for clarity, recommended 20px+ font size
- **Unicode Ranges**:
  - U+0000 to U+FFFF: Outlined squares **with hex codes displayed**
  - U+10000 to U+FFFFF: Outlined squares (no hex codes)
  - U+100000 to U+10FFFD: Filled squares (no hex codes)

This feature makes it easy to identify characters by their Unicode codepoint at a glance.

### ✅ December 26, 2025 - Filled Squares for Plane 16

**Implemented**: Symbols from U+100000 to U+10FFFD now display as **filled rounded squares** instead of outlined ones.

- **U+0000 to U+FFFF** (Basic Multilingual Plane): Outlined rounded squares **with hex codes**
- **U+10000 to U+FFFFF** (Planes 1-15): Outlined rounded squares with transparent interior
- **U+100000 to U+10FFFD** (Plane 16): Filled (solid) rounded squares

This visual distinction helps identify characters from different Unicode planes.

> **Note**: U+10FFFE and U+10FFFF are excluded as they are Unicode non-characters.

### ✅ December 27, 2025 - 5-Digit Split Layout for Supplementary Planes

**Implemented**: Characters from U+10000 to U+FFFFF now display their hexadecimal codes with a special split layout.

- **Layout Design**:
  - **Left section**: Plane digit (first hex digit) displayed **larger** at 220 units
  - **Right section**: Remaining 4 hex digits in **2x2 grid** at 140 units
  - **Grid spacing**: 40 units (doubled from BMP's 20 units for better readability)
  - **Consistent padding**: ~75 units on all sides (horizontal matches vertical)
- **Example**: U+E12AB displays with large 'E' on left and '12AB' in grid on right
- **Visual Hierarchy**: Plane digit is 57% larger (220 vs 140 units) for immediate plane identification
- **Balanced Layout**: Equal margins on all sides for professional appearance
- **Consistency**: Same outlined rounded square border as BMP characters

**Development Process**:
- Created [`test.py`](file:///Users/denis.ivanov108/Developer-private/mono-pfont/test.py) for rapid testing with sample glyphs
- Created Test Cases tab in index.html for visual verification
- Went through 4 iterations based on user feedback:
  1. Initial: Too cramped spacing
  2. Increased spacing: Better, but grid too far right
  3. Balanced position: Good, but inconsistent padding
  4. **Final**: Consistent ~75-unit padding on all sides ✅

**Final Measurements** (for 620-unit inner area):
- Plane digit: Starts at 75 units from left, size 220 units
- Grid section: Starts at 268 units from left
- Grid spacing: 40 units between cells
- Right margin: 75 units (matches left, top, bottom)

This enhancement makes supplementary plane characters easily identifiable by their plane number while providing full codepoint information.

### ✅ December 27, 2025 - 3x5 Pixel Grid Rendering for All Hex Digits

**Problem**: Previous implementations used inconsistent rendering approaches (7-segment for numbers, custom outlines for letters), resulting in variable appearance and maintainability challenges.

**Solution**: Complete redesign of the `draw_hex_digit` function using a unified 3x5 pixel grid approach for all hex digits.

**Implemented**:
- **3x5 Grid Pattern**: Each hex digit (0-9, A-F) is defined as a bitmap-style pattern of filled cells in a 3-column by 5-row grid
- **Coordinate-Based Definition**: Each digit is simply a list of `(col, row)` tuples indicating which cells to fill
- **Example Patterns**:
  - '0': Rectangle outline with filled cells at edges
  - '1': Single vertical column in the center
  - 'A': Triangle shape with horizontal crossbar
  - 'E': Three horizontal bars attached to left vertical
- **Cell Spacing**: 4% gap between cells for crisp, clean rendering
- **Consistent Aspect Ratio**: Maintains 60% width-to-height (3:5 grid)

**Benefits**:
- ✅ **Unified rendering**: Same approach for all 16 hex digits (0-9, A-F)
- 📏 **Cleaner code**: Reduced from ~150 lines to ~75 lines (50% reduction)
- 🎯 **Better legibility**: Bitmap-style rendering is clearer at small display sizes
- 🔧 **Easier maintenance**: Simple coordinate lists vs complex segment calculations
- 💪 **Consistent appearance**: All digits use the same grid-based rendering system

**Files Modified**:
- [`utils.py`](file:///Users/denis.ivanov108/Developer-private/mono-pfont/utils.py#L158-L233) - Complete rewrite of `draw_hex_digit()` function

**Testing**: Verified with [`test.py`](file:///Users/denis.ivanov108/Developer-private/mono-pfont/test.py) generating a test font with representative glyphs and the Test Cases tab in `index.html` for visual confirmation - all hex digits (0-9, A-F) now render correctly in clean 3x5 grid patterns.

### ✅ December 27, 2025 - Comprehensive Hex Digit Test Suite

**Objective**: Expand test coverage to systematically verify all hex digits (0-9, A-F) in various combinations to identify and fix any rendering issues.

**Implemented**:
- **Expanded Test Suite**: Increased from 11 to **46 test codepoints** covering comprehensive hex digit combinations
- **BMP Tests (19 cases)**: Sequential patterns (U+0123 → U+F012) testing all digits in different positions
- **Supplementary Planes (15 cases)**: All plane digits 1-F with varying 4-digit combinations
- **Plane 16 (5 cases)**: Filled squares with diverse digit patterns
- **Updated Test Files Created**:
  - [`test.py`](file:///Users/denis.ivanov108/Developer-private/mono-pfont/test.py) - Quick test font generator with sample glyphs
  - Test Cases tab in `index.html` - Grid-based visual test page for easy verification

**Test Coverage Examples**:
- All sequential: U+1234, U+2345, U+3456
- Digit transitions: U+6789, U+789A, U+89AB
- All letters: U+ABCD, U+BCDE, U+CDEF
- Edge cases: U+0000, U+FFFD, U+0041

**Benefits**:
- ✅ **Complete coverage**: Every hex digit tested in multiple contexts
- 🔍 **Issue detection**: Systematic approach identifies rendering problems quickly
- 📊 **Visual verification**: Grid layout makes comparison easy
- 🚀 **Fast iteration**: 8-second generation enables rapid testing

### ✅ December 27, 2025 - Fixed Broken Hex Digits (Issue #2 and #A)

**Problem**: Visual rendering issues with hex digits '2' and 'A' in the 3x5 pixel grid:
- **Digit '2'**: Row 1 incorrectly showed right-side pixel instead of left-side pixel, creating a '3' shape instead of the proper S-curve
- **Digit 'A'**: Missing bottom corner pixels (rows 0-1), preventing proper triangle formation

**Solution**: Corrected the 3x5 pixel grid patterns in `draw_hex_digit` function:
- **'2' Fix**: Changed row 1 from `(2,1)` to `(0,1)` to complete the S-curve (right→left transition)
  - Before: `[(0,0), (1,0), (2,0), (2,1), (0,2), (1,2), (2,2), (2,3), (0,4), (1,4), (2,4)]` ❌ Creates '3' shape
  - After: `[(0,0), (1,0), (2,0), (0,1), (0,2), (1,2), (2,2), (2,3), (0,4), (1,4), (2,4)]` ✅ Creates '2' shape
  - Pattern: Top bar → Right side (row 3) → Middle bar (row 2) → Left side (row 1) → Bottom bar
- **'A' Fix**: Added missing side pixels at rows 0-1 to form complete triangle legs
  - Before: `[(0,0), (0,1), (0,2), (1,2), (2,2), (0,3), (2,3), (0,4), (1,4), (2,4)]`
  - After: `[(0,0), (2,0), (0,1), (2,1), (0,2), (1,2), (2,2), (0,3), (2,3), (0,4), (1,4), (2,4)]`

**Verification**:
- Regenerated test font with 39 comprehensive test glyphs
- Visually verified correct rendering in browser Test Cases tab in `index.html`
- Confirmed fixes in multiple contexts (BMP, supplementary planes)
- Example glyphs tested: U+01234 ('2'), U+0ABCD ('A'), U+E12AB (both '2' and 'A')

**Files Modified**:
- [`utils.py`](file:///Users/denis.ivanov108/Developer-private/mono-pfont/utils.py#L180) - Corrected pixel patterns for digits '2' and 'A'

**Impact**: All hex digits now render correctly with proper shapes and visual consistency across the entire Unicode range.

### ✅ December 27, 2025 - U+FFFD Diagonal X (Simplified Solution)

**Problem**: Control characters like U+0000 (NULL) were displaying with hex codes, making them look identical to normal characters. The original issue: "U+0000 looks the same as U+FFFD".

**Initial Attempt**: Implemented empty squares for control characters (U+0001-U+001F, U+007F) AND diagonal X for U+FFFD. This worked but added unnecessary complexity.

**Final Solution**: Simplified to only special-case U+FFFD with diagonal X. Removed all control character empty square logic.

**Why This Works**:
1. Browsers automatically replace U+0000 (NULL) with U+FFFD for security/stability
2. By making U+FFFD show a diagonal X, U+0000 automatically shows X too
3. All other characters (including control chars) show hex codes
4. Result: U+0000 is visually distinct (shows X) vs normal chars (show hex codes)

**Implementation**:
- Added `draw_thick_line()` to [`utils.py`](file:///Users/denis.ivanov108/Developer-private/mono-pfont/utils.py#L158-L185) for drawing diagonal lines
- Added `draw_replacement_character()` to [`glyphs.py`](file:///Users/denis.ivanov108/Developer-private/mono-pfont/glyphs.py#L4-L38) for U+FFFD rendering
- Updated `create_glyph()` to check only for U+FFFD (single special case)
- Line width: 40 units, padding: 100 units from edges

**Verification Results**:
- ✅ U+0000: Shows diagonal **X** (browser forces → U+FFFD)
- ✅ U+0001, U+001F, U+007F: Show **hex codes** (00/01, 00/1F, 00/7F)
- ✅ U+FFFD: Shows diagonal **X**
- ⚠️ U+000A (line feed): Shows as whitespace (browser behavior)

**Files Modified**:
- [`utils.py`](file:///Users/denis.ivanov108/Developer-private/mono-pfont/utils.py#L158-L185) - Added `draw_thick_line()`
- [`glyphs.py`](file:///Users/denis.ivanov108/Developer-private/mono-pfont/glyphs.py#L4-L38) - Added `draw_replacement_character()`, removed control character logic
- [`glyphs.py`](file:///Users/denis.ivanov108/Developer-private/mono-pfont/glyphs.py#L380-L386) - Simplified `create_glyph()` to single U+FFFD check
- [`test.py`](file:///Users/denis.ivanov108/Developer-private/mono-pfont/test.py#L16-L22) - Added control character test cases
- Test Cases tab in `index.html` - Displays control character test section

**Impact**: Clean, simple solution with only one special case (U+FFFD). Solves the original problem elegantly - U+0000 now looks different (X) from normal characters (hex codes).

### ✅ December 27, 2025 - Improved Digit Visibility and Plane 16 Distinction

**Session Summary**: Three major improvements to hex digit visibility and visual distinction:

1. **Increased Digit Sizes by 37%**:
   - DIGIT_SIZE: 190 → 260 units
   - GRID_SPACING: 20 → 30 units  
   - Plane digit: 220 → 290 units
   - Utilized space freed from previous border removal
   - Improved visibility at small font sizes (16px and below)

2. **Removed Gaps Between Pixels (Solid Digits)**:
   - Changed gap from `size * 0.04` to `0`
   - Creates solid, unified shapes instead of pixelated/dotted appearance
   - Dramatically improved readability
   - Digits now appear as cohesive forms

3. **Vertical Line for Plane 16**:
   - Added vertical line through middle of Plane 16 glyphs (U+100000-U+10FFFD)
   - Uses `draw_thick_line` approach (same as U+FFFD diagonal X)
   - Line width: 40 units (matches border thickness)
   - Visually separates left/right digit pairs in 2x2 grid
   - Provides clear visual distinction from other Unicode ranges

**Files Modified**:
- [`config.py`](file:///Users/denis.ivanov108/Developer-private/mono-pfont/config.py#L25-L26) - Updated DIGIT_SIZE and GRID_SPACING
- [`glyphs.py`](file:///Users/denis.ivanov108/Developer-private/mono-pfont/glyphs.py#L135) - Updated plane_digit_size to 290
- [`glyphs.py`](file:///Users/denis.ivanov108/Developer-private/mono-pfont/glyphs.py#L245-L256) - Added vertical line using draw_thick_line
- [`utils.py`](file:///Users/denis.ivanov108/Developer-private/mono-pfont/utils.py#L95-L99) - Cleaned up commented border code
- [`utils.py`](file:///Users/denis.ivanov108/Developer-private/mono-pfont/utils.py#L166) - Changed gap to 0 for solid digits

**Impact**: 
- ✅ **37% larger digits** - much better visibility
- ✅ **Solid appearance** - professional look
- ✅ **Excellent readability** - clear even at 16px font size  
- ✅ **Plane 16 distinction** - vertical line makes it instantly recognizable
- ✅ **Cleaner codebase** - removed 125 lines of unused commented code



## Verification Standards

To ensure the font meets quality standards, verify the following criteria:

### Visual QA Checklist
- **U+FFFD (Replacement Character)**:
  - [ ] Must display diagonal **X** inside rounded square
  - [ ] Must be visually distinct from normal BMP characters (which show hex codes)
  - [ ] U+0000 should also show X (browser forces NULL→U+FFFD)
- **BMP Characters (U+0000-U+FFFC, excluding U+FFFD)**:
  - [ ] Must show 4-digit hex code in 2x2 grid
  - [ ] Digits must be **solid** and **large** (260 units)
  - [ ] Digits must be legible at 16px font size
  - [ ] Filled black rounded square background
  - [ ] Note: U+000A (line feed), U+0009 (tab) may show as whitespace (browser behavior)
- **Supplementary Planes (U+10000-U+FFFFF)**:
  - [ ] **Left side**: Plane digit must be larger (290 units vs 260 units for grid)
  - [ ] **Right side**: Remaining 4 digits in 2x2 grid
  - [ ] All digits must be solid
  - [ ] Padding must be consistent on all sides (~75 units)
- **Plane 16 (U+100000-U+10FFFD)**:
  - [ ] Must be a **filled** rounded square
  - [ ] Must show last 4 digits in 2x2 grid (solid digits)
  - [ ] Must have **vertical line through middle** (40-unit width)
  - [ ] Vertical line must separate left/right digit pairs
- **General**:
  - [ ] All hex digits must be **solid** (no pixelated/dotted appearance)
  - [ ] Digits must use 260-unit size (37% larger than old 190-unit size)
  - [ ] No "tiny dot" glyphs (indicates path winding error)
  - [ ] 'A' must have a horizontal crossbar and pixels at both bottom corners (triangle shape)
  - [ ] '2' must have S-curve shape (not look like '3' or '5')
  - [ ] All digits (0-9, A-F) must be clearly legible at 16px font size

### Automated Checks
- **Validation**: `glyphs.validate_font_glyphs(font)` must be called during generation.
- **Non-characters**: Ensure U+FFFE, U+FFFF, and U+FDD0-U+FDEF are excluded.

---

## Extensibility Guide

How to modify or extend the font:

### Adding a New Layout
1.  **Define Logic**: Add a new drawing function in `glyphs.py` (e.g., `draw_special_layout`).
2.  **Dispatch**: Update `create_glyph` in `glyphs.py` to call your new function for a specific Unicode range.
3.  **Test**: Update `test.py` to include a codepoint from your new range.

### Changing Design Parameters
- **Stroke Width / Dimensions**: Update constants in `config.py`.
    - `BOX_STROKE_WIDTH`: Thickness of the rounded square.
    - `DIGIT_SIZE`: Size of the hex digits.
- **Digit Shapes**: Modify `draw_hex_digit` in `utils.py`.

### Debugging Paths
If new glyphs look wrong (e.g., filled when they should be outlined):
1.  Open the `.otf` in FontForge GUI.
2.  Select the glyph.
3.  Check **Element > Correct Direction**.
4.  Ensure your code in `utils.py` respects clockwise (fill) vs counter-clockwise (hole) winding.

---

## Next Steps (Future Enhancements)

Completed features:

1. ✅ Add hexadecimal codepoint display inside each square (U+0000-U+FFFF)
2. ✅ Implement 2x2 grid layout for BMP characters  
3. ✅ Implement filled squares with hex digits for Plane 16 (U+100000-U+10FFFD)
4. ✅ Modular code architecture with separated concerns
5. ✅ Add 5-digit split layout for supplementary planes (U+10000-U+FFFFF) with plane digit indicator

Future work could include:

- ⏳ Optimize file sizes with glyph compression
- ⏳ Add CSS font-variant subsets for different styles
- ⏳ Create automated test suite

---

## Quick Reference

### Common Commands

```bash
# Generate all fonts
fontforge -script main.py

# Start test server
python3 -m http.server 8080

# Open test page
open http://localhost:8080/index.html

# Install FontForge (macOS)
brew install fontforge

# Check FontForge version
fontforge --version

# Open specific font file in FontForge GUI
fontforge dist/UnicodeHexMono_00000_0F25F.otf
```

### Important File Locations

```
/Users/denis.ivanov108/Developer-private/mono-pfont/
├── main.py              # Entry point - run this with fontforge
├── generator.py         # Core generation logic
├── config.py            # All configuration constants
├── utils.py             # Drawing primitives, codepoint validation
├── glyphs.py            # Glyph creation dispatch
├── test.py              # Quick test script (7 glyphs, ~5 seconds)
├── index.html           # Font showcase with Test Cases tab
└── dist/                # Generated font files (19 .otf files)
    ├── UnicodeHexMono_00000_0F25F.otf
    ├── UnicodeHexMono_0F260_1DCE1.otf
    ├── UnicodeHexMono_TEST.otf  # Test font (if generated)
    └── ... (17 more files)
```

### Key Code Locations

**To change font appearance**:
- Font size, stroke width: [`config.py`](file:///Users/denis.ivanov108/Developer-private/mono-pfont/config.py) lines 12-27
- Hex digit grid patterns: [`utils.py`](file:///Users/denis.ivanov108/Developer-private/mono-pfont/utils.py) lines 158-230 (3×4 grid-based rendering)
- Rounded square drawing: [`utils.py`](file:///Users/denis.ivanov108/Developer-private/mono-pfont/utils.py) lines 19-156

**To modify glyph rendering logic**:
- BMP glyphs (U+0000-U+FFFF): [`glyphs.py`](file:///Users/denis.ivanov108/Developer-private/mono-pfont/glyphs.py) - `draw_hex_code_2x2()`
- Supplementary Planes 1-15 (U+10000-U+FFFFF): [`glyphs.py`](file:///Users/denis.ivanov108/Developer-private/mono-pfont/glyphs.py) - `draw_hex_code_5digit_split()`
- Plane 16 glyphs (U+100000-U+10FFFD): [`glyphs.py`](file:///Users/denis.ivanov108/Developer-private/mono-pfont/glyphs.py) - `draw_hex_code_2x2_filled()`
- Glyph dispatch logic: [`glyphs.py`](file:///Users/denis.ivanov108/Developer-private/mono-pfont/glyphs.py) - `create_glyph()`

**To change Unicode range or file splitting**:
- Unicode ranges: [`config.py`](file:///Users/denis.ivanov108/Developer-private/mono-pfont/config.py) lines 29-35
- Glyphs per file: [`config.py`](file:///Users/denis.ivanov108/Developer-private/mono-pfont/config.py) line 39
- Codepoint validation: [`utils.py`](file:///Users/denis.ivanov108/Developer-private/mono-pfont/utils.py) lines 3-16

**To modify font metadata**:
- Font names, version: [`config.py`](file:///Users/denis.ivanov108/Developer-private/mono-pfont/config.py) lines 5-10
- Font object creation: [`generator.py`](file:///Users/denis.ivanov108/Developer-private/mono-pfont/generator.py) lines 6-42

### Critical Constants

```python
# From config.py
EM_SIZE = 1000              # Font coordinate system size
BOX_SIZE = 700              # Glyph box dimensions (700×700)
BOX_STROKE_WIDTH = 40       # Border thickness
CORNER_RADIUS = 70          # Rounded corner radius
DIGIT_SIZE = 190            # Hex digit height (increased for better visibility)
DIGIT_STROKE_WIDTH = 25     # Hex digit stroke
GRID_SPACING = 20           # Space between digits in BMP 2×2 grid
GLYPHS_PER_FILE = 60000     # Max glyphs per font file

# Split layout constants (in glyphs.py - for U+10000 to U+FFFFF)
plane_digit_size = 220      # Plane digit size (57% larger than standard)
grid_spacing = 40           # Grid spacing for supplementary planes (doubled)
vertical_padding = ~75      # Consistent padding on all sides (calculated)
spacing_between_sections = 50  # Gap between plane digit and grid
```

### Bézier Curve Magic Number

The constant **0.448** appears throughout the code - this is the control point offset for approximating a 90° circular arc with a cubic Bézier curve:
- Mathematically: `4/3 * tan(π/8) ≈ 0.5522847498...`
- Simplified approximation: `0.448` works well for font rendering

---

**Last Updated**: December 27, 2025  
**Status**: ✅ Complete - Full Unicode coverage with modular architecture and custom hex digit rendering  
**Latest Feature**: Custom hex digit rendering with dual modes (7-segment for numbers, vector outlines for letters)


