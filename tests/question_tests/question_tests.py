import unittest
from src.question_c.ancestor_consensus import get_most_likely_ancestor_consensus

class TestAncestorConsensus(unittest.TestCase):

    def test_multiple_occurrences(self):
        dna_string1 = "GATATATGCATATACTT"
        dna_string2 = "ATAT"
        result = get_most_likely_ancestor_consensus(dna_string1, dna_string2)
        self.assertEqual(result, (2, 4, 10)) 

    def test_no_occurrence(self):
       
        dna_string1 = "GATATATGCATATACTT"
        dna_string2 = "XYZ"
        result = get_most_likely_ancestor_consensus(dna_string1, dna_string2)
        self.assertEqual(result, ()) 

    def test_single_occurrence(self):
        
        dna_string1 = "GATATCGAT" 
        dna_string2 = "ATAT"
        result = get_most_likely_ancestor_consensus(dna_string1, dna_string2)
        self.assertEqual(result, (2,))  

    def test_empty_occurrence(self):
       
        dna_string1 = "GATACGTG"
        dna_string2 = "XYZ"
        result = get_most_likely_ancestor_consensus(dna_string1, dna_string2)
        self.assertEqual(result, ())  

    def test_edge_case_substring_longer_than_string(self):
        
        dna_string1 = "GAT"
        dna_string2 = "GATAT"
        result = get_most_likely_ancestor_consensus(dna_string1, dna_string2)
        self.assertEqual(result, ())  

if __name__ == "__main__":
    unittest.main()



   


