from dataclasses import dataclass
from enum import Enum, IntEnum
from typing import List, Optional


class PortState(str, Enum):
    OPEN = "open"
    CLOSED = "closed"
    FILTERED = "filtered"


class Severity(IntEnum):
    INFO = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4


@dataclass
class PortFinding:
    port: int
    service: Optional[str]
    state: PortState
    banner: Optional[str] = None


@dataclass
class HostResult:
    host: str
    findings: List[PortFinding]
    took_ms: int


@dataclass
class ScanSummary:
    total_ports: int
    open_ports: int
    score: int  # 0–100 (placeholder simple)


@dataclass
class ScanResult:
    host_result: HostResult
    summary: ScanSummary
