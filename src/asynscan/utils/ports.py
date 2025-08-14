from typing import List


def parse_ports(spec: str) -> List[int]:
    """
    Acepta formatos:
      - "22,80,443"
      - "1-1024"
      - "22,80,1000-1010"
    Devuelve lista ordenada y sin duplicados.
    """
    ports: set[int] = set()
    for token in spec.split(","):
        token = token.strip()
        if not token:
            continue
        if "-" in token:
            a, b = token.split("-", 1)
            start = int(a)
            end = int(b)
            if start > end or start < 1 or end > 65535:
                raise ValueError(f"Rango de puertos inválido: {token}")
            ports.update(range(start, end + 1))
        else:
            p = int(token)
            if p < 1 or p > 65535:
                raise ValueError(f"Puerto inválido: {p}")
            ports.add(p)
    return sorted(ports)
