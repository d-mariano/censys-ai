from typing import List, Optional
from pydantic import BaseModel


class CertificateSubject(BaseModel):
    common_name: Optional[str] = None
    organization: Optional[str] = None
    country: Optional[str] = None


class CertificateIssuer(BaseModel):
    common_name: Optional[str] = None
    organization: Optional[str] = None
    country: Optional[str] = None


class ValidityPeriod(BaseModel):
    not_before: Optional[str] = None
    not_after: Optional[str] = None
    length_days: Optional[int] = None
    status: Optional[str] = None


class KeyInfo(BaseModel):
    algorithm: Optional[str] = None
    key_size: Optional[int] = None
    public_key_fingerprint: Optional[str] = None


class CertificateAuthority(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    validation_level: Optional[str] = None


class CertificateTransparency(BaseModel):
    logs_count: Optional[int] = None
    first_seen: Optional[str] = None
    logs: Optional[List[str]] = None


class ValidationPaths(BaseModel):
    apple: Optional[bool] = None
    chrome: Optional[bool] = None
    microsoft: Optional[bool] = None
    mozilla: Optional[bool] = None


class Validation(BaseModel):
    trusted_by_major_browsers: Optional[bool] = None
    validation_paths: Optional[ValidationPaths] = None


class SecurityAnalysis(BaseModel):
    zlint_status: Optional[str] = None
    failed_lints: Optional[List[str]] = None
    risk_level: Optional[str] = None


class UsageIndicators(BaseModel):
    ever_seen_in_scan: Optional[bool] = None


class Certificate(BaseModel):
    fingerprint_sha256: str
    fingerprint_sha1: Optional[str] = None
    fingerprint_md5: Optional[str] = None
    domains: Optional[List[str]] = None
    subject: Optional[CertificateSubject] = None
    issuer: Optional[CertificateIssuer] = None
    validity_period: Optional[ValidityPeriod] = None
    key_info: Optional[KeyInfo] = None
    certificate_authority: Optional[CertificateAuthority] = None
    certificate_transparency: Optional[CertificateTransparency] = None
    validation: Optional[Validation] = None
    security_analysis: Optional[SecurityAnalysis] = None
    usage_indicators: Optional[UsageIndicators] = None


class CertificatesDatasetMetadata(BaseModel):
    description: Optional[str] = None
    created_at: Optional[str] = None
    data_sources: Optional[List[str]] = None
    certificates_count: Optional[int] = None
    certificate_fingerprints: Optional[List[str]] = None


class CertificatesDataset(BaseModel):
    metadata: CertificatesDatasetMetadata
    certificates: List[Certificate]
