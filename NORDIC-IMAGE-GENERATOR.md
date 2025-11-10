# Nordic Minimalism AI Image Generator

## Overview

This AI-powered image generator creates authentic Nordic minimalism visuals for your website using OpenAI's DALL-E 3. It's specifically designed to generate images that embody authentic Scandinavian design principles like **Lagom**, **Hygge**, and **Democratic Design**.

## Features

- ✅ **Authentic Nordic Aesthetics** - Generates images following genuine Scandinavian design principles
- ✅ **Multiple Categories** - Hero images, textures, patterns, materials, lifestyle scenes
- ✅ **Responsive Sizes** - Auto-generates multiple sizes and WebP formats
- ✅ **SEO Optimized** - AI-generated alt text for accessibility
- ✅ **Database Tracking** - Keeps track of all generated images
- ✅ **Nordic Color Palette** - Uses authentic warm neutrals and natural tones

## Setup

### 1. Install Dependencies
```bash
pip install -r requirements-ai.txt
```

### 2. Get OpenAI API Key
1. Visit [OpenAI Platform](https://platform.openai.com/api-keys)
2. Create an account and get your API key
3. Copy `.env.example` to `.env`
4. Add your API key to `.env`:
```bash
cp .env.example .env
# Edit .env and add your key
OPENAI_API_KEY=your_actual_api_key_here
```

### 3. Create Images Directory
```bash
mkdir -p images/{hero,textures,patterns,materials,lifestyle,nature,interiors}
```

## Usage

### Generate Suggested Nordic Images
```bash
# Generate a complete set of Nordic images for your website
python nordic_image_generator.py --suggested
```

This creates:
- `hero-main` - Main hero image showcasing Nordic principles
- `texture-birch-wood` - Natural birch wood texture
- `texture-linen-fabric` - Warm linen fabric texture
- `pattern-nordic-geometric` - Subtle geometric patterns
- `lifestyle-hygge` - Cozy hygge lifestyle scene
- `nature-scandinavian-forest` - Peaceful Nordic forest
- `interior-living-space` - Nordic living space example

### Generate Specific Images
```bash
# Generate specific Nordic image
python nordic_image_generator.py --generate hero-main

# Generate with custom prompt
python nordic_image_generator.py --generate texture-wool-knit --prompt "chunky cream wool texture with soft shadows"

# Generate lifestyle scene
python nordic_image_generator.py --generate lifestyle-lagom --prompt "perfectly balanced Nordic workspace"
```

### List Generated Images
```bash
python nordic_image_generator.py --list
```

## Image Categories

### Hero Images
- `hero-main` - Main website hero
- `hero-philosophy` - Philosophy section background
- `hero-principles` - Design principles showcase

### Textures (Perfect for CSS backgrounds)
- `texture-birch-wood` - Natural birch wood grain
- `texture-linen-fabric` - Warm linen weave
- `texture-stone-surface` - Smooth limestone/sandstone
- `texture-wool-knit` - Cozy wool knit patterns

### Patterns
- `pattern-nordic-geometric` - Subtle geometric shapes
- `pattern-organic-shapes` - Flowing natural forms

### Materials
- `material-ceramic` - Handcrafted Nordic ceramics
- `material-glass` - Clean Nordic glassware

### Lifestyle
- `lifestyle-hygge` - Cozy Danish hygge scenes
- `lifestyle-lagom` - Swedish lagom balance

### Nature
- `nature-scandinavian-forest` - Birch forests
- `nature-nordic-landscape` - Rolling Nordic hills

### Interiors
- `interior-nordic-kitchen` - Scandinavian kitchen design
- `interior-living-space` - Nordic living rooms

## Nordic Design Principles Built-In

The generator automatically incorporates authentic Nordic principles:

### Color Palette
- Warm whites (`#FAFAF9`) instead of pure white
- Linen tones (`#F5F4F0`) for warmth
- Sage green (`#8B9A8A`) for natural accents
- Warm taupe (`#B4A89A`) for earthiness
- Natural wood tones and soft grays

### Aesthetic Guidelines
- **Lagom** - Perfect balance, not too much or too little
- **Hygge** - Warm, cozy, inviting atmosphere
- **Natural Materials** - Wood, linen, stone, ceramic
- **Soft Lighting** - Natural, diffused illumination
- **Organic Shapes** - Gentle curves and natural forms

## File Structure

Generated images are organized by category:
```
images/
├── hero/
│   ├── hero-main.jpg
│   ├── hero-main.webp
│   ├── hero-main_800w.jpg
│   └── hero-main_400w.jpg
├── textures/
│   ├── texture-birch-wood.jpg
│   └── texture-linen-fabric.jpg
├── patterns/
├── materials/
├── lifestyle/
├── nature/
└── interiors/
```

## Integration with Your Website

### Using Generated Images in CSS
```css
/* Hero section with generated Nordic background */
.hero {
    background-image: url('images/hero/hero-main.webp');
    background-size: cover;
    background-position: center;
}

/* Subtle texture overlays */
.section::before {
    content: '';
    background-image: url('images/textures/texture-linen-fabric_400w.webp');
    opacity: 0.05;
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
}
```

### Using in HTML
```html
<!-- Responsive Nordic image -->
<picture>
    <source srcset="images/lifestyle/lifestyle-hygge.webp" type="image/webp">
    <img src="images/lifestyle/lifestyle-hygge.jpg" 
         alt="Cozy Nordic lifestyle scene embodying hygge principles"
         loading="lazy">
</picture>
```

## Database Tracking

All generated images are tracked in `nordic_images.json`:
```json
{
  "images": {
    "hero-main": {
      "filename": "hero-main.jpg",
      "path": "/path/to/images/hero/hero-main.jpg",
      "alt_text": "Nordic minimalist living room with natural light",
      "category": "hero",
      "style": "nordic_minimalism",
      "generated": "2024-11-10T14:30:00"
    }
  }
}
```

## Cost Considerations

- **DALL-E 3 HD**: ~$0.080 per image
- **Suggested set**: ~$0.56 for 7 core images
- **Custom images**: Generate as needed

## Tips for Best Results

### Effective Prompts
- Mention specific Nordic elements: "birch wood", "linen", "hygge"
- Include lighting: "soft natural light", "warm diffused lighting"
- Specify atmosphere: "calm", "inviting", "balanced"
- Reference colors: "warm whites", "sage green", "natural wood tones"

### Nordic-Specific Keywords
- **Materials**: birch, linen, wool, ceramic, stone
- **Colors**: sage, taupe, cream, oatmeal, warm gray
- **Atmosphere**: hygge, lagom, cozy, calm, balanced
- **Style**: Scandinavian, Nordic, minimalist, natural

## Troubleshooting

### API Key Issues
```bash
# Check if .env file exists and has correct key
cat .env
# Should show: OPENAI_API_KEY=sk-...
```

### Image Generation Fails
- Check internet connection
- Verify OpenAI API key is valid
- Ensure sufficient API credits

### Directory Permissions
```bash
# Create directories with proper permissions
mkdir -p images/{hero,textures,patterns,materials,lifestyle,nature,interiors}
chmod 755 images/
```

## Examples

### Generate Hero Image
```bash
python nordic_image_generator.py --generate hero-main --prompt "Scandinavian living room with large windows, birch furniture, linen textiles, warm natural light, hygge atmosphere"
```

### Generate Texture for CSS Background
```bash
python nordic_image_generator.py --generate texture-birch-wood --prompt "close-up birch wood grain, natural blonde color, organic texture, soft lighting"
```

### Generate Lifestyle Scene
```bash
python nordic_image_generator.py --generate lifestyle-hygge --prompt "cozy reading nook with wool blanket, candles, natural light, Nordic interior"
```

---

**This tool transforms your Nordic Minimalism website from text-heavy to visually compelling while maintaining authentic Scandinavian design principles.**
