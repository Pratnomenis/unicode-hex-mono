"""
Glyph creation and rendering for UnicodeHexMono font.

This module handles the creation of individual glyphs for different Unicode ranges:
- U+FFFD: Replacement character with diagonal X
- U+0000-U+FFFF (BMP): 4-digit hex code in 2x2 grid
- U+10000-U+FFFFF (Planes 1-15): 5-digit hex with large plane digit + 2x2 grid
- U+100000-U+10FFFD (Plane 16): 4-digit hex in 2x2 grid with vertical divider

Each glyph is rendered inside a rounded square border with appropriate styling.
"""

import config
import utils


# ============================================================================
# Glyph Drawing Functions
# ============================================================================

def draw_replacement_character(glyph):
    """
    Draw U+FFFD (replacement character) with a diagonal cross (X) inside.
    This makes it visually distinct from both control characters (empty squares)
    and normal characters (hex codes).
    """
    pen = glyph.glyphPen()
    
    # Draw outer rounded square border
    x_left = config.BOX_MARGIN
    y_bottom = config.GLYPH_Y_OFFSET
    utils.draw_rounded_square(pen, x_left, y_bottom, config.BOX_SIZE, config.CORNER_RADIUS)
    
    # Draw diagonal cross (X) inside
    # Calculate inner area
    inner_size = config.BOX_SIZE - 2 * config.BOX_STROKE_WIDTH
    inner_x = config.BOX_MARGIN + config.BOX_STROKE_WIDTH
    inner_y = config.GLYPH_Y_OFFSET + config.BOX_STROKE_WIDTH
    
    # Add padding for the X
    x1 = inner_x + config.REPLACEMENT_CHAR_PADDING
    y1 = inner_y + config.REPLACEMENT_CHAR_PADDING
    x2 = inner_x + inner_size - config.REPLACEMENT_CHAR_PADDING
    y2 = inner_y + inner_size - config.REPLACEMENT_CHAR_PADDING
    
    line_width = config.BOX_STROKE_WIDTH  # Same thickness as border (40 units)
    
    # Draw first diagonal (\) from top-left to bottom-right
    utils.draw_thick_line(pen, x1, y2, x2, y1, line_width)
    
    # Draw second diagonal (/) from bottom-left to top-right
    utils.draw_thick_line(pen, x1, y1, x2, y2, line_width)
    
    pen = None


def draw_hex_code_2digit(glyph, codepoint):
    """
    Draw a 2-digit hexadecimal code (last 2 digits) in huge size, centered.
    Used for U+0000 to U+00FF (ASCII & Extended ASCII).
    
    Args:
        glyph: FontForge glyph object
        codepoint: Unicode codepoint value (0x0000 to 0x00FF)
    """
    # Convert codepoint to 2-digit hex string (only last 2 digits)
    hex_str = f"{codepoint:02X}"  # e.g., "4A" for U+004A
    
    pen = glyph.glyphPen()
    
    # Draw outer rounded square border
    x_left = config.BOX_MARGIN
    y_bottom = config.GLYPH_Y_OFFSET
    utils.draw_rounded_square(pen, x_left, y_bottom, config.BOX_SIZE, config.CORNER_RADIUS)
    
    # Calculate positioning for 2 huge digits (horizontal layout)
    inner_size = config.BOX_SIZE - 2 * config.BOX_STROKE_WIDTH
    inner_x = config.BOX_MARGIN + config.BOX_STROKE_WIDTH
    inner_y = config.GLYPH_Y_OFFSET + config.BOX_STROKE_WIDTH
    
    # Two digits side by side with spacing
    digit_width = config.TWO_DIGIT_SIZE * 0.6  # Aspect ratio 60%
    total_width = 2 * digit_width + config.GRID_SPACING
    
    # Center the two digits horizontally
    offset_x = (inner_size - total_width) / 2
    offset_y = (inner_size - config.TWO_DIGIT_SIZE) / 2  # Center vertically
    
    # Draw first digit (left)
    utils.draw_hex_digit(pen, hex_str[0],
                         inner_x + offset_x,
                         inner_y + offset_y,
                         config.TWO_DIGIT_SIZE)
    
    # Draw second digit (right)
    utils.draw_hex_digit(pen, hex_str[1],
                         inner_x + offset_x + digit_width + config.GRID_SPACING,
                         inner_y + offset_y,
                         config.TWO_DIGIT_SIZE)
    
    pen = None


