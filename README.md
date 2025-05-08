# Visual knowledge graph generator
## Installation
### 1. Clone the repository
```bash
git clone https://github.com/Varker00/Knowledge-graphs.git
cd Knowledge-graphs
```

### 2. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```


## Running the script

Place your `.json` files in the `json/` directory. Each file should contain a list of graph edges. Example format:

```json
[
    {
        "node_1": "cat", 
        "node_2": "fish",
        "edge": "likes to eat"
    },
    {
        "node_1": "cat",
        "node_2": "pet",
        "edge": "is often a"
    }
]
```

Run the main script:

```bash
python3 main.py
```

The resulting HTML and PNG files will be saved in the `graphs/` directory.