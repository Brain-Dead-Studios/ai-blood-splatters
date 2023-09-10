import openai
import uuid
import requests

def gen_variations(fname, num_variations = 1):
    source_img = open(fname, "rb")
    response = openai.Image.create_variation(
        image = source_img,
        n = num_variations,
        size="512x512"
    )

    print(response)

    filename = fname.split("/")[-1].split(".")[0]

    for i in range(num_variations):
        url = response["data"][i]["url"]
        with open("generated/" + filename + "_" + str(uuid.uuid4()) + ".png", "wb") as f:
            f.write(requests.get(url).content)

if __name__ == "__main__":
    for i in range(1, 9):
        gen_variations("512/bloodsplatter" + str(i) + ".png", 4)