def consultarCPF(cpf, dataNascimento):
    if(cpf == "000.000.000-00" and dataNascimento == "00/00/0000"):
        return True
    else:
        return False