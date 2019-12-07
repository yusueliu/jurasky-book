from math import log


class BaseNgramModel(object):
    """
    The BaseNgramModel creates an n-gram language model.
    """
    
    def __init__(self, ngram_counter):
        """
        BaseNgramModel is initialized with an NgramCounter
        """
        self.n = ngram_counter.n
        self.ngram_counter = ngram_counter
        self.ngrams = ngram_counter.allgrams[ngram_counter.n]
        self._check_against_vocab = self.ngram_counter.check_against_vocab
        
    def score(self, word, context):
        """
        For a given string representation of a word, and a string word context,
        return the maximum likelihood score that the word will follow the
        context.
        
        fdist[context].freq(word) == fdist[(context, word)] / fdist[context]
        """
        context = self.check_context(context)
        
        return self.ngrams[context].freq(word)
    
    def check_context(self, context):
        """
        Ensures that the context is not longer than or equal to the model's
        highest n-gram order.
        
        Returns the context as a tuple.
        """
        if len(context) >= self.n:
            raise ValueError("Context too long for this n-gram")
            
        return tuple(context)
    
    def logscore(self, word, context):
        """
        For a given string representation of a word, and a word context,
        computes the log probability of the word in the context.
        """
        score = self.score(word, context)
        if score <= 0.0:
            return float("-inf")        
        return log(score, 2)

    def entropy(self, text):
        """Calculate the approximate cross-entropy of the n-gram model for a 
        given text represented as a list of comma-separated strings.
        This is the average log probability of each word in the text.
        
        Parameters
        ----------
        text : str
        """
        normed_text = (self._check_against_vocab(word) for word in text)
        entropy = 0.0
        processed_ngrams = 0
        for ngram in self.ngram_counter.to_ngrams(normed_text):
            context, word = tuple(ngram[:-1]), ngram[-1]
            entropy += self.logscore(word, context)
            processed_ngrams += 1
        return -(entropy / processed_ngrams)

    def perplexity(self, text):
        """Given list of comma-separated strings, claculates the perplexity
        of the text.
        """
        return pow(2.0, self.entropy(text))
