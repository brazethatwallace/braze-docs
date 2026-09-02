---
nav_title: Assistência técnica em proteção de dados
article_title: Assistência técnica de proteção de dados nos Serviços Braze
page_order: 1
description: "Esta página fornece instruções técnicas para que você gerencie, por meio dos Serviços Braze, solicitações de indivíduos em relação a seus direitos de dados pessoais."
alias: /help/dp-technical-assistance/
permalink: /dp-technical-assistance/
hide_toc: true
---

<!--
Warning! Don't make any changes to this document without approval from the legal department.
-->

# Assistência técnica de proteção de dados nos Serviços Braze {#data-protection-technical-assistance-in-the-braze-services}

Há uma série de leis de proteção de dados que regulam o que as organizações podem fazer com dados pessoais ("Leis de Proteção de Dados"), incluindo o Regulamento Geral de Proteção de Dados da UE e do Reino Unido ("GDPR"), a Lei de Privacidade do Consumidor da Califórnia ("CCPA") e a Lei de Portabilidade e Responsabilidade de Seguros de Saúde ("HIPAA"). Existem outras leis e regulamentações nacionais, estaduais e específicas do setor que podem se aplicar ao seu negócio.

Essas Leis de Proteção de Dados concedem aos indivíduos "direitos de privacidade" sobre seus dados pessoais. As organizações são obrigadas a receber e responder a solicitações de indivíduos que exercem seus direitos de privacidade. Os Serviços Braze podem ajudar você a cumprir essas Leis de Proteção de Dados, fornecendo recursos para facilitar determinadas ações exigidas por essas leis. Este documento fornece instruções técnicas para usar esses recursos para gerenciar solicitações de direitos de privacidade. Cabe a você determinar quais Leis de Proteção de Dados se aplicam ao seu negócio e agir em conformidade com elas.

## Aviso legal {#legal-disclaimer}

Nada do que se segue pretende ser, nem deve ser considerado, aconselhamento jurídico da Braze. Recomendamos que você busque a orientação do seu próprio assessor jurídico em relação à sua situação específica e a como as Leis de Proteção de Dados se aplicam a você e ao seu uso dos Serviços da Braze.

## Terminologia {#terminology}

Para os fins deste documento, qualquer referência a dados pessoais também pode ser entendida como uma referência a informações pessoais ou informações de identificação pessoal ("Dados Pessoais"). Por questão de simplicidade, geralmente utilizamos a linguagem do GDPR ao abordar os direitos dos usuários finais. A linguagem do GDPR é frequentemente intercambiável ou está alinhada de forma próxima com um termo ou conceito definido em outras Leis de Proteção de Dados.

## Conceitos básicos {#the-basics}

A maioria das leis de privacidade define três principais partes interessadas envolvidas no processamento de Dados Pessoais: titulares dos dados, controladores de dados e processadores de dados. Cada grupo tem diferentes direitos e responsabilidades em relação ao uso de Dados Pessoais:

- Um titular dos dados é um indivíduo cujos Dados Pessoais estão sendo processados pelo processador de dados ou controlador de dados
- Um controlador de dados é uma entidade que determina as finalidades e os meios do processamento de Dados Pessoais
- Um processador de dados é uma entidade que processa Dados Pessoais em nome e sob as instruções do controlador de dados

Em relação aos Serviços da Braze:

- Os titulares dos dados são, por exemplo, os usuários finais do seu aplicativo de cliente (por exemplo, seus clientes) ou seus colaboradores que são usuários corporativos na sua instância dos Serviços da Braze.
- Você, o cliente da Braze, é o controlador de dados que decide como e por que os Dados Pessoais dos titulares dos dados serão coletados e processados dentro dos Serviços da Braze.
- A Braze é um processador de dados que processa Dados Pessoais nos Serviços da Braze em seu nome e de acordo com as instruções que recebemos de você.

Os termos acima são do GDPR, mas, por exemplo, termos comparáveis sob a CCPA são:
- "consumidores" para titulares dos dados.
- "empresas" para controladores de dados.
- "prestadores de serviço" para processadores de dados.

Abaixo, você encontrará informações relevantes sobre as solicitações de direitos de privacidade mais comuns feitas pelos titulares dos dados, incluindo como você pode responder a elas por meio dos recursos técnicos dos Serviços da Braze.

## O direito de ser informado {#the-right-to-be-informed}

O direito de ser informado abrange sua obrigação de fornecer "informações sobre o processamento justo de dados", normalmente por meio de um aviso de privacidade. Ele enfatiza a necessidade de transparência sobre como você usa dados pessoais.

### Recomendação da Braze {#braze-recommendation}

