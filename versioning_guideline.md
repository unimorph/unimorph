Versioning guideline draft
==========================


Repository structure
--------------------

The [GitHub organization UniMorph] contains many repositories for different languages (`eng`, `deu`, `sqi`, ...), one meta-repository called `unimorph` for the UniMorph *bundle* (containing this document), and a repository `unimorph.github.io`, in which the website is developed.
All repositories have issue trackers that serve repository-specific causes.

#### The individual language repositories

Each repository that contains data for an individual language contains a `README` with a primary maintainer and contact info as well as other useful information (completion, data sources, ...).
This file and the data is primarily maintained by people working on this language.

#### The `unimorph` repo

The big `unimorph` meta-repo (used for UniMorph *bundles*) contains a `README`, this versioning guideline file and all language repositories as [git submodules].
This way commits in the `unimorph` repos are used to fix certain states of the language repositories that are included as submodules, i.e., the act of updating a language in the bundle is represented in a commit.

In addition to this implicit representation a file containing the list of all languages and their respecitve versions will be automatically created and updated in the repository for easier viewing.

The `unimorph` repo is manipulated only by UniMorph maintainers, ideally one person (assisted by a number of shell scripts for distribution and overview generation).


Distribution process
--------------------

All individual language releases and all bundle releases are available at all times. They are distributed as compressed archives using [Github Releases].

A *release for an individual language* is manually created once a language maintainer decides that there have been enough improvements (in the form of one or multiple commits in the repository).
The maintainer creates a tag for the most recent commit, after which a release is automatically created and bound to this tag and archived versions of the data are attached to it.

A *release for the whole UniMorph bundle* is likewise created when enough improvements across all languages make it desirable. Again, a tag is created, a release automatically bound to it, and one big archive attached to it.


Version numbering
-----------------

Both individual languages as well as complete UniMorph bundles will be assigned version numbers.

| release             | version number schema       |
|---------------------|-----------------------------|
| Individual language | `$schemaver`.`$languagever` |
| UniMorph bundle     | `$schemaver`.`$bundlever`   |

#### `$schemaver`
The number `$schemaver` is not likely to change anytime soon, i.e., this will stay `1`, until some big/breaking change to schema or data format is made. A big/breaking change is defined as one that requires all languages to be updated.
It is shared between all languages and the bundle.

#### `$languagever`
The number `$languagever` is incremented for each language individually (i.e., `$languagever` is not shared between languages or with the bundle), whenever improvements are enough to warrant a new individual release of the language.
It is independent of all `$bundlever` values.

#### `$bundlever`
Like `$languagever`, `$bundlever` is incremented for each new release.
It is independent of all `$languagever` values.

### Example

For the first release we will have `eng-1.0` and `deu-1.0` as languages. These sets are downloadable individually as well as as one bundle `unimorph-1.0`.

After the release some work is being made on German data, resulting in an individual-language release `deu-1.1`, but the improvements are not deemed interesting enough for a re-release of the UniMorph bundle.

More work is being put into the German data, it reaches `deu-1.2`, the English data is also improved to a version `eng-1.1` and we add Albanian data, whose first release will then be `sqi-1.0`.

At this point we decide that it is time for a new bundle release and release `unimorph-1.1`, containing `deu-1.2`, `eng-1.1` and `sqi-1.0`.


[GitHub organization UniMorph]: https://github.com/orgs/unimorph/
[git submodules]: https://git-scm.com/book/en/v2/Git-Tools-Submodules
[Github Releases]: https://help.github.com/articles/creating-releases/