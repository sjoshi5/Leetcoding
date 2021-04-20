class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        return((len(set(sentence)))==26)
            
#check if there are 26 unique characters in the sentence