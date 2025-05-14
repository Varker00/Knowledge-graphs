import os
import sys
import json
import time
from selenium import webdriver
from PIL import Image
from pyvis.network import Network


def main():
    input_path = sys.argv[1] if len(sys.argv) > 1 else "../json"
    output_path = sys.argv[2] if len(sys.argv) > 2 else "../graphs"

    net = Network(height="800px", width="100%", directed=True, notebook=False)

    for filename in os.listdir(input_path):
        if filename.endswith(".json"):
            with open(os.path.join(input_path, filename), 'r', encoding='utf-8') as f:
                data = json.load(f)
                for item in data:
                    node1 = item["node_1"]
                    node2 = item["node_2"]
                    edge_label = item["edge"]
                    weight = item.get("weight", 1)
                    net.add_node(node1, label=node1)
                    net.add_node(node2, label=node2)

                    # Add edge with label
                    net.add_edge(node1, node2, label=edge_label, weight=weight)

    html_path = f"{output_path}/knowledge_graph.html"
    net.save_graph(html_path)

if __name__ == '__main__':
    main()
