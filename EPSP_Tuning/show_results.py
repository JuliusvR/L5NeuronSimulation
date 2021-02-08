from analyze_EPSPs import *

def plot_EPSPs(file, time = 4000):
    df = pd.read_csv(file)
    epsps = np.array(df["EPSP"])
    # plt.figure()
    # plt.hist(epsps, bins = 400)

    # plt.figure()
    # plt.hist(epsps, bins = 400)
    # plt.xscale("log")
    print("Mean: ", np.mean(epsps))
    print("Std: ", np.std(epsps))
    plt.figure()
    sb.distplot(epsps)
    plt.xscale('log')

    plt.figure()
    sb.distplot(epsps)

    plt.show()

plot_EPSPs("scaled_results/0.45_0.4_EPSPs.csv")

plot_scatter("EPSP_files/scale_0.2_EPSPs.csv", label="scaled 0.2")
plot_scatter("EPSP_files/0.2_EPSPs.csv", label="base 0.2")
plt.axhline(y = 0.2, color = 'green', linestyle = '-', label="target3")

plot_scatter("EPSP_files/scale_0.8_EPSPs.csv", label="scaled 0.8")
plot_scatter("EPSP_files/0.8_EPSPs.csv", label="base 0.8")
plt.axhline(y = 0.8, color = 'green', linestyle = '-', label="target2")

plot_scatter("EPSP_files/scale_0.4_EPSPs.csv", label="scaled 0.4")
plot_scatter("EPSP_files/0.4_EPSPs.csv", label="base 0.4")
plt.axhline(y = 0.4, color = 'green', linestyle = '-', label="target1") 
plt.xlabel("Distance from soma (um)")
plt.ylabel("Somatic EPSP magnitude")
plt.legend()
# plot_scatter("EPSP_files/0.8_EPSPs.csv")
#plot_scatter("EPSP_files/1250_0.4_EPSPs.csv")
plt.show()