def draw_hex_code_2x2(glyph, codepoint):
    """
    Draw a 4-digit hexadecimal code in a 2x2 grid layout inside the glyph.
    
    Args:
        glyph: FontForge glyph object
        codepoint: Unicode codepoint value (0x0100 to 0xFFFF)
    """
    # Convert codepoint to 4-digit hex string
    hex_str = f"{codepoint:04X}"

    pen = glyph.glyphPen()

    # Calculate grid positioning
    # Inner area: BOX_SIZE - 2 * BOX_STROKE_WIDTH
    inner_size = config.BOX_SIZE - 2 * config.BOX_STROKE_WIDTH
    inner_x = config.BOX_MARGIN + config.BOX_STROKE_WIDTH
    inner_y = config.GLYPH_Y_OFFSET + config.BOX_STROKE_WIDTH
    
    # 2x2 grid: each cell gets half the space minus spacing
    cell_width = (inner_size - config.GRID_SPACING) / 2
    cell_height = (inner_size - config.GRID_SPACING) / 2
    
    # Center digits within cells
    digit_width = config.DIGIT_SIZE * 0.65
    offset_x = (cell_width - digit_width) / 2
    offset_y = (cell_height - config.DIGIT_SIZE) / 2
    
    x_left = config.BOX_MARGIN
    y_bottom = config.GLYPH_Y_OFFSET
    utils.draw_rounded_square(pen, x_left, y_bottom, config.BOX_SIZE, config.CORNER_RADIUS)

    # Grid positions (row, col) -> (y_index, x_index)
    # Top-left: hex_str[0]
    utils.draw_hex_digit(pen, hex_str[0], 
                   inner_x + offset_x, 
                   inner_y + cell_height + config.GRID_SPACING + offset_y, 
                   config.DIGIT_SIZE)
    
    # Top-right: hex_str[1]
    utils.draw_hex_digit(pen, hex_str[1], 
                   inner_x + cell_width + config.GRID_SPACING + offset_x, 
                   inner_y + cell_height + config.GRID_SPACING + offset_y, 
                   config.DIGIT_SIZE)
    
    # Bottom-left: hex_str[2]
    utils.draw_hex_digit(pen, hex_str[2], 
                   inner_x + offset_x, 
                   inner_y + offset_y, 
                   config.DIGIT_SIZE)
    
    # Bottom-right: hex_str[3]
    utils.draw_hex_digit(pen, hex_str[3], 
                   inner_x + cell_width + config.GRID_SPACING + offset_x, 
                   inner_y + offset_y, 
                   config.DIGIT_SIZE)
    
    pen = None



