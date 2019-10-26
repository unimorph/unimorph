#!/usr/bin/env python3
"""UniMorph: Annotated morphology in the world's languages\n
Quick usage:
    analyze a sentence:
        cat spanish.txt | unimorph -l spa
    download datasets:
        cat iso-codes.txt | xargs -I@ unimorph download --lang @
"""
import argparse
import logging
import os
import pathlib
import subprocess
import sys
from typing import List

import pandas as pd

__version__ = "0.0.3"

USERHOME = pathlib.Path.home()
UNIMORPH_DIR_ = os.environ.get("UNIMORPH", USERHOME / ".unimorph")
UNIMORPH_DIR = pathlib.Path(UNIMORPH_DIR_)

CITATION = r"""
@inproceedings{kirov-etal-2018-unimorph,
    title = "{U}ni{M}orph 2.0: Universal Morphology",
    author = {Kirov, Christo  and
      Cotterell, Ryan  and
      Sylak-Glassman, John  and
      Walther, G{\'e}raldine  and
      Vylomova, Ekaterina  and
      Xia, Patrick  and
      Faruqui, Manaal  and
      Mielke, Sebastian  and
      McCarthy, Arya D.  and
      K{\"u}bler, Sandra  and
      Yarowsky, David  and
      Eisner, Jason  and
      Hulden, Mans},
    booktitle = "Proceedings of the Eleventh International Conference on Language Resources and Evaluation ({LREC} 2018)",
    month = may,
    year = "2018",
    address = "Miyazaki, Japan",
    publisher = "European Language Resources Association (ELRA)",
    url = "https://www.aclweb.org/anthology/L18-1293",
}
"""


def is_empty(dir: pathlib.Path) -> bool:
    assert dir.is_dir()
    return list(dir.iterdir()) == []


def not_loaded(lang: str) -> bool:
    output_dir = UNIMORPH_DIR / lang
    return (not output_dir.exists()) or is_empty(output_dir)


def download_unimorph(lang: str):
    output_dir = UNIMORPH_DIR / lang
    output_dir.mkdir(exist_ok=True, parents=True)

    if not_loaded(lang):
        logging.info(f"Downloading unimorph/{lang} to {output_dir}")
        subprocess.run(
            ["git", "clone", f"https://github.com/unimorph/{lang}.git"],
            check=True,
            cwd=UNIMORPH_DIR,
        )
    assert output_dir.is_dir()


def load_dataset(lang: str, specific_file=None):
    if specific_file is None:
        specific_file = lang

    download_unimorph(lang)

    language_path = UNIMORPH_DIR / lang / specific_file
    data = pd.read_csv(
        language_path, header=None, sep="\t", names=["lemma", "form", "features"]
    )
    return data


def inflect_word(word: str, *, lang: str, features=None):
    data = load_dataset(lang)
    if features is None:
        result = data[data.lemma == word]
    else:
        result = data[(data.lemma == word) & (data.features == features)]
    return result.to_csv(sep="\t", index=False, header=None)


def analyze_word(word: str, *, lang: str):
    data = load_dataset(lang)
    return data[data.form == word].to_csv(sep="\t", index=False, header=None)


def get_list_of_datasets() -> List[str]:
    command = r"""
        for i in {1..2}
        do
          curl -s "https://api.github.com/orgs/unimorph/repos?per_page=100&page=$i"
        done |
          grep ssh_url |
          grep -o 'git@github.com:unimorph/[a-z]\{3\}.git' |
          cut -c25-27
        """

    data = subprocess.run(
        command, shell=True, check=True, capture_output=True, encoding="utf-8"
    )
    return sorted(filter(bool, data.stdout.split("\n")))


def parse_args():
    parser = argparse.ArgumentParser(
        __doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        "mode", choices={"download", "list", "citation", "inflect", "analyze"}
    )
    parser.add_argument("--language", "-l", help="language (3-letter ISO 639-3 code)")
    parser.add_argument("--word", "-w", type=str)
    parser.add_argument("--features", type=str)

    parser.add_argument(
        "--quiet",
        "-q",
        default=False,
        action="store_true",
        help="suppress informative output",
    )
    parser.add_argument(
        "-V", "--version", action="version", version=f"%(prog)s {__version__}"
    )
    args = parser.parse_args()

    if args.language is not None and len(args.language) != 3:
        parser.error("--language must be a 3-letter ISO 639-3 code!")

    return args


def main() -> None:
    args = parse_args()

    sys.stdin = open(
        sys.stdin.fileno(), mode="r", encoding="utf-8", buffering=True, newline="\n"
    )
    sys.stdout = open(sys.stdout.fileno(), mode="w", encoding="utf-8", buffering=True)

    if not args.quiet:
        logging.basicConfig(level=logging.INFO, format="unimorph: %(message)s")

    if args.mode == "download":
        download_unimorph(args.language)
        sys.exit(0)
    elif args.mode == "list":
        print(list(get_list_of_datasets()))
        sys.exit(0)
    elif args.mode == "citation":
        print(CITATION)
        sys.exit(0)
    elif args.mode == "inflect":
        print(
            inflect_word(args.word, lang=args.language, features=args.features), end=""
        )
    elif args.mode == "analyze":
        print(analyze_word(args.word, lang=args.language), end="")
    else:
        raise ValueError(f"Unknown mode {args.mode}")


if __name__ == "__main__":
    main()
