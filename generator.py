"""
Font generation engine for UnicodeHexMono.

This module orchestrates the multi-file font generation process:
- Collects valid Unicode codepoints
- Separates ASCII (U+0000-U+00FF) into dedicated file for performance
- Splits remaining codepoints into chunks (60,000 glyphs per file)
- Creates FontForge font objects with proper metadata
- Generates individual glyphs for each codepoint
- Validates and exports OTF font files

The multi-file approach is necessary because OpenType fonts have a hard limit
of 65,535 glyphs per file, while Unicode has over 1 million codepoints.
"""

import os
import fontforge
import config
import utils
import glyphs

# ============================================================================
# Font Object Creation
# ============================================================================

def create_font_object():
    """Create and configure a new FontForge font object with proper metadata."""
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
    
    # Set OS/2 table properties (required for proper font rendering)
    font.os2_vendor = "PFNT"  # 4-character vendor ID
    font.os2_version = 4
    font.os2_winascent = config.ASCENT
    font.os2_windescent = config.DESCENT
    font.os2_typoascent = config.ASCENT
    font.os2_typodescent = -config.DESCENT
    font.os2_typolinegap = 0
    font.os2_panose = (2, 11, 6, 9, 3, 0, 0, 2, 0, 4)  # Monospaced
    
    # Set PostScript name (required for macOS)
    font.appendSFNTName('English (US)', 'PostScriptName', config.FONT_NAME)
    font.appendSFNTName('English (US)', 'Family', config.FONT_FAMILY)
    font.appendSFNTName('English (US)', 'Fullname', config.FONT_FULLNAME)
    font.appendSFNTName('English (US)', 'Preferred Family', config.FONT_FAMILY)
    font.appendSFNTName('English (US)', 'Compatible Full', config.FONT_FULLNAME)
    
    return font

# ============================================================================
# Multi-File Font Generation
# ============================================================================

