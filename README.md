# UniMorph: The Universal Morphology Initiative

[![PyPI
version](https://badge.fury.io/py/unimorph.svg)](https://pypi.org/project/unimorph)
[![Supported Python
versions](https://img.shields.io/pypi/pyversions/unimorph.svg)](https://pypi.org/project/unimorph)

The Universal Morphology (UniMorph) project is a collaborative 
effort to improve how NLP handles complex morphology in the world’s 
languages. The goal of UniMorph is to annotate morphological data
in a universal schema that allows an inflected word from any 
language to be defined by its lexical meaning, typically carried 
by the lemma, and by a rendering of its inflectional form in terms 
of a bundle of morphological features from our schema. The 
specification of the schema is described in [Sylak-Glassman (2016)](http://www.unimorph.org/doc/Sylak-Glassman_2016_-_UniMorph_Schema_User_Guide.pdf).

---

This tool provides turnkey command-line access to morphological annotations in over 100 languages.

To install the UniMorph Python extension, install it from PyPI:

 ```bash
 pip3 install unimorph
 ```

The tool will then be available to you from the command-line as `unimorph`. To see the features available, run `unimorph --help`.

## Usage

Query the available UniMorph languages' ISO 639-3 codes.

```bash
unimorph list
```

Give the complete paradigm for a lemma.

```bash
unimorph inflect --word recken --lang deu
```

Get a particular form of the lemma.

```bash
unimorph inflect --word recken --features V;IND;PRS;2;SG --lang deu
```

Analyze a word form: What are its lemma and features?

```bash
unimorph analyze --word gereckt --lang deu
```

(You can also use short param names.)

```bash
unimorph analyze -w gereckt -l deu
```

Records in UniMorph's inflectional databases cannot hope to exhaustively cover a language's lexicon, especially in light of novel words. If a word is missing, let us know.

## Contribution

UniMorph is an open project! We want you!

Found a bug? Want to contribute source code? Submit an issue or pull request to the appropriate [GitHub repository](https://github.com/unimorph). Language-specific corrections or additions should be marked in their corresponding repository; improvements to the `unimorph` command-line tool should be noted in the [`unimorph` repository](https://github.com/unimorph/unimorph).

## Citation

If you use the latest version of the UniMorph datasets (v2.0), please cite [Kirov et al. (2018)](https://www.aclweb.org/anthology/L18-1293/):

```bibtex
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
      McCarthy, Arya  and
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
```

If you refer to the latest version of the universal annotation schema, please cite [Sylak-Glassman et al. (2015)](https://www.aclweb.org/anthology/P15-2111/):

```bibtex
@inproceedings{sylak-glassman-etal-2015-language,
    title = "A Language-Independent Feature Schema for Inflectional Morphology",
    author = "Sylak-Glassman, John  and
      Kirov, Christo  and
      Yarowsky, David  and
      Que, Roger",
    booktitle = "Proceedings of the 53rd Annual Meeting of the Association for Computational Linguistics and the 7th International Joint Conference on Natural Language Processing (Volume 2: Short Papers)",
    month = jul,
    year = "2015",
    address = "Beijing, China",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/P15-2111",
    doi = "10.3115/v1/P15-2111",
    pages = "674--680",
}
```

## Advanced usage

`unimorph` stores language databases in a default location. This can be overridden by setting the shell environment variable `UNIMORPH` to the preferred folder.