def draw_hex_code_5digit_split(glyph, codepoint):
    """
    Draw a 5-digit hexadecimal code with special layout:
    - First digit (plane) is larger on the left
    - Remaining 4 digits in 2x2 grid on the right
    
    Used for U+10000 to U+FFFFF range.
    
    Args:
        glyph: FontForge glyph object
        codepoint: Unicode codepoint value (0x10000 to 0xFFFFF)
    """
    # Convert codepoint to 5-digit hex string
    hex_str = f"{codepoint:05X}"
    
    pen = glyph.glyphPen()
    
    # Draw the rounded square border
    x_left = config.BOX_MARGIN
    y_bottom = config.GLYPH_Y_OFFSET
    utils.draw_rounded_square(pen, x_left, y_bottom, config.BOX_SIZE, config.CORNER_RADIUS)
    
    # Calculate inner area
    inner_size = config.BOX_SIZE - 2 * config.BOX_STROKE_WIDTH
    inner_x = config.BOX_MARGIN + config.BOX_STROKE_WIDTH
    inner_y = config.GLYPH_Y_OFFSET + config.BOX_STROKE_WIDTH
    
    # Calculate vertical padding for reference (this gives us the target horizontal padding)
    cell_height = (inner_size - config.SUPPLEMENTARY_GRID_SPACING) / 2
    vertical_padding = (cell_height - config.DIGIT_SIZE) / 2  # ~75 units
    
    # LEFT SECTION: Large plane digit
    plane_digit = hex_str[0]  # First digit (e.g., 'E' from 'E12AB')
    
    # Position: left side with padding matching vertical padding, vertically centered
    plane_x = inner_x + vertical_padding  # Match vertical padding (~75 units from left edge)
    plane_y = inner_y + (inner_size - config.PLANE_DIGIT_SIZE) / 2  # Vertically centered
    
    utils.draw_hex_digit(pen, plane_digit, plane_x, plane_y, config.PLANE_DIGIT_SIZE)
    
    # RIGHT SECTION: 2x2 grid for remaining 4 digits
    # Calculate grid position to have balanced margins
    plane_digit_width = config.PLANE_DIGIT_SIZE * 0.65  # ~189 units
    grid_start_x = plane_x + plane_digit_width + config.PLANE_SECTION_SPACING
    
    # Calculate available width for grid (accounting for right margin matching vertical padding)
    available_width = inner_size - (grid_start_x - inner_x) - vertical_padding
    
    # 2x2 grid calculations
    cell_width = (available_width - config.SUPPLEMENTARY_GRID_SPACING) / 2
    
    digit_width = config.DIGIT_SIZE * 0.65
    offset_x = (cell_width - digit_width) / 2
    offset_y = vertical_padding  # Use the same padding as calculated above
    
    # Draw 2x2 grid: hex_str[1] to hex_str[4]
    # Top-left: hex_str[1]
    utils.draw_hex_digit(pen, hex_str[1],
                         grid_start_x + offset_x,
                         inner_y + cell_height + config.SUPPLEMENTARY_GRID_SPACING + offset_y,
                         config.DIGIT_SIZE)
    
    # Top-right: hex_str[2]
    utils.draw_hex_digit(pen, hex_str[2],
                         grid_start_x + cell_width + config.SUPPLEMENTARY_GRID_SPACING + offset_x,
                         inner_y + cell_height + config.SUPPLEMENTARY_GRID_SPACING + offset_y,
                         config.DIGIT_SIZE)
    
    # Bottom-left: hex_str[3]
    utils.draw_hex_digit(pen, hex_str[3],
                         grid_start_x + offset_x,
                         inner_y + offset_y,
                         config.DIGIT_SIZE)
    
    # Bottom-right: hex_str[4]
    utils.draw_hex_digit(pen, hex_str[4],
                         grid_start_x + cell_width + config.SUPPLEMENTARY_GRID_SPACING + offset_x,
                         inner_y + offset_y,
                         config.DIGIT_SIZE)
    
    pen = None


