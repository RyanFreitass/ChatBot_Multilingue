import re

class Validacao:
    def validar_data(data):
        padrao = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'

        if re.match(padrao, data):
            dia, mes, ano = map(int, data.split('/'))

            if mes in [4, 6, 9, 11] and dia > 30:
                return "Data inválida. Este mês tem apenas 30 dias"

            if mes > 12 or mes < 1:
                return "Data inválida. Este mês não existe"


            return "Data Válida"
        
        else:
            return "Data Inválida"
        

    
    def validacao_rg(rg):
        rg_limpo = re.sub(r'[^0-9Xx]', '', rg)

        padrao = r'^\d{2}\.\d{3}\.\d{3}-[\dXx]$'  

        if re.match(padrao, rg):
            return 'Formato válido'
        else:
            if 8 <= len(rg_limpo) <= 9:
                return "Formato não padrão, mas quantidade de dígitos válida"
            else:
                return "Formato inválido"
            
    
    def validar_email(email):
        padrao = r'^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(padrao, email))
    

    def validar_cpf(cpf):
        #remove caracteres ñ numericos
        cpf = re.sub(r'[^0-9]', '', cpf)

        #verifica se tem 11 digitos
        if len(cpf) != 11:
            return False
        
        #verificar se n sao todos digitos iguais
        if cpf == cpf[0] * 11:
            return False
        
        #formato para exibição: 123.456.789-00
        padrao_formatado = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'

        return True

