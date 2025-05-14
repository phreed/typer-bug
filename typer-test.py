import typer

def main(name: str = typer.Argument("World", help="The person to greet")):
    print(f"Hello {name}")

if __name__ == "__main__":
    typer.run(main)

