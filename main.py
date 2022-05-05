import json

from rich.columns import Columns
from rich.console import Console, Group
from rich.panel import Panel


def get_json():
    with open('flist-kavi.json') as f:
        char = json.load(f)

    return char


def get_info_panel(info):
    return Panel(info, title="Info")

def get_details_panel(details):
    details_cols = []

    for detail in details:
        col = '\n'.join([f"[b]{d['title']}[/b] {d['value']}" for d in detail['details']])
        details_cols.append(Panel(col, title=detail['title'], expand=True))

    return Columns(details_cols)


def get_images_panel(images):
    ims = "\n".join([image['href'] for image in images])
    return Panel(ims, title="Images")

def get_kinks_panel(kink_categories):
    kink_cols = []

    for category, kinks in kink_categories.items():
        col = '\n'.join([kink['name'] for kink in kinks])
        kink_cols.append(Panel(col, title=category, expand=True))

    return Columns(kink_cols, title="Kinks")


def main():
    console = Console()

    char = get_json()

    info_panel = get_info_panel(char['tabs']['info'])
    details_panel = get_details_panel(char['tabs']['details'])
    images_panel = get_images_panel(char['tabs']['images'])
    kinks_panel = get_kinks_panel(char['kinks'])


    group = Group(info_panel, details_panel, images_panel, kinks_panel)
    console.print(group)


if __name__ == '__main__':
    main()
