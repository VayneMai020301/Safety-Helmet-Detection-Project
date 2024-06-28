
from cfg import os, glob, shutil,tqdm, YOLOv10
from cfg import device, RESULT_PATH, MODEL_PATH, MODEL_HELMET_PATH

if os.path.exists(RESULT_PATH):
    shutil.rmtree(RESULT_PATH)
os.mkdir(RESULT_PATH)

def __test(image_path):

    model = YOLOv10(MODEL_HELMET_PATH); model.to(device)
    result = model(source = image_path, conf = 0.4)

    return result
i = 10
if __name__ == "__main__":
    for index,path in tqdm.tqdm(enumerate(glob.glob("Safety_Helmet_Dataset/test/images/*.jpg"))):

        __test(path)[0].save(f"{RESULT_PATH}/helmet_detection_{index}.png")
        if (i ==4) :break
        i+=1