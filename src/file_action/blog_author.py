import enum
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

import bs4 as bs


class TitleType(enum.Enum):
    MR = ("Mr.",)
    MS = ("Ms.",)
    MRS = ("Mrs.",)
    MISS = ("Miss.",)


@dataclass
class BlogAuthor:
    name_prefix: Optional[str]
    first_name: str
    middle_name: Optional[str]
    last_name: str


def extract_details(html_files: List[Path]):
    failure_cases = []
    success_cases: List[BlogAuthor] = []
    for file in html_files:
        if file.is_file():
            soup = bs.BeautifulSoup(file.read_text(), features="html.parser")
            if soup.find("html") is not None:
                name_prefixes = [tag.text for tag in soup.find_all(class_="name-prefix")]
                first_name = soup.find(id="first-name").text
                middle_names = [tag.text for tag in soup.find_all(class_="middle-name")]
                last_name = soup.find(id="last-name").text
                if len(first_name) + len(middle_names) == 0 or last_name[0].islower():
                    failure_cases.append(file)
                elif len(name_prefixes) == 0:
                    failure_cases.append(file)
                else:
                    catenated_name_prefixes = ""
                    for name_prefix in name_prefixes:
                        title_type: Optional[TitleType] = None
                        if name_prefix == "Mr.":
                            title_type = TitleType.MR
                        elif name_prefix == "Mrs.":
                            title_type = TitleType.MRS
                        elif name_prefix == "Ms.":
                            title_type = TitleType.MS
                        elif name_prefix == "Miss.":
                            title_type = TitleType.MISS
                        if title_type is not None:
                            catenated_name_prefixes += " " + title_type.value[0]
                    catenated_name_prefixes = catenated_name_prefixes.rstrip()
                    if len(catenated_name_prefixes) == 0:
                        failure_cases.append(file)
                        continue
                    catenated_middle_names = ""
                    if len(first_name) != 0 and len(last_name) != 0:
                        if len(middle_names) > 0:
                            for middle_name in middle_names:
                                if middle_name:
                                    catenated_middle_names += " " + middle_name
                            catenated_middle_names = catenated_middle_names.lstrip()
                    else:
                        failure_cases.append(file)
                        continue
                    success_cases.append(
                        BlogAuthor(
                            name_prefix=catenated_name_prefixes,
                            first_name=first_name,
                            middle_name=catenated_middle_names,
                            last_name=last_name,
                        )
                    )
            else:
                failure_cases.append(file)
                continue
        else:
            failure_cases.append(file)
            continue
    return success_cases, failure_cases
