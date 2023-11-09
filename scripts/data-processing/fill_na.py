import sys
import os
import io

if len(sys.argv) != 2:
    sys.stderr.write("Arguments error. Usage:\n")
    sys.stderr.write("\tpython get_features.py data-file\n")
    sys.exit(1)
f_input = sys.argv[1]
f_output = os.path.join("data", "stage2", "train.csv")
os.makedirs(os.path.join("data", "stage2"), exist_ok=True)

def process_data(fd_in, fd_out):
    arr_fixed_acidity = []
    arr_volatile_acidity = []
    arr_citric_acid = []
    arr_residual_sugar = []
    arr_chlorides = []
    arr_density = []
    arr_pH = []
    arr_alcohol = []
    arr_log_quality = []
    for line in fd_in:
        line = line.rstrip('\n').split(',')
        arr_fixed_acidity.append(line[1])
        arr_volatile_acidity.append(line[2])
        arr_citric_acid.append(line[3])
        if line[4]:
            arr_residual_sugar.append(float(line[4]))
        else:
            arr_residual_sugar.append(0)
        arr_chlorides.append(line[5])
        arr_density.append(line[7])
        if line[8]:
            arr_pH.append(float(line[8]))
        else:
            arr_pH.append(0)
        arr_alcohol.append(line[10])
        arr_log_quality.append(line[11])

    s_suga = sum(arr_residual_sugar)
    s_pH = sum(arr_pH)
    
    for i in range(len(arr_pH)):
        if arr_pH[i] == 0:
            arr_pH[i] = round(s_pH / len(arr_pH), 2)
    
    for i in range(len(s_suga)):
        if arr_residual_sugar[i]:
            arr_residual_sugar[i] = round(s_suga / len(arr_residual_sugar), 2)
    
    for p_fixed_acidity, p_volatile_acidity, p_citric_acid, p_residual_sugar, p_chlorides, p_density, p_pH, p_alcohol, p_log_quality in zip(arr_fixed_acidity, arr_volatile_acidity, arr_citric_acid, arr_residual_sugar, arr_chlorides, arr_density, arr_pH, arr_alcohol, arr_log_quality):
        fd_out.write("{},{},{},{},{},{},{},{},{}\n".format(p_fixed_acidity, p_volatile_acidity, p_citric_acid, p_residual_sugar, p_chlorides, p_density, p_pH, p_alcohol, p_log_quality))

with io.open(f_input, encoding="utf8") as fd_in:
    with io.open(f_output, "w", encoding="utf8") as fd_out:
        process_data(fd_in, fd_out)