import asyncio
from typing import Optional

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from censys_ai.services.summarization.summarizer import Summarizer
from censys_ai.services.summarization.config import SummarizationConfig
from censys_ai.models.host import HostsDataset
from censys_ai.models.web_property import WebPropertiesDataset
from censys_ai.models.certificate import CertificatesDataset


router = APIRouter()


class SingleSummarizationResponse(BaseModel):
    summary: str


class SummarizationResponse(BaseModel):
    hosts_summary: Optional[str] = None
    web_properties_summary: Optional[str] = None
    certificates_summary: Optional[str] = None
    summary: Optional[str] = None


def get_summarizer() -> Summarizer:
    """
    Dependency to provide a Summarizer instance.
    """
    return Summarizer(SummarizationConfig(model="vertex_ai/gemini-2.0-flash-lite-001"))


@router.post(
    "/hosts",
    response_model=SingleSummarizationResponse,
    summary="Summarize a hosts dataset"
)
async def summarize_hosts(
    dataset: HostsDataset,
    summarizer: Summarizer = Depends(get_summarizer),
):
    """
    Summarize a Censys hosts dataset.
    """
    result = await summarizer.summarize_hosts(dataset)
    return SingleSummarizationResponse(summary=result)


@router.post(
    "/web-properties",
    response_model=SingleSummarizationResponse,
    summary="Summarize a web properties dataset"
)
async def summarize_web_properties(
    dataset: WebPropertiesDataset,
    summarizer: Summarizer = Depends(get_summarizer),
):
    """
    Summarize a Censys web properties dataset.
    """
    result = await summarizer.summarize_web_properties(dataset)
    return SingleSummarizationResponse(summary=result)


@router.post(
    "/certificates",
    response_model=SingleSummarizationResponse,
    summary="Summarize a certificates dataset"
)
async def summarize_certificates(
    dataset: CertificatesDataset,
    summarizer: Summarizer = Depends(get_summarizer),
):
    """
    Summarize a Censys certificates dataset.
    """
    result = await summarizer.summarize_certificates(dataset)
    return SingleSummarizationResponse(summary=result)


@router.post(
    "/summarize",
    response_model=SummarizationResponse,
    summary="Summarize multiple datasets"
)
async def summarize(
    hosts: Optional[HostsDataset] = None,
    web_properties: Optional[WebPropertiesDataset] = None,
    certificates: Optional[CertificatesDataset] = None,
    summarizer: Summarizer = Depends(get_summarizer),
):
    """
    Summarize multiple Censys datasets together.
    """
    tasks = []
    host_result_index = None
    web_properties_result_index = None
    certificates_result_index = None
    
    if hosts:
        tasks.append(summarizer.summarize_hosts(hosts))
        host_result_index = len(tasks) - 1
    if web_properties:
        tasks.append(summarizer.summarize_web_properties(web_properties))
        web_properties_result_index = len(tasks) - 1
    if certificates:
        tasks.append(summarizer.summarize_certificates(certificates))
        certificates_result_index = len(tasks) - 1

    if not tasks:
        raise HTTPException(status_code=400, detail="At least one dataset must be provided")

    tasks.append(summarizer.summarize(hosts, web_properties, certificates))
    summary_result_index = len(tasks) - 1

    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    hosts_result = results[host_result_index] if host_result_index is not None else None
    web_props_result = results[web_properties_result_index] if web_properties_result_index is not None else None
    certs_result = results[certificates_result_index] if certificates_result_index is not None else None
    summary_result = results[summary_result_index]
    
    return SummarizationResponse(
        hosts_summary=hosts_result,
        web_properties_summary=web_props_result,
        certificates_summary=certs_result,
        summary=summary_result,
    )
