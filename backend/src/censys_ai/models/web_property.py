from typing import List, Optional, Dict, Any
from pydantic import BaseModel, ConfigDict


class WebEndpoint(BaseModel):
    endpoint_type: Optional[str] = None
    path: Optional[str] = None
    banner: Optional[str] = None
    banner_hash_sha256: Optional[str] = None
    banner_hex: Optional[str] = None
    transport_protocol: Optional[str] = None

    model_config = ConfigDict(extra='allow')


class WebProperty(BaseModel):
    port: Optional[int] = None
    scan_timed: Optional[str] = None
    hostname: Optional[str] = None
    labels: Optional[List[str]] = None
    endpoints: Optional[List[WebEndpoint]] = None
    misconfigs: Optional[List[Dict[str, Any]]] = None
    exposures: Optional[List[Dict[str, Any]]] = None
    vulns: Optional[List[Dict[str, Any]]] = None
    software: Optional[List[Dict[str, Any]]] = None
    hardware: Optional[List[Dict[str, Any]]] = None
    operating_system: Optional[List[Dict[str, Any]]] = None
    tls: Optional[List[Dict[str, Any]]] = None


class WebPropertiesDatasetMetadata(BaseModel):
    description: Optional[str] = None
    created_at: Optional[str] = None
    data_sources: Optional[List[str]] = None
    web_properties_count: Optional[int] = None
    hostnames_analyzed: Optional[List[str]] = None


class WebPropertiesDataset(BaseModel):
    metadata: WebPropertiesDatasetMetadata = None
    web_properties: List[WebProperty] = None
