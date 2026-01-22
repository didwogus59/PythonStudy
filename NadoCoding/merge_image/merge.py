from PIL import Image

def mergeImage(path, option, files, onProgress) :
    images = [Image.open(file) for file in files]
    
    widths, heights = zip(*[image.size for image in images])
    
    maxWidths = max(widths)
    totalHeights = sum(heights)

    merged = Image.new("RGB", (maxWidths, totalHeights), (0,0,0))
    y_offset = 0
    gap = 0
    width = -1
    format = "jpg"
    #Set Image Width
    if option[0] == 1 :
        width = 1024
    elif option[0] == 2 :
        width = 800
    elif option[0] == 3 :
        width = 640

    #Set Image Gap
    if option[1] == 1 :
        gap = 30
    elif option[1] == 2 :
        gap = 50
    elif option[1] == 3 :
        gap = 70

    #Set Image Format
    if option[1] == 1 :
        format = "png"
    elif option[1] == 2 :
        format = "bmp"

    for idx, image in enumerate(images) :
        resizedY = image.size[1]
        resized = image
        if width != -1 :
            resizedY = int(image.size[1] * width / image.size[0])
            resized = image.resize((width, resizedY))
        merged.paste(resized, (0, y_offset))
        y_offset += resizedY + gap
        progress = (idx + 1 ) / len(images) * 100
        onProgress(progress)
    
    print(format)
    file_name = "/merged." + format
    merged.save(path + file_name)
    pass