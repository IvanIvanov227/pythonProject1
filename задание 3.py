from PIL import ImageDraw


class FishImageDraw(ImageDraw.ImageDraw):
    def __init__(self, img):
        super().__init__(img)
        self.image = ImageDraw.Draw(img)
        self.img = img

    def fish(self, xy, fill):
        x = xy[0]
        y = xy[1]
        w = xy[2]
        d = xy[3]
        self.image.ellipse((x, y, w + x, (d // 2 * 3) + y), fill=fill[0])
        self.image.ellipse(((x + d) - d//4, y + d//2, (x + d) + d//4, y + d), fill=fill[1])
        self.image.rectangle((x + (w//2) - d, y - d//4, x + w//2 + d, y), fill=fill[2])
        self.image.polygon([(x + w, y + (3 * d // 4)), (x + w + d, y), (x + w + d, y + (3 * d // 2))], fill=fill[2])
