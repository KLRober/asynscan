import time
from typing import List

from .models import HostResult, PortFinding, PortState, ScanResult, ScanSummary


def simulate_scan(host: str, ports: List[int]) -> ScanResult:
    """
    Simula un escaneo rápido: marca 22 y 80 como abiertos si están en la lista,
    el resto cerrados. Calcula un score simple.
    """
    t0 = time.perf_counter()

    findings: List[PortFinding] = []
    for p in ports:
        if p in (22, 80, 443):
            service = {22: "ssh", 80: "http", 443: "https"}.get(p)
            findings.append(PortFinding(port=p, service=service, state=PortState.OPEN, banner=None))
        else:
            findings.append(PortFinding(port=p, service=None, state=PortState.CLOSED, banner=None))

    open_ports = sum(1 for f in findings if f.state == PortState.OPEN)
    total_ports = len(findings)
    # Score ficticio: 100 - (open_ports * 10) pero no menor que 0
    score = max(0, 100 - open_ports * 10)

    took_ms = int((time.perf_counter() - t0) * 1000)
    host_result = HostResult(host=host, findings=findings, took_ms=took_ms)
    summary = ScanSummary(total_ports=total_ports, open_ports=open_ports, score=score)
    return ScanResult(host_result=host_result, summary=summary)
