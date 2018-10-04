import subprocess

def fetch_utilization():
    output = subprocess.Popen( ['nvidia-smi','-q','--display=UTILIZATION'], stdout=subprocess.PIPE ).communicate()[0]
    utilization = output[output.find('Gpu')+30:output.find('Gpu')+32]
    return utilization

def fetch_temperature():
    output = subprocess.Popen( ['nvidia-smi','-q','--display=TEMPERATURE'], stdout=subprocess.PIPE ).communicate()[0]
    temperature = output[output.find('GPU Current Temp')+30:output.find('GPU Current Temp')+32]
    return temperature
