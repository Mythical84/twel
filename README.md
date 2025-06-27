<h1 align="center">The Worst Ever Language (twel)</h1>


<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
  <img alt="Maintenance" src="https://img.shields.io/badge/Maintained%3F-no-red" />
  <a href="https://github.com/Mythical84/twel/blob/main/LICENSE" target="_blank">
  <img alt="License: MIT" src="https://img.shields.io/github/license/mythical84/twel" />
  </a>
  <img alt="Documentation" src="https://img.shields.io/badge/Documentation-Mythical83.com-blue">
</p>


## Description
The Worst Ever Language (twel) is a programming language I built over the course of a couple weeks (although the stdlib was written a couple months later). This was meant to be the first time I wrote a true programming language, and not wanting to spend a lot of time on it I took many shortcuts and made many poor design decisions, leading to me eventually giving the language the name it is now stuck with.

## Installation
Download the tar.gz from the releases tab, or follow the below instructions to build from scratch.

## Building
1. Clone the git repository
```
git clone https://github.com/Mythical84/twel
cd twel
```

2. Install dependencies
```
pip install antlr4-python3-runtime
pip install pyinstaller
```

3. Build final binary
```
pyinstaller language.py
```

4. Move stdlib files to the _internal folder
```
mv *.twl dist/language/_internal
```

## Usage
To run the interpreter on a twel file, run
```
./language <filename>.twl
```

## License
Distributed under the Mozilla Public License 2.0. See LICENSE for more details.
