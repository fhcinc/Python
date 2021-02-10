# Call this function after running gld_align to visualize the aligned data.
# Assumptions:
# uE Interface : Channel 1, microelectrode recording, sampled at 32 kHz.
# Lf Interface : Channel 1, EOG channel, sampled at 1 kHz.
# Sync Interface: Digin 1, TTL input, sampled at 32 kHZ.
import numpy as np
import matplotlib.pyplot as plt

def gld_view_aligned(t1, t2):
    n = len(t1.segments)
    eog_delays = np.zeros(n)  # holds mean MER-EOG misalignment per segment.
    segs = list(range(0, n))
    # segs = [9]

    for k in range(0, n):
        nseg = k
        if nseg not in segs:
            continue

        plt.figure(nseg+1)
        sf_mer = t1.segments[nseg].sampling_rate_mer[0]  # MER sampling rate recorded on the first device.
        sf_eog = t2.segments[nseg].sampling_rate_lf[0]  # EOG data sampling rate recorded on the second device.
        sf_lfp = t1.segments[nseg].sampling_rate_lf
        sf_analog = t1.segments[nseg].aux.sampling_rate;
  
         # Normalize data to more easily visualize alignment
        mer = t1.segments[nseg].channels[1].continuous  # MER data
        mean = np.mean(mer)
        maxim = max(mer)
        mer = [(x - mean) / maxim for x in mer]

        eog = t2.segments[nseg].channels[1].lf
        mean = np.mean(eog)
        maxim = max(eog)
        eog = [(x - mean) / maxim for x in eog]

        analog = t1.segments[nseg].aux.channels[0].continuous;
        analog = np.subtract(analog, np.mean(analog));
        analog = np.divide(analog,max(analog));
        tanalog = np.linspace(0, len(analog)/sf_analog, num=len(analog))

        # time base for the mer:
        tm = np.linspace(0, len(mer) / sf_mer, num=len(mer))
        teog = np.linspace(0, len(eog) / sf_eog, num=len(eog))

        nixmeraux = []
        for i in range(0, len(mer) - 1 ):
            if abs(mer[i+1] - mer[i]) > 0.25:
                nixmeraux.append(i)

        nixmer = []
        for i in range(0, len(nixmeraux) - 1 ):
            if tm[nixmeraux[i+1]] - tm[nixmeraux[i]] > 0.001:
                nixmer.append(nixmeraux[i])

        nixeogaux = []
        for i in range(0, len(eog) - 1):
            if abs(eog[i+1] - eog[i]) > 0.25:
                nixeogaux.append(i)

        nixeog = []
        for i in range(0, len(nixeogaux) - 1 ):
            if teog[nixeogaux[i+1]] - teog[nixeogaux[i]] > 0.002:
                nixeog.append(nixeogaux[i])

        if len([tm[i] for i in nixmer]) >= 10 and len([teog[i] for i in nixeog]) >= 10:
            aux = []
            for i in range(0, 10):
                #print(F'\ndiff (MER-EOG) = {tm[nixmer[i]] - teog[nixeog[i]]}')
                aux.append(tm[nixmer[i]] - teog[nixeog[i]])

            #print(F'\n(MER-EOG): nseg = {nseg}, mean = {np.mean(aux)}')
            eog_delays[nseg] = np.mean(aux)

        merPlot, = plt.plot(tm, mer, label='MER')
        eogPlot, = plt.plot(teog, eog, label='LFP')
        analogPlot = plt.plot(tanalog, analog, label='Analog')

        # plot( tlf, lfp)
        meredgePlot, = plt.plot([tm[x] for x in nixmer], [mer[x] for x in nixmer], '*', label='MER-EDGE')
        eogedgePlot, = plt.plot([teog[x] for x in nixeog], [eog[x] for x in nixeog], 'o', label='EOG-EDGE')

        plt.title('Segment ' + str(nseg))

        if t1.segments[nseg].sync:
            if any(t1.segments[nseg].sync.digin):
                diginPlot, = plt.plot(t1.segments[nseg].sync.rt_timestamps, t1.segments[nseg].sync.digin, '-*',
                                      label='DIGIN')
                plt.legend(handles=[merPlot, eogPlot, meredgePlot, eogedgePlot, diginPlot])
            else:
                plt.legend(handles=[merPlot, eogPlot, meredgePlot, eogedgePlot])
        else:
            plt.legend(handles=[merPlot, eogPlot, meredgePlot, eogedgePlot])

        plt.xlabel('Seconds')
        plt.ylabel('Normalized amplitude')
        plt.ylim((-2.5, 1.5))

    plt.figure(n)
    plt.title('EOG delays')
    plt.stem([1000*abs(x) for x in eog_delays], use_line_collection=True)
    plt.ylabel( 'ms')
    plt.xlabel('Segment')
    print(F'\nmean delay = {np.mean(eog_delays)}')

    plt.show()


