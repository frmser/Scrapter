import base64
import cv2
from fastapi import WebSocket, FastAPI

import barcode
import robot

app = FastAPI()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    print("started")
    await websocket.accept()
    try:
        while True:
            json = await websocket.receive_json()
            # print(f"Received packet: {json['type']}")
            if json['type'] == "image":
                with open("imageToSave.jpg", "wb") as fh:
                    # print(json['data']["base64"])
                    print("received image")
                    img = base64.b64decode(json['data']["base64"].replace("data:image/jpeg;base64,", ""))
                    fh.write(img)
                    name, classification, imgurl = barcode.scan()
                    if (name == ''):
                        print("no match")
                        await websocket.send_json({})
                    else:
                        await websocket.send_json({"name": name, "productType": classification, "image": imgurl})
                        print(name)
                        print(classification)
                        robot.move(classification)


    except Exception as e:
        print(e)
    finally:
        await websocket.close()