def draw_hex_code_2x2_filled(glyph, codepoint):
    """
    Draw a 6-digit hexadecimal code in a 2x2 grid layout with vertical line through middle.
    Same as BMP but with a distinctive vertical line splitting the glyph in half.
    
    Args:
        glyph: FontForge glyph object
        codepoint: Unicode codepoint value (0x100000 to 0x10FFFF)
    """
    # Convert codepoint to 6-digit hex string
    hex_str = f"{codepoint:06X}"
    
    pen = glyph.glyphPen()

    # Draw the same outline square as BMP
    x_left = config.BOX_MARGIN
    y_bottom = config.GLYPH_Y_OFFSET
    utils.draw_rounded_square(pen, x_left, y_bottom, config.BOX_SIZE, config.CORNER_RADIUS_PLANE16)

    # Calculate grid positioning (same as BMP)
    inner_size = config.BOX_SIZE - 2 * config.BOX_STROKE_WIDTH
    inner_x = config.BOX_MARGIN + config.BOX_STROKE_WIDTH
    inner_y = config.GLYPH_Y_OFFSET + config.BOX_STROKE_WIDTH
    
    # 2x2 grid: each cell gets half the space minus spacing
    cell_width = (inner_size - config.GRID_SPACING) / 2
    cell_height = (inner_size - config.GRID_SPACING) / 2
    
    # Center digits within cells
    digit_width = config.DIGIT_SIZE * 0.6
    offset_x = (cell_width - digit_width) / 2
    offset_y = (cell_height - config.DIGIT_SIZE) / 2
    
    # Draw digits (same as BMP - dark on light background)
    # Top-left: hex_str[2]
    utils.draw_hex_digit(pen, hex_str[2], 
                   inner_x + offset_x, 
                   inner_y + cell_height + config.GRID_SPACING + offset_y, 
                   config.DIGIT_SIZE)
    
    # Top-right: hex_str[3]
    utils.draw_hex_digit(pen, hex_str[3], 
                   inner_x + cell_width + config.GRID_SPACING + offset_x, 
                   inner_y + cell_height + config.GRID_SPACING + offset_y, 
                   config.DIGIT_SIZE)
    
    # Bottom-left: hex_str[4]
    utils.draw_hex_digit(pen, hex_str[4], 
                   inner_x + offset_x, 
                   inner_y + offset_y, 
                   config.DIGIT_SIZE)
    
    # Bottom-right: hex_str[5]
    utils.draw_hex_digit(pen, hex_str[5], 
                   inner_x + cell_width + config.GRID_SPACING + offset_x, 
                   inner_y + offset_y, 
                   config.DIGIT_SIZE)
    
    # Add vertical line through the middle
    inner_size = config.BOX_SIZE - 2 * config.BOX_STROKE_WIDTH
    inner_x = config.BOX_MARGIN + config.BOX_STROKE_WIDTH
    inner_y = config.GLYPH_Y_OFFSET + config.BOX_STROKE_WIDTH
    
    # Calculate middle x position
    middle_x = config.BOX_MARGIN + config.BOX_SIZE / 2
    
    # Vertical line from top to bottom of inner area
    line_width = config.BOX_STROKE_WIDTH  # Same thickness as border (40 units)
    utils.draw_thick_line(pen, middle_x, inner_y, middle_x, inner_y + inner_size, line_width)
    
    pen = None




# ============================================================================
# Helper Functions
# ============================================================================

def _draw_notdef_glyph(glyph):
    """
    Draw the .notdef glyph as an outlined rounded square.
    This creates a frame by drawing outer and inner rounded rectangles.
    """
    pen = glyph.glyphPen()
    
    x_left = config.BOX_MARGIN
    y_bottom = config.GLYPH_Y_OFFSET
    
    # Draw outer rounded square (clockwise)
    utils.draw_rounded_square(pen, x_left, y_bottom, config.BOX_SIZE, config.CORNER_RADIUS)
    
    # Draw inner rounded square (counter-clockwise for hole)
    # Calculate inner box dimensions
    inner_margin = config.BOX_STROKE_WIDTH
    inner_size = config.BOX_SIZE - 2 * inner_margin
    inner_radius = max(0, config.CORNER_RADIUS - inner_margin)
    inner_x = x_left + inner_margin
    inner_y = y_bottom + inner_margin
    
    # For a hole, we need to draw counter-clockwise
    # We'll draw the same shape but in reverse
    r = min(inner_radius, inner_size / 2)
    
    # Start from bottom-left, go counter-clockwise
    pen.moveTo((inner_x + r, inner_y))
    
    # Bottom-left arc
    pen.curveTo(
        (inner_x + r * 0.448, inner_y),
        (inner_x, inner_y + r * 0.448),
        (inner_x, inner_y + r)
    )
    
    # Left edge
    pen.lineTo((inner_x, inner_y + inner_size - r))
    
    # Top-left arc
    pen.curveTo(
        (inner_x, inner_y + inner_size - r * 0.448),
        (inner_x + r * 0.448, inner_y + inner_size),
        (inner_x + r, inner_y + inner_size)
    )
    
    # Top edge
    pen.lineTo((inner_x + inner_size - r, inner_y + inner_size))
    
    # Top-right arc
    pen.curveTo(
        (inner_x + inner_size - r * 0.448, inner_y + inner_size),
        (inner_x + inner_size, inner_y + inner_size - r * 0.448),
        (inner_x + inner_size, inner_y + inner_size - r)
    )
    
    # Right edge
    pen.lineTo((inner_x + inner_size, inner_y + r))
    
    # Bottom-right arc
    pen.curveTo(
        (inner_x + inner_size, inner_y + r * 0.448),
        (inner_x + inner_size - r * 0.448, inner_y),
        (inner_x + inner_size - r, inner_y)
    )
    
    # Bottom edge
    pen.lineTo((inner_x + r, inner_y))
    
    pen.closePath()
    pen = None




