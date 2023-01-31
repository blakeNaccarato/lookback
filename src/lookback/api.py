"""API"""

from datetime import datetime, timedelta

from lookback import board
from lookback.times import end_of_today


def agg_comments(kept_comments: list[board.Action]) -> list[board.Action]:
    """Aggregate comments by their header."""

    # Split comments which represent multiple headings into individual comments
    split_comments: list[board.Action] = []
    for comment in kept_comments:
        if comment.data.text.count("###") > 1:
            split_comments.extend(split_comment(comment))
        else:
            split_comments.append(comment)

    # Aggregate comments associated with the same heading
    misc_heading = "### Miscellaneous"
    texts = [comment.data.text for comment in split_comments]
    seen: dict[str, board.Action] = {}
    keep: list[bool] = []
    for text, comment in zip(texts, split_comments):
        (first_line, *rest) = text.split("\n\n")
        if not first_line.startswith("###"):
            first_line = misc_heading
            comment.data.text = f"{first_line}\n\n{comment.data.text}"
        match first_line.split():
            case ["###", *_]:
                if prev_comment := seen.get(first_line):
                    prev_comment.data.text += "\n\n" + "\n\n".join(rest)
                    keep.append(False)
                else:
                    seen[first_line] = comment
                    keep.append(True)
            case _:
                raise ValueError(f"Invalid comment: {comment.data.text}")
    kept_comments = [comment for comment, keep in zip(split_comments, keep) if keep]

    # Return comments with the "Miscellaneous" heading at the end
    return sorted(
        kept_comments, key=lambda comment: comment.data.text.startswith(misc_heading)
    )


def split_comment(comment: board.Action) -> list[board.Action]:
    """Split a comment with multiple headers into comments representing one header."""
    texts = [f"### {text}" for text in comment.data.text.split("### ")[1:]]
    comments: list[board.Action] = []
    for text in texts:
        subcomment = comment.copy()
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
