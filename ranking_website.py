import streamlit as st

st.header("Digite sua nota do PAS 2", divider="rainbow")
st.markdown("ignore o resto")
def get_medias():
    with open('pas2_resultado_limpo.txt', "r") as file:
        total_total = 0
        total_ingles = 0
        total_discursiva = 0
        total_redacao = 0
        qnt_candidatos = 0

        for x, i in enumerate(file):
            data_student = i.split(",")
            nome, nota_ingles, nota_total, nota_discursiva, nota_redacao = data_student[1], float(
                data_student[2]), float(data_student[4]), float(data_student[5]), float(data_student[6])

            qnt_candidatos += 1
            total_ingles += float(nota_ingles)
            total_total += float(nota_total)
            total_discursiva += float(nota_discursiva)
            total_redacao += float(nota_redacao)
            store_data(nota_ingles, nota_discursiva, nota_total, nota_redacao)

        media_ingles = total_ingles / qnt_candidatos
        media_total = total_total / qnt_candidatos
        media_discursiva = total_discursiva / qnt_candidatos
        media_redacao = total_redacao / qnt_candidatos
        file.close()
    return media_ingles, media_discursiva, media_total, media_redacao


def get_dict():
    dict_notas_totais = {}
    with open('pas2_resultado_limpo.txt', "r") as file:
        for x, i in enumerate(file):
            data_student = i.split(",")
            nome, nota_ingles, nota_total, nota_discursiva, nota_redacao = data_student[1], float(
                data_student[2]), float(data_student[4]), float(data_student[5]), float(data_student[6])

            # starts dict
            if nota_total in dict_notas_totais:
                dict_notas_totais[nota_total] = dict_notas_totais[nota_total] + 1
            else:
                dict_notas_totais[nota_total] = 1

        file.close()
    dict_notas_totais = dict(sorted(dict_notas_totais.items()))
    return dict_notas_totais



def rank_nota(nota_usuario):
    qnt_candidatos = 0
    nota_maior_que_usuario = 0
    nota_menor_que_usuario = 0
    nota_igual_usuario = 0
    with open('pas2_resultado_limpo.txt', "r") as file:
        for x, i in enumerate(file):
            data_student = i.split(",")
            nome, nota_ingles, nota_total, nota_discursiva, nota_redacao = data_student[1], float(
                data_student[2]), float(data_student[4]), float(data_student[5]), float(data_student[6])

            qnt_candidatos += 1
            #para nota normal (TODO: redacao)
            if nota_total > nota_usuario:
                nota_maior_que_usuario += 1
            elif nota_total < nota_usuario:
                nota_menor_que_usuario += 1
            else:
                nota_igual_usuario += 1
    file.close()
    return nota_maior_que_usuario,nota_menor_que_usuario,nota_igual_usuario,qnt_candidatos


def find_nota_by_name(nome_usuario):
    with open('.idea/text_files/pas2_resultado_limpo.txt', "r") as file:
        for x, i in enumerate(file):
            data_student = i.split(",")
            nome = data_student[1].lstrip().lower()
            if nome_usuario == nome:
                return float(data_student[4])
        raise NameError


'''
def main_m():
    lista_medias = get_medias()
    print(f"A média de inglês é {round(lista_medias[0], 2)}")
    print(f"A média da discursiva é {round(lista_medias[1], 2)}")
    print(f"A média total é {round(lista_medias[2], 2)}")
    print(f"A média da redação é {round(lista_medias[3], 2)}")

def main_h():
    final_dict = get_dict()
    histogram(final_dict)
'''

def main():

    lista_rank = rank_nota(float(st.text_input("Diga sua nota")))
    st.markdown(f"Você ficou no top {lista_rank[0]} de um total de {lista_rank[3]}! Isso é entre os top {round(lista_rank[0]/lista_rank[3] * 100, 2)}% !"
            f"E {lista_rank[2]-1} pessoas tiveram a mesma nota que você!")
    #except ValueError:
        #grade = find_nota_by_name(grade_input.lower())
        #print(grade)
        #lista_rank = rank_nota(grade)
        #print(f"Você ficou no top {lista_rank[0]} de um total de {lista_rank[3]}! Isso é entre os top {round(lista_rank[0] / lista_rank[3] * 100,2)}% !"
           # f"E {lista_rank[2]-1} pessoas tiveram a mesma nota que você!")

'''
def main():
    user_input = ""
    while user_input not in ("m", "c", "h"):
        user_input = st.text_input("Acessar: Médias gerais (M) / Comparar (C) / Histograma (H). \n").lower()
        if user_input == "m":
            main_m()
        elif user_input == "c":
            main_c()
        elif user_input == "h":
            main_h()

'''

if __name__ == '__main__':
    main()