A maioria das leis de proteção de dados enfatiza a necessidade de transparência em relação a como você usa dados pessoais. Essa é a responsabilidade dos controladores de dados, que normalmente mantêm um aviso de privacidade facilmente acessível aos usuários de seus produtos e serviços e que abrange o processamento realizado pela Braze.

## O direito de acesso {#the-right-of-access}

De acordo com as leis de proteção de dados, os titulares de dados podem ter o direito de obter:

- Confirmação de que seus dados pessoais estão sendo processados,
- Acesso aos seus dados pessoais, e
- Outras informações complementares conforme determinado pela lei de proteção de dados aplicável.

### Recomendação da Braze

Para fornecer dados pessoais da Braze em um formato legível por máquina em resposta a uma solicitação de acesso de um titular de dados, você pode exportar o perfil do usuário final fazendo uma chamada de API or interface de programação do aplicativo (API) para as [REST or transferir estado representacional APIs]({{site.baseurl}}/api/endpoints/export) da Braze, usando o identificador do usuário (definido por você como o `external_id` fornecido à Braze) e/ou o identificador do dispositivo.

#### BrazeAI Decisioning Studio™

Para atender a uma solicitação de direito de acesso relacionada a dados pessoais no BrazeAI Decisioning Studio™, entre em contato com o gerente da sua conta informando os customer_id(s) e/ou e-mail(s) relevantes.

## O direito à retificação {#the-right-to-rectification}

Os indivíduos têm o direito de ter seus dados pessoais corrigidos caso estejam incorretos ou incompletos. Se você divulgou os dados pessoais em questão a terceiros, pode ser necessário informá-los sobre a retificação, quando possível.

### Recomendação da Braze

Caso um titular de dados solicite que você corrija imprecisões nos dados pessoais que estão sendo processados por você ou pela Braze em seu nome, você pode usar os SDKs da Braze ou as [REST or transferir estado representacional APIs]({{site.baseurl}}/api/endpoints/user_data/post_user_track) da Braze para corrigir esses dados pessoais.

## O direito à exclusão {#the-right-to-erasure}

O direito à exclusão também é conhecido como "o direito de ser esquecido" ou "direito de ser apagado".

### Recomendação da Braze

#### Exclusão padrão {#standard-deletion}

Após interromper a coleta de dados, você pode usar o [endpoint da REST or transferir estado representacional API or interface de programação do aplicativo (API) de exclusão de usuários da Braze]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) para excluir um usuário final, o que removerá todos os registros desse usuário final dos serviços da Braze:

- Para usuários finais que possuem um external_id nos serviços da Braze, você pode usar esse ID para excluir os dados desse usuário final.
- Para usuários finais anônimos que não possuem um external_id nos serviços da Braze, você pode recuperar o identificador de dispositivo desse usuário final usando o SDK or kit de desenvolvimento de software da Braze e usá-lo para encontrar o perfil de usuário final associado a esse dispositivo. Depois, você pode usar a API or interface de programação do aplicativo (API) de exclusão de usuários para excluir o perfil associado a esse usuário final.

Excluir um usuário final dos serviços da Braze excluirá permanentemente o perfil de usuário centralizado da Braze para esse usuário final, conforme definido pelo `external_id` fornecido. Isso inclui informações estruturadas do perfil que a Braze coletou por padrão ou que você configurou os serviços da Braze para coletar, como informações do dispositivo, país, idioma e endereço de e-mail.

Observe que o endereço de e-mail ou número de telefone associado ao perfil do usuário final ainda pode estar armazenado na Braze, pois pode estar associado ao perfil de outro usuário final. Endereços de e-mail e números de telefone não são únicos nos serviços da Braze. Isso significa que sua equipe pode ter configurado a Braze para armazenar o mesmo endereço de e-mail ou número de telefone em vários perfis de usuário. Se sua equipe configurou a Braze dessa forma, esteja ciente de que pode ser necessário excluir todos os perfis de usuário que representam um determinado titular de dados para cumprir uma solicitação de exclusão desse titular, e sua equipe precisará fazer várias chamadas de API or interface de programação do aplicativo (API) para excluir todos os perfis de usuário que se referem a um determinado titular de dados.

#### BrazeAI Decisioning Studio™

Para atender a uma solicitação de direito à exclusão em relação a dados pessoais no BrazeAI Decisioning Studio™, entre em contato com seu gerente de conta com os customer_id(s) e/ou e-mail(s) relevantes. Seu gerente de conta pode providenciar a exclusão de todos os dados pessoais associados encontrados no data warehouse.

#### Considerações adicionais sobre exclusão {#additional-deletion-considerations}

<style>
#considerations td {
    word-break: break-word;
    width: 100%;
    font-size: 16px;
}
</style>

