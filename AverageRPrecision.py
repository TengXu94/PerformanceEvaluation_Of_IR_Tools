import ScorerFileManager


class AverageRPrecision:
    def __init__(self):
        self.sfm = ScorerFileManager.ScorerFileManager()
        self.ground_truth = self.sfm.get_ground_truth()

    def compute_r_precision(self, result_all_queries):
        relevant_counter = {}
        n = 0
        for query_id, relevant_docs in self.ground_truth.items():
            relevant_docs = self.ground_truth.get(query_id)
            relevant_cardinality = len(relevant_docs)
            relevant_counter[query_id] = 0
            n += 1
            b = 0
            for doc_id in result_all_queries.get(query_id):
                b += 1
                if b == relevant_cardinality:
                    break
                if doc_id in relevant_docs:
                    relevant_counter[query_id] += 1
        relevant_counter[query_id] = relevant_counter[query_id]/n
        return relevant_counter

    def compute_average_r_precision(self, result_all_queries):
        relevant_counter = self.compute_r_precision(result_all_queries)
        my_sum = 0
        count = 0
        for value in relevant_counter.values():
            my_sum += value
            count += 1
        return my_sum/count















