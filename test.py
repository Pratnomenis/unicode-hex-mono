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
    # Control characters - should now show hex codes (except U+0000 shows X due to browser)
    0x0000,    # NULL - browser forces to U+FFFD (shows X)
    0x0001,    # Start of Heading - should show 00/01
    0x000A,    # Line Feed - should show 00/0A
    0x001F,    # Unit Separator - should show 00/1F
    0x007F,    # Delete - should show 00/7F
    
    # BMP: Systematic testing of all hex digits in different positions
    0x0123,    # All low digits
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
