import socket
#chama o sitema externo para se conctar com o cliente

#vai se conectar em algum servidor
#AF_INET ipv4
#SOCKT_STREAM conexão tcp ip
#client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#client.settimeout(0.05)

ip=input("Digite o host ou ip a ser verificado: ")
port=int(input("DIgite a porta ser verificado: "))
#definir onde vai se conectar e porta
#Recebe um codigo da conexão tcp
#code =client.connect_ex(("google.com", 80))
#code =client.connect_ex((ip, port))

ports=[]
count=0
while count <10:
    ports.append(int(input("DIgite a porta ser verificado: ")))
    count +=1


for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.05)
    code = client.connect_ex((ip, port))
    # Porta aberta 0 sucesso
    if code == 0:
        print(str(port), "  ->Porta aberta")
    else:
        print(str(port), "  ->Porta fechada")
print("Scan finalizado")


