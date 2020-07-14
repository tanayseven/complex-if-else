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


def test_invalid_file():
    invalid_input_file = MockPath(has_valid_file_path=False)
    input_files = [invalid_input_file]
    success_cases, failure_cases = extract_details(input_files)
    assert len(success_cases) == 0
    assert len(failure_cases) == 1


def test_not_valid_html():
    input_file_without_valid_html = MockPath(text_content="foo bar")
    input_files = [input_file_without_valid_html]
    success_cases, failure_cases = extract_details(input_files)
    assert len(success_cases) == 0
    assert len(failure_cases) == 1


def test_empty_first_name():
    input_file_without_valid_html = MockPath(text_content=empty_html_template.format(
        name_title="Mr.",
        first_name="",
        middle_name="",
        last_name="Neumann",
    ))
    input_files = [input_file_without_valid_html]
    success_cases, failure_cases = extract_details(input_files)
    assert len(success_cases) == 0
    assert len(failure_cases) == 1


def test_last_name_not_in_title_case():
    input_file_without_valid_html = MockPath(text_content=empty_html_template.format(
        name_title="Mr.",
        first_name="John",
        middle_name="von",
        last_name="neumann",
    ))
    input_files = [input_file_without_valid_html]
    success_cases, failure_cases = extract_details(input_files)
    assert len(success_cases) == 0
    assert len(failure_cases) == 1


def test_no_name_prefixes_exist():
    input_file_without_valid_html = MockPath(text_content=empty_html_template.format(
        name_title="",
        first_name="John",
        middle_name="von",
        last_name="Neumann",
    ))
    input_files = [input_file_without_valid_html]
    success_cases, failure_cases = extract_details(input_files)
    assert len(success_cases) == 0
    assert len(failure_cases) == 1


def test_no_name_prefixes_provided():
    input_file_without_valid_html = MockPath(text_content="""<html>
    <body>
    <div id="author">
    <p>
    <span id="first-name">{first_name}</span>
    <span class="middle-name">{middle_name}</span>
    <span id="last-name">{last_name}</span></p>
    </div>
    </body
    </html>""".format(
        first_name="John",
        middle_name="von",
        last_name="Neumann",
    ))
    input_files = [input_file_without_valid_html]
    success_cases, failure_cases = extract_details(input_files)
    assert len(success_cases) == 0
    assert len(failure_cases) == 1
