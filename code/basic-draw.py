import matplotlib.pyplot as pl
import numpy as np
import matplotlib.ticker as mtick
from matplotlib.ticker import FuncFormatter


alphas = np.arange(0,1.1,0.1)


cf_auc = 0.90912627741119933
cf_rmse = 0.2678988784020445


ctr_auc = 0.70826845653721149
ctr_rmse = 0.44613114838656404





aucs = [[0.5, 0.68875105231376665, 0.69167789591111761, 0.69261401492384411, 0.75166090160636334, 0.69331973212907494, 0.70057401223676219, 0.75249061738545986, 0.72182750030680676, 0.75394764534131697, 0.75145124097729221], [0.70826845653721149, 0.71053716053207161, 0.71334938883806032, 0.6940385589143101, 0.69089301219366472, 0.68749433534599147, 0.69209666038968409, 0.71145789474679288, 0.71328298451733152, 0.70137869863728675, 0.5], [0.5, 0.57686051062645816, 0.64929253182838909, 0.66894298180049971, 0.73425979040977896, 0.67898452058019276, 0.68785233286934899, 0.74265806877710971, 0.73107093839236192, 0.75092204103476567, 0.75142677169681438], [0.71833159872555541, 0.72226492550271715, 0.72239151490818698, 0.7195513719961466, 0.72107896454635212, 0.72177034992248545, 0.72234562202898611, 0.70949230909162242, 0.70136695778971836, 0.69936203339384861, 0.5]]
rmses = [[0.5, 0.4960297768786537, 0.48958538166420046, 0.48167159490012623, 0.4788024904519481, 0.47499894128559284, 0.4734016057733254, 0.47107391990800557, 0.4718742853174972, 0.47073196730930844, 0.47063653774458764], [0.44613114838656404, 0.41134427184018413, 0.38417144704709577, 0.5629974819972645, 0.4920500270788526, 0.450044403560727, 0.4385618119679866, 0.42997819252918523, 0.39594045754513174, 0.36560628187850336, 0.5], [0.5, 0.49602984563412583, 0.4895872644423111, 0.4816755906046606, 0.4788041406939825, 0.4750138544966989, 0.4734234646206976, 0.471096471922998, 0.471900327716593, 0.4707494595744563, 0.4706288392279884], [0.36869288943501993, 0.3699690364091164, 0.36958596891892653, 0.3695356437411906, 0.3667842216676706, 0.3653158431705889, 0.3598560080668008, 0.3599999492277996, 0.36101123888115955, 0.3630293393451554, 0.5]]






pl.figure(figsize=(14,4))


pl.subplot(1,4,1)
pl.plot(alphas,map(lambda x: ctr_auc,alphas))
pl.plot(alphas,aucs[1], 'sb-')
pl.plot(alphas,aucs[3], '+r-')
# pl.ylim(0.5, 0.8)
pl.xlabel(r'$\alpha$')
pl.ylabel('AUC')
min_list = [min(aucs[1]),min(aucs[3]),ctr_auc]
max_list = [max(aucs[1]),max(aucs[3]),ctr_auc]
mi = min(min_list) - 0.05
ma = max(max_list)+0.05
pl.ylim([mi,ma])
pl.title('CTR AUC Performance')
pl.grid(True)
pl.legend(['Base','Disjoint','Joint'],loc='lower left')


print 'Joint Vs Disjoint'
diff_cf_auc = map(lambda x: round(x,4)*100, (np.array(aucs[2])-np.array(aucs[0]))/np.array(aucs[0]))
print diff_cf_auc
diff_ctr_auc = map(lambda x: round(x,4)*100, (np.array(aucs[3])-np.array(aucs[1]))/np.array(aucs[1]))
print diff_ctr_auc
diff_cf_rmse = map(lambda x: round(x,4)*100, (np.array(rmses[2])-np.array(rmses[0]))/np.array(rmses[0]))
print diff_cf_rmse
diff_ctr_rmse = map(lambda x: round(x,4)*100, (np.array(rmses[3])-np.array(rmses[1]))/np.array(rmses[1]))
print diff_ctr_rmse

print 'Joint Vs Base'
diff_cf_auc_base = map(lambda x: round(x-cf_auc,4)*100, aucs[2])
print diff_cf_auc_base
diff_ctr_auc_base = map(lambda x: round(x-ctr_auc,4)*100, aucs[3])
print diff_ctr_auc_base
diff_cf_rmse_base = map(lambda x: round(x-cf_rmse,4)*100, rmses[2])
print diff_cf_rmse_base
diff_ctr_rmse_base = map(lambda x: round(x-ctr_rmse,4)*100, rmses[3])
print diff_ctr_rmse_base

single = diff_ctr_auc.index(max(diff_ctr_auc))
base = diff_ctr_auc_base.index(max(diff_ctr_auc_base))
single_line = str(single/10.) + ' & ' + str(max(diff_ctr_auc)) + ' & ' + str(round(aucs[1][single]*100,2))
base_line = str(base/10.) + ' & ' + str(max(diff_ctr_auc_base)) + ' & ' + str(round(ctr_auc*100,2))
print single_line + ' & ' + base_line


pl.subplot(1,4,2)
pl.bar(alphas-0.03,diff_ctr_auc, 0.03)
pl.bar(alphas,diff_ctr_auc_base, 0.03, color='r')

ax = pl.gca()
fmt = '%.0f%%' # Format you want the ticks, e.g. '40%'
xticks = mtick.FormatStrFormatter(fmt)
ax.yaxis.set_major_formatter(xticks)

pl.xlim(-0.1,1.1)
pl.ylim(-8, 8)
pl.xlabel(r'$\alpha$')
pl.ylabel('AUC Improvement')
pl.title('CTR AUC Improvement')
pl.grid(True)
pl.legend(['Joint vs Disjoint','Joint vs Base'],loc='lower left')



pl.subplot(1,4,3)
pl.plot(alphas,map(lambda x: ctr_rmse,alphas))
pl.plot(alphas,rmses[1], 'sb-')
pl.plot(alphas,rmses[3], '+r-')
#pl.ylim(0.5, 0.8)
pl.xlabel(r'$\alpha$')
pl.ylabel('RMSE')
min_list = [min(rmses[1]),min(rmses[3]),ctr_rmse]
max_list = [max(rmses[1]),max(rmses[3]),ctr_rmse]
mi = min(min_list) - 0.05
ma = max(max_list) + 0.05
pl.ylim([mi,ma])
pl.title('CTR RMSE Performance')
pl.grid(True)
pl.legend(['Base','Disjoint','Joint'],loc='upper right')


pl.subplot(1,4,4)
pl.bar(alphas-0.03,diff_ctr_rmse, 0.03)
pl.bar(alphas,diff_ctr_rmse_base, 0.03, color='r')

ax = pl.gca()
fmt = '%.0f%%' # Format you want the ticks, e.g. '40%'
xticks = mtick.FormatStrFormatter(fmt)
ax.yaxis.set_major_formatter(xticks)

pl.xlabel(r'$\alpha$')
pl.xlim(-0.1,1.1)
pl.ylim(-50,10)
pl.ylabel('RMSE Drop')
pl.grid(True)
pl.title('CTR RMSE Drop')
pl.legend(['Joint vs Disjoint','Joint vs Base'],loc='lower left')



pl.tight_layout()
#pl.show()

pl.savefig('basic-perf4.pdf', dpi=300)
pl.close()



