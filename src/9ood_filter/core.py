
"""Core functions of 9ood Filter."""


def detect_personal_info(text):
    """Find personal information in the given text.

    Args:
        text (str): Text to check.

    Returns:
        list[dict]: A list of detected personal information.

    Examples:
        >>> detect_personal_info("Email: test@example.com")
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
