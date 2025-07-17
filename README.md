# Censys AI

AI-powered assistant for analyzing and summarizing Censys cybersecurity datasets with a clean, modern interface.

![Censys AI Screenshot](https://via.placeholder.com/800x500.png?text=Censys+AI+Interface)

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

#### Development Commands
- Run tests: `uv run test`
- Lint code: `uv run lint`
- Format code: `uv run format`
- Generate OpenAPI docs: `uv run docs`

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
- Use `uv` for all Python dependency management and scripts
- Use `npm` for frontend development
- Edit `pyproject.toml` to manage dependencies and scripts
- See `specs/stories/` for user stories and acceptance criteria

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
