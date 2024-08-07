"""API."""

import re
from datetime import datetime, timedelta

from lookback import board
from lookback.times import end_of_today

SPACE = " "
HEAD3 = "###"
ANY_HEAD_CONTENTS = re.compile(r"^#+\s.*", re.MULTILINE)
HEAD3_TOKEN = re.compile(rf"^{HEAD3}{SPACE}", re.MULTILINE)
MISC_HEADING = f"{HEAD3}{SPACE}Miscellaneous"


def indent_report(report: str, title: str) -> str:
    """Indent all headings in a report and give it a top-level heading."""
    report_indented = ANY_HEAD_CONTENTS.sub(r"#\g<0>", report)
    return f"# {title}\n\n{report_indented}"


def agg_comments(comments: list[board.Action]) -> list[board.Action]:
    """Aggregate comments by their header."""
    # Split comments which represent multiple headings into individual comments
    split_comments: list[board.Action] = []
    for comment in comments:
        split_comments.extend(split_comment(comment))

    # Aggregate comments associated with the same heading
    texts = [comment.data.text for comment in split_comments]
    seen: dict[str, board.Action] = {}
    keep: list[bool] = []
    for text, comment in zip(texts, split_comments, strict=True):
        (first_line, *rest) = text.split("\n\n")
        if not HEAD3_TOKEN.match(first_line):
            first_line = MISC_HEADING
            comment.data.text = f"{first_line}\n\n{comment.data.text}"
        # TODO: Replace match/case with regex. Brittle code here due to cases not being
        # TODO: able to use HEAD3 without binding it.
        match first_line.split():
            case ["###", *_]:
                if prev_comment := seen.get(first_line):
                    prev_comment.data.text += "\n\n" + "\n\n".join(rest)
                    keep.append(False)
                else:
                    seen[first_line] = comment
                    keep.append(True)
            case _:
                raise ValueError(f"Invalid comment:\n\n{comment.data.text}")
    kept_comments = [
        comment for comment, keep in zip(split_comments, keep, strict=True) if keep
    ]

    # Return comments with the "Miscellaneous" heading at the end
    return sorted(
        kept_comments, key=lambda comment: comment.data.text.startswith(MISC_HEADING)
    )


def split_comment(comment: board.Action) -> list[board.Action]:
    """Split a comment with multiple headers into comments representing one header."""
    if HEAD3 not in comment.data.text:
        comment.data.text = f"{MISC_HEADING}\n\n{comment.data.text}"
    texts = [
        f"{HEAD3}{SPACE}{text}" for text in HEAD3_TOKEN.split(comment.data.text)[1:]
    ]
    comments: list[board.Action] = []
    for text in texts:
        subcomment = comment.model_copy(deep=True)
        subcomment.data.text = text
        comments.append(subcomment)
    return comments


def sort_comments(comments: list[board.Action]) -> list[board.Action]:
    """Sort comments in chronological order."""
    return sorted(comments, key=lambda comment: datetime.fromisoformat(comment.date))


def filter_comments(comments: list[board.Action], card: str = "", days: int = 0):
    """Filter comments."""
    card_limit = card or None
    date_limit = end_of_today - timedelta(days=days) if days != 0 else None
    return [
        comment
        for comment in comments
        if comment.data.card
        and comment.data.card.name
        and (not card_limit or comment.data.card.name == card)
        and (not date_limit or datetime.fromisoformat(comment.date) > date_limit)
    ]


def get_comments(board: board.Model) -> list[board.Action]:
    """Get comments in chronological order."""
    return [action for action in board.actions if action.type == "commentCard"]
