#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CSS generation module for UnicodeHexMono font.

This module scans the dist/ folder for generated .otf font files and creates
a production-ready font.css file with @font-face declarations for npm distribution.

The CSS follows modern best practices:
- Uses font-display: swap for better performance
- Includes proper unicode-range selectors for optimized loading
- Uses relative paths compatible with npm packages
- Includes comprehensive documentation comments

Usage:
    import css_generator
    css_generator.generate_css()
"""

import os
import re
import config


def parse_font_filename(filename):
    """
    Extract Unicode range and format from font filename.
    
    Args:
        filename: Font filename (e.g., 'UnicodeHexMono_00000_0F25F.otf' or '.woff2')
    
    Returns:
        Tuple of (start_codepoint, end_codepoint, start_hex, end_hex, format) or None if invalid
        Example: (0, 0x0F25F, '00000', '0F25F', 'otf')
    """
    # Pattern: UnicodeHexMono_<start>_<end>.(otf|woff2)
    pattern = r'UnicodeHexMono_([0-9A-F]{5,6})_([0-9A-F]{5,6})\.(otf|woff2)'
    match = re.match(pattern, filename, re.IGNORECASE)
    
    if match:
        start_hex = match.group(1).upper()
        end_hex = match.group(2).upper()
        file_format = match.group(3).lower()
        start_cp = int(start_hex, 16)
        end_cp = int(end_hex, 16)
        return (start_cp, end_cp, start_hex, end_hex, file_format)
    
    return None


def generate_css_content(font_ranges):
    """
    Generate CSS content with @font-face declarations.
    
    Args:
        font_ranges: List of tuples (start_cp, end_cp, start_hex, end_hex, formats_dict)
                    where formats_dict = {'otf': 'filename.otf', 'woff2': 'filename.woff2'}
    
    Returns:
        String containing the complete CSS content
    """
    css_lines = []
    
    # Header comment
    css_lines.append("/**")
    css_lines.append(f" * {config.FONT_NAME} Font Family")
    css_lines.append(f" * Version: {config.FONT_VERSION}")
    css_lines.append(" *")
    css_lines.append(" * A monospaced font covering all Unicode characters (U+0000 to U+10FFFD)")
    css_lines.append(" * Each glyph displays its hexadecimal codepoint in a rounded square")
    css_lines.append(" *")
    css_lines.append(" * Usage:")
    css_lines.append(" *   @import 'unicode-hex-mono/dist/font.css';")
    css_lines.append(" *   font-family: 'UnicodeHexMono', monospace;")
    css_lines.append(" *")
    css_lines.append(f" * Total font ranges: {len(font_ranges)}")
    css_lines.append(" * Formats: WOFF2 (web optimized) + OTF (OpenType fallback)")
    css_lines.append(" * Browser optimization: Only needed files are loaded via unicode-range")
    css_lines.append(" */")
    css_lines.append("")
    
    # Generate @font-face for each range
    for idx, (start_cp, end_cp, start_hex, end_hex, formats) in enumerate(font_ranges):
        # Add separator comment between font-face declarations
        if idx > 0:
            css_lines.append("")
        
        # Comment showing which Unicode range this covers
        css_lines.append(f"/* Unicode Range: U+{start_hex} - U+{end_hex} ({end_cp - start_cp + 1:,} codepoints) */")
        
        # @font-face declaration
        css_lines.append("@font-face {")
        css_lines.append(f"  font-family: '{config.FONT_FAMILY}';")
        
        # Build src with multiple formats (WOFF2 first for better compression)
        src_parts = []
        if 'woff2' in formats:
            src_parts.append(f"url('./{formats['woff2']}') format('woff2')")
        if 'otf' in formats:
            src_parts.append(f"url('./{formats['otf']}') format('opentype')")
        
        if len(src_parts) > 1:
            css_lines.append(f"  src: {src_parts[0]},")
            for part in src_parts[1:-1]:
                css_lines.append(f"       {part},")
            css_lines.append(f"       {src_parts[-1]};")
        else:
            css_lines.append(f"  src: {src_parts[0]};")
        
        css_lines.append(f"  unicode-range: U+{start_hex}-{end_hex};")
        css_lines.append("  font-weight: normal;")
        css_lines.append("  font-style: normal;")
        css_lines.append("  font-display: swap;")
        css_lines.append("}")
    
    return "\n".join(css_lines) + "\n"


def write_css_file(output_path, content):
    """
    Write CSS content to file.
    
    Args:
        output_path: Path to output CSS file
        content: CSS content string
    """
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)


def generate_css():
    """
    Main function to generate font.css from font files in dist/ folder.
    
    Scans the dist/ directory for .otf and .woff2 files, extracts their Unicode ranges,
    groups by range, and generates a complete font.css file with @font-face declarations.
    """
    dist_dir = 'dist'
    output_path = os.path.join(dist_dir, 'font.css')
    
    # Check if dist directory exists
    if not os.path.exists(dist_dir):
        print(f"ERROR: {dist_dir}/ directory not found")
        print("Please run font generation first: fontforge -script main.py")
        return
    
    # Scan for font files (.otf and .woff2)
    print(f"\nScanning {dist_dir}/ for font files...")
    font_data = {}  # Key: (start_cp, end_cp, start_hex, end_hex), Value: {format: filename}
    
    for filename in os.listdir(dist_dir):
        if not (filename.endswith('.otf') or filename.endswith('.woff2')):
            continue
        
        # Skip test fonts
        if filename == 'UnicodeHexMono_TEST.otf' or filename == 'UnicodeHexMono_TEST.woff2':
            continue
        
        parsed = parse_font_filename(filename)
        if parsed:
            start_cp, end_cp, start_hex, end_hex, file_format = parsed
            range_key = (start_cp, end_cp, start_hex, end_hex)
            
            if range_key not in font_data:
                font_data[range_key] = {}
            
            font_data[range_key][file_format] = filename
            print(f"  Found: {filename} (U+{start_hex} - U+{end_hex}) [{file_format.upper()}]")
        else:
            print(f"  Skipping: {filename} (invalid filename format)")
    
    if not font_data:
        print(f"\nERROR: No valid font files found in {dist_dir}/")
        print("Font files should follow pattern: UnicodeHexMono_<start>_<end>.(otf|woff2)")
        return
    
    # Convert to sorted list of ranges with formats
    font_ranges = []
    for (start_cp, end_cp, start_hex, end_hex), formats in font_data.items():
        font_ranges.append((start_cp, end_cp, start_hex, end_hex, formats))
    
    # Sort by start codepoint
    font_ranges.sort(key=lambda x: x[0])
    
    print(f"\nFound {len(font_ranges)} Unicode ranges")
    total_files = sum(len(formats) for _, _, _, _, formats in font_ranges)
    print(f"Total font files: {total_files}")
    
    # Generate CSS
    print(f"\nGenerating CSS...")
    css_content = generate_css_content(font_ranges)
    
    # Write to file
    write_css_file(output_path, css_content)
    
    # Summary
    print(f"\n{'=' * 70}")
    print(f"✓ Generated: {output_path}")
    print(f"  Unicode ranges: {len(font_ranges)}")
    print(f"  Total font files: {total_files}")
    print(f"  Formats: OTF + WOFF2")
    print(f"  CSS size: {len(css_content):,} bytes ({len(css_content) / 1024:.1f} KB)")
    print(f"  @font-face declarations: {len(font_ranges)}")
    print(f"{'=' * 70}")
    
    # Show sample CSS
    print("\nSample CSS (first 2 @font-face declarations):")
    print("-" * 70)
    lines = css_content.split('\n')
    # Find first two @font-face blocks
    font_face_count = 0
    for i, line in enumerate(lines):
        print(line)
        if line.strip() == '}':
            font_face_count += 1
            if font_face_count == 2:
                print("...")
                break
    print("-" * 70)


if __name__ == "__main__":
    generate_css()