def generate_multi_file():
    """Generate multiple font files to cover the full Unicode range.
    
    Strategy:
    - File 1: ASCII & Extended ASCII (U+0000-U+00FF) - 256 glyphs
    - Files 2+: Remaining codepoints in 60,000-glyph chunks
    """
    print("\nMode: Multi-file generation")
    print(f"Glyphs per file (non-ASCII): {config.GLYPHS_PER_FILE}")
    print(f"Unicode range: U+{config.UNICODE_MIN:05X} - U+{config.UNICODE_MAX:05X}")
    
    # Ensure dist directory exists
    os.makedirs('dist', exist_ok=True)
    
    # Collect all valid codepoints
    print("\nCollecting valid codepoints...")
    all_codepoints = []
    for cp in range(config.UNICODE_MIN, config.UNICODE_MAX + 1):
        if utils.is_valid_codepoint(cp):
            all_codepoints.append(cp)
    
    total_codepoints = len(all_codepoints)
    print(f"Total valid codepoints: {total_codepoints:,}")
    
    # Separate ASCII range (U+0000-U+00FF) from the rest
    ascii_range_end = 0x00FF
    ascii_codepoints = [cp for cp in all_codepoints if cp <= ascii_range_end]
    remaining_codepoints = [cp for cp in all_codepoints if cp > ascii_range_end]
    
    print(f"\nASCII & Extended ASCII (U+0000-U+00FF): {len(ascii_codepoints):,} glyphs")
    print(f"Remaining codepoints (U+0100+): {len(remaining_codepoints):,} glyphs")
    
    # Calculate total number of files
    num_remaining_files = (len(remaining_codepoints) + config.GLYPHS_PER_FILE - 1) // config.GLYPHS_PER_FILE
    total_files = 1 + num_remaining_files  # 1 ASCII file + remaining chunks
    
    print(f"\nWill generate {total_files} font files:")
    print(f"  - 1 ASCII file (U+0000-U+00FF)")
    print(f"  - {num_remaining_files} files for remaining Unicode")
    
    font_files = []
    
    # ========================================================================
    # STEP 1: Generate ASCII & Extended ASCII file (U+0000-U+00FF)
    # ========================================================================
    print(f"\n{'=' * 70}")
    print(f"File 1/{total_files}: ASCII & Extended ASCII")
    print(f"U+{ascii_codepoints[0]:05X} - U+{ascii_codepoints[-1]:05X}")
    print(f"Glyphs in this file: {len(ascii_codepoints):,}")
    print(f"{'=' * 70}")
    
    # Create font
    font = create_font_object()
    
    # Generate glyphs for ASCII range
    print("Generating glyphs...")
    for i, cp in enumerate(ascii_codepoints):
        glyphs.create_glyph(font, cp)
        if (i + 1) % 50 == 0:
            print(f"  {i + 1:,} / {len(ascii_codepoints):,} glyphs generated...")
    
    # Add .notdef glyph
    print("Creating .notdef glyph...")
    glyphs.create_notdef_glyph(font)
    
    # Validate glyphs
    print("Validating glyphs...")
    glyphs.validate_font_glyphs(font)
    
    # Generate OTF filename
    min_cp = ascii_codepoints[0]
    max_cp = ascii_codepoints[-1]
    output_path_otf = f"dist/UnicodeHexMono_{min_cp:05X}_{max_cp:05X}.otf"
    print(f"\nGenerating {output_path_otf}...")
    
    # Generate OTF
    font.generate(output_path_otf, flags=('opentype', 'omit-instructions', 'dummy-dsig'))
    font_files.append(output_path_otf)
    
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
        font_files.append(output_path_woff2)
        print(f"✓ Generated: {output_path_woff2}")
        print(f"  Format: WOFF2 (optimized for web)")
    except ImportError:
        print("⚠ fonttools not installed - skipping WOFF2 generation")
        print("  Install with: pip3 install --break-system-packages fonttools brotli")
    
    font.close()
    
    # ========================================================================
    # STEP 2: Generate remaining files in 60k chunks
    # ========================================================================
    for file_idx in range(num_remaining_files):
        start_idx = file_idx * config.GLYPHS_PER_FILE
        end_idx = min(start_idx + config.GLYPHS_PER_FILE, len(remaining_codepoints))
        chunk = remaining_codepoints[start_idx:end_idx]
        
        if not chunk:
            continue
        
        min_cp = chunk[0]
        max_cp = chunk[-1]
        
        print(f"\n{'=' * 70}")
        print(f"File {file_idx + 2}/{total_files}: U+{min_cp:05X} - U+{max_cp:05X}")
        print(f"Glyphs in this file: {len(chunk):,}")
        print(f"{'=' * 70}")
        
        # Create font
        font = create_font_object()
        
        # Generate glyphs for this chunk
        print("Generating glyphs...")
        for i, cp in enumerate(chunk):
            glyphs.create_glyph(font, cp)
            if (i + 1) % 1000 == 0:
                print(f"  {i + 1:,} / {len(chunk):,} glyphs generated...")
        
        # Add .notdef glyph
        print("Creating .notdef glyph...")
        glyphs.create_notdef_glyph(font)
        
        # Validate glyphs
        print("Validating glyphs...")
        glyphs.validate_font_glyphs(font)
        
        # Generate OTF filename
        output_path_otf = f"dist/UnicodeHexMono_{min_cp:05X}_{max_cp:05X}.otf"
        print(f"\nGenerating {output_path_otf}...")
        
        # Generate OTF with proper flags
        font.generate(output_path_otf, flags=('opentype', 'omit-instructions', 'dummy-dsig'))
        font_files.append(output_path_otf)
        
        print(f"✓ Generated: {output_path_otf}")
        print(f"  Total glyphs in file: {len(font)}")
        
        # Generate WOFF2 using fonttools
        output_path_woff2 = f"dist/UnicodeHexMono_{min_cp:05X}_{max_cp:05X}.woff2"
        print(f"\nGenerating {output_path_woff2}...")
        print("  Converting OTF to WOFF2 using fonttools...")
        try:
            from fontTools.ttLib import TTFont
            otf_font = TTFont(output_path_otf)
            otf_font.flavor = 'woff2'
            otf_font.save(output_path_woff2)
            font_files.append(output_path_woff2)
            print(f"✓ Generated: {output_path_woff2}")
            print(f"  Format: WOFF2 (optimized for web)")
        except ImportError:
            print("⚠ fonttools not installed - skipping WOFF2 generation")
            print("  Install with: pip3 install --break-system-packages fonttools brotli")
        
        font.close()
    
    # Summary
    print("\n" + "=" * 70)
    print("SUCCESS!")
    print(f"Generated {len(font_files)} font files ({total_files} ranges × 2 formats):")
    for f in font_files:
        print(f"  - {f}")
    print(f"Total codepoints covered: {total_codepoints:,}")
    print(f"Formats: OTF (OpenType) + WOFF2 (Web optimized)")
    print("=" * 70)