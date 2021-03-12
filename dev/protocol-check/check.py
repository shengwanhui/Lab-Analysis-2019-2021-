"""
This script lists the protocol for every ABF in a list.
Its purpose is to identify ABFs in a list that may have an incorrect/unintended protocol.
"""

import pyabf


def showProtocolForAbf(abfFilePath):
    """
    Display the ABF ID and its protocol
    """
    abf = pyabf.ABF(abfFilePath, loadData=False)
    print(abf.abfID, abf.protocol)


abfListRaw = """
### TDTOMATO POSITIVE

# 0111
X:/Data/OT-Cre/calcium-mannitol/2017-08-28 Mannitol 2P/01-14-2021 MT IC/21114015.abf
X:/Data/OT-Cre/calcium-mannitol/2017-08-28 Mannitol 2P/01-14-2021 MT IC/21114033.abf
X:/Data/OT-Cre/calcium-mannitol/2017-08-28 Mannitol 2P/01-14-2021 MT IC/21117002.abf
X:/Data/OT-Cre/calcium-mannitol/2017-08-28 Mannitol 2P/01-14-2021 MT IC/21117008.abf
X:/Data/OT-Cre/calcium-mannitol/2017-08-28 Mannitol 2P/01-14-2021 MT IC/21117018.abf
X:/Data/OT-Cre/calcium-mannitol/2017-08-28 Mannitol 2P/01-14-2021 MT IC/21117024.abf
X:/Data/OT-Cre/calcium-mannitol/2017-08-28 Mannitol 2P/01-14-2021 MT IC/21117029.abf
X:/Data/OT-Cre/calcium-mannitol/2017-08-28 Mannitol 2P/01-14-2021 MT IC/21117035.abf
X:/Data/OT-Cre/calcium-mannitol/2017-08-28 Mannitol 2P/01-14-2021 MT IC/21118003.abf
X:/Data/OT-Cre/calcium-mannitol/2017-08-28 Mannitol 2P/01-14-2021 MT IC/21118009.abf
X:/Data/OT-Cre/calcium-mannitol/2017-08-28 Mannitol 2P/01-14-2021 MT IC/21118016.abf
X:/Data/OT-Cre/calcium-mannitol/2017-08-28 Mannitol 2P/01-14-2021 MT IC/21118021.abf
X:/Data/OT-Cre/calcium-mannitol/2017-08-28 Mannitol 2P/01-14-2021 MT IC/21118030.abf

# 0112
X:/Data/OT-Cre/calcium-mannitol/2017-08-28 Mannitol 2P/01-14-2021 MT IC/21114016.abf
X:/Data/OT-Cre/calcium-mannitol/2017-08-28 Mannitol 2P/01-14-2021 MT IC/21114034.abf
X:/Data/OT-Cre/calcium-mannitol/2017-08-28 Mannitol 2P/01-14-2021 MT IC/21117003.abf
X:/Data/OT-Cre/calcium-mannitol/2017-08-28 Mannitol 2P/01-14-2021 MT IC/21117009.abf
X:/Data/OT-Cre/calcium-mannitol/2017-08-28 Mannitol 2P/01-14-2021 MT IC/21117019.abf
X:/Data/OT-Cre/calcium-mannitol/2017-08-28 Mannitol 2P/01-14-2021 MT IC/21117025.abf
X:/Data/OT-Cre/calcium-mannitol/2017-08-28 Mannitol 2P/01-14-2021 MT IC/21117030.abf
X:/Data/OT-Cre/calcium-mannitol/2017-08-28 Mannitol 2P/01-14-2021 MT IC/21117036.abf
X:/Data/OT-Cre/calcium-mannitol/2017-08-28 Mannitol 2P/01-14-2021 MT IC/21118004.abf
X:/Data/OT-Cre/calcium-mannitol/2017-08-28 Mannitol 2P/01-14-2021 MT IC/21118010.abf
X:/Data/OT-Cre/calcium-mannitol/2017-08-28 Mannitol 2P/01-14-2021 MT IC/21118017.abf
X:/Data/OT-Cre/calcium-mannitol/2017-08-28 Mannitol 2P/01-14-2021 MT IC/21118022.abf
X:/Data/OT-Cre/calcium-mannitol/2017-08-28 Mannitol 2P/01-14-2021 MT IC/21118031.abf

### TDTOMATO NEGATIVE

# 0111
X:/Data/OT-Cre/calcium-mannitol/2020-09-04 MT on tdt- neurons/20904015.abf
X:/Data/OT-Cre/calcium-mannitol/2020-09-04 MT on tdt- neurons/20910003.abf
X:/Data/OT-Cre/calcium-mannitol/2020-09-04 MT on tdt- neurons/20911002.abf
X:/Data/OT-Cre/calcium-mannitol/2020-09-04 MT on tdt- neurons/20911012.abf
X:/Data/OT-Cre/OT-GCaMP-nonspecific/09-07-19 TGOT ephys/19o10003.abf
X:/Data/OT-Cre/OT-GCaMP-nonspecific/09-07-19 TGOT ephys/20224019.abf
X:/Data/OT-Cre/OT-GCaMP-nonspecific/09-07-19 TGOT ephys/20313008.abf
X:/Data/OT-Cre/OT-GCaMP-nonspecific/09-07-19 TGOT ephys/20313015.abf

# 0112
X:/Data/OT-Cre/calcium-mannitol/2020-09-04 MT on tdt- neurons/20904002.abf
X:/Data/OT-Cre/calcium-mannitol/2020-09-04 MT on tdt- neurons/20904005.abf
X:/Data/OT-Cre/calcium-mannitol/2020-09-04 MT on tdt- neurons/20904016.abf
X:/Data/OT-Cre/calcium-mannitol/2020-09-04 MT on tdt- neurons/20904021.abf
X:/Data/OT-Cre/calcium-mannitol/2020-09-04 MT on tdt- neurons/20904025.abf
X:/Data/OT-Cre/calcium-mannitol/2020-09-04 MT on tdt- neurons/20910004.abf
X:/Data/OT-Cre/calcium-mannitol/2020-09-04 MT on tdt- neurons/20910009.abf
X:/Data/OT-Cre/calcium-mannitol/2020-09-04 MT on tdt- neurons/20910013.abf
X:/Data/OT-Cre/calcium-mannitol/2020-09-04 MT on tdt- neurons/20910017.abf
X:/Data/OT-Cre/calcium-mannitol/2020-09-04 MT on tdt- neurons/20911007.abf
X:/Data/OT-Cre/calcium-mannitol/2020-09-04 MT on tdt- neurons/20911013.abf
X:/Data/OT-Cre/OT-GCaMP-nonspecific/09-07-19 TGOT ephys/20224020.abf
X:/Data/OT-Cre/OT-GCaMP-nonspecific/09-07-19 TGOT ephys/20313009.abf
X:/Data/OT-Cre/OT-GCaMP-nonspecific/09-07-19 TGOT ephys/20313016.abf
"""

if __name__ == "__main__":
    lines = abfListRaw.split("\n")
    for line in lines:
        if (line.startswith("X:")):
            showProtocolForAbf(line)
        else:
            print(line)
