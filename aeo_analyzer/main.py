import json
import logging
from typing import Dict, Any
from aeo_analyzer.utils import fetch_url, parse_html

class AEOAnalyzer:
    def __init__(self, target_url: str):
        self.target_url = target_url
        self.soup = None
        self.response = None

    def run_audit(self) -> Dict[str, Any]:
        """Runs complete AEO & Technical SEO evaluation."""
        logging.info(f"Starting audit for: {self.target_url}")
        self.response = fetch_url(self.target_url)
        
        if not self.response:
            return {"error": "Target URL reached network error or timeout."}

        self.soup = parse_html(self.response.text)

        results = {
            "target_url": self.target_url,
            "status_code": self.response.status_code,
            "technical_seo": self._check_technical_seo(),
            "aeo_readiness": self._check_aeo_structure()
        }
        return results

    def _check_technical_seo(self) -> Dict[str, Any]:
        canonical = self.soup.find("link", rel="canonical")
        title = self.soup.find("title")
        meta_desc = self.soup.find("meta", attrs={"name": "description"})

        return {
            "title": title.text.strip() if title else None,
            "meta_description": meta_desc["content"].strip() if meta_desc and "content" in meta_desc.attrs else None,
            "has_canonical": True if canonical else False,
            "canonical_href": canonical["href"] if canonical and "href" in canonical.attrs else None
        }

    def _check_aeo_structure(self) -> Dict[str, Any]:
        schema_scripts = self.soup.find_all("script", type="application/ld+json")
        h1_tags = [h1.text.strip() for h1 in self.soup.find_all("h1")]
        h2_tags = [h2.text.strip() for h2 in self.soup.find_all("h2")]
        
        # Check for direct answer blocks under H2/H3 (40-60 word paragraphs)
        paragraphs = [p.text.strip() for p in self.soup.find_all("p")]
        concise_answers = [p for p in paragraphs if 30 <= len(p.split()) <= 65]

        return {
            "has_json_ld_schema": len(schema_scripts) > 0,
            "schema_blocks_count": len(schema_scripts),
            "h1_count": len(h1_tags),
            "h1_content": h1_tags,
            "h2_headings_count": len(h2_tags),
            "direct_answer_blocks_found": len(concise_answers)
        }

if __name__ == "__main__":
    import sys
    url = sys.argv[1] if len(sys.argv) > 1 else "https://example.com"
    analyzer = AEOAnalyzer(url)
    audit_report = analyzer.run_audit()
    print(json.dumps(audit_report, indent=4))
