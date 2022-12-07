# pyqgisdams

## WIP.
Adapting the reverse site selection of the GeoDAR dataset/Perry's paper to pyQGIS and expanding (?).

This repository provides a framework for the semi-autonomous implemetation of the dedeuplication by proximity methodology proposed in:
>Perry Godse. (2022). Improving Dam Datasets To Identify Micro-hydro Suitibility: Spatial Data Driven Approach. GEOM4005: Undergraduate Directed Study In Geomatics, Carleton University, student paper.

## Citing the template

If you have used this template in your work, please cite the following publication:

> Tom Pollard et al. (2016). Template for writing a PhD thesis in Markdown. Zenodo. http://dx.doi.org/10.5281/zenodo.58490

## Quickstart
If you're a mac user and you have conda and brew installed, run the following in your terminal to install and generate the example outputs:
```bash
# get texlive
brew install --cask mactex

# update tlmgr and packages
sudo tlmgr update --self

# make python venv and install pandoc
conda create -n phd -y python=3.7 pandoc
conda activate phd

# Install required python and texlive packages
make install
```

## Why write my thesis in Markdown?

Markdown is a super-friendly plain text format that can be easily converted to a bunch of other formats like PDF, Word and LaTeX. You'll enjoy working in Markdown because:
- it is a clean, plain-text format...
- ...but you can use LaTeX when you need it (for example, in laying out mathematical formula).
- it doesn't suffer from the freezes and crashes that some of us experience when working with large, image-heavy Word documents.
- it automatically handles the table of contents, bibliography etc with Pandoc.
- comments, drafts of text, etc can be added to the document by wrapping them in &lt;!--  --&gt;
- it works well with Git, so keeping backups is straightforward. Just commit the changes and then push them to your repository.
- it is able to take advantage of autocompletion capabilities for figures and citations in several text editors (VSCode, Sublime, etc.)
- there is no lock-in. If you decide that Markdown isn't for you, then just output to Word, or whatever, and continue working in the new format.

## Are there any reasons not to use Markdown?

There are some minor annoyances:
- if you haven't worked with Markdown before then you'll find yourself referring to the style-guide fairly often at first.
- it isn't possible to add a short caption to tables ~~and figures~~ ([figures are now fixed](https://github.com/tompollard/phd_thesis_markdown/pull/47), thanks to @martisak). This means that /listoftables includes the long-caption, which probably isn't what you want. If you want to include the list of tables, then you'll need to write it manually.

## How is the template organised?

- README.md => these instructions.
- License.md => terms of reuse (MIT license).
- Makefile => contains instructions for using Pandoc to produce the final thesis.
- output/ => directory to hold the final version.
- source/ => directory to hold the thesis content. Includes the references.bib file.
- scratch/ => directory to hold tables which can be converted between different formats.
- source/figures/ => directory to hold the figures.
- style/ => directory to hold the style documents.
