import typer

from .main import simulate_scan
from .utils.ports import parse_ports

app = typer.Typer(help="ASYNScan - Escáner de puertos TCP asíncrono (base CLI)")


@app.command()
def version():
    """Muestra la versión de la herramienta."""
    typer.echo("asynscan v0.1.0 (CLI base)")


@app.command()
def scan(
    host: str = typer.Option(..., "--host", "-h", help="Host o IP a escanear", show_default=False),
    ports: str = typer.Option("1-1024", "--ports", "-p", help="Rango o lista (ej: 22,80,443 o 1-1024)"),
    timeout: float = typer.Option(1.0, "--timeout", help="Timeout por puerto (segundos)"),
    concurrency: int = typer.Option(100, "--concurrency", help="Máximo de tareas concurrentes"),
):
    """
    Prepara un escaneo. En 3.3 conectamos esto con la lógica real asíncrona.
    """
    if timeout <= 0:
        typer.secho("Error: --timeout debe ser > 0", fg=typer.colors.RED, err=True)
        raise typer.Exit(code=2)
    if concurrency < 1:
        typer.secho("Error: --concurrency debe ser >= 1", fg=typer.colors.RED, err=True)
        raise typer.Exit(code=2)

    try:
        port_list = parse_ports(ports)
    except ValueError as e:
        typer.secho(f"Error en --ports: {e}", fg=typer.colors.RED, err=True)
        raise typer.Exit(code=2)

    # (Por ahora) simular el escaneo
    result = simulate_scan(host, port_list)

    # Salida amigable mínima (luego añadimos JSON/Markdown)
    typer.echo(f"Host: {result.host_result.host}")
    typer.echo(f"Tiempo: {result.host_result.took_ms} ms")
    typer.echo(
        f"Score: {result.summary.score}/100  |  Puertos abiertos: "
        f"{result.summary.open_ports}/{result.summary.total_ports}"
    )
    typer.echo("Resultados:")
    for f in result.host_result.findings[:10]:  # limitar salida en consola
        state = "abierto" if f.state.value == "open" else f.state.value
        svc = f" ({f.service})" if f.service else ""
        typer.echo(f" - {f.port}{svc}: {state}")
    if len(result.host_result.findings) > 10:
        typer.echo(f" ... y {len(result.host_result.findings) - 10} más")


def main():
    app()


if __name__ == "__main__":
    main()
