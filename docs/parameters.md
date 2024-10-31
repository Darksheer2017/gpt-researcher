# API Parameters Documentation

This document provides a comprehensive list of all parameters accepted by the API.

## BasicReport Parameters

- `query` (str): The research query.
- `report_type` (str): The type of report.
- `report_source` (str): The source of the report.
- `source_urls` (list): List of source URLs.
- `tone` (Tone): The tone of the report.
- `config_path` (str): Path to the configuration file.
- `websocket` (WebSocket): WebSocket for real-time communication.
- `headers` (dict, optional): HTTP headers.
- `report_tone` (str, optional): Tone of the report.
- `report_sources` (list, optional): List of report sources.
- `subtopics` (list, optional): List of subtopics.
- `additional_context` (str, optional): Additional context for the report.
- `summary_length` (int, optional): Length of the summary.
- `include_references` (bool, optional): Whether to include references.

## DetailedReport Parameters

- `query` (str): The research query.
- `report_type` (str): The type of report.
- `report_source` (str): The source of the report.
- `source_urls` (list): List of source URLs.
- `config_path` (str, optional): Path to the configuration file.
- `tone` (Tone): The tone of the report.
- `websocket` (WebSocket, optional): WebSocket for real-time communication.
- `subtopics` (list, optional): List of subtopics.
- `headers` (dict, optional): HTTP headers.
- `report_tone` (str, optional): Tone of the report.
- `report_sources` (list, optional): List of report sources.
- `additional_context` (str, optional): Additional context for the report.
- `summary_length` (int, optional): Length of the summary.
- `include_references` (bool, optional): Whether to include references.

## API Endpoints

### `/api/initiate_research`

- `task` (str): The research task.
- `report_type` (str): The type of report.
- `agent` (str): The agent to use.
- `report_tone` (str, optional): Tone of the report.
- `report_sources` (list, optional): List of report sources.
- `source_urls` (list, optional): List of source URLs.
- `tone` (str, optional): The tone of the report.
- `config_path` (str, optional): Path to the configuration file.
- `headers` (dict, optional): HTTP headers.
- `subtopics` (list, optional): List of subtopics.
- `additional_context` (str, optional): Additional context for the report.
- `summary_length` (int, optional): Length of the summary.
- `include_references` (bool, optional): Whether to include references.

### `/ws`

- WebSocket endpoint for real-time communication.
