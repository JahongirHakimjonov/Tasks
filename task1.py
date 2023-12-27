import asyncio
import os

import httpx


class FileManager:
    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode

    def __enter__(self):
        self.file = open(file=self.file_path, mode=self.mode)
        return self.file

    def __exit__(self, *args, **kwargs):
        self.file.close()


async def send_request(url, data):
    async with httpx.AsyncClient() as client:
        response = await client.post(url, data=data)
        return response.status_code


def read_fruit_data(file_path):
    with FileManager(file_path, "r") as file:
        file_data = [line.strip() for line in file]
        fruit_data = {
            "name": file_data[0],
            "price": int(file_data[1].split()[0]),
            "text": file_data[2]
        }
    return fruit_data


async def main():
    url = 'http://164.92.64.76/desc/'
    folder_path = 'descriptions'
    files = os.listdir(folder_path)

    with FileManager("results.txt", "w") as results_file:
        for i, file in enumerate(files, start=1):
            if file.endswith('.txt'):
                fruit_data = read_fruit_data(os.path.join(folder_path, file))
                response = await send_request(url, fruit_data)
                response_text = f"Results: {str(i).zfill(3)}.txt , {response}\n"
                results_file.write(response_text)


asyncio.run(main())
