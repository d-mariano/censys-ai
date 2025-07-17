from typing import Optional
from litellm import acompletion

from censys_ai.services.summarization.prompts import DATASET_PROMPT_TEMPLATE, MULTIPLE_DATASET_PROMPT_TEMPLATE
from censys_ai.services.summarization.config import SummarizationConfig
from censys_ai.models.host import HostsDataset
from censys_ai.models.web_property import WebPropertiesDataset
from censys_ai.models.certificate import CertificatesDataset


class SummarizationError(Exception):
    pass


class Summarizer:
    def __init__(self, config: SummarizationConfig):
        self.config = config

    async def summarize(
        self,
        hosts_dataset: Optional[HostsDataset],
        web_property_dataset: Optional[WebPropertiesDataset],
        certificate_dataset: Optional[CertificatesDataset],
    ) -> str:
        """
        Summarize multiple Censys datasets
        """            
        return await self._call_llm(MULTIPLE_DATASET_PROMPT_TEMPLATE.format(
            hosts_dataset=hosts_dataset,
            web_property_dataset=web_property_dataset,
            certificate_dataset=certificate_dataset
        ))

    async def summarize_hosts(self, dataset: HostsDataset) -> str:
        """
        Summarize a Censys hosts dataset
        """
        return await self._call_llm(DATASET_PROMPT_TEMPLATE.format(
            dataset=dataset,
            dataset_type="Host"
        ))

    async def summarize_web_properties(self, dataset: WebPropertiesDataset) -> str:
        """
        Summarize a Censys web properties dataset
        """
        return await self._call_llm(DATASET_PROMPT_TEMPLATE.format(
            dataset=dataset,
            dataset_type="Web Property"
        ))

    async def summarize_certificates(self, dataset: CertificatesDataset) -> str:
        """
        Summarize a Censys certificates dataset
        """
        return await self._call_llm(DATASET_PROMPT_TEMPLATE.format(
            dataset=dataset,
            dataset_type="Certificate"
        ))

    async def _call_llm(self, prompt: str) -> str:
        response = await acompletion(
            model=self.config.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=self.config.temperature,
            max_tokens=self.config.max_tokens,
        )
        return response.choices[0].message.content
