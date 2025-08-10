import imageio,os

images_list = sorted(os.listdir("12-Gif/images"))

IMAGE = []
for image_name in images_list:
    path = f"12-Gif/images/{image_name}"
    image = imageio.imread(path,)
    IMAGE.append(image)

imageio.mimsave("12-Gif/result.gif",IMAGE)

