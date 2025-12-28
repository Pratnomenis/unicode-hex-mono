#!/usr/bin/env fontforge
# -*- coding: utf-8 -*-
"""
FontForge script to generate UnicodeHexMono font.
Each glyph is a rounded square for all Unicode codepoints U+0000 to U+10FFFF.

Usage: fontforge -script main.py
Output: UnicodeHexMono.otf
"""

import generator
import css_generator
import config

def main():
    print("=" * 70)
    print(f"Creating {config.FONT_NAME} font family...")
    print("=" * 70)
    
    # Generate font files
    generator.generate_multi_file()
    
    # Generate CSS file for npm distribution
    print("\n" + "=" * 70)
    print("Generating font.css for npm distribution...")
    print("=" * 70)
    css_generator.generate_css()


if __name__ == "__main__":
    main()

