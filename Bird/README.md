# Notes from Natural Language Processing with Python
by Bird, Klein and Loper: https://www.nltk.org/book/

NLTK is a beautiful library for learning NLP, but some of its functionality can be a little clunky. This directory follows the chapters of the book and the topics it covers, but different texts / libraries will be substituted to make it useful in practical applications.

I'll follow the book using one of the projects that I'm currently working on - sentiments analysis of Reddit comments. Yes, not all of the comments are irate.

Note that I have tried to use SpaCy for comparison if possible. You need to download a language model in order to use SpaCy. To install spaCy, run
```
pip install spacy
python -m spacy download en_core_web_sm
```
This installs the `small` model. Alternatively there are `md` and `lg` but these will take more time and space to download.