<table id="considerations">
  <caption>Considerações adicionais sobre exclusão</caption>
<tbody>
  <tr>
    <td>
        <p>Os clientes podem criar campos personalizados para propriedades de eventos e extras de mensagens. Esses campos não são destinados a dados pessoais e, por isso, não estão incluídos no processo de exclusão padrão descrito acima. No entanto, se você usar a Braze para inserir ou coletar dados pessoais por meio de propriedades de eventos e extras de mensagens, poderá configurar o processo de exclusão acionado pelo endpoint da REST or transferir estado representacional API or interface de programação do aplicativo (API) de exclusão de usuários para também incluir esses campos, de forma que os dados contidos neles sejam excluídos também.</p>
        <p>As configurações padrão são aplicadas no nível da empresa, mas você pode optar por excluir os seguintes campos quando o processo de exclusão for executado, no nível do grupo de apps/espaço de trabalho:</p>
    <ul>
        <li>PROPERTIES para USERS_BEHAVIORS_CUSTOMEVENT</li>
        <li>PROPERTIES para USERS_BEHAVIORS_PURCHASE</li>
        <li>MESSAGE_EXTRAS para:
            <ul>
            <li>USERS_MESSAGES_CONTENTCARD</li>
            <li>USERS_MESSAGES_EMAIL_SEND</li>
            <li>USERS_MESSAGES_PUSHNOTIFICATION_SEND</li>
            <li>USERS_MESSAGES_PUSHNOTIFICATION_RETRYSEND_SHARED</li>
            <li>USERS_MESSAGES_WEBHOOK_SEND</li>
            <li>USERS_MESSAGES_SMS_SEND</li>
            <li>Eventos futuros de envio de mensagens</li>
            </ul>
        </li>
    </ul>
    <p>As configurações para isso podem ser acessadas em <b>Configurações da empresa</b> > <b>Configurações de administrador</b> > <b>Configurações de segurança</b>. As preferências de exclusão de dados são definidas por tipo de evento ou categoria. Apenas um usuário com permissões de administrador pode fazer alterações nessas configurações. Alternativamente, um administrador pode delegar essas permissões a outro usuário.</p>
    <p>Se um tipo de evento ou extra de mensagem estiver configurado para ser incluído no processo de exclusão, os dados nesse campo serão excluídos daqui em diante para os usuários para os quais você está executando o endpoint da REST or transferir estado representacional API or interface de programação do aplicativo (API) de exclusão de usuários. Além disso, ao selecionar essa preferência de exclusão, na próxima tarefa de exclusão agendada, os dados desses campos serão excluídos de quaisquer conjuntos de dados anonimizados existentes que contenham esses campos. Não será possível restaurar os campos de dados excluídos.</p>
    </td>
  </tr>
</tbody>
</table>

#### Análise de dados {#analytics}

Para manter a integridade da análise de dados de uso de Campaigns e aplicativos, dados agregados anônimos não serão modificados quando um usuário final for excluído. Por exemplo, a Braze não diminuirá o número total de sessões de um app quando um usuário final for excluído. As sessões em que esse usuário final visitou o app ainda serão incluídas no número total de visitas a esse app, mas esses dados não estarão conectados de nenhuma forma ao perfil do usuário final esquecido, garantindo que esses dados anonimizados e agregados não possam ser vinculados a um usuário final individual.

A análise de dados nos serviços da Braze está vinculada ao identificador de usuário final da Braze. Após o perfil do usuário final ter sido excluído, o identificador de usuário da Braze efetivamente se torna um identificador completamente anonimizado, pois a Braze não consegue vinculá-lo a nenhum usuário final individual.

#### Após a exclusão ter sido realizada {#once-deletion-has-happened}

De modo geral, espera-se que você faça esforços razoáveis para notificar os titulares de dados quando tiver cumprido sua solicitação de exclusão de seus dados pessoais. Um usuário final excluído pode se registrar novamente ou voltar a interagir com seu app ou serviço em uma data posterior, e a Braze não será capaz de identificá-lo como o usuário excluído ou esquecido. Os serviços da Braze não são capazes de criar listas de identificadores de usuários excluídos ou endereços de e-mail em seu nome.

## O direito à restrição de processamento {#the-right-to-restriction-of-processing}

Os titulares de dados podem ter o direito de "bloquear" ou suprimir o processamento de seus Dados Pessoais em determinadas circunstâncias. Restringir o processamento significa não realizar nenhum processamento ao qual o titular dos dados tenha se oposto.

### Recomendação da Braze

