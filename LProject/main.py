# flask, pandas, scikit-learn, pickle-mixin

from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle


app=Flask(__name__)

model = pickle.load(open("Laptop.pkl", 'rb'))
lp = pd.read_csv("CLaptop.csv")

@app.route('/')
def index():
    company = sorted(lp['Company'].unique())
    typeName = sorted(lp['TypeName'].unique())
    inches =  sorted(lp['Inches'].unique())
    cpus = sorted(lp['CpuS'].unique())
    ram = sorted(lp['Ram'].unique())
    memory_type = sorted(lp['Memorytype'].unique())
    memory = sorted(lp['Memory'].unique())
    gpu = sorted(lp['Gpu'].unique())
    weight = sorted(lp['Weight'].unique())
    cpu = sorted(lp['Cpu'].unique())
    company.insert(0,"Select Brand")
    typeName.insert(0, "Select Laptop Type ")
    inches.insert(0, "Select The Inches of You Laptop Screen")
    cpus.insert(0, "Select The Speed Of CPU")
    ram.insert(0, "Select RAM")
    memory_type.insert(0, "Select Type Of The Memory")
    memory.insert(0, "Select Memory")
    gpu.insert(0, "Select GPU")
    weight.insert(0, "Select Weight Of The Laptop")
    cpu.insert(0, "Select CPU")
    return render_template('index.html', company=company, typeName= typeName, inches= inches, cpus=cpus, ram=ram, memory_type=memory_type, memory=memory, gpu=gpu, weight=weight, cpu=cpu)


