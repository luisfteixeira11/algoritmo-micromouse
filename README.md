versão do python q eu to usando: 3.13.3
    
    Passo 1 - Construir uma matriz 16x16 do labirinto

    Passo 2 - Ajustar a matriz de acordo com o começo de onde o micromouse iniciou

Loop enquanto o robô não chegar ao 0 na matriz de inundação:

    Passo 3 - Atualiza a Matriz de "Inundação"*

    Passo 4 - Robô registra as paredes do local na matriz**

    Passo 5 - Robô se move para o menor número da matriz de inundação

    Passo 6 - Lógica de escolhas do Robô

----
*: Uma matriz de inundação é como se alguém jogasse água em um lugar que ele quer chegar e a água iria "despejando" pelo labirinto, mas nesse caso a água seria a distância até o lugar que a gente quer da matriz.

![tipoessa](https://miro.medium.com/v2/resize:fit:720/format:webp/1*sH-M8zTmmnKyBewXb7GqjQ.png)

Notem que os lugares de chegada tão como 0 e a distância as seguintes dão a distância ideal dela até a celula e vai ser atualizada com base nas paredes que o micromouse vai identificando (considerando que o micromouse não sabe da maioria dessas paredes vermelhas, só a primeira)

**: As paredes da matriz seriam ilustradas em representações binárias
![eessa](https://miro.medium.com/v2/resize:fit:720/format:webp/1*dhFlf8CtoDKifTVqS3-zqg.jpeg)

    Cima - Baixo - Esquerda - Direita (tanto faz a ordem, na imagem acima tá diferente)
    0 0 0 0 - 0 - sem parede pra nenhum dos lados
    1 0 0 0 - 8 - so tem parede em cima
    0 1 1 1  - 7 -  ele so pode andar pra cima pq é o unico lugar possivel, pq tem paredes em todos os lados
