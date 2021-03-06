Versioning guideline draft
==========================


Repository structure
--------------------

The [GitHub organization UniMorph] contains many repositories for different languages (`eng`, `deu`, `sqi`, ...), one meta-repository called `unimorph` for the UniMorph *bundle* (containing this document), and a repository `unimorph.github.io`, in which the website is developed.
All repositories have issue trackers that serve repository-specific causes.

### The individual language repositories

Individual language repositories are primarily maintained by people working on this language.
They contain the following files (using `eng` as an example):

##### eng

The main data containing lines of the form `$lemma<TAB>$word<TAB>$features`, where `$features` consists of semicolon-separated tokens.

##### VERSION

This autogenerated file contains the version that is used, i.e. `1.2.3` or `1.2.3-dirty` if the "dirty" repository is used instead of a packaged release (see below).

##### README.md

This file contains both autogenerated and non-generated portions. An example might look like this:

```
eng (v1.2.3)
===

English is a language.
Data for it is obtainable.
We actually obtained it.
Also we did this one weird thing with the data.


How to refer
------------

#### Citation

@InProceedings{DreEis11Discovering,
  author    = {Cool Person and Even Cooler Person and Really Cool Person},
  title     = {UniMorph is really cool},
  booktitle = {Proceedings of a really cool conference},
  year      = {2018},
}

The paper is available at SOME_REALLY_COOL_BUT_STATIC_LINK.

#### Data set name

If you use this data individually, please refer to it as
"eng-local-1.2.3 available at unimorph.org". If you use it as part
of UniMorph release x.y.z, please refer to it as "UniMorph-x.y.z/eng".
The latter is generally preferred.

Maintainers
-----------

* Some person (some@address.tld)
* Another person (another@address.tld)

Changelog
---------

v1.2.3:
  Fixed yet another typo, ugh.
  Maybe we shouldn't release this stuff in the middle of the night.
v1.2.2:
  Fixed another typo.
  I guess it did happen again.
v1.2.1:
  Fixed some typo.
  Surely this will not happen again.
v1.2.0:
  Added new data from this weird resource we found.
v1.1.1:
  Fix encoding issues
v1.1.0:
  Added substantial new data
v1.0.0:
  Initial (toy) data
```

Here the version number at the top, the data set name section of "How to refer", and the changelog at the bottom are generated by a script on release, as we see in the section "Making a new release".

### The `unimorph` repo

The big `unimorph` meta-repo (used for UniMorph *bundles*) contains a `README`, this versioning guideline file and all language repositories as [git submodules].
This way commits in the `unimorph` repos are used to fix certain states of the language repositories that are included as submodules, i.e., the act of updating a language in the bundle is represented in a commit.

In addition to this implicit representation a file containing the list of all languages and their respecitve versions will be automatically created and updated in the repository for easier viewing.

The `unimorph` repo is manipulated only by UniMorph maintainers, ideally one person (assisted by a number of shell scripts for distribution and overview generation).


Distribution scheme
-------------------

All individual language releases and all bundle releases are available at all times. They are distributed as compressed archives using [Github Releases].

A *release for an individual language* is manually created once a language maintainer decides that there have been enough improvements (in the form of one or multiple commits in the repository).
The maintainer creates a tag for the most recent commit, after which a release is automatically created and bound to this tag and archived versions of the data are attached to it.

A *release for the whole UniMorph bundle* is likewise created when enough improvements across all languages make it desirable. Again, a tag is created, a release automatically bound to it, and one big archive attached to it.


Making a new release
--------------------

Commits are made and pushed, then the language maintainer can go to `$WEBSITE`, where a script is running that helps with the release process.
The script proposes:
 * a new version number and
 * a changelog based on the commit messages since the last release

Once the maintainer confirms their choice, the script:
 1)  clones the repository to start manipulating it
 2)  writes the new version number into `VERSION`
 3)  exchanges the version number in the first line of `README.md`
 4)  adds the changelog to the "Changelog" section in `README.md`
 5)  commits these changes
 6)  tags this commit with the version number
 7)  pushes commit and tag to GitHub
 8)  creates a release from the tag, version number and changelog
 9)  appends "dirty" to the version numbers in `VERSION` and the first line of `README.md`
 10) commits this "dirty"-change
 11) pushes it to GitHub
 12) deletes the local repository copy.

Thus `VERSION` is fully auto-generated and `README.md` partially.

If any of these steps do not work (e.g., if autogenerated sections have been overwritten), the language maintainer and a UniMorph maintainer are sent an email with error details (the former is read from `README.md`).

*Note that the automatic generation of train/dev/test splits could be integrated after step 4, if we want to perform it automatically.*


Version numbering
-----------------

Both individual languages as well as complete UniMorph bundles will be assigned version numbers.

| release             | version number schema       | complete version name                     |
|---------------------|-----------------------------|-------------------------------------------|
| Individual language | `$schemaver`.`$languagever` | `$lang`-local-`$schemaver`.`$languagever` |
| *example*           | 1.2.3                       | eng-local-1.2.3                           |
| UniMorph bundle     | `$schemaver`.`$bundlever`   | UniMorph-`$schemaver`.`$bundlever`        |
| *example*           | 1.1.0                       | UniMorph-1.1.0                            |

Note that individual languages in a UniMorph bundle can still be referenced as "UniMorph-`$schemaver`.`$bundlever`/`$lang`", e.g., UniMorph-1.1.0/eng.

#### `$lang`

The three-letter ISO language code.

#### `$schemaver`
The number `$schemaver` is not likely to change anytime soon, i.e., this will stay `1`, until some big/breaking change to schema or data format is made. A big/breaking change is defined as one that requires all languages to be updated.
It is shared between all languages and the bundle.

#### `$languagever`
The identifier `$languagever` stands for a two-tuple of numbers, the *minor version* and the *patch/bugfix number* (see [semantic versioning] for an explanation of the difference).
It is incremented for each language individually (i.e., `$languagever` is not shared between languages or with the bundle), whenever improvements are enough to warrant a new individual release of the language.
It is independent of all `$bundlever` values.

#### `$bundlever`
Like `$languagever`, `$bundlever` is a `minor.patch`-style two-tuple that is incremented for each new release.
It is independent of all `$languagever` values.

### Example

For the first release we will have *eng-local-1.0.0* and *deu-local-1.0.0* as languages. These sets are downloadable individually as well as as one bundle *UniMorph-1.0.0* (containing *UniMorph-1.0.0/eng* and *UniMorph-1.0.0/deu*).

After the release some work is being made on German data, resulting in an individual-language release *deu-local-1.1.0*, but the improvements are not deemed interesting enough for a re-release of the UniMorph bundle. Good call, since a mistake is found and fixed for *deu-local-1.1.1*.

More work is being put into the German data, it reaches *deu-local-1.2.0*, the English data is also improved to a version *eng-local-1.1.0* and we add Albanian data, whose first release will then be *sqi-local-1.0.0*.

At this point we decide that it is time for a new bundle release and release *unimorph-1.1.0*, containing the data of *deu-local-1.2.0*, *eng-local-1.1.0*, and *sqi-local-1.0.0*, referenced in the bundle as *UniMorph-1.1.0/deu*, *UniMorph-1.1.0/eng*, and *UniMorph-1.1.0/sqi*, respectively.


[GitHub organization UniMorph]: https://github.com/orgs/unimorph/
[git submodules]: https://git-scm.com/book/en/v2/Git-Tools-Submodules
[semantic versioning]: http://semver.org/
[Github Releases]: https://help.github.com/articles/creating-releases/