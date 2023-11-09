import sys
import os
import io

if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython get_features.py data-file\n")
    sys.exit(1)
f_input = sys.argv[1]
f_output = os.path.join("data", "stage1", "train.csv")
os.makedirs(os.path.join("data", "stage1"), exist_ok=True)

def process_data(fd_in, fd_out):
    fd_in.readline()
    for line in fd_in:
        line = line.rstrip('\n').split(',')
        fixed_acidity = line[1]
        volatile_acidity = line[2]
        citric_acid = line[3]
        residual_sugar = line[4]
        chlorides = line[5]
        density = line[7]
        pH = line[8]
        alcohol = line[10]
        log_quality = line[11]
        fd_out.write("{},{},{},{},{},{},{},{},{}\n".format(fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, density, pH, alcohol, log_quality))

with io.open(f_input, encoding="utf8") as fd_in:
    with io.open(f_output, "w", encoding="utf8") as fd_out:
        process_data(fd_in, fd_out)