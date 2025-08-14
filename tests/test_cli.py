import os
import subprocess
import sys


def run_cli(args):
    env = os.environ.copy()
    env["PYTHONPATH"] = "src"
    cmd = [sys.executable, "-m", "asynscan.cli"] + args
    return subprocess.run(cmd, env=env, capture_output=True, text=True)


def test_cli_version_runs():
    r = run_cli(["version"])
    assert r.returncode == 0
    assert "asynscan v0.1.0" in r.stdout


def test_cli_scan_simulated():
    r = run_cli(["scan", "--host", "127.0.0.1", "-p", "22,80,443"])
    assert r.returncode == 0
    # Debe listar esos puertos
    assert "22" in r.stdout and "80" in r.stdout and "443" in r.stdout
