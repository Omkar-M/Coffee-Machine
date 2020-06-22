spin = input()
elect_charge = input()
if spin == '1/2' and elect_charge == '-1/3':
    print('Strange', 'Quark')
elif spin == '1/2' and elect_charge == '2/3':
    print('Charm', 'Quark')
elif spin == '1/2' and elect_charge == '-1':
    print('Electron', 'Lepton')
elif spin == '1/2' and elect_charge == '0':
    print('Muon', 'Lepton')
elif spin == '1' and elect_charge == '0':
    print('Photon', 'Boson')
