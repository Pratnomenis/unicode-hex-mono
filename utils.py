"""
Drawing utilities for UnicodeHexMono font generation.

This module provides low-level drawing primitives for creating glyphs:
- Codepoint validation (excluding surrogates and non-characters)
- Rounded square path generation using Bézier curves
- Thick line drawing for X symbols and dividers
- Hex digit rendering using 3x5 pixel grid patterns

All drawing functions use FontForge's pen API to draw vector paths.
"""

import config

def is_valid_codepoint(cp):
    """Check if codepoint is valid and not in surrogate range."""
    if cp < config.UNICODE_MIN or cp > config.UNICODE_MAX:
        return False
    if config.SURROGATE_START <= cp <= config.SURROGATE_END:
        return False
    # Exclude non-characters: U+FFFE, U+FFFF and U+nFFFE, U+nFFFF for each plane
    # These are permanent non-characters and can cause cmap table errors
    if (cp & 0xFFFF) >= 0xFFFE:  # Check if last 4 hex digits are FFFE or FFFF
        return False
    # Exclude Arabic Presentation Forms-B non-characters (U+FDD0..U+FDEF)
    if 0xFDD0 <= cp <= 0xFDEF:
        return False
    return True


def draw_rounded_square(pen, x, y, size, radius):
    """
    Draw a filled rounded square using Bézier curves.
    
    Args:
        pen: FontForge glyph pen
        x, y: bottom-left corner coordinates
        size: width and height of the square
        radius: corner radius for rounding
    
    The path is drawn clockwise starting from the bottom-left corner.
    Uses Bézier constant 0.448 for 90° circular arc approximation.
    """
    # Clamp radius to not exceed half the size
    r = min(radius, size / 2)
    
    # Calculate corner positions
    # Bottom-left corner
    pen.moveTo((x + r, y))
    
    # Bottom edge to bottom-right corner
    pen.lineTo((x + size - r, y))
    
    # Bottom-right rounded corner (arc)
    # Arc from bottom to right side
    pen.curveTo(
        (x + size - r * 0.448, y),
        (x + size, y + r * 0.448),
        (x + size, y + r)
    )
    
    # Right edge to top-right corner
    pen.lineTo((x + size, y + size - r))
    
    # Top-right rounded corner (arc)
    # Arc from right to top side
    pen.curveTo(
        (x + size, y + size - r * 0.448),
        (x + size - r * 0.448, y + size),
        (x + size - r, y + size)
    )
    
    # Top edge to top-left corner
    pen.lineTo((x + r, y + size))
    
    # Top-left rounded corner (arc)
    # Arc from top to left side
    pen.curveTo(
        (x + r * 0.448, y + size),
        (x, y + size - r * 0.448),
        (x, y + size - r)
    )
    
    # Left edge to bottom-left corner
    pen.lineTo((x, y + r))
    
    # Bottom-left rounded corner (arc)
    # Arc from left to bottom side
    pen.curveTo(
        (x, y + r * 0.448),
        (x + r * 0.448, y),
        (x + r, y)
    )
    
    pen.closePath()



def draw_thick_line(pen, x1, y1, x2, y2, width):
    """
    Draw a thick line as a filled rectangle rotated along the line direction.
    
    Args:
        pen: FontForge glyph pen
        x1, y1: Starting point coordinates
        x2, y2: Ending point coordinates
        width: Line thickness
    """
    import math
    
    # Calculate angle and length
    dx = x2 - x1
    dy = y2 - y1
    angle = math.atan2(dy, dx)
    
    # Calculate perpendicular offset for line width
    offset_x = -math.sin(angle) * width / 2
    offset_y = math.cos(angle) * width / 2
    
    # Draw rectangle along the line (clockwise)
    pen.moveTo((x1 + offset_x, y1 + offset_y))
    pen.lineTo((x2 + offset_x, y2 + offset_y))
    pen.lineTo((x2 - offset_x, y2 - offset_y))
    pen.lineTo((x1 - offset_x, y1 - offset_y))
    pen.closePath()

