"""Convert the 18 SVG use-case diagrams to vector PDF for XeLaTeX."""
from pathlib import Path
import pymupdf


def main():
    images = Path(__file__).resolve().parent / "sections" / "images"
    sources = [images / f"UC_{number:02d}.svg" for number in range(1, 19)]
    missing = [str(source) for source in sources if not source.is_file()]
    if missing:
        raise FileNotFoundError("Missing diagrams: " + ", ".join(missing))
    for source in sources:
        target = source.with_suffix(".pdf")
        with pymupdf.open(source) as svg:
            pdf_bytes = svg.convert_to_pdf()
        with pymupdf.open(stream=pdf_bytes, filetype="pdf") as pdf:
            pdf.save(target, garbage=4, deflate=True)
        print(f"Prepared {target.name}")


if __name__ == "__main__":
    main()
