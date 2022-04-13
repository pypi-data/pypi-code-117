"""CLI tools."""
import asyncio
import functools
import http.cookies
import os
import typing

import click

import genshin

if os.name == "nt":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())  # type: ignore


T = typing.TypeVar("T", bound=typing.Any)

cli: click.Group = click.Group("cli")


def asynchronous(func: typing.Callable[..., typing.Awaitable[typing.Any]]) -> typing.Callable[..., typing.Any]:
    """Make an asynchronous function runnable by click."""

    @functools.wraps(func)
    def wrapper(*args: typing.Any, **kwargs: typing.Any) -> typing.Any:
        return asyncio.run(func(*args, **kwargs))

    return wrapper


def client_command(func: typing.Callable[..., typing.Awaitable[typing.Any]]) -> typing.Callable[..., typing.Any]:
    """Make a click command that uses a Client."""

    @click.option("--cookies", help="Cookie header to use in authentication.", default=None)
    @click.option("--lang", help="Default language.", default="en-us")
    @click.option("--debug", is_flag=True, hidden=True)
    @functools.wraps(func)
    @asynchronous
    async def command(
        cookies: typing.Optional[str] = None,
        lang: str = "en-us",
        debug: bool = False,
        **kwargs: typing.Any,
    ) -> typing.Any:
        client = genshin.Client(cookies, lang=lang, debug=debug)
        if cookies is None:
            client.set_browser_cookies()

        return await func(client, **kwargs)

    return command


@cli.command()
@client_command
async def accounts(client: genshin.Client) -> None:
    """Get all of your genshin accounts."""
    data = await client.get_game_accounts()

    for account in data:
        click.echo(
            f"{click.style(str(account.uid), bold=True)} - {account.nickname} AR {account.level} ({account.server_name})"
        )


genshin_group: click.Group = click.Group("genshin", help="Genshin-related commands.")
honkai_group: click.Group = click.Group("honkai", help="Honkai-related commands.")
cli.add_command(genshin_group)
cli.add_command(honkai_group)


@genshin_group.command("stats")
@click.argument("uid", type=int)
@client_command
async def genshin_stats(client: genshin.Client, uid: int) -> None:
    """Show simple genshin statistics."""
    cuid = click.style(str(uid), fg="blue")
    click.echo(f"User stats of {cuid}\n")

    data = await client.get_partial_genshin_user(uid)

    click.secho("Stats:", fg="yellow")
    for k, v in data.stats.as_dict(lang=client.lang).items():
        value = click.style(str(v), bold=True)
        click.echo(f"{k}: {value}")

    click.echo()
    click.secho("Explorations:", fg="yellow")
    for area in data.explorations:
        perc = click.style(str(area.explored) + "%", bold=True)
        click.echo(f"{area.name}: explored {perc} | {area.type} level {area.level}")

    if data.teapot is not None:
        click.echo()
        click.secho("Teapot:", fg="yellow")
        level = click.style(str(data.teapot.level), bold=True)
        comfort = click.style(str(data.teapot.comfort), bold=True)
        click.echo(f"level {level} | comfort {comfort} ({data.teapot.comfort_name})")
        click.echo(f"Unlocked realms: {', '.join(r.name for r in data.teapot.realms)}")


@honkai_group.command("stats")
@click.argument("uid", type=int)
@client_command
async def honkai_stats(client: genshin.Client, uid: int) -> None:
    """Show simple honkai statistics."""
    cuid = click.style(str(uid), fg="blue")
    click.echo(f"User stats of {cuid}\n")

    data = await client.get_honkai_user(uid)

    click.secho("Stats:", fg="yellow")
    for k, v in data.stats.as_dict(lang=client.lang).items():
        if isinstance(v, dict):
            click.echo(f"{k}:")
            for nested_k, nested_v in typing.cast("dict[str, object]", v).items():
                click.echo(f"  {nested_k}: {click.style(str(nested_v), bold=True)}")
        else:
            click.echo(f"{k}: {click.style(str(v), bold=True)}")


