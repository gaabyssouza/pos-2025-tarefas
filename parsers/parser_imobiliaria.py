
import json

with open("parsers/imobiliaria.json", "r", encoding="utf-8") as f:
    dados = json.load(f)


imoveis = dados["imobiliaria"]["imoveis"]


print("Menu de Imoveis: ")
for i, imovel in enumerate(imoveis):
    print(f"{i} - {imovel['descricao']}")
print("5 - Sair")


while True:
    opcao = input("Digite o id do imovel que deseja ver (ou '5' para sair): ").strip()

    if opcao.lower() == '5':
        print("Encerrando o programa.")
        break

    if opcao.isdigit():
        indice = int(opcao)

        if 0 <= indice < len(imoveis):
            imovel = imoveis[indice]

            print(" Detalhes do imovel ")
            print(f"Descrição: {imovel['descricao']}")

            print("Proprietario do imovel:")
            print(f"  Nome: {imovel['proprietario']['nome']}")
            print(f"  Telefones: {', '.join(imovel['proprietario']['telefones'])}")

            if "email" in imovel["proprietario"]:
                print(f"  Email: {imovel['proprietario']['email']}")
            elif "emails" in imovel["proprietario"]:
                print(f"  Emails: {', '.join(imovel['proprietario']['emails'])}")

            print("Endereco:")
            print(f"  Rua: {imovel['endereco']['rua']}")
            print(f"  Bairro: {imovel['endereco']['bairro']}")
            print(f"  Cidade: {imovel['endereco']['cidade']}")

            if "numero" in imovel["endereco"]:
                print(f"  Numero: {imovel['endereco']['numero']}")

            print("Caracteristicas do imovel:")
            print(f"  Tamanho: {imovel['caracteristicas']['tamanho']}")
            print(f"  Quartos: {imovel['caracteristicas']['numQuartos']}")
            print(f"  Banheiros: {imovel['caracteristicas']['numBanheiros']}")

            print(f"Valor: R$ {imovel['valor']}")
        else:
            print("ID invalido. Tente novamente.")
    else:
        print("Entrada invalida. Digite um numero ou 'x' para sair.")
