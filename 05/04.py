class Report:
    def render(self, data):
        return self._format_header() + self._format_body(data) + self._format_footer()

    def _format_header(self):
        return ""

    def _format_body(self, data):
        return ""

    def _format_footer(self):
        return ""


class HtmlReport(Report):
    def _format_header(self):
        return "<html><h1>Report</h1>"

    def _format_body(self, data):
        items = "".join(f"<li>{item}</li>" for item in data)
        return f"<ul>{items}</ul>"

    def _format_footer(self):
        return "<p>End</p></html>"


r = HtmlReport()
print(r.render(["A", "B"]))
