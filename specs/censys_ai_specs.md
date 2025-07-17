# Censys AI Summarization Agent - Project Specifications

## Project Overview
Develop a stateless full-stack AI agent that can intelligently summarize Censys cybersecurity data, providing actionable insights from datasets through an intuitive web interface.

## Technical Stack
- **Backend**: Python, FastAPI
- **Frontend**: TypeScript, React, Mantine
- **AI/ML**: LiteLLM for unified AI model access
- **Architecture**: Stateless, no database required

## Stories

### 1. Project Initialization
**Tasks:**
- [ ] Create basic project structure (frontend/, backend/)
- [ ] Initialize backend using pyenv and setup a venv for Python, add requirements for FastAPI, LiteLLM, and dotenv
- [ ] Initialize frontend for TypeScript, React, and Mantine, use yarn
- [ ] Initialize README.md with project overview
- [ ] Configure .gitignore for both frontend and backend

**Acceptance Criteria:**
- Project structure follows best practices
- Dependencies are properly managed
- Initial README provides project context
- .gitignore is properly configured

### 2. Data Processing
**Tasks:**
- [ ] Create data models/schemas for Censys datasets (Host, Web Property, Certificate)

**Documentation References:**
- [Censys Platform Datasets](https://docs.censys.com/docs/platform-datasets)

### 3. Create Summarization Service w/ Separate Summarizer Functions
**Tasks:**
- [ ] Implement framework agnostic Censys summarization service using dependency injection
- [ ] For starters, injection parameters should simply be LiteLLM parameters or an LLMConfig class to be used w/ LiteLLM
- [ ] Implement individual dataset summarizer functions (Host, Web Property, Certificate)
- [ ] Implement error handling and fallback mechanisms

**Acceptance Criteria:**
- Censys datasets are presented to the LLM in a format that is easy to parse as context
- Successfully summarize individual Censys datasets using LiteLLM
- Handles API failures gracefully
- Configurable model parameters and providers
- Agnostic service that uses dependency injection for model properties

**Documentation References:**
- [LiteLLM Documentation](https://docs.litellm.ai/docs/)
- [Censys Platform Datasets](https://docs.censys.com/docs/platform-datasets)

### 4. Multi-Dataset Summarization
**Tasks:**
- [ ] Create unified multi-dataset summarizer function
- [ ] Add prompt engineering for Censys data context
- [ ] Implement error handling and fallback mechanisms
- [ ] Add summary quality validation and formatting

**Acceptance Criteria:**
- Censys datasets are presented to the LLM in a format that is easy to parse as context
- Successfully summarize multiple Censys datasets using LiteLLM

**Documentation References:**
- [LiteLLM Documentation](https://docs.litellm.ai/docs/)
- [Censys Platform Datasets](https://docs.censys.com/docs/platform-datasets)

### 5. Backend API Development
**Tasks:**
- [ ] Setup .env.example file for environment variable management to include LLM parameters, i.e OpenAI API key, model name, etc.
- [ ] Create REST API structure using FastAPI
- [ ] Implement dataset upload/input endpoint
- [ ] Create individual dataset summarization endpoints
- [ ] Add multi-dataset summarization endpoint
- [ ] FastAPI app should build the summarization service using a factory function and inject environment variables via dotenv
- [ ] Implement health check and status endpoints
- [ ] Add request/response validation
- [ ] Create unit and integration tests
- [ ] Add API documentation (OpenAPI/Swagger)
- [ ] Update README.md with server start instructions

**Acceptance Criteria:**
- RESTful API design with proper HTTP status codes
- Request/response validation
- Support for different input formats
- 80%+ test coverage
- Comprehensive API documentation
- Robust error handling

### 6. Frontend Development
**Tasks:**
- [ ] Create responsive layout structure
- [ ] Implement data upload/input interface
- [ ] Create summary display components
- [ ] Add loading states and error handling
- [ ] Implement basic styling and UX
- [ ] Add progress indicators for processing
- [ ] Implement summary export functionality
- [ ] Create summary comparison features
- [ ] Add summary customization options
- [ ] Update package.json accordingly
- [ ] Update README.md with client start instructions

**Acceptance Criteria:**
- Intuitive user interface with responsive design
- Clear data visualization
- Proper error messaging
- Support for different input methods
- Smooth user experience with clear visual feedback
- Functional export and customization features

### 7. End-to-End Integration
**Tasks:**
- [ ] Integrate frontend with backend
- [ ] Test complete data flow from input to summary
- [ ] Implement comprehensive error handling
- [ ] Add logging and monitoring
- [ ] Create E2E test scenarios

**Acceptance Criteria:**
- Seamless frontend-backend integration
- Complete user journey testing
- Comprehensive error handling
- Proper logging implementation
- All E2E tests passing

### 8. Documentation
**Tasks:**
- [ ] Document API endpoints and usage
- [ ] Create user guide with examples
- [ ] Document AI approach and techniques used
- [ ] Create future enhancements list
- [ ] Add testing instructions (manual and automated)
- [ ] Update README.md with any missing setup and run instructions

**Acceptance Criteria:**
- Clear setup and deployment instructions
- Complete API and user documentation
- Technical documentation for developers
- Comprehensive future enhancements list
- Deployment configuration ready for production

## Architecture Decisions

### Summarization Strategy
**Option A: Individual Dataset Summarizers**
- Separate endpoints for each dataset type
- Specialized prompts for each data format
- Allows focused analysis per dataset

**Option B: Unified Multi-Dataset Summarizer**
- Single endpoint that processes all datasets together
- Holistic analysis across all data types
- Provides comprehensive security posture overview

**Recommendation**: Implement both approaches
- Individual summarizers for detailed analysis
- Multi-dataset summarizer for comprehensive insights
- Let users choose based on their needs

### LiteLLM Integration Benefits
- Unified interface for multiple AI providers
- Built-in fallback mechanisms
- Cost optimization features
- Easy model switching and testing

## Open Questions
1. Should we prioritize individual dataset summaries or unified multi-dataset analysis?
2. What specific security insights should be highlighted in summaries?
3. Are there compliance requirements for AI model usage?

## Success Metrics
- Functional summarization of Censys data (individual and multi-dataset)
- Clean, maintainable stateless architecture
- Comprehensive documentation
- Effective LiteLLM integration
- User-friendly interface
- Robust error handling and testing
