


from cfg import YOLOv10,  device, config

def train():

    print(f'device: {device}')
    model = YOLOv10(config["model_path"]);model.to(device)
    
    model.train( data   = config["yaml_path"] ,
                epochs  = config["epochs"],
                batch   = config["batch_size"],
                imgsz   = config["img_size"] )


if __name__ == "__main__":
    train()