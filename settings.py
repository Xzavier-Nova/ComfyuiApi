import uuid
import requests
from PIL import Image


def get_uuid():
    # 生成uuid
    return str(uuid.uuid4())


class ComfyuiScheduler:
    base_host = 'http://127.0.0.1:8188'

    def __init__(self, workflow_api, username='default'):
        self.username = username  # 用户名作为文件夹名称，用以隔离不同用户的文件。
        self.client_id = get_uuid()  # 核心！通过这个id来追踪任务进度。
        self.workflow_api = workflow_api

    def push_task(self):
        res = requests.post(
            f'{self.base_host}/prompt',
            json=self.workflow_api
        )

    def get_queue(self):
        # 获取队列信息，用于计算自己的任务处在当前队列位置。
        res = requests.get(
            f'{self.base_host}/queue'
        )

    def get_task_status(self):
        # 可以获取更加详细的点给钱任务的执行进度。需要搭配相关解析器~
        res = requests.get(
            f'{self.base_host}/ws?clientId={self.client_id}'
        )

    def task_status_parser(self):
        # 获取任务状态的解析器
        pass

    def upload_image(self, image: Image.Image):
        image_bytes = image.tobytes()
        if image.mode == 'RGBA':
            image_suffix_name = 'png'
        else:
            image_suffix_name = 'jpg'
        image_name = f'{self.username}_{self.client_id}_.{image_suffix_name}'
        res = requests.post(
            f'{self.base_host}/upload/image',
            files={'image': (f'{self.username}/{image_name}.{image_suffix_name}', image_bytes, 'image/png')},
            data={

            }
        )
