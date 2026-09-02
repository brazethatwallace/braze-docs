---
page_order: 5
nav_title: Termos importantes
article_title: Termos importantes sobre SMS, MMS e RCS
alias: /sms_terms_to_know/

layout: glossary_page
glossary_top_header: "Termos importantes"
glossary_top_text: "Confira os termos a seguir para saber mais sobre os ecossistemas, tecnologias e processos de SMS, MMS e RCS."
page_type: glossary
description: "Este glossário define vários termos de SMS, MMS e RCS que você deve conhecer."
channel:
  - SMS
  - MMS
  - RCS

glossaries:
  - name: SMS (Short Message Service)
    description: Um canal de envio de mensagens criado em 1980 e uma das tecnologias de mensagens de texto mais antigas. Também é um dos canais de mensagens de texto mais difundidos e utilizados. Esse canal é uma forma mais direta de alcançar seus usuários e clientes do que a maioria dos outros canais de envio de mensagens, pois utiliza o número de telefone pessoal deles. Por isso, o SMS possui mais regras e regulamentações do que outros canais de envio de mensagens.
  - name: Short Code
    description: Trata-se de uma sequência curta e fácil de memorizar, com 5 a 6 dígitos, que permite aos remetentes enviar mais mensagens a taxas mais consistentes do que números longos (uma mensagem por segundo).<br><br>É necessário ter um código curto ou um código longo.
  - name: Long Code
    description: É o número de telefone padrão de 10 dígitos (na maioria dos países) que permite aos remetentes enviar mais mensagens a uma taxa de uma mensagem por segundo.<br><br>É necessário ter um código curto ou um código longo.
  - name: Encoding
    description: A conversão de qualquer coisa em uma forma codificada. O conteúdo de SMS pode ser codificado em GSM-7 ou UCS-2.
  - name: GSM-7 Encoding (Global System for Mobile Communications)
    description: O GSM-7 é o padrão de codificação mais comum para a maioria das mensagens SMS. Ele utiliza a maior parte dos alfabetos grego e inglês, além de alguns caracteres adicionais. Você pode saber mais sobre a codificação GSM-7 e quais conjuntos de caracteres podem ser usados na <a href='https://en.wikipedia.org/wiki/GSM_03.38#GSM_7-bit_default_alphabet_and_extension_table_of_3GPP_TS_23.038_.2F_GSM_03.38' title="GSM 7-bit default alphabet and extension table">Wikipédia</a>. Idiomas como chinês, coreano ou japonês precisam ser transferidos usando a codificação de caracteres UCS-2 de 16 bits. <br> <br> Você pode estimar que o limite de caracteres por Segment para esse tipo de codificação é de 128 caracteres.
  - name: UCS-2 Encoding (Universal Coded Character Set)
    description: A codificação UCS-2 é um padrão de codificação de fallback, especialmente quando uma mensagem não pode ser codificada usando GSM-7 ou quando um idioma precisa de mais de 128 caracteres para ser renderizado. O UCS-2 é melhor medido por <a href='https://en.wikipedia.org/wiki/Code_point'>code points</a>, em vez de "caracteres". De qualquer forma, você pode estimar que o limite de caracteres por Segment para esse tipo de codificação é de 67 caracteres.
  - name: Subscription Groups for SMS
    description: Os grupos de inscrições são uma ferramenta da Braze que permite segmentar níveis específicos de inscrição de usuários ou clientes. Os grupos de inscrições para SMS são construídos internamente com base no seu serviço de mensagens e não podem ser compartilhados entre espaços de trabalho.
  - name: Message Segments
    description: Um Segment de mensagem é um agrupamento de até um número definido de caracteres (160 para codificação GSM-7; 67 para codificação UCS-2) que será enviado em um único despacho de SMS. Se você enviar um SMS com 161 caracteres usando codificação GSM-7, verá que dois (2) segmentos de mensagem foram enviados. O envio de múltiplos segmentos de mensagem pode resultar em cobranças adicionais.
  - name: Message Service
    description: Uma coleção de códigos longos, códigos curtos e IDs alfanuméricos usados para enviar sua mensagem SMS com a Braze.
  - name: Keyword
    description: "Uma palavra curta que é enviada para um código curto ou longo para interagir com um programa de SMS predefinido ou para solicitar o descadastramento de um programa específico ou de todos os programas em um código. Por exemplo, <code>STOP</code>. As palavras-chave devem <br> - ser alfanuméricas <br> - não ter espaços <br> - ter menos de 10 caracteres. <br> <br> Uma combinação específica de palavra-chave e código curto só pode ser usada em um programa ativo por vez. Se uma palavra-chave já em uso por outro programa for inserida, um erro de validação será exibido. <br> <br> Existem duas categorias obrigatórias de palavras-chave com as quais todos os provedores de conteúdo SMS devem estar em conformidade: <code>STOP</code> e <code>HELP</code>."
  - name: Mandatory Keyword HELP
    description: Para cada programa criado na plataforma SMS Campaign Manager, o conteúdo para essa palavra-chave deve ser fornecido e precisa atender às melhores práticas e à conformidade com as operadoras por país ou região em que o tráfego de SMS está sendo enviado e recebido. Na maioria dos casos, esse conteúdo deve conter uma breve explicação do programa de SMS e como fazer o descadastramento.
  - name: Global STOP Keywords
    description: As variações incluem <code>STOP</code>, <code>END</code>, <code>QUIT</code>, <code>UNSUBSCRIBE</code>, <code>CANCEL</code>, <code>STOPALL</code>. Essas são chamadas de <code>Global-Stop-Keywords</code>. Se qualquer uma dessas palavras-chave for enviada por mensagem de texto para um código curto ou longo, o número de celular (o número do telefone celular de origem) será descadastrado de todos os programas de SMS ativos naquele código ao qual está associado.
  - name: Vanity Code
    description: Um código curto personalizado é um número de telefone de 5 a 6 dígitos especificamente selecionado por uma marca. Códigos curtos personalizados são associados à marca e mais fáceis de serem lembrados pelos consumidores.
  - name: Shared Short Code
    description: Ao usar um código curto compartilhado, todas as mensagens de texto, independentemente de qual empresa ou organização as envia, chegam ao dispositivo móvel do consumidor a partir do mesmo número de telefone de 5 a 6 dígitos. Embora os códigos curtos compartilhados tenham custo relativamente baixo e estejam disponíveis imediatamente, isso significa que sua empresa não terá um código curto dedicado e estará sujeita a outras empresas seguirem o protocolo correto com seu código curto compartilhado.
  - name: Alphanumeric Sender ID
    description: O ID de remetente alfanumérico permite que você defina o nome da sua empresa ou marca como o ID do remetente usando caracteres alfanuméricos ao enviar mensagens unidirecionais para países compatíveis.
  - name: Toll-Free Number
    description: Um número de telefone gratuito (toll-free) é um número de telefone que é cobrado por todas as chamadas recebidas, em vez de gerar cobranças para o assinante de telefone de origem. Números gratuitos nos EUA e no Canadá são habilitados para SMS, e os assinantes são cobrados por mensagens de texto enviadas e recebidas.<br><br>O envio de mensagens por número gratuito funciona melhor quando seu caso de uso é pessoa a pessoa, como suporte ao cliente ou vendas, em que tanto o remetente quanto o destinatário mantêm uma conversa por mensagem de texto.
  - name: One-Way Messaging
    description: O envio de mensagens unidirecional permite que você se comunique com seus clientes enviando mensagens de texto. O envio de mensagens unidirecional é útil se você estiver implementando um ID de remetente alfanumérico em mercados onde códigos longos e curtos não estão disponíveis.
  - name: Two-Way Messaging
    description: O envio de mensagens bidirecional permite que você mantenha uma conversa enviando e recebendo mensagens de texto.
  - name: MMS (Multimedia Message Service)
    description: O MMS é usado para enviar mensagens contendo ativos multimídia (JPEG, GIF, PNG) para telefones celulares. Assim como o SMS, o MMS é um canal de envio de mensagens de alta urgência que permite que você se comunique com os clientes imediatamente. O MMS amplia as capacidades do SMS, oferecendo a possibilidade de adicionar mídia a mensagens SMS que, de outra forma, seriam apenas texto.
  - name: RCS (Rich Communication Services)
    description: O Rich Communication Services (RCS) aprimora o SMS tradicional, permitindo que as marcas entreguem mensagens que não são apenas informativas, mas também muito mais envolventes. O RCS traz recursos como mídia de alta qualidade, botões interativos e perfis de remetente com identidade visual diretamente nos apps de mensagens pré-instalados dos usuários.
  - name: RCS-Verified Sender
    description: A entidade remetente de uma mensagem RCS, ou o que o destinatário vê em seu dispositivo para identificar de onde a mensagem está vindo. Os remetentes verificados RCS contêm o nome da empresa, legenda, identidade visual e um selo de verificação. Depois que você fornecer as informações necessárias de registro do remetente RCS à Braze, a Braze cuidará do registro e da configuração do grupo de inscrições.
  - name: SMS Fallback
    description: Se uma mensagem RCS não puder ser entregue (por exemplo, falta de suporte da operadora na região), a Braze ainda tentará entregar a mensagem por SMS quando existir um código SMS dentro do grupo de inscrições.
  - name: Basic RCS
    description: Mensagens RCS somente de texto com até 160 caracteres. Cobradas como uma única mensagem. Essa categoria é usada apenas no modelo global.
  - name: Single RCS
    description: Mensagens RCS somente de texto com mais de 160 caracteres ou que incluem elementos avançados, como botões ou mídia. Cobradas como uma única mensagem. Essa categoria é usada apenas no modelo global.
  - name: Rich RCS
    description: Mensagens RCS somente de texto, com ou sem sugestões ou botões limitados. Cobradas por Segment (160 bytes UTF-8). Essa categoria é usada apenas no modelo dos Estados Unidos.
  - name: Rich Media RCS
    description: Mensagens RCS que incluem um arquivo de mídia (imagem, vídeo) ou um Rich Card. Cobradas como uma única mensagem, independentemente do tamanho da mensagem. Essa categoria é usada apenas no modelo dos Estados Unidos.
---