---
nav_title: Mensagens da direita para a esquerda
article_title: Criar mensagens da direita para a esquerda
page_order: 1
alias: /right_to_left_messages/
page_type: reference
description: "Esta página aborda as melhores práticas para criar mensagens na Braze que são lidas da direita para a esquerda."
---

# Criar mensagens da direita para a esquerda {#create-right-to-left-messages}

> A aparência final das mensagens da direita para a esquerda depende em grande parte de como os prestadores de serviço (como Apple, Android e Google) as renderizam. Esta página aborda as melhores práticas para criar mensagens da direita para a esquerda, para que suas mensagens sejam exibidas da forma mais precisa possível.

## Aparência da mensagem {#message-appearance}

Ao criar uma mensagem da direita para a esquerda, tenha em mente o seguinte:

- **Aparência no dashboard da Braze:** Quando uma mensagem aparece no dispositivo de um usuário, sua aparência é amplamente determinada pelo sistema operacional e pelas configurações de idioma do dispositivo&#8212;o que significa que o que você vê no dashboard nem sempre é 100% preciso.
- **Aparência no dispositivo:** A Apple e o Android têm controle significativo sobre como as mensagens são renderizadas, enquanto os provedores de serviço de e-mail (ESPs) têm algum controle. A personalização de e-mail HTML na Braze pode ser mais flexível; no entanto, a mesma mensagem ainda pode ser renderizada de forma diferente em dispositivos diferentes, com base nas configurações do usuário.

Além disso, verifique a pontuação e os emojis para determinar se sua mensagem está sendo renderizada no formato padrão ou da direita para a esquerda.

| Renderização ocidental padrão | Renderização da direita para a esquerda |
|------------------|------------------------|
| Exibe o ponto de exclamação e o emoji no **final** das frases. | Exibe o ponto de exclamação e o emoji no **início** da frase. |
| ![Um exemplo de mensagem com renderização padrão.]({% image_buster /assets/img/right-to-left/standard.png %}) | ![Um exemplo de mensagem da direita para a esquerda.]({% image_buster /assets/img/right-to-left/right-to-left.png %}) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Aparência da mensagem" }

## Criando uma mensagem da direita para a esquerda {#creating-a-right-to-left-message}

Para criar sua mensagem da direita para a esquerda na Braze:

1. Redija sua mensagem padrão no editor da Braze.
2. Copie o texto da mensagem da Braze e use uma ferramenta de localização para convertê-lo em uma mensagem da direita para a esquerda.
3. Cole a mensagem convertida de volta na Braze.
4. Verifique a formatação e o alinhamento do texto. Se você estiver criando um e-mail de arrastar e soltar ou HTML, pode fazer isso dentro do criador. Caso contrário, será necessário usar um processador de texto separado.<br><br>![Menu do editor de arrastar e soltar de e-mail com botão para alternar o alinhamento do texto entre direita para esquerda e esquerda para direita.]({% image_buster /assets/img/rtl_button.png %}){: style="max-width:50%;"}

## Considerações {#considerations}

### Notificações por push longas {#long-push-notifications}

O método de copiar e colar para mensagens push pode ser difícil de usar com notificações por push mais longas, pois conteúdos mais extensos podem ser renderizados em várias linhas em um dispositivo móvel. Se você copiar o texto da mensagem de fora da Braze (como de um documento do Word) e colá-lo diretamente na Braze, o alinhamento das frases e o posicionamento das palavras podem mudar. Para evitar esse cenário, copie e cole em partes e adicione uma quebra de linha. Por exemplo, copie e cole as cinco primeiras palavras, adicione uma quebra de linha, copie as próximas cinco palavras, adicione uma quebra de linha, e assim por diante.

As funções de pré-visualização e teste são feitas para mensagens da esquerda para a direita, então mensagens da direita para a esquerda não serão renderizadas corretamente na seção **Preview & Test**, mas serão renderizadas corretamente nos dispositivos dos usuários se as configurações estiverem definidas para isso. Sugerimos enviar mensagens para você mesmo em um ambiente real para confirmar que elas são renderizadas corretamente com base nas configurações do dispositivo.

### Alinhamento do título e do corpo {#title-and-body-alignment}

Para notificações por push, o alinhamento do título geralmente segue as configurações de idioma do dispositivo, enquanto o alinhamento do corpo pode seguir o primeiro caractere direcional forte em cada linha (trate cada linha após uma quebra de linha separadamente). Isso significa que uma única notificação por push pode misturar alinhamentos entre linhas — por exemplo, uma linha de corpo da direita para a esquerda seguida por uma linha da esquerda para a direita. Quando você precisar de um layout previsível, mantenha a consistência direcional e use quebras de linha entre segmentos de idiomas mistos.

{% alert note %}
A renderização ainda depende do sistema operacional do dispositivo e do cliente de push. Envie [mensagens de teste]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/) para seus próprios dispositivos para confirmar o alinhamento antes de publicar.
{% endalert %}

### Texto bidirecional {#bi-directional-text}

Muitos usuários que escrevem em idiomas da direita para a esquerda na verdade usam texto bidirecional: uma combinação de idiomas da esquerda para a direita e da direita para a esquerda. Por exemplo, um profissional de marketing pode enviar uma mensagem em hebraico com o nome de uma empresa em inglês. A Braze não consegue lidar com a formatação de texto bidirecional. Duas formas de evitar problemas de formatação são: evitar completamente o texto bidirecional ou separar o texto da esquerda para a direita do texto da direita para a esquerda usando quebras de linha.

{% alert tip %}
A formatação adequada para texto bidirecional é especialmente importante ao criar mensagens que incluem códigos promocionais; códigos promocionais geralmente estão em formato da esquerda para a direita, pois os mesmos códigos podem ser usados em diferentes mercados. Duas formas de acomodar códigos promocionais são: usar uma imagem para o código promocional ou adicionar o código promocional no final da mensagem após uma quebra de linha.
{% endalert %}

### Caracteres especiais, números e emojis {#special-characters-numbers-and-emojis}

Caracteres especiais (como pontuação, símbolos matemáticos e moedas), números, marcadores e emojis podem "pular de lugar" ao criar mensagens da direita para a esquerda na Braze. Para contornar isso, escreva seu texto com a formatação adequada em um processador de texto externo e depois cole o texto na Braze. Também pode ajudar evitar colocar emojis no início do texto e, em vez disso, separá-los (assim como caracteres especiais e números) do texto com quebras de linha para evitar problemas de alinhamento.

### Mensagens em árabe {#arabic-messages}

Ao redigir mensagens em árabe, use tamanhos de fonte significativamente maiores para obter a mesma legibilidade que você teria com outros idiomas. Sugerimos usar um tamanho de fonte cerca de 20% maior do que o tamanho usual para idiomas que usam o alfabeto latino ou romano. Isso ocorre porque as fontes árabes são feitas em tamanho menor para acomodar o espaço vertical ocupado pelos diacríticos (acentos).