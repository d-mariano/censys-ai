import censysLogo from './assets/censys.png'
import { useState } from 'react';
import { useMutation } from '@tanstack/react-query';
import { 
  Button, 
  Space, 
  Paper, 
  Text,
  Textarea,
  Flex,
  Alert,
  Loader,
} from '@mantine/core';
import { IconServer, IconWorld, IconCertificate, IconAlertCircle } from '@tabler/icons-react';
import Markdown from 'react-markdown'
import { SummarizationApi } from './api/summarization';
import type { SummarizationResponse } from './api/openapi';

function App() {
  const [hostsQuery, setHostsQuery] = useState('');
  const [webPropertiesQuery, setWebPropertiesQuery] = useState('');
  const [certificatesQuery, setCertificatesQuery] = useState('');
  const [error, setError] = useState<string | null>(null);
  const [summary, setSummary] = useState<SummarizationResponse | null>();

  const summarizeMutation = useMutation({
    mutationFn: ({hostsQuery, webPropertiesQuery, certificatesQuery}: {hostsQuery: string, webPropertiesQuery: string, certificatesQuery: string}) => 
      SummarizationApi.summarize(hostsQuery, webPropertiesQuery, certificatesQuery),
    onSuccess: (data) => {
      setError(null);
      setSummary(data);
    },
    onError: (err: Error) => {
      setError(err.message || 'Failed to generate hosts summary');
      setSummary(null);
    }
  });

  const isLoading = summarizeMutation.isPending;

  const handleSubmit = async () => {
    // Clear any previous errors and summary
    setError(null);
    setSummary(null);
    try {
      summarizeMutation.mutate({hostsQuery, webPropertiesQuery, certificatesQuery});
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An unknown error occurred');
    }
  };

  return (
    <Flex gap="md" style={{
      display: "flex",
      flexDirection: "column",
      width: "100%",
      height: "100%",
      maxHeight: "100%",
      maxWidth: 1920,
      margin: "auto",
      padding: 20,
    }}>
      <Flex display="flex" direction="row" justify="space-between" align="center" gap="md">
        <a href="https://censys.io/" target="_blank" rel="noopener noreferrer">
          <img src={censysLogo} alt="Censys logo" height="50" />
        </a>
        <h1>Censys AI</h1>
      </Flex>

      <Flex display="flex" direction="row" justify="center" align="flex-start" flex={1} gap="md">
        <Paper withBorder style={{flex: 1, height: "100%", display: "flex", alignItems: "center", justifyContent: "center", padding: 5}}>
          {error ? <Alert variant="light" color="red" title="Something Went Wrong" icon={<IconAlertCircle />}>
            {error}
          </Alert> : (
            isLoading ? <Loader /> : (
              summary ? <div style={{ maxHeight: 400, overflowY: "auto"}}><Markdown>{summary.summary || 'N/A'}</Markdown></div> : <Text style={{ textAlign: "center" }}>Upload a dataset below</Text>
            )
          )}
        </Paper>
      </Flex>

      <Flex display="flex" direction="row" justify="center" align="flex-start" flex={1} gap="md">
        <Paper withBorder style={{height: "100%", flex: 1, padding: 5}}>
          <IconServer size={32} stroke={1.5} />
          {isLoading ? <Text style={{ textAlign: "center" }}>Generating summary...</Text> : (
            summary?.hosts_summary ? <div style={{ maxHeight: 350, overflowY: "auto"}}><Markdown>{summary.hosts_summary}</Markdown></div> : <Text style={{ textAlign: "center" }}>Upload a hosts dataset below</Text>
          )}
        </Paper>
        <Paper withBorder style={{height: "100%", flex: 1, padding: 5}}>
          <IconWorld size={32} stroke={1.5} />
          {isLoading ? <Text style={{ textAlign: "center" }}>Generating summary...</Text> : (
            summary?.web_properties_summary ? <div style={{ maxHeight: 350, overflowY: "auto"}}><Markdown>{summary.web_properties_summary}</Markdown></div> : <Text style={{ textAlign: "center" }}>Upload a web properties dataset below</Text>
          )}
        </Paper>
        <Paper withBorder style={{height: "100%", flex: 1, padding: 5}}>
          <IconCertificate size={32} stroke={1.5} />
          {isLoading ? <Text style={{ textAlign: "center" }}>Generating summary...</Text> : (
            summary?.certificates_summary ? <div style={{ maxHeight: 350, overflowY: "auto"}}><Markdown>{summary.certificates_summary}</Markdown></div> : <Text style={{ textAlign: "center" }}>Upload a certificates dataset below</Text>
          )}
        </Paper>
      </Flex>

      <Space h="md" />

      <Flex display="flex" direction="row" justify="center" align="flex-start" gap="sm" style={{marginBottom: 15}}>
        <Paper p="md" style={{ flex: 1 }}>
          <Text fw={500} mb="sm">Hosts Dataset</Text>
          <Textarea
            disabled={isLoading}
            size="xl"
            placeholder="Paste Hosts Dataset here..."
            value={hostsQuery}
            onChange={(e) => setHostsQuery(e.currentTarget.value)}
            rows={4}
          />
        </Paper>
        
        <Paper p="md" style={{ flex: 1 }}>
          <Text fw={500} mb="sm">Web Properties Dataset</Text>
          <Textarea
            disabled={isLoading}
            size="xl"
            placeholder="Paste Web Properties Dataset here..."
            value={webPropertiesQuery}
            onChange={(e) => setWebPropertiesQuery(e.currentTarget.value)}
            rows={4}
          />
        </Paper>
        
        <Paper p="md" style={{ flex: 1 }}>
          <Text fw={500} mb="sm">Certificates Dataset</Text>
          <Textarea
            disabled={isLoading}
            size="xl"
            placeholder="Paste Certificates Dataset here..."
            value={certificatesQuery}
            onChange={(e) => setCertificatesQuery(e.currentTarget.value)}
            rows={4}
          />
        </Paper>
      </Flex>

      <div style={{ display: "flex", justifyContent: "center", alignItems: "center" }}>
        <Button variant="filled" onClick={handleSubmit} disabled={isLoading || (!hostsQuery && !webPropertiesQuery && !certificatesQuery)}>
          Summarize
        </Button>
      </div>
    </Flex>
  )
}

export default App
