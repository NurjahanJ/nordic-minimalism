#!/usr/bin/env python3
"""
Nordic Minimalism AI Image Generator
Generates authentic Nordic design visuals for the website
"""

import os
import json
import argparse
import subprocess
from pathlib import Path
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv
import requests
from PIL import Image

class NordicImageGenerator:
    """AI image generator for Nordic Minimalism website"""
    
    def __init__(self):
        # Load environment
        load_dotenv()
        
        self.root = Path(__file__).parent
        self.images_dir = self.root / "images"
        self.db_file = self.root / "nordic_images.json"
        
        # Initialize OpenAI
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in .env file")
        
        self.client = OpenAI(api_key=api_key)
        
        # Load/create image database
        self.db = self.load_db()
        
        # Nordic image categories
        self.categories = {
            'hero': 'hero',
            'textures': 'textures',
            'patterns': 'patterns',
            'materials': 'materials',
            'lifestyle': 'lifestyle',
            'nature': 'nature',
            'interiors': 'interiors'
        }
        
        print("Nordic Image Generator Ready")
    
    def load_db(self):
        """Load image database"""
        if self.db_file.exists():
            with open(self.db_file, 'r') as f:
                return json.load(f)
        return {"images": {}, "last_updated": None}
    
    def save_db(self):
        """Save image database"""
        self.db["last_updated"] = datetime.now().isoformat()
        with open(self.db_file, 'w') as f:
            json.dump(self.db, f, indent=2)
    
    def get_category_from_name(self, image_name):
        """Auto-detect category from image name"""
        for category in self.categories:
            if image_name.startswith(category):
                return category
        
        # Fallback based on common patterns
        if 'hero' in image_name or 'banner' in image_name:
            return 'hero'
        elif 'texture' in image_name or 'wood' in image_name or 'stone' in image_name:
            return 'textures'
        elif 'pattern' in image_name or 'geometric' in image_name:
            return 'patterns'
        elif 'material' in image_name or 'fabric' in image_name:
            return 'materials'
        elif 'lifestyle' in image_name or 'living' in image_name:
            return 'lifestyle'
        elif 'nature' in image_name or 'landscape' in image_name:
            return 'nature'
        elif 'interior' in image_name or 'room' in image_name:
            return 'interiors'
        else:
            return 'hero'  # Default
    
    def generate_nordic_prompt(self, image_name, user_prompt=None):
        """Generate Nordic-specific prompts based on authentic design principles"""
        
        # Base Nordic aesthetic principles
        base_context = """Professional photography in authentic Nordic minimalism style, 
        warm and inviting atmosphere, natural materials, soft lighting, 
        muted earth tones, hygge feeling, lagom balance, democratic design principles"""
        
        # Specific Nordic contexts based on image name
        nordic_contexts = {
            # Hero images
            'hero-main': 'Scandinavian living room with natural light streaming through large windows, birch wood furniture, linen textiles, sage green accents, cozy hygge atmosphere',
            'hero-philosophy': 'Minimalist Nordic workspace with natural wood desk, simple ceramic objects, soft natural lighting, warm neutral colors, calm and balanced composition',
            'hero-principles': 'Nordic interior showcasing lagom principle - not too much, not too little, perfect balance of furniture and space, natural materials, warm whites',
            
            # Texture backgrounds
            'texture-birch-wood': 'Close-up of beautiful birch wood grain texture, natural blonde wood, soft organic patterns, warm lighting, high resolution detail',
            'texture-linen-fabric': 'Natural linen fabric texture in warm off-white, organic weave pattern, soft and tactile appearance, Nordic textile aesthetic',
            'texture-stone-surface': 'Smooth limestone or sandstone texture, warm beige tones, natural surface variations, Scandinavian material aesthetic',
            'texture-wool-knit': 'Chunky wool knit texture in cream or oatmeal color, cozy Nordic textile, soft shadows, hygge feeling',
            
            # Geometric patterns
            'pattern-nordic-geometric': 'Subtle geometric pattern inspired by Nordic design, soft lines, warm neutral colors, minimal and elegant',
            'pattern-organic-shapes': 'Organic flowing shapes in muted Nordic colors, inspired by Scandinavian landscapes, soft and natural',
            
            # Material close-ups
            'material-ceramic': 'Handcrafted ceramic objects in Nordic style, matte finish, warm earth tones, simple elegant forms',
            'material-glass': 'Nordic glassware with clean lines, clear or slightly tinted, natural light reflections, minimalist aesthetic',
            
            # Lifestyle scenes
            'lifestyle-hygge': 'Cozy Nordic lifestyle scene, person reading with warm blanket, candles, natural light, comfortable and inviting',
            'lifestyle-lagom': 'Perfectly balanced Nordic scene showing lagom principle, organized space with just enough objects, calm atmosphere',
            
            # Nature inspiration
            'nature-scandinavian-forest': 'Scandinavian forest with birch trees, soft natural light filtering through leaves, peaceful and serene',
            'nature-nordic-landscape': 'Nordic landscape with rolling hills, muted colors, soft light, inspiring natural beauty',
            
            # Interior elements
            'interior-nordic-kitchen': 'Nordic kitchen with light wood cabinets, white counters, natural materials, clean lines, warm atmosphere',
            'interior-living-space': 'Scandinavian living space with natural light, neutral colors, organic shapes, cozy textiles, minimal furniture'
        }
        
        context = nordic_contexts.get(image_name, "Nordic minimalism inspired scene with natural materials, warm lighting, and calm atmosphere")
        
        # Nordic color palette guidance
        color_guidance = """Use authentic Nordic color palette: warm whites (#FAFAF9), 
        linen (#F5F4F0), sage green (#8B9A8A), warm taupe (#B4A89A), 
        natural wood tones, soft grays, never pure white or black"""
        
        if user_prompt:
            prompt = f"{base_context}, {user_prompt}, {context}, {color_guidance}"
        else:
            prompt = f"{base_context}, {context}, {color_guidance}"
        
        return prompt
    
    def generate_alt_text(self, image_name, prompt):
        """Generate SEO-optimized alt text for Nordic images"""
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Generate concise, SEO-optimized alt text for Nordic minimalism images. Focus on visual elements and Nordic design principles. Keep under 125 characters."},
                    {"role": "user", "content": f"Generate alt text for a Nordic minimalism image: {prompt}"}
                ],
                max_tokens=50
            )
            
            alt_text = response.choices[0].message.content.strip()
            alt_text = alt_text.strip('"\'')
            
            return alt_text
            
        except Exception as e:
            print(f"Alt text generation failed: {e}")
            # Fallback alt text
            fallbacks = {
                'hero-main': 'Nordic minimalist living room with natural light and warm materials',
                'texture-birch-wood': 'Natural birch wood grain texture in Nordic style',
                'texture-linen-fabric': 'Warm linen fabric texture for Nordic minimalism',
                'pattern-nordic-geometric': 'Subtle geometric pattern in Nordic design style',
                'lifestyle-hygge': 'Cozy Nordic lifestyle scene embodying hygge principles',
                'nature-scandinavian-forest': 'Peaceful Scandinavian forest with birch trees'
            }
            
            return fallbacks.get(image_name, f"Nordic minimalism {image_name.replace('-', ' ')}")
    
    def generate_image(self, image_name, prompt):
        """Generate image using DALL-E with Nordic specifications"""
        
        print(f"Generating Nordic image: {image_name}")
        print(f"Prompt: {prompt}")
        
        try:
            response = self.client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1024",  # Square format good for Nordic layouts
                quality="hd",      # High quality for design use
                n=1
            )
            
            image_url = response.data[0].url
            
            # Download image
            img_response = requests.get(image_url)
            img_response.raise_for_status()
            
            return img_response.content
            
        except Exception as e:
            print(f"Image generation failed: {e}")
            raise
    
    def save_image(self, image_name, image_data):
        """Save image with multiple sizes optimized for web use"""
        
        category = self.get_category_from_name(image_name)
        category_dir = self.images_dir / self.categories[category]
        
        # Ensure directory exists
        category_dir.mkdir(parents=True, exist_ok=True)
        
        # Save original image first
        temp_path = category_dir / f"{image_name}_temp.jpg"
        
        with open(temp_path, 'wb') as f:
            f.write(image_data)
        
        try:
            with Image.open(temp_path) as img:
                # Convert to RGB if necessary
                if img.mode in ('RGBA', 'P'):
                    img = img.convert('RGB')
                
                # Generate multiple sizes for responsive design
                sizes = [
                    (1200, f"{image_name}.jpg"),      # Full size
                    (1200, f"{image_name}.webp"),     # Full size WebP
                    (800, f"{image_name}_800w.jpg"),  # Medium
                    (800, f"{image_name}_800w.webp"), # Medium WebP
                    (400, f"{image_name}_400w.jpg"),  # Small
                    (400, f"{image_name}_400w.webp")  # Small WebP
                ]
                
                saved_files = []
                
                for width, filename in sizes:
                    # Calculate height maintaining aspect ratio
                    aspect_ratio = img.height / img.width
                    height = int(width * aspect_ratio)
                    
                    # Resize image
                    resized = img.resize((width, height), Image.Resampling.LANCZOS)
                    
                    # Save path
                    save_path = category_dir / filename
                    
                    # Save based on format
                    if filename.endswith('.webp'):
                        resized.save(save_path, 'WEBP', quality=90, optimize=True)
                    else:
                        resized.save(save_path, 'JPEG', quality=90, optimize=True)
                    
                    saved_files.append(str(save_path))
                    print(f"Saved: {save_path}")
                
                # Clean up temp file
                temp_path.unlink()
                
                # Return main image path
                main_path = category_dir / f"{image_name}.jpg"
                return str(main_path)
                
        except Exception as e:
            print(f"Image processing failed: {e}")
            # Fallback - just save the original
            main_path = category_dir / f"{image_name}.jpg"
            temp_path.rename(main_path)
            return str(main_path)
    
    def generate_nordic_image(self, image_name, user_prompt=None):
        """Complete workflow: generate Nordic image, save, update database"""
        
        print(f"\nGenerating Nordic image: {image_name}")
        
        # Generate Nordic-specific prompt
        prompt = self.generate_nordic_prompt(image_name, user_prompt)
        
        # Generate image
        image_data = self.generate_image(image_name, prompt)
        
        # Save image
        image_path = self.save_image(image_name, image_data)
        
        # Generate alt text
        alt_text = self.generate_alt_text(image_name, prompt)
        
        # Update database
        self.db["images"][image_name] = {
            "filename": f"{image_name}.jpg",
            "path": image_path,
            "alt_text": alt_text,
            "prompt": prompt,
            "user_prompt": user_prompt,
            "generated": datetime.now().isoformat(),
            "category": self.get_category_from_name(image_name),
            "style": "nordic_minimalism"
        }
        
        self.save_db()
        
        print(f"Nordic image generated successfully!")
        print(f"Path: {image_path}")
        print(f"Alt text: {alt_text}")
        
        return True
    
    def list_images(self):
        """List all generated Nordic images"""
        
        print("\nGenerated Nordic Images:")
        print("=" * 60)
        
        if not self.db["images"]:
            print("No images generated yet.")
            return
        
        for name, data in self.db["images"].items():
            print(f"\n{name}")
            print(f"   Category: {data['category']}")
            print(f"   Style: {data.get('style', 'nordic_minimalism')}")
            print(f"   Alt text: {data['alt_text']}")
            print(f"   Generated: {data['generated'][:19]}")
            if data.get('user_prompt'):
                print(f"   Custom prompt: {data['user_prompt']}")
    
    def generate_suggested_images(self):
        """Generate a set of suggested Nordic images for the website"""
        
        suggested_images = [
            ('hero-main', 'Main hero image showcasing Nordic minimalism principles'),
            ('texture-birch-wood', 'Natural birch wood texture for backgrounds'),
            ('texture-linen-fabric', 'Linen fabric texture for warmth'),
            ('pattern-nordic-geometric', 'Subtle geometric pattern for visual interest'),
            ('lifestyle-hygge', 'Cozy lifestyle scene embodying hygge'),
            ('nature-scandinavian-forest', 'Peaceful Nordic forest scene'),
            ('interior-living-space', 'Nordic living space example')
        ]
        
        print("Generating suggested Nordic images for your website...")
        
        for image_name, description in suggested_images:
            print(f"\n--- Generating: {image_name} ---")
            try:
                self.generate_nordic_image(image_name, description)
            except Exception as e:
                print(f"Failed to generate {image_name}: {e}")
                continue
        
        print("\n✅ Suggested Nordic images generation complete!")

def main():
    """CLI interface for Nordic Image Generator"""
    
    parser = argparse.ArgumentParser(description='Nordic Minimalism AI Image Generator')
    
    parser.add_argument('--generate', type=str, help='Generate specific Nordic image (e.g., hero-main)')
    parser.add_argument('--prompt', type=str, help='Custom prompt for image generation')
    parser.add_argument('--list', action='store_true', help='List all generated images')
    parser.add_argument('--suggested', action='store_true', help='Generate suggested Nordic images')
    
    args = parser.parse_args()
    
    try:
        generator = NordicImageGenerator()
        
        if args.list:
            generator.list_images()
            
        elif args.generate:
            success = generator.generate_nordic_image(args.generate, args.prompt)
            if success:
                print(f"\n✅ Nordic image '{args.generate}' generated successfully!")
                
        elif args.suggested:
            generator.generate_suggested_images()
            
        else:
            parser.print_help()
            print("\nExample usage:")
            print("python nordic_image_generator.py --generate hero-main")
            print("python nordic_image_generator.py --generate texture-birch-wood --prompt 'close-up detail'")
            print("python nordic_image_generator.py --suggested")
            print("python nordic_image_generator.py --list")
            
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0

if __name__ == '__main__':
    exit(main())
