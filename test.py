#!/usr/bin/env fontforge
"""
Quick test script to generate a comprehensive sample font for verifying hex digit rendering.
This script tests all hex digits (0-9, A-F) in various combinations across BMP, supplementary planes, and Plane 16.
"""

import fontforge

import config
import glyphs

# Test codepoints to systematically verify all hex digits (0-9, A-F) in different positions
test_codepoints = [
    # ===== NEW: ASCII & Extended ASCII (U+0000-U+00FF) - 2-digit huge display =====
    # Control characters (U+0000-U+001F)
    0x0000,    # NULL - browser forces to U+FFFD (shows X) or 00
    0x0001,    # SOH - should show 01 (huge, centered)
    0x0009,    # TAB - should show 09 (huge, centered)
    0x000A,    # LF - should show 0A (huge, centered)
    0x000D,    # CR - should show 0D (huge, centered)
    0x001B,    # ESC - should show 1B (huge, centered)
    0x001F,    # Unit Separator - should show 1F (huge, centered)
    
    # Printable ASCII (U+0020-U+007E)
    0x0020,    # SPACE - should show 20 (huge, centered)
    0x0030,    # '0' - should show 30 (huge, centered)
    0x0039,    # '9' - should show 39 (huge, centered)
    0x0041,    # 'A' - should show 41 (huge, centered)
    0x005A,    # 'Z' - should show 5A (huge, centered)
    0x0061,    # 'a' - should show 61 (huge, centered)
    0x007A,    # 'z' - should show 7A (huge, centered)
    0x007E,    # '~' - should show 7E (huge, centered)
    0x007F,    # DEL - should show 7F (huge, centered)
    
    # C1 Controls + Latin-1 Supplement (U+0080-U+00FF)
    0x0080,    # PAD - should show 80 (huge, centered)
    0x0090,    # DCS - should show 90 (huge, centered)
    0x009F,    # APC - should show 9F (huge, centered)
    0x00A0,    # NBSP - should show A0 (huge, centered)
    0x00A9,    # © - should show A9 (huge, centered)
    0x00B0,    # ° - should show B0 (huge, centered)
    0x00C0,    # À - should show C0 (huge, centered)
    0x00D0,    # Ð - should show D0 (huge, centered)
    0x00E0,    # à - should show E0 (huge, centered)
    0x00F0,    # ð - should show F0 (huge, centered)
    0x00FF,    # ÿ - should show FF (huge, centered)
    
    # ===== BMP (U+0100-U+FFFF) - 4-digit 2x2 grid display =====
    # Systematic testing of all hex digits in different positions
    0x0100,    # First after ASCII range - should show 01/00 (2x2 grid)
    0x0123,    # All low digits - should show 01/23 (2x2 grid)
    0x1234,    # Sequential digits
    0x2345,
    0x3456,
    0x4567,
    0x5678,
    0x6789,
    0x789A,    # Transition to letters
    0x89AB,
    0x9ABC,
    0xABCD,    # All letters
    0xBCDE,
    0xCDEF,
    0xDEF0,    # Letters wrapping to digits
    0xEF01,
    0xF012,    # Complete test
    
    # Additional edge cases
    0xFFFD,    # High F's (FFFF is excluded as non-character) - should show FF/FD
    0x0041,    # Basic Latin 'A' - should show 00/41
    
    # Supplementary Planes 1-15: Test split layout with different plane digits
    0x10000,   # Plane 1, first codepoint - should show "1" + "0000"
    0x23456,   # Plane 2 - should show "2" + "3456"
    0x3789A,   # Plane 3 - should show "3" + "789A"
    0x4BCDE,   # Plane 4 - should show "4" + "BCDE"
    0x5F012,   # Plane 5 - should show "5" + "F012"
    0x6ABCD,   # Plane 6 - should show "6" + "ABCD"
    0x71234,   # Plane 7 - should show "7" + "1234"
    0x89ABC,   # Plane 8 - should show "8" + "9ABC"
    0x9DEF0,   # Plane 9 - should show "9" + "DEF0"
    0xA5678,   # Plane 10 (A) - should show "A" + "5678"
    0xBBDD8,   # Plane 11 (B) - should show "B" + "BDD8"
    0xCDEF0,   # Plane 12 (C) - should show "C" + "DEF0"
    0xD1234,   # Plane 13 (D) - should show "D" + "1234"
    0xE12AB,   # Plane 14 (E) - should show "E" + "12AB" (reference example)
    0xFFFFD,   # Plane 15 (F), last - should show "F" + "FFFD"
    
    # Plane 16: Filled squares with various digit combinations
    0x100000,  # Plane 16, first - should show filled square with "0000"
    0x101234,  # should show filled square with "1234"
    0x10ABCD,  # should show filled square with "ABCD"
    0x10BDD8,  # should show filled square with "BDD8"
    0x10F012,  # should show filled square with "F012"
]

print("Creating test font...")
font = fontforge.font()
font.fontname = "UnicodeHexMono_Test"
font.familyname = "UnicodeHexMono Test"
font.fullname = "UnicodeHexMono Test"
font.encoding = "UnicodeFull"
font.em = config.EM_SIZE
font.ascent = config.ASCENT
font.descent = config.DESCENT

print(f"\nGenerating {len(test_codepoints)} test glyphs...")
for cp in test_codepoints:
    print(f"  Creating glyph U+{cp:05X}")
    glyphs.create_glyph(font, cp)

# Add .notdef
print("\nCreating .notdef glyph...")
glyphs.create_notdef_glyph(font)

# Generate OTF
output_path_otf = "dist/UnicodeHexMono_TEST.otf"
print(f"\nGenerating {output_path_otf}...")
font.generate(output_path_otf, flags=('opentype', 'omit-instructions', 'dummy-dsig'))
print(f"✓ Generated: {output_path_otf}")

# Generate WOFF2 using fonttools (FontForge's WOFF2 is broken)
output_path_woff2 = "dist/UnicodeHexMono_TEST.woff2"
print(f"\nGenerating {output_path_woff2}...")
print("  Converting OTF to WOFF2 using fonttools...")
try:
    from fontTools.ttLib import TTFont
    otf_font = TTFont(output_path_otf)
    otf_font.flavor = 'woff2'
    otf_font.save(output_path_woff2)
    print(f"✓ Generated: {output_path_woff2}")
except ImportError:
    print("⚠ fonttools not installed - skipping WOFF2 generation")
    print("  Install with: pip3 install --break-system-packages fonttools brotli")

print(f"\n✅ Test fonts generated successfully!")
print(f"   Formats: OTF + WOFF2")
print(f"\nTest codepoints included ({len(test_codepoints)} total):")
for cp in test_codepoints:
    hex_str = f"{cp:06X}"
    print(f"  U+{hex_str}")

font.close()
