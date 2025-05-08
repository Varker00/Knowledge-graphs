import os
import json
import time
from selenium import webdriver
from PIL import Image
from pyvis.network import Network


def main():
    for category in ["Animals", "People"]:
        input_path = f"./json/{category}"
        output_path = "./graphs"

        net = Network(height="800px", width="100%", directed=True, notebook=False)

        for filename in os.listdir(input_path):
            if filename.endswith(".json"):
                with open(os.path.join(input_path, filename), 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for item in data:
                        node1 = item["node_1"]
                        node2 = item["node_2"]
                        edge_label  = item["edge"]
                        net.add_node(node1, label=node1)
                        net.add_node(node2, label=node2)

                        # Add edge with label
                        net.add_edge(node1, node2, label=edge_label)
        html_path = f"{output_path}/Html/knowledge_graph_{category}.html"
        image_path = f"{output_path}/Images/{category}.png"
        net.save_graph(html_path)
        # Display html for user
        # net.show(html_path, notebook=False)

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Run in headless mode
        driver = webdriver.Chrome(options=options)

        driver.get(f'file://{os.path.abspath(html_path)}')

        time.sleep(3)

        driver.save_screenshot(image_path)

        image = Image.open(image_path)
        # Define the area to crop (left, top, right, bottom)
        image_cropped = image.crop((0, 0, image.width, image.height))
        image_cropped.save(image_path)

        driver.quit()

if __name__ == '__main__':
    main()