@app.route('/predict', methods=['POST'])
def predict():
    company = (request.form.get('company'))
    if (company == 'Acer'):
        company= '0'
    elif (company == 'Apple'):
        company= '1'
    elif (company == 'Asus'):
        company= '2'
    elif (company == 'Chuwi'):
        company= '3'
    elif (company == 'Dell'):
        company= '4'
    elif (company == 'Fujitsu'):
        company= '5'
    elif (company == 'Google'):
        company= '6'
    elif (company == 'HP'):
        company= '7'
    elif (company == 'Huawei'):
        company= '8'
    elif (company == 'LG'):
        company= '9'
    elif (company == 'Lenovo'):
        company= '10'
    elif (company == 'MSI'):
        company= '11'
    elif (company == 'Mediacom'):
        company= '12'
    elif (company == 'Microsoft'):
        company= '13'
    elif (company == 'Razer'):
        company= '14'
    elif (company == 'Samsung'):
        company= '15'
    elif (company == 'Toshiba'):
        company= '16'
    elif (company == 'Vero'):
        company= '17'
    else:
        company= '18'
    typeName = request.form.get('typeName')
    if (typeName == '2 in 1 Convertible'):
        typeName= '0'
    elif (typeName == 'Gaming'):
        typeName= '1'
    elif (typeName == 'Netbook'):
        typeName= '2'
    elif (typeName == 'Notebook'):
        typeName= '3'
    elif (typeName == 'Ultrabook'):
        typeName= '4'
    else:
        typeName= '5'
    inches = request.form.get('inches')
    cpus = request.form.get('cpus')
    ram = request.form.get('ram')
    memory_type = request.form.get('memory_type')
    if (memory_type == 'Flash Storage'):
        memory_type= '0'
    elif (memory_type == 'HDD'):
        memory_type= '1'
    elif (memory_type == 'Hybrid'):
        memory_type= '2'
    else:
        memory_type= '3'
    memory = request.form.get('memory')
    gpu = request.form.get('gpu')
    if (gpu == 'AMD FirePro W4190M'):
        gpu= '0'
    elif (gpu == 'AMD FirePro W5130M'):
        gpu= '1'
    elif (gpu == 'AMD R17M-M1-70'):
        gpu= '2'
    elif (gpu == 'AMD R4 Graphics'):
        gpu= '3'
    elif (gpu == 'AMD Radeon 520'):
        gpu= '4'
    elif (gpu == 'AMD Radeon 530'):
        gpu= '5'
    elif (gpu == 'AMD Radeon 540'):
        gpu= '6'
    elif (gpu == 'AMD Radeon Pro 455'):
        gpu= '7'
    elif (gpu == 'AMD Radeon Pro 555'):
        gpu= '8'
    elif (gpu == 'AMD Radeon Pro 560'):
        gpu= '9'
    elif (gpu == 'AMD Radeon R2'):
        gpu= '10'
    elif (gpu == 'AMD Radeon R3'):
        gpu= '11'
    elif (gpu == 'AMD Radeon R4'):
        gpu= '12'
    elif (gpu == 'AMD Radeon R5'):
        gpu= '13'
    elif (gpu == 'AMD Radeon R5 430'):
        gpu= '14'
    elif (gpu == 'AMD Radeon R5 520'):
        gpu= '15'
    elif (gpu == 'AMD Radeon R5 M315'):
        gpu= '16'
    elif (gpu == 'AMD Radeon R5 M330'):
        gpu= '17'
    elif (gpu == 'AMD Radeon R5 M420'):
        gpu= '18'
    elif (gpu == 'AMD Radeon R5 M420X'):
        gpu= '19'
    elif (gpu == 'AMD Radeon R5 M430'):
        gpu= '20'
    elif (gpu == 'AMD Radeon R7'):
        gpu= '21'
    elif (gpu == 'AMD Radeon R7 M360'):
        gpu= '22'
    elif (gpu == 'AMD Radeon R7 M365X'):
        gpu= '23'
    elif (gpu == 'AMD Radeon R7 M440'):
        gpu= '24'
    elif (gpu == 'AMD Radeon R7 M445'):
        gpu= '25'
    elif (gpu == 'AMD Radeon R7 M460'):
        gpu= '26'
    elif (gpu == 'AMD Radeon R7 M465'):
        gpu= '27'
    elif (gpu == 'AMD Radeon R9 M385'):
        gpu= '28'
    elif (gpu == 'AMD Radeon RX 540'):
        gpu= '29'
    elif (gpu == 'AMD Radeon RX 550'):
        gpu = '30'
    elif (gpu == 'AMD Radeon RX 560'):
        gpu = '31'
    elif (gpu == 'AMD Radeon RX 580'):
        gpu = '32'
    elif (gpu == 'Intel Graphics 620'):
        gpu = '33'
    elif (gpu == 'Intel HD Graphics'):
        gpu = '34'
    elif (gpu == 'Intel HD Graphics 400'):
        gpu = '35'
    elif (gpu == 'Intel HD Graphics 405'):
        gpu = '36'
    elif (gpu == 'Intel HD Graphics 500'):
        gpu = '37'
    elif (gpu == 'Intel HD Graphics 505'):
        gpu = '38'
    elif (gpu == 'Intel HD Graphics 510'):
        gpu = '39'
    elif (gpu == 'Intel HD Graphics 515'):
        gpu = '40'
    elif (gpu == 'Intel HD Graphics 520'):
        gpu = '41'
    elif (gpu == 'Intel HD Graphics 530'):
        gpu = '42'
    elif (gpu == 'Intel HD Graphics 5300'):
        gpu = '43'
    elif (gpu == 'Intel HD Graphics 540'):
        gpu = '44'
    elif (gpu == 'Intel HD Graphics 6000'):
        gpu = '45'
    elif (gpu == 'Intel HD Graphics 615'):
        gpu = '46'
    elif (gpu == 'Intel HD Graphics 620'):
        gpu = '47'
    elif (gpu == 'Intel HD Graphics 630'):
        gpu = '48'
    elif (gpu == 'Intel Iris Graphics 540'):
        gpu = '49'
    elif (gpu == 'Intel Iris Graphics 550'):
        gpu = '50'
    elif (gpu == 'Intel Iris Plus Graphics 640'):
        gpu = '51'
    elif (gpu == 'Intel Iris Plus Graphics 650'):
        gpu = '52'
    elif (gpu == 'Intel Iris Pro Graphics'):
        gpu = '53'
    elif (gpu == 'Intel UHD Graphics 620'):
        gpu = '54'
    elif (gpu == 'Nvidia GTX 980 SLI'):
        gpu = '55'
    elif (gpu == 'Nvidia GeForce 150MX'):
        gpu = '56'
    elif (gpu == 'Nvidia GeForce 920'):
        gpu = '57'
    elif (gpu == 'Nvidia GeForce 920M'):
        gpu = '58'
    elif (gpu == 'Nvidia GeForce 920MX'):
        gpu = '59'
    elif (gpu == 'Nvidia GeForce 930M'):
        gpu = '60'
    elif (gpu == 'Nvidia GeForce 930MX'):
        gpu = '61'
    elif (gpu == 'Nvidia GeForce 940M'):
        gpu = '62'
    elif (gpu == 'Nvidia GeForce 940MX'):
        gpu = '63'
    elif (gpu == 'Nvidia GeForce GT 940MX'):
        gpu = '64'
    elif (gpu == 'Nvidia GeForce GTX 1050'):
        gpu = '65'
    elif (gpu == 'Nvidia GeForce GTX 1050M'):
        gpu = '66'
    elif (gpu == 'Nvidia GeForce GTX 1050Ti'):
        gpu = '67'
    elif (gpu == 'Nvidia GeForce GTX 1060'):
        gpu = '68'
    elif (gpu == 'Nvidia GeForce GTX 1070'):
        gpu = '69'
    elif (gpu == 'Nvidia GeForce GTX 1080'):
        gpu = '70'
    elif (gpu == 'Nvidia GeForce GTX 930MX'):
        gpu = '71'
    elif (gpu == 'Nvidia GeForce GTX 940M'):
        gpu = '72'
    elif (gpu == 'Nvidia GeForce GTX 940MX'):
        gpu = '73'
    elif (gpu == 'Nvidia GeForce 950M'):
        gpu = '74'
    elif (gpu == 'Nvidia GeForce GTX 960'):
        gpu = '75'
    elif (gpu == 'Nvidia GeForce GTX 960<U+039C>'):
        gpu = '76'
    elif (gpu == 'Nvidia GeForce GTX 960M'):
        gpu = '77'
    elif (gpu == 'Nvidia GeForce GTX 965M'):
        gpu = '78'
    elif (gpu == 'Nvidia GeForce GTX 970M'):
        gpu = '79'
    elif (gpu == 'Nvidia GeForce GTX 980M'):
        gpu = '80'
    elif (gpu == 'Nvidia GeForce GTX1050 Ti'):
        gpu = '81'
    elif (gpu == 'Nvidia GeForce GTX1060'):
        gpu = '82'
    elif (gpu == 'Nvidia GeForce GTX1080'):
        gpu = '83'
    elif (gpu == 'Nvidia GeForce MX130'):
        gpu = '84'
    elif (gpu == 'Nvidia GeForce MX150'):
        gpu = '85'
    elif (gpu == 'Nvidia Quadro 3000M'):
        gpu = '86'
    elif (gpu == 'Nvidia Quadro M1000M'):
        gpu = '87'
    elif (gpu == 'Nvidia Quadro M1200'):
        gpu = '88'
    elif (gpu == 'Nvidia Quadro M2000M'):
        gpu = '89'
    elif (gpu == 'Nvidia Quadro M2200'):
        gpu = '90'
    elif (gpu == 'Nvidia Quadro M2200M'):
        gpu = '91'
    elif (gpu == 'Nvidia Quadro M500M'):
        gpu = '92'
    elif (gpu == 'Nvidia Quadro M520M'):
        gpu = '93'
    elif (gpu == 'Nvidia Quadro M620'):
        gpu = '94'
    else:
        gpu= '95'
    weight = request.form.get('weight')
    cpu = request.form.get('cpu')
    if (cpu == '5'):
        cpu = '1'
    elif (cpu == '6110'):
        cpu = '2'
    elif (cpu == '8800P'):
        cpu = '3'
    elif (cpu == '9000'):
        cpu = '4'
    elif (cpu == '9000e'):
        cpu = '5'
    elif (cpu == '9220'):
        cpu = '6'
    elif (cpu == '9410'):
        cpu = '7'
    elif (cpu == '9420'):
        cpu = '8'
    elif (cpu == '9600P'):
        cpu = '9'
    elif (cpu == '9620P'):
        cpu = '10'
    elif (cpu == '9830P'):
        cpu = '11'
    elif (cpu == '9i700P'):
        cpu = '12'
    elif (cpu == '9i720P'):
        cpu = '13'
    elif (cpu == 'A10-9620P'):
        cpu = '14'
    elif (cpu == 'A6-9220'):
        cpu = '15'
    elif (cpu == 'A9-9420'):
        cpu = '16'
    elif (cpu == 'Dual Core'):
        cpu = '17'
    elif (cpu == 'E2-6110'):
        cpu = '18'
    elif (cpu == 'E2-9000'):
        cpu = '19'
    elif (cpu == 'E2-9000e'):
        cpu = '20'
    elif (cpu == 'E3-1505M'):
        cpu = '21'
    elif (cpu == 'E3-1535M'):
        cpu = '22'
    elif (cpu == 'M'):
        cpu = '23'
    elif (cpu == 'Quad Core'):
        cpu = '24'
    elif (cpu == 'X5-Z8350'):
        cpu = '25'
    elif (cpu == 'Z8350'):
        cpu = '26'
    elif (cpu == 'i3'):
        cpu = '27'
    elif (cpu == 'i5'):
        cpu = '28'
    elif (cpu == 'i7'):
        cpu = '29'
    elif (cpu == 'i7110'):
        cpu = '30'
    elif (cpu == 'i7210'):
        cpu = '31'
    elif (cpu == 'i7310'):
        cpu = '32'
    elif (cpu == 'i7410'):
        cpu = '33'
    elif (cpu == 'x5-Z8300'):
        cpu = '34'
    elif (cpu == 'x5-Z8350'):
        cpu = '35'
    else:
        cpu = '36'

    prediction = model.predict(pd.DataFrame([[company,typeName,inches,cpus,ram,memory_type,memory,gpu,weight,cpu]], columns=['Company','TypeName','Inches','CpuS','Ram','Memorytype','Memory','Gpu','Weight','Cpu']))
    return str(np.round(prediction[0],2))

if __name__ == "__main__":
    app.run(debug=True)
