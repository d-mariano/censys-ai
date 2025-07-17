# Censys AI

AI-powered assistant for analyzing and summarizing Censys cybersecurity datasets with a clean, modern interface.

![Censys AI Screenshot](screenshot.png)

## Features

- 🚀 **Modern Tech Stack**
  - FastAPI backend with Python 3.10+
  - React + TypeScript + Mantine UI frontend
  - End-to-end type safety with OpenAPI

- 🔍 **Powerful Analysis**
  - Simultaneously analyze multiple Censys datasets
  - Individual and combined dataset summarization
  - Interactive results with Markdown rendering

- 🛠 **Developer Friendly**
  - Modular summarization pipeline with LiteLLM
  - Modern dependency management with [uv](https://docs.astral.sh/uv/)
  - Comprehensive error handling and loading states
  - Responsive design for all screen sizes

## Requirements
- Python 3.10+
- Node.js 18+
- [uv](https://docs.astral.sh/uv/) (install via `curl -LsSf https://astral.sh/uv/install.sh | sh`)
- npm (comes with Node.js)

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Node.js 18+
- [uv](https://docs.astral.sh/uv/) (install via `curl -LsSf https://astral.sh/uv/install.sh | sh`)

### Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create and activate virtual environment
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
uv pip install -e ".[dev]"

# Start the development server
uv run start
```

### Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start the development server
npm start
```

The frontend will be available at `http://localhost:3000`

## Project Structure

```
censys-ai/
├── backend/                  # FastAPI backend
│   ├── src/
│   │   └── censys_ai/       # Python package
│   │       ├── api/         # API routes and models
│   │       ├── services/    # Business logic
│   │       └── models/      # Data models
│   ├── tests/               # Backend tests
│   └── pyproject.toml       # Project configuration
│
├── frontend/                # React frontend
│   ├── public/              # Static files
│   └── src/                 # Source code
│       ├── api/             # API client code
│       ├── components/      # Reusable components
│       └── App.tsx          # Main application component
│
├── example_datasets/        # Sample datasets for testing
└── README.md                # This file
```

## Development Workflow
- Made use of Claude to iterate on specs, see `specs/Censys AI Summarization Agent - Project Specifications.pdf` for original version
- Made changes and stored them in `specs/censys_ai_specs.md`
- Split requirements into individual story specs in `specs/stories/`
- Used Windsurf to assist in spec implementation
- Your mileage may vary, had to make some changes to the specs to get them to work, also reduced scope of some specs to make them more achievable

## Future Enhancements
- Improve UI in terms of both user experience and code quality
    - Better error reporting
    - File upload support
    - Conversational UI?
- Improve prompt engineering to use more specialized instructions per dataset, lean on Censys docs for more info
- Support streaming
- If supporting a conversational experience, add support for saving conversation history
- Add support for saving results to a file
- Potentially use an actual thought loop to iterate on datasets and specific questions
- Potentially make datasets more RAGable for better context and more specific questions

## References
- [Censys Platform Datasets](https://docs.censys.com/docs/platform-datasets)
- [Censys Host Dataset](https://docs.censys.com/docs/platform-host-dataset)
- [Censys Web Property Dataset](https://docs.censys.com/docs/platform-web-property-dataset)
- [Censys Certificate Dataset](https://docs.censys.com/docs/platform-certificate-dataset)
- [uv Documentation](https://docs.astral.sh/uv/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Mantine UI](https://mantine.dev/)
- [LiteLLM](https://github.com/BerriAI/litellm)

---

For questions or contributions, please contact Dave Mariano.
