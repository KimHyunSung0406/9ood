
"""Core functions of 9ood Filter."""

from pathlib import Path

SUPPORTED_EXTENSIONS = {".txt", ".md", ".csv"}


def read_document(input_path):
    """Read and validate a .txt, .md, or .csv document file as a string.

    Args:
        input_path (str | Path): Path to the input document file (.txt, .md, or .csv).

    Returns:
        str: The full text content of the file.

    Raises:
        TypeError: If `input_path` is not a string or Path object.
        ValueError: If the file extension is not `.txt`, `.md`, or `.csv`.
        FileNotFoundError: If the file does not exist at `input_path`.

    Examples:
        >>> read_document("sample.txt")  # doctest: +SKIP
        '작성자: 홍길동'
    """
    if not isinstance(input_path, (str, Path)):
        raise TypeError("input_path must be a str or Path")

    path = Path(input_path)
    if path.suffix.lower() not in SUPPORTED_EXTENSIONS:
        raise ValueError(
            f"Unsupported file format: '{path.suffix}'. Only .txt, .md, and .csv are supported."
        )
    if not path.is_file():
        raise FileNotFoundError(f"File not found: '{input_path}'")

    try:
        return path.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError:
        return path.read_text(encoding="cp949")


def detect_personal_info(text):
    """Detect personal information such as names, emails, and phone numbers.

    Args:
        text (str): The input text to scan.

    Returns:
        list[dict]: A list of detected personal information.

    Examples:
        >>> detect_personal_info("Contact: test@example.com")
        [{'category': 'email', 'value': 'test@example.com'}]
    """
    raise NotImplementedError

def replace_personal_info(text, replacements):
    """Replace personal information with custom text.

    Args:
        text (str): Text containing personal information.
        replacements (dict): Replacement text for each category.

    Returns:
        str: Text with personal information replaced.

    Examples:
        >>> replace_personal_info(
        ...     "Email: test@example.com",
        ...     {"email": "[이메일]"}
        ... )
        'Email: [이메일]'
    """
    raise NotImplementedError


def remove_personal_info(text):
    """Remove personal information from the given text.

    Args:
        text (str): Text containing personal information.

    Returns:
        str: Text with personal information removed.

    Examples:
        >>> remove_personal_info("Email: test@example.com")
        'Email: '
    """
    raise NotImplementedError


def anonymize_file(input_path, output_path, replacements):
    """Anonymize personal information in a document file.

    Args:
        input_path (str): Path to the original file.
        output_path (str): Path to save the anonymized file.
        replacements (dict): Replacement text for each category.

    Returns:
        str: Path to the saved file.

    Examples:
        >>> anonymize_file(
        ...     "input.txt", "output.txt", {"email": "[이메일]"}
        ... )
        'output.txt'
    """
    raise NotImplementedError


def summarize_changes(detections):
    """Count detected personal information by category.

    Args:
        detections (list[dict]): List of detected personal information.

    Returns:
        dict: Number of detected items for each category.

    Examples:
        >>> summarize_changes([
        ...     {"category": "email", "value": "test@example.com"}
        ... ])
        {'email': 1}
    """
    raise NotImplementedError
