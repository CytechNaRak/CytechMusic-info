from PIL import Image, ImageSequence, ImageDraw, ImageOps

def crop_to_circle_gif(input_path, output_path):
    try:
        im = Image.open(input_path)
        
        frames = []
        
        # Determine the size for the circular crop (use the smaller dimension)
        size = min(im.size)
        
        # Create a circular mask
        mask = Image.new('L', (size, size), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, size, size), fill=255)
        
        for frame in ImageSequence.Iterator(im):
            # Convert to RGBA
            frame = frame.convert("RGBA")
            
            # Center crop the frame to a square
            frame = ImageOps.fit(frame, (size, size), centering=(0.5, 0.5))
            
            # Apply the mask
            frame.putalpha(mask)
            
            frames.append(frame)

        # Save as new GIF
        # Note: transparency=0 might be needed for some viewers, or disposal=2
        frames[0].save(
            output_path,
            save_all=True,
            append_images=frames[1:],
            optimize=False,
            duration=im.info.get('duration', 100),
            loop=0,
            disposal=2
        )
        print(f"Successfully saved circular cropped GIF to {output_path}")

    except Exception as e:
        print(f"Error: {e}")

crop_to_circle_gif('logo.gif', 'logo_circle.gif')
