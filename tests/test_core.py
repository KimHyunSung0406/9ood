"""Unit tests for good_pi_filter.core."""

import pytest

from good_pi_filter import read_document


# normal: valid .txt and .md files with Korean content
def test_read_document_reads_txt_and_md(tmp_path):
    txt_file = tmp_path / "sample.txt"
    md_file = tmp_path / "notes.md"
    txt_file.write_text("작성자: 홍길동\n연락처: 010-1234-5678", encoding="utf-8")
    md_file.write_text("# 회의록\n- 이메일: test@example.com", encoding="utf-8")

    assert read_document(txt_file) == "작성자: 홍길동\n연락처: 010-1234-5678"
    assert read_document(str(md_file)) == "# 회의록\n- 이메일: test@example.com"


# boundary: empty file returns empty string
def test_read_document_empty_file(tmp_path):
    empty_file = tmp_path / "empty.txt"
    empty_file.write_text("", encoding="utf-8")

    assert read_document(empty_file) == ""


# wrong input: unsupported file extension must raise ValueError
def test_read_document_rejects_unsupported_extension(tmp_path):
    pdf_file = tmp_path / "document.pdf"
    pdf_file.write_text("dummy content", encoding="utf-8")

    with pytest.raises(ValueError):
        read_document(pdf_file)


# wrong input: missing file must raise FileNotFoundError
def test_read_document_missing_file_raises_error(tmp_path):
    missing_file = tmp_path / "nonexistent.txt"

    with pytest.raises(FileNotFoundError):
        read_document(missing_file)
