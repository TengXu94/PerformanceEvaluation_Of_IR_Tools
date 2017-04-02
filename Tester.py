import AverageRPrecision
import ScorerFileManager

sfm = ScorerFileManager.ScorerFileManager()
scorer_to_test = sfm.get_out_cran_def_countscorer()
avg_maker = AverageRPrecision.AverageRPrecision()

#avg_maker_nmdcg = AverageNMDCG.AverageNMDCGPrecision()

print(avg_maker.compute_average_r_precision(scorer_to_test))

#nMDCG
#print(avg_maker_nmdcg.averagenMDCG(avg_maker_nmdcg.nMDCG_evaluation(scorer_to_test)))