Os Serviços da Braze não suportam a restrição de processamento de categorias individuais de Dados Pessoais. Se um titular de dados solicitar a restrição do processamento de determinados subconjuntos de seus Dados Pessoais, você deve usar as [APIs da Braze]({{site.baseurl}}/api/home) para exportar o(s) perfil(is) completo(s) desse usuário final e, em seguida, [excluí-lo(s)]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) da Braze. As APIs da Braze podem ser usadas para reimportar esses dados caso o usuário final posteriormente permita que você processe esses subconjuntos específicos de seus Dados Pessoais. Além disso, você deve recomendar que seu usuário final desinstale ou faça logout de todos os seus aplicativos que usam o SDK or kit de desenvolvimento de software da Braze para interromper a coleta de quaisquer dados adicionais sobre o titular dos dados.

Para clientes que usam apenas o BrazeAI Decisioning Studio™, você não deve mais enviar dados para o Decisioning Studio.

## O direito à portabilidade de dados {#the-right-to-data-portability}

O direito à portabilidade de dados permite que os titulares dos dados obtenham e reutilizem seus dados pessoais para seus próprios fins em diferentes serviços. Os dados pessoais devem ser fornecidos em um formato estruturado, legível por máquina e de uso comum.

### Recomendação da Braze

Assim como no direito de acesso, você pode usar a [REST or transferir estado representacional API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/endpoints/export) da Braze para exportar os dados pessoais de um usuário final e fornecê-los ao titular dos dados conforme sua solicitação. Além disso, entre em contato com seu gerente de conta informando os customer_id(s) e/ou e-mail(s) relevantes para solicitar uma cópia de quaisquer dados pessoais armazenados no BrazeAI Decisioning Studio.

## O direito de objeção {#the-right-to-object}

Os indivíduos podem ter o direito de se opor a:

- processamento com base em interesses legítimos ou na execução de uma tarefa de interesse público/exercício de autoridade oficial (incluindo criação de perfis);
- marketing direto (incluindo criação de perfis); e
- processamento para fins de pesquisa científica/histórica e estatísticas.

### Recomendação da Braze

A Braze oferece a capacidade de marcar um perfil de usuário como cancelado de SMS, e-mails ou notificações por push por meio de nossas [REST or transferir estado representacional APIs]({{site.baseurl}}/api/home) e dos SDKs para [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=swift), [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=android) e [Web]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes?sdktab=web). Se você receber objeções de titulares de dados quanto ao recebimento dessas mensagens, poderá usar as APIs da Braze para cancelar a inscrição desses usuários finais.

Se isso não for suficiente, para evitar o processamento de dados pessoais do usuário final pela Braze, o perfil do usuário final deve ser excluído da mesma forma especificada na seção "Direito à exclusão".

## Direitos relacionados à tomada de decisões automatizada e à criação de perfis {#rights-related-to-automated-decision-making-and-profiling}

Algumas leis de proteção de dados impedem, ou permitem que os titulares dos dados optem por não participar de, tomadas de decisões automatizadas ou criação de perfis em determinadas circunstâncias, especialmente para decisões que "produzem um efeito legal ou um efeito similarmente significativo sobre o indivíduo."

### Recomendação da Braze

A Braze não realiza nenhuma ação automatizada de criação de perfis ou de tomada de decisões com ramificações legais ou equivalentes para os titulares dos dados. Se você acredita que o seu próprio uso dos serviços da Braze terá impactos legais ou equivalentes e recebeu uma objeção a isso, pode optar por excluir o perfil de usuário da mesma maneira descrita em "Direito ao apagamento."

## Publicidade direcionada {#targeting-advertising}

De acordo com algumas leis de privacidade estaduais dos EUA, os titulares de dados podem se opor ao uso de seus dados pessoais para fins de publicidade direcionada.

### Recomendação da Braze

Ao criar públicos para fins de direcionamento de anúncios aos seus titulares de dados, você deve garantir que excluiu todos os titulares de dados que se opuseram à publicidade direcionada, por exemplo, consumidores da Califórnia que exerceram seu direito de "Não Vender ou Compartilhar" nos termos da CCPA.

Para saber mais sobre como criar públicos para sincronizar com plataformas de terceiros, consulte [Audience sync]({{site.baseurl}}/partners/canvas_audience_sync).

## O direito à não discriminação {#the-right-to-non-discrimination}

Os titulares de dados têm o direito de exercer seus direitos de privacidade sem discriminação.

### Recomendação da Braze

Ao utilizar os serviços da Braze, os clientes devem garantir que não discriminem os titulares de dados que exerceram seus direitos de privacidade. Por exemplo, recomendamos que os titulares de dados que exerceram seus direitos de privacidade não sejam segmentados em públicos nem direcionados de maneira que possa discriminá-los.