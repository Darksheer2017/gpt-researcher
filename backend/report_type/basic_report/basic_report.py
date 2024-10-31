from fastapi import WebSocket

from gpt_researcher.master.agent import GPTResearcher
from gpt_researcher.utils.enum import Tone


class BasicReport:
    def __init__(
        self,
        query: str,
        report_type: str,
        report_source: str,
        source_urls,
        tone: Tone,
        config_path: str,
        websocket: WebSocket,
        headers=None,
        report_tone: str = None,
        report_sources: list = None
    ):
        self.query = query
        self.report_type = report_type
        self.report_source = report_source
        self.source_urls = source_urls
        self.tone = tone
        self.config_path = config_path
        self.websocket = websocket
        self.headers = headers or {}
        self.report_tone = report_tone
        self.report_sources = report_sources

    async def run(self):
        # Initialize researcher
        researcher = GPTResearcher(
            query=self.query,
            report_type=self.report_type,
            report_source=self.report_source,
            source_urls=self.source_urls,
            tone=self.tone,
            config_path=self.config_path,
            websocket=self.websocket,
            headers=self.headers,
            report_tone=self.report_tone,
            report_sources=self.report_sources
        )

        await researcher.conduct_research()
        report = await researcher.write_report()
        return report
