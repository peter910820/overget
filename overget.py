import click

from src.get import GetData

@click.command()
@click.option("-G", "--get", 'url', required=True)
def main(url: str):
    g = GetData(url)
    print(g.get_data())

if __name__== "__main__":
    main()