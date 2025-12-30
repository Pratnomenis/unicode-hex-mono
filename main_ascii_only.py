#!/usr/bin/env fontforge
"""
Quick script to regenerate only the ASCII & Extended ASCII font file (U+0000-U+00FF).
Useful for testing changes to the 2-digit display without waiting for full generation.

Usage:
    fontforge -script main_ascii_only.py
"""

import os
import fontforge
import config
import utils
import glyphs

def main():
    print("=" * 70)
    print("Generating ASCII & Extended ASCII font file only")
    print("=" * 70)
    
    # Ensure dist directory exists
    os.makedirs('dist', exist_ok=True)
    
    # Define ASCII range
    ascii_codepoints = [cp for cp in range(0x0000, 0x0100) if utils.is_valid_codepoint(cp)]
    
    print(f"\nASCII & Extended ASCII (U+0000-U+00FF): {len(ascii_codepoints)} glyphs")
    print(f"\nGenerating font file...")
    
    # Create font
    font = fontforge.font()
    
    # Set font metadata
    font.fontname = config.FONT_NAME
    font.familyname = config.FONT_FAMILY
    font.fullname = config.FONT_FULLNAME
    font.version = config.FONT_VERSION
    font.copyright = config.FONT_COPYRIGHT
    font.weight = config.FONT_STYLE
    
    # Set encoding to UnicodeFull
    font.encoding = "UnicodeFull"
    
    # Set font metrics
    font.em = config.EM_SIZE
    font.ascent = config.ASCENT
    font.descent = config.DESCENT
    
    # Set OS/2 table properties
    font.os2_vendor = "PFNT"
    font.os2_version = 4
    font.os2_winascent = config.ASCENT
    font.os2_windescent = config.DESCENT
    font.os2_typoascent = config.ASCENT
    font.os2_typodescent = -config.DESCENT
    font.os2_typolinegap = 0
    font.os2_panose = (2, 11, 6, 9, 3, 0, 0, 2, 0, 4)
    
    # Set PostScript name
    font.appendSFNTName('English (US)', 'PostScriptName', config.FONT_NAME)
    font.appendSFNTName('English (US)', 'Family', config.FONT_FAMILY)
    font.appendSFNTName('English (US)', 'Fullname', config.FONT_FULLNAME)
    font.appendSFNTName('English (US)', 'Preferred Family', config.FONT_FAMILY)
    font.appendSFNTName('English (US)', 'Compatible Full', config.FONT_FULLNAME)
    
    # Generate glyphs
    print("Generating glyphs...")
    for i, cp in enumerate(ascii_codepoints):
        glyphs.create_glyph(font, cp)
        if (i + 1) % 50 == 0:
            print(f"  {i + 1} / {len(ascii_codepoints)} glyphs generated...")
    
    # Add .notdef glyph
    print("Creating .notdef glyph...")
    glyphs.create_notdef_glyph(font)
    
    # Validate glyphs
    print("Validating glyphs...")
    glyphs.validate_font_glyphs(font)
    
    # Generate OTF
    min_cp = ascii_codepoints[0]
    max_cp = ascii_codepoints[-1]
    output_path_otf = f"dist/UnicodeHexMono_{min_cp:05X}_{max_cp:05X}.otf"
    
    print(f"\nGenerating {output_path_otf}...")
    font.generate(output_path_otf, flags=('opentype', 'omit-instructions', 'dummy-dsig'))
    print(f"✓ Generated: {output_path_otf}")
    print(f"  Total glyphs in file: {len(font)}")
    
    # Generate WOFF2
    output_path_woff2 = f"dist/UnicodeHexMono_{min_cp:05X}_{max_cp:05X}.woff2"
    print(f"\nGenerating {output_path_woff2}...")
    print("  Converting OTF to WOFF2 using fonttools...")
    try:
        from fontTools.ttLib import TTFont
        otf_font = TTFont(output_path_otf)
        otf_font.flavor = 'woff2'
        otf_font.save(output_path_woff2)
        print(f"✓ Generated: {output_path_woff2}")
        print(f"  Format: WOFF2 (optimized for web)")
    except ImportError:
        print("⚠ fonttools not installed - skipping WOFF2 generation")
        print("  Install with: python3.14 -m pip install --break-system-packages fonttools brotli")
    
    font.close()
    
    # Summary
    print("\n" + "=" * 70)
    print("SUCCESS!")
    print(f"Generated ASCII font files:")
    print(f"  - {output_path_otf}")
    print(f"  - {output_path_woff2}")
    print(f"Total codepoints: {len(ascii_codepoints)}")
    print("=" * 70)

if __name__ == "__main__":
    main()
