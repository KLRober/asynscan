import typer

app = typer.Typer(help="ASYNScan - Escáner de puertos TCP asíncrono (base CLI)")


@app.command()
def version():
    """Muestra la versión de la herramienta."""
    # Nota: vamos a mover __version__ a un lugar central más adelante
    typer.echo("asynscan v0.1.0 (CLI base)")


@app.command()
def scan(
    host: str = typer.Option(..., "--host", "-h", help="Host o IP a escanear", show_default=False),
    ports: str = typer.Option("1-1024", "--ports", "-p", help="Rango o lista (ej: 22,80,443 o 1-1024)"),
    timeout: float = typer.Option(1.0, "--timeout", help="Timeout por puerto (segundos)"),
    concurrency: int = typer.Option(100, "--concurrency", help="Máximo de tareas concurrentes"),
):
    """
    Prepara un escaneo (placeholder).
    En 3.2 conectamos esto con la lógica real.
    """
    typer.echo(f"[CLI] Preparando escaneo → host={host}, ports={ports}, timeout={timeout}, concurrency={concurrency}")
    typer.echo("⚠ Aún no implementado el motor de escaneo (llega en 3.2).")


def main():
    app()


if __name__ == "__main__":
    main()
