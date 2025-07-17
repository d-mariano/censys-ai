from typing import Any, Dict, List, Optional
from pydantic import BaseModel

class Coordinates(BaseModel):
    latitude: float
    longitude: float


class Location(BaseModel):
    city: Optional[str] = None
    country: Optional[str] = None
    country_code: Optional[str] = None
    coordinates: Optional[Coordinates] = None
    province: Optional[str] = None
    postal_code: Optional[str] = None
    timezone: Optional[str] = None
    continent: Optional[str] = None


class AutonomousSystem(BaseModel):
    asn: int
    name: str
    country_code: Optional[str] = None
    description: Optional[str] = None
    bgp_prefix: Optional[str] = None


class WhoisNetwork(BaseModel):
    handle: Optional[str] = None
    name: Optional[str] = None
    cidrs: Optional[List[str]] = None
    updated: Optional[str] = None


class Whois(BaseModel):
    network: Optional[WhoisNetwork] = None


class SoftwareEvidence(BaseModel):
    data_path: Optional[str] = None
    found_value: Optional[str] = None
    literal_match: Optional[str] = None


class Software(BaseModel):
    product: Optional[str] = None
    vendor: Optional[str] = None
    version: Optional[str] = None
    source: Optional[str] = None
    confidence: Optional[float] = None
    evidence: Optional[List[SoftwareEvidence]] = None
    type: Optional[List[str]] = None
    part: Optional[str] = None
    cpe: Optional[str] = None
    components: Optional[List[str]] = None


class Vulnerability(BaseModel):
    cve_id: str
    severity: Optional[str] = None
    cvss_score: Optional[float] = None
    description: Optional[str] = None


class Service(BaseModel):
    port: int
    protocol: str
    banner: Optional[str] = None
    banner_hash_sha256: Optional[str] = None
    banner_hex: Optional[str] = None
    transport_protocol: Optional[str] = None
    software: Optional[List[Software]] = None
    vulnerabilities: Optional[List[Vulnerability]] = None
    labels: Optional[List[str]] = None
    cert: Optional[Dict[str, Any]] = None  # Could be expanded with a Cert model

class ThreatIntelligence(BaseModel):
    security_labels: Optional[List[str]] = None
    risk_level: Optional[str] = None

class DNS(BaseModel):
    hostname: Optional[str] = None

class Host(BaseModel):
    ip: str
    location: Optional[Location] = None
    autonomous_system: Optional[AutonomousSystem] = None
    whois: Optional[Whois] = None
    dns: Optional[DNS] = None
    services: Optional[List[Service]] = None
    threat_intelligence: Optional[ThreatIntelligence] = None


class HostsDatasetMetadata(BaseModel):
    description: Optional[str] = None
    created_at: Optional[str] = None
    data_sources: Optional[List[str]] = None
    hosts_count: Optional[int] = None
    ips_analyzed: Optional[List[str]] = None


class HostsDataset(BaseModel):
    metadata: HostsDatasetMetadata
    hosts: List[Host]
