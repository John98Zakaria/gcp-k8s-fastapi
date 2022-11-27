import tomllib

with open("pyproject.toml", "rb") as f:
    parsed_toml = tomllib.load(f)

print(parsed_toml["tool"]["poetry"]["version"])
