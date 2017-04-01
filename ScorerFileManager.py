
class ScorerFileManager:
    def __init__(self):
        self.ground_truth_path = "/Users/White_Orchard/Desktop/HW1/Cranfield_DATASET/cran_Ground_Truth.tsv"
        #def stemmer
        self.out_cran_def_countscorer_path = "/Users/White_Orchard/Desktop/HW1/out_cran_def_countscorer.tsv"
        self.out_cran_def_BM25_path = "/Users/White_Orchard/Desktop/HW1/out_cran_def_BM25.tsv"
        self.out_cran_def_tfidf_path = "/Users/White_Orchard/Desktop/HW1/out_cran_def_tfidf.tsv"
        #eng stemmer
        self.out_cran_eng_countscorer_path = "/Users/White_Orchard/Desktop/HW1/out_cran_eng_countscorer.tsv"
        self.out_cran_eng_BM25_path = "/Users/White_Orchard/Desktop/HW1/out_cran_eng_BM25.tsv"
        self.out_cran_eng_tfidf_path = "/Users/White_Orchard/Desktop/HW1/out_cran_eng_tfidf.tsv"
        #eng_stop stemmer
        self.out_cran_eng_stop_countscorer_path = "/Users/White_Orchard/Desktop/HW1/out_cran_def_countscorer.tsv"
        self.out_cran_eng_stop_BM25_path = "/Users/White_Orchard/Desktop/HW1/out_cran_def_BM25.tsv"
        self.out_cran_eng_stop_tfidf_path = "/Users/White_Orchard/Desktop/HW1/out_cran_def_tfidf.tsv"

    def from_file_to_dictionary(self, file_path):
        file = open(file_path, "r")
        lines = file.readlines()
        dictionary = {}
        i = 1
        while i < len(lines):
            parsed_line = lines[i].split()
            query_id = parsed_line[0]
            doc_id = parsed_line[1]
            if dictionary.get(query_id) is not None:
                dictionary.get(query_id).append(doc_id)
            else:
                dictionary[query_id] = [doc_id]
            i += 1
        file.close()
        return dictionary

    def get_ground_truth(self):
        return self.from_file_to_dictionary(self.ground_truth_path)

    def get_out_cran_def_countscorer(self):
        return self.from_file_to_dictionary(self.out_cran_def_countscorer_path)