# ============================================================================
# Main Glyph Creation
# ============================================================================

def create_glyph(font, codepoint):
    """
    Create a single glyph with appropriate rendering based on Unicode range.
    
    Args:
        font: FontForge font object
        codepoint: Unicode codepoint value (0x0000 to 0x10FFFD)
    
    Glyph rendering strategy:
    - U+FFFD: Diagonal X in outlined square
    - U+0000-U+FFFF: 4-digit hex code in 2x2 grid
    - U+10000-U+FFFFF: 5-digit hex (large plane digit + 2x2 grid)
    - U+100000-U+10FFFD: 4-digit hex in 2x2 grid with vertical divider
    """
    # Create or get glyph
    glyph = font.createChar(codepoint)
    
    # Set glyph width (monospaced)
    glyph.width = config.GLYPH_WIDTH
    
    # Clear any existing contours
    glyph.clear()
    
    # Determine which type of rounded square to draw based on codepoint range
    if 0x100000 <= codepoint <= 0x10FFFF:
        # Plane 16: Filled rounded square with last 4 hex digits in 2x2 grid
        draw_hex_code_2x2_filled(glyph, codepoint)
    elif 0x10000 <= codepoint <= 0xFFFFF:
        # Supplementary Planes 1-15: Outlined square with plane digit + 2x2 grid
        draw_hex_code_5digit_split(glyph, codepoint)
    elif 0x0000 <= codepoint <= 0xFFFF:
        # BMP: Check for special cases
        if codepoint == 0xFFFD:
            # U+FFFD replacement character: Square with diagonal X
            draw_replacement_character(glyph)
        elif 0x0000 <= codepoint <= 0x00FF:
            # ASCII & Extended ASCII: 2-digit huge display
            draw_hex_code_2digit(glyph, codepoint)
        else:
            # Other BMP (U+0100-U+FFFC): 4-digit hex in 2x2 grid
            draw_hex_code_2x2(glyph, codepoint)
    else:
        # Fallback: outlined square (this shouldn't normally be reached)
        _draw_notdef_glyph(glyph)


def create_notdef_glyph(font):
    """
    Create the .notdef glyph (displayed for undefined characters).
    Renders as an outlined rounded square.
    
    Args:
        font: FontForge font object
    
    Returns:
        The created .notdef glyph object
    """
    notdef = font.createChar(-1, ".notdef")
    notdef.width = config.GLYPH_WIDTH
    _draw_notdef_glyph(notdef)
    return notdef


# ============================================================================
# Font Validation
# ============================================================================

def validate_font_glyphs(font):
    """
    Validate that all glyphs in the font have proper outlines.
    Remove any glyphs that are empty or invalid.
    
    Args:
        font: FontForge font object
    """
    glyphs_to_remove = []
    
    for glyph in font.glyphs():
        # Skip .notdef
        if glyph.glyphname == ".notdef":
            continue
        
        # Check if glyph has any contours
        if not glyph.foreground or len(glyph.foreground) == 0:
            # Glyph has no outline data
            glyphs_to_remove.append(glyph.encoding)
    
    # Remove invalid glyphs
    for encoding in glyphs_to_remove:
        if encoding >= 0:
            font.removeGlyph(encoding)
