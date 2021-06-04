import argparse
from os import mkdir
import pathlib
import apInactivation
import apInspect
import numpy as np


def plotInspection(abfPath: pathlib.Path, outputFolder: pathlib.Path, dvdtThreshold: float, maxTime=4, padSteps=70):
    curve = apInactivation.getInactivationTimes(str(abfPath),
                                                apThreshold=dvdtThreshold)
    curve = apInactivation.removeTrailingZeros(curve)
    curve = apInactivation.padWith(curve, maxTime, padSteps)
    curve = apInactivation.removeEarlyInactivation(curve)
    saveBase = outputFolder.joinpath(f"{abfPath.name}" +
                                     "-inactivation")
    apInspect.highlightInactivation3(str(abfPath), curve,
                                     saveAs=f"{saveBase}-inspect.png")
    np.savetxt(f"{saveBase}-timeBySweep.csv", curve, fmt="%5f")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Spike inactivation analysis')

    parser.add_argument('--abf', help='Path to the ABF file',
                        metavar='FilePath', type=str, required=True)

    parser.add_argument('--output', help='Folder to save analysis files in',
                        metavar='FolderPath', type=str, required=True)

    parser.add_argument('--dvdt', help='Threshold to use for AP detection (mV/ms)',
                        metavar='Number', type=float, required=True)

    args = parser.parse_args()

    abfPath = pathlib.Path(args.abf)
    if abfPath.exists() == False or abfPath.is_file() == False:
        raise Exception(f"file does not exist: {abfPath}")

    if not pathlib.Path(args.output).parent.exists():
        raise Exception(
            f"parent folder does not exist: {pathlib.Path(args.output).parent}")
    outputFolder = pathlib.Path(args.output)
    if not outputFolder.exists():
        outputFolder.mkdir()

    plotInspection(abfPath, outputFolder, dvdtThreshold=args.dvdt)

    print("DONE")
