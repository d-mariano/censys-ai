import axios from 'axios';
import { config } from './config';
import type { SummarizationResponse, SingleSummarizationResponse } from './openapi';


export const SummarizationApi = {
  async summarizeHosts(query: string): Promise<SingleSummarizationResponse> {
    const response = await axios.post<SingleSummarizationResponse>(
      `${config.baseURL}/summarization/hosts`,
      JSON.parse(query),
      {
        headers: config.headers,
        timeout: config.timeout,
      }
    );
    return response.data;
  },

  async summarizeWebProperties(query: string): Promise<SingleSummarizationResponse> {
    const response = await axios.post<SingleSummarizationResponse>(
      `${config.baseURL}/summarization/web-properties`,
      JSON.parse(query),
      {
        headers: config.headers,
        timeout: config.timeout,
      }
    );
    return response.data;
  },

  async summarizeCertificates(query: string): Promise<SingleSummarizationResponse> {
    const response = await axios.post<SingleSummarizationResponse>(
      `${config.baseURL}/summarization/certificates`,
      JSON.parse(query),
      {
        headers: config.headers,
        timeout: config.timeout,
      }
    );
    return response.data;
  },

  async summarizeAll(
    hostsQuery: string,
    webPropertiesQuery: string,
    certificatesQuery: string
  ): Promise<SummarizationResponse> {
    const response = await axios.post<SummarizationResponse>(
      `${config.baseURL}/summarization/summarize`,
      { 
        hosts: JSON.parse(hostsQuery),
        webProperties: JSON.parse(webPropertiesQuery),
        certificates: JSON.parse(certificatesQuery)
      },
      {
        headers: config.headers,
        timeout: config.timeout,
      }
    );
    return response.data;
  },

  async summarize(
    hostsQuery: string,
    webPropertiesQuery: string,
    certificatesQuery: string
  ): Promise<SummarizationResponse> {
    const response = await axios.post<SummarizationResponse>(
      `${config.baseURL}/summarization/summarize`,
      { 
        hosts: hostsQuery ? JSON.parse(hostsQuery) : null,
        webProperties: webPropertiesQuery ? JSON.parse(webPropertiesQuery) : null,
        certificates: certificatesQuery ? JSON.parse(certificatesQuery) : null
      }
    );
    console.log(response);
    return response.data;
  },
};
