---
nav_title: Descontinuação do TLS 1.0 e 1.1
page_order: 2

page_type: update
description: "Este artigo descreve a descontinuação do TLS 1.0 e TLS 1.1 pela Braze, concluída em maio de 2018."
---
# Descontinuação do TLS 1.0 e 1.1 {#tls-10-11-deprecation}

{% alert update %}
A Braze removeu o suporte para cifras de Segurança da Camada de Transporte (TLS) tanto no TLS 1.0 quanto no 1.1, de acordo com as recomendações feitas pelo Conselho de Padrões de Segurança PCI. Realizamos essa descontinuação de suporte em duas fases, concluídas em maio de 2018.
{% endalert %}

## Contexto {#background}

A Braze está descontinuando cifras de Segurança da Camada de Transporte (TLS) conhecidas como fracas tanto no TLS 1.0 quanto no 1.1, de acordo com as recomendações feitas pelo Conselho de Padrões de Segurança PCI em duas fases que se concluem em maio de 2018.

Essa mudança não está sendo feita em resposta a qualquer violação ou problema relacionado à plataforma da Braze, mas como uma medida de precaução para manter nossos padrões de segurança e dados de excelência, e para proteger proativamente nossos clientes e seus consumidores.

Nos últimos anos, uma série de problemas de segurança sistemáticos associados tanto ao TLS quanto ao seu predecessor, Secure Sockets Layer (SSL), incluindo [POODLE](https://www.us-cert.gov/ncas/alerts/TA14-290A), [Heartbleed](https://en.wikipedia.org/wiki/Heartbleed), [LOGJAM](https://en.wikipedia.org/wiki/Logjam_(computer_security)) e outros, ameaçaram o tráfego web criptografado e expuseram partes da internet a violações de segurança. Juntamente com outras empresas de tecnologia, a Braze já tomou medidas para desativar protocolos e cifras de criptografia fracos à medida que os ataques são descobertos — por exemplo, removendo o suporte para SSLv3 em 2014.

Mais recentemente, o PCI Security Standards Council publicou orientações relacionadas à criptografia em abril de 2015 para o [Payment Card Industry Data Security Standard](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard) (PCI-DSS). A orientação exclui SSL 3.0, TLS 1.0 e alguns dos conjuntos de cifras suportados pelo TLS 1.1 da sua lista de protocolos de cifras criptográficas fortes, e incentiva as empresas a descontinuarem o suporte para esses protocolos ou cifras para garantir a segurança dos usuários da internet.

Um conjunto de cifras é uma combinação de algoritmos que fornecem criptografia, autenticação e integridade das comunicações ao negociar uma conexão SSL ou TLS segura. Quando se descobre que é possível quebrar uma cifra específica — independentemente de haver ou não ataques conhecidos no momento — a cifra é considerada como tendo "fraquezas" que poderiam possibilitar ataques futuros. Ao excluir essas cifras TLS dos requisitos de conformidade PCI DSS, o Conselho PCI DSS está exigindo que os prestadores de serviço suportem apenas os melhores padrões de criptografia. O Conselho PCI DSS estabeleceu um prazo até 30 de junho de 2018 para conformidade com o requisito de criptografia para interromper o suporte ao TLS 1.0 e TLS 1.1.

## Plano de descontinuação da Braze {#brazes-deprecation-plan}
Para cumprir as recomendações do Conselho PCI DSS, a Braze aumentará as versões mínimas de TLS que suportamos em nossos Serviços. Para dar a você uma ideia melhor sobre nosso plano de conformidade e seu impacto potencial na sua marca e nos seus usuários, há duas fases principais em nosso plano que você deve conhecer:

### Fase 1: 1º de outubro de 2017 {#phase-1-october-1-2017}

A Braze removerá a capacidade de usar as seguintes cifras do dashboard web e das REST or transferir estado representacional APIs da Braze:

- `TLS_RSA_WITH_AES_256_CBC_SHA`
- `TLS_RSA_WITH_AES_128_CBC_SHA`
- `TLS_RSA_WITH_AES_256_CBC_SHA256`
- `TLS_RSA_WITH_AES_256_GCM_SHA384`
- `TLS_RSA_WITH_AES_128_CBC_SHA256`
- `TLS_RSA_WITH_AES_128_GCM_SHA256`
- `TLS_RSA_WITH_3DES_EDE_CBC_SHA`

Essa mudança não deve impactar os clientes que acessam o dashboard da Braze, pois todos os navegadores web modernos suportam cifras mais seguras. No entanto, se você encontrar um erro de criptografia SSL ao acessar o dashboard web após 1º de outubro, poderá resolver o problema simplesmente atualizando para a versão mais recente do seu navegador de internet or navegador web.

Sua equipe de engenharia deve garantir que não esteja usando nenhuma dessas cifras para comunicação de servidor para servidor com as REST or transferir estado representacional APIs da Braze. Se estiverem, precisarão atualizar o código para usar cifras de criptografia mais seguras antes de 1º de outubro para continuar utilizando as APIs da Braze. No entanto, para manter o suporte a dispositivos móveis antigos e desatualizados que podem estar usando cifras fracas, a Braze continuará a suportar essas cifras nas APIs que recebem dados dos nossos SDKs.

### Fase 2: 31 de maio de 2018 {#phase-2-may-31-2018}

A Braze desativará o suporte para TLS 1.0 e TLS 1.1 em todos os Serviços da Braze em 31 de maio de 2018 — incluindo o dashboard da Braze, REST or transferir estado representacional APIs e APIs que se comunicam com nossos SDKs. Também removeremos o suporte para as cifras listadas na seção anterior em conexão com as APIs que recebem dados do SDK or kit de desenvolvimento de software. Isso significa que toda comunicação TLS 1.0 e 1.1 de e para a Braze não será mais suportada pela nossa rede a partir dessa data.

Como resultado dessa mudança, alguns dispositivos móveis antigos ou desatualizados — provavelmente aqueles que executam versões antigas do Android — podem perder a capacidade de se comunicar com a Braze, impedindo-os de enviar dados para a Braze ou receber mensagens no app da Braze. No entanto, prevemos que a mudança afetará apenas um pequeno número de dispositivos. Qualquer dispositivo afetado também perderá a capacidade de se comunicar com qualquer website ou serviço compatível com PCI um mês depois, em 30 de junho de 2018, data definida pelo Conselho PCI DSS para a remoção das cifras TLS 1.0 e TLS 1.1.

## Plano de ação {#action-plan}
Se a sua marca estiver utilizando as REST or transferir estado representacional APIs da Braze, fale com sua equipe de engenharia para garantir que todas as chamadas de servidor para servidor para a Braze estejam usando TLS 1.2 até a data indicada, a fim de evitar uma interrupção do serviço. Saiba que algumas linguagens de programação — como o Java 7 — usam versões mais antigas do TLS por padrão, então sua equipe de engenharia pode precisar fazer algumas alterações no código para atender aos requisitos de criptografia atualizados.

Dispositivos Apple não serão afetados pela descontinuação planejada da Braze porque a Apple exige TLS 1.2 desde o final de 2016. O mesmo vale para os navegadores web modernos, então não prevemos que essas mudanças terão qualquer impacto no uso do Web SDK or kit de desenvolvimento de software. No entanto, dispositivos Android executando Android 4.4 (KitKat) ou inferior podem não usar TLS 1.2 por padrão, então tome medidas para fazer upgrade de qualquer uma das suas integrações Android para pelo menos a versão 2.0.3 do SDK or kit de desenvolvimento de software da Braze (que usa TLS 1.2 por padrão, se o dispositivo em questão puder suportá-lo) até 31 de maio de 2018.

Por fim, devido às fraquezas conhecidas no TLS 1.0 e no conjunto de cifras TLS 1.1, é possível que ataques surjam no futuro, o que exigiria que a Braze acelerasse nosso plano de descontinuação para proteger a segurança de todos os nossos clientes. A Braze monitorará o estado da segurança e quaisquer ataques relevantes associados aos protocolos TLS 1.0 e 1.1, e manterá você informado caso tomemos conhecimento de quaisquer ataques que alterem o cronograma estabelecido nas seções anteriores. Mas, por causa desse impacto potencial, recomendamos fortemente que você trabalhe com sua equipe de engenharia para garantir que suas chamadas de API or interface de programação do aplicativo (API) para a Braze estejam protegidas com TLS 1.2 e que você planeje fazer upgrade para o SDK or kit de desenvolvimento de software mais recente do Android nos próximos meses.