def draw_hex_digit(pen, digit, x, y, size):
    """
    Draw a single hexadecimal digit (0-9, A-F) using a 3x5 pixel grid.
    Each digit is defined as a pattern of filled cells in a 3-column by 5-row grid.
    
    Args:
        pen: FontForge glyph pen
        digit: Hex digit character ('0'-'9', 'A'-'F')
        x, y: Bottom-left corner coordinates
        size: Height of the digit
    """
    
    # Digit dimensions - width is 60% of height for 3:5 aspect ratio
    width = size * 0.6
    
    # Define 3x5 grid patterns for each hex digit
    # Grid format: list of (col, row) tuples where col is 0-2 (left to right)
    # and row is 0-4 (bottom to top)
    digit_patterns = {
        '0': [(0,0), (1,0), (2,0), (0,1), (2,1), (0,2), (2,2), (0,3), (2,3), (0,4), (1,4), (2,4)],
        '1': [(1,0), (1,1), (1,2), (1,3), (1,4)],
        '2': [(0,0), (1,0), (2,0), (0,1), (0,2), (1,2), (2,2), (2,3), (0,4), (1,4), (2,4)],
        '3': [(0,0), (1,0), (2,0), (2,1), (0,2), (1,2), (2,2), (2,3), (0,4), (1,4), (2,4)],
        '4': [(0,4), (0,3), (0,2), (1,2), (2,0), (2,1), (2,2), (2,3), (2,4)],
        '5': [(0,0), (1,0), (2,0), (2,1), (0,2), (1,2), (2,2), (0,3), (0,4), (1,4), (2,4)],
        '6': [(0,0), (1,0), (2,0), (0,1), (2,1), (0,2), (1,2), (2,2), (0,3), (0,4), (1,4), (2,4)],
        '7': [(2,0), (2,1), (2,2), (2,3), (0,4), (1,4), (2,4)],
        '8': [(0,0), (1,0), (2,0), (0,1), (2,1), (0,2), (1,2), (2,2), (0,3), (2,3), (0,4), (1,4), (2,4)],
        '9': [(0,0), (1,0), (2,0), (2,1), (0,2), (1,2), (2,2), (0,3), (2,3), (0,4), (1,4), (2,4)],
        'A': [(0,0), (2,0), (0,1), (2,1), (0,2), (1,2), (2,2), (0,3), (2,3), (0,4), (1,4), (2,4)],
        'B': [(0,0), (1,0), (0,1), (2,1), (0,2), (1,2), (0,3), (2,3), (0,4), (1,4)],
        'C': [(0,0), (1,0), (2,0), (0,1), (0,2), (0,3), (0,4), (1,4), (2,4)],
        'D': [(0,0), (1,0), (0,1), (2,1), (0,2), (2,2), (0,3), (2,3), (0,4), (1,4)],
        'E': [(0,0), (1,0), (2,0), (0,1), (0,2), (1,2), (2,2), (0,3), (0,4), (1,4), (2,4)],
        'F': [(0,0), (0,1), (0,2), (1,2), (2,2), (0,3), (0,4), (1,4), (2,4)],
    }
    
    # Get the pattern for this digit
    digit = digit.upper()
    pattern = digit_patterns.get(digit, [])
    
    # Calculate cell dimensions for solid appearance
    cell_height = size / 5  # 5 rows
    cell_width = width / 3  # 3 columns
    
    # Helper to draw a filled rectangle
    def draw_rect(x1, y1, x2, y2):
        pen.moveTo((x1, y1))
        pen.lineTo((x2, y1))
        pen.lineTo((x2, y2))
        pen.lineTo((x1, y2))
        pen.closePath()
    
    # Draw each cell in the pattern
    for col, row in pattern:
        # Calculate cell position
        cell_x = x + col * cell_width
        cell_y = y + row * cell_height
        
        # Draw the cell
        draw_rect(cell_x, cell_y, cell_x + cell_width, cell_y + cell_height)