@genshin_group.command("characters")
@click.argument("uid", type=int)
@client_command
async def genshin_characters(client: genshin.Client, uid: int) -> None:
    """Show genshin characters."""
    cuid = click.style(str(uid), fg="blue")
    click.echo(f"Characters of {cuid}")

    characters = await client.get_genshin_characters(uid)
    characters = sorted(characters, key=lambda c: (c.level, c.rarity), reverse=True)

    for char in characters:
        color = {
            "Anemo": "bright_green",
            "Pyro": "red",
            "Hydro": "bright_blue",
            "Electro": "magenta",
            "Cryo": "bright_cyan",
            "Geo": "yellow",
            "Dendro": "green",
        }[char.element]

        click.echo()
        name = click.style(char.name, bold=True)
        element = click.style(char.element, fg=color)
        click.echo(f"{name} ({'★' * char.rarity} {element})")
        click.echo(f"lvl {char.level} C{char.constellation}, friendship lvl {char.friendship}")
        click.echo(
            f"Weapon: {char.weapon.name} ({'★' * char.weapon.rarity} {char.weapon.type}) - "
            f"lvl {char.weapon.level} R{char.weapon.refinement}"
        )

        if char.artifacts:
            click.echo("Artifacts:")
            for arti in char.artifacts:
                click.echo(f" - {arti.pos_name}: {arti.set.name} ({'★' * arti.rarity})")

        if char.outfits:
            click.echo(f"Outfits: {', '.join(o.name for o in char.outfits)}")


@genshin_group.command("notes")
@client_command
async def genshin_notes(client: genshin.Client) -> None:
    """Show real-Time notes."""
    click.echo("Real-Time notes.")

    data = await client.get_notes()

    click.echo(f"{click.style('Resin:', bold=True)} {data.current_resin}/{data.max_resin}")
    click.echo(
        f"{click.style('Commissions:', bold=True)} " f"{data.completed_commissions}/{data.max_commissions}",
        nl=False,
    )
    if data.completed_commissions == data.max_commissions and not data.claimed_commission_reward:
        click.echo(f" | [{click.style('X', fg='red')}] Haven't claimed rewards")
    else:
        click.echo()
    click.echo(
        f"{click.style('Used resin cost-halving opportunities:', bold=True)} "
        f"{data.max_resin_discounts - data.remaining_resin_discounts}/{data.max_resin_discounts}"
    )

    click.echo(f"\n{click.style('Expeditions:', bold=True)} " f"{len(data.expeditions)}/{data.max_expeditions}")
    for expedition in data.expeditions:
        if expedition.remaining_time > 0:
            seconds = expedition.remaining_time
            remaining = f"{seconds // 3600:02.0f}:{seconds % 3600 // 60:02.0f} remaining"
            click.echo(f" - {expedition.status} | {remaining} - {expedition.character.name}")
        else:
            click.echo(f" - {expedition.status} | {expedition.character.name}")


@cli.command()
@click.option("--limit", help="The maximum amount of wishes to show.", default=None)
@client_command
async def wishes(client: genshin.Client, limit: typing.Optional[int] = None) -> None:
    """Show a nicely formatted wish history."""
    client.set_authkey()

    banner_names = await client.get_banner_names()
    longest = max(len(v) for v in banner_names.values())

    async for wish in client.wish_history(limit=limit):
        banner = click.style(wish.banner_name.ljust(longest), bold=True)
        click.echo(f"{banner} | {wish.time.astimezone()} - {wish.name} ({'★' * wish.rarity} {wish.type})")


@cli.command()
@client_command
async def pity(client: genshin.Client) -> None:
    """Calculate the amount of pulls until pity."""
    client.set_authkey()

    banners = await client.get_banner_names()
    for banner, name in banners.items():
        # skip the novice banner
        if banner == 100:
            continue

        click.echo()
        click.secho(name, fg="yellow")

        accum = 0
        async for wish in client.wish_history(banner):
            accum += 1
            if wish.rarity == 5:
                a = click.style(str(90 - accum), bold=True)
                n = click.style(wish.name, fg="green")
                click.secho(f"Pulled {n} {accum} pulls ago. {a} pulls left until pity.")
                break
        else:
            a = click.style(str(90 - accum), bold=True)
            click.secho(f"Never pulled a 5*. At most {a} pulls left until pity")


@cli.command()
@client_command
async def banner_ids(client: genshin.Client) -> None:
    """Get the banner ids from logs."""
    ids = genshin.utility.get_banner_ids()

    click.echo("\n".join(ids) + "\n")

    if len(ids) < 3:
        click.echo("Please open all detail pages!")
        return

    for banner in await client.get_banner_details(ids):
        click.echo(f"{banner.banner_id} - {banner.banner_type_name} ({banner.banner_type})")


@cli.command(hidden=True)
def authkey() -> None:
    """Get an authkey from logfiles."""
    click.echo(genshin.utility.get_authkey())


@cli.command()
@click.argument("account")
@click.argument("password")
@click.option("--port", help="Webserver port.", type=int, default=5000)
@asynchronous
async def login(account: str, password: str, port: int) -> None:
    """Login with a password."""
    client = genshin.Client()
    cookies = await client.login_with_password(account, password, port=port)

    base: http.cookies.BaseCookie[str] = http.cookies.BaseCookie(cookies)
    click.echo(f"Your cookies are: {click.style(base.output(header='', sep=';'), bold=True)}")


if __name__ == "__main__":
    cli()
