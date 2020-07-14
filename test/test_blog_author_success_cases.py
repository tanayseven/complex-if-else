from dataclasses import dataclass

from src.file_action.blog_author import extract_details

empty_html_template = """<html>
<body>
<div id="author">
<p>
<span class="name-prefix">{name_title}</span>
<span id="first-name">{first_name}</span>
<span class="middle-name">{middle_name}</span>
<span id="last-name">{last_name}</span></p>
</div>
</body
</html>"""


@dataclass
class MockPath:
    has_valid_file_path: bool = True
    text_content: str = ""

    def is_file(self) -> bool:
        return self.has_valid_file_path

    def read_text(self) -> str:
        return self.text_content


def test_with_name_prefix_mr():
    input_file_without_valid_html = MockPath(text_content=empty_html_template.format(
        name_title="Mr.",
        first_name="John",
        middle_name="von",
        last_name="Neumann",
    ))
    input_files = [input_file_without_valid_html]
    success_cases, failure_cases = extract_details(input_files)
    assert len(success_cases) == 1
    assert len(failure_cases) == 0


def test_with_name_prefix_ms():
    input_file_without_valid_html = MockPath(text_content=empty_html_template.format(
        name_title="Ms.",
        first_name="John",
        middle_name="von",
        last_name="Neumann",
    ))
    input_files = [input_file_without_valid_html]
    success_cases, failure_cases = extract_details(input_files)
    assert len(success_cases) == 1
    assert len(failure_cases) == 0


def test_with_name_prefix_mrs():
    input_file_without_valid_html = MockPath(text_content=empty_html_template.format(
        name_title="Mrs.",
        first_name="John",
        middle_name="von",
        last_name="Neumann",
    ))
    input_files = [input_file_without_valid_html]
    success_cases, failure_cases = extract_details(input_files)
    assert len(success_cases) == 1
    assert len(failure_cases) == 0


def test_with_name_prefix_miss():
    input_file_without_valid_html = MockPath(text_content=empty_html_template.format(
        name_title="Miss.",
        first_name="John",
        middle_name="von",
        last_name="Neumann",
    ))
    input_files = [input_file_without_valid_html]
    success_cases, failure_cases = extract_details(input_files)
    assert len(success_cases) == 1
    assert len(failure_cases) == 0
