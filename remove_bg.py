from PIL import Image, ImageSequence

def remove_background(input_path, output_path):
    try:
        im = Image.open(input_path)
        
        # Get the background color from the top-left pixel of the first frame
        bg_color = im.convert("RGB").getpixel((0, 0))
        print(f"Detected background color: {bg_color}")

        frames = []
        for frame in ImageSequence.Iterator(im):
            frame = frame.convert("RGBA")
            datas = frame.getdata()

            new_data = []
            for item in datas:
                # Check if the pixel matches the background color (with some tolerance if needed)
                # Here we do exact match for simplicity first
                if item[0] == bg_color[0] and item[1] == bg_color[1] and item[2] == bg_color[2]:
                    new_data.append((255, 255, 255, 0)) # Transparent
                else:
                    new_data.append(item)

            frame.putdata(new_data)
            frames.append(frame)

        # Save as new GIF
        frames[0].save(
            output_path,
            save_all=True,
            append_images=frames[1:],
            optimize=False,
            duration=im.info.get('duration', 100),
            loop=0,
            disposal=2 # Restore to background
        )
        print(f"Successfully saved to {output_path}")

    except Exception as e:
        print(f"Error: {e}")

remove_background('logo.gif', 'logo_transparent.gif')
