import typer
app = typer.Typer()
@app.command()
def forge(description: str):
    print(f"Forging: {description}")
if __name__ == "__main__":
    app()