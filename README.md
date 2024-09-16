# This project is a sample of Object Detection

## Setup Project

### Install uv (*package manager*)
#### Windows
> `powershell -c "irm https://astral.sh/uv/install.ps1 | iex"`
#### Unix-based
> `curl -LsSf https://astral.sh/uv/install.sh | sh`

### Activate environment
> `uv sync` then `source .venv/bin/activate`

## Run Project
> `uv run uvicorn main:app --reload`

## Containerization
### Build
> `docker build -t <image>:<version> .`

### Run image
> `docker run -d --name <container-name> -p <port>:<port> <image-name>`

## Example input on Playground (Altair/GraphiQL/Apollo)
### Mutation
```graphql
mutation($file: Upload!) {
  detectObjects(file: $file) {
    className
    confidence
    bbox
  }
}
```

### Query
```graphql
{
  detectObjects(imagePath: "image.jpg") {
    className
    confidence
    bbox
  }
}
```
