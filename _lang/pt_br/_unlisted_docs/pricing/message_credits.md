---
nav_title: Créditos de mensagem - Calculadora
permalink: "/message_credits_calc/"
hidden: true
noindex: true
hide_toc: true
---

# Créditos de mensagem - Calculadora {#message-credits-calculator}

<style type="text/css">
#message_credit table {
  margin: 0 auto;
  color: #333;
  background: white;
  border: 1px solid grey;
  font-size: 12pt;
  border-collapse: collapse;
  padding: 3px 2px;
}
#message_credit select {
  border: 1px solid grey !important;
  border-radius: 5px;
  padding: 2px 10px;
}
#message_credit input[type=text] {
  border: 1px solid grey !important;
  border-radius: 5px;
  padding: 2px 10px;
}
#message_credit table th {
  color: #FFFFFF;
  background: #0B6FA4;
  text-align: center;
  border: 1px solid #ddd;
}
#message_credit table td {
  color: #333;
  border: 1px solid #ddd;
}

#message_credit tr:nth-child(even){
  background: #D0E4F5;
}

#message_credit tr:hover { background-color: #801ED7; }
#message_credit #message_error { display: inline-block; }
#message_credit td:nth-child(1),
#message_credit td:nth-child(3) {
  word-break: keep-all;
  min-width: 180px;
}
#message_credit td:nth-child(2),
#message_credit td:nth-child(4),
#message_credit td:nth-child(5),
#message_credit td:nth-child(6) {
  text-align: right !important;
}
</style>
<div id="message_credit">
Créditos de mensagem:
<select id="credit_type">
<option value="0">Delta</option>
<option value="1">Theta</option>
<option value="2">Gamma</option>
<option value="3">Sigma</option>
<option value="4">Lambda</option>
</select><br />
Taxas unitárias de crédito: <input type="text" id="credit_rate" value="0" />
<div id="message_error"></div><br /><br />
<table aria-label="Créditos de mensagem - Calculadora">
  <thead>
  <tr>
    <th>
      Canal
    </th>
    <th>
      Proporção de créditos
    </th>
    <th>
      Destino
    </th>
    <th>
      Multiplicador
    </th>
    <th>
      Créditos/Mensagem
    </th>
    <th>
      Taxas implícitas
    </th>
  </tr>
  </thead>
  <tbody>
  <tr><td>SMS - US / CA</td><td id="sms_-_us_ca_united_states_ratio"></td><td>Estados Unidos</td><td id="sms_-_us_ca_united_states_multiplier"></td><td id="sms_-_us_ca_united_states_credit"></td><td id="sms_-_us_ca_united_states_rates"></td></tr>
  <tr><td>SMS - US / CA</td><td id="sms_-_us_ca_united_states_toll_free_ratio"></td><td>Estados Unidos Toll Free</td><td id="sms_-_us_ca_united_states_toll_free_multiplier"></td><td id="sms_-_us_ca_united_states_toll_free_credit"></td><td id="sms_-_us_ca_united_states_toll_free_rates"></td></tr>
  <tr><td>SMS - US / CA</td><td id="sms_-_us_ca_canada_ratio"></td><td>Canadá</td><td id="sms_-_us_ca_canada_multiplier"></td><td id="sms_-_us_ca_canada_credit"></td><td id="sms_-_us_ca_canada_rates"></td></tr>
  <tr><td>SMS - US / CA</td><td id="sms_-_us_ca_canada_toll_free_ratio"></td><td>Canadá Toll Free</td><td id="sms_-_us_ca_canada_toll_free_multiplier"></td><td id="sms_-_us_ca_canada_toll_free_credit"></td><td id="sms_-_us_ca_canada_toll_free_rates"></td></tr>
  <tr><td>MMS - US / CA</td><td id="mms_-_us_ca_united_states_ratio"></td><td>Estados Unidos</td><td id="mms_-_us_ca_united_states_multiplier"></td><td id="mms_-_us_ca_united_states_credit"></td><td id="mms_-_us_ca_united_states_rates"></td></tr>
  <tr><td>MMS - US / CA</td><td id="mms_-_us_ca_united_states_toll_free_ratio"></td><td>Estados Unidos Toll Free</td><td id="mms_-_us_ca_united_states_toll_free_multiplier"></td><td id="mms_-_us_ca_united_states_toll_free_credit"></td><td id="mms_-_us_ca_united_states_toll_free_rates"></td></tr>
  <tr><td>MMS - US / CA</td><td id="mms_-_us_ca_canada_long_code_ratio"></td><td>Canadá Long Code</td><td id="mms_-_us_ca_canada_long_code_multiplier"></td><td id="mms_-_us_ca_canada_long_code_credit"></td><td id="mms_-_us_ca_canada_long_code_rates"></td></tr>
  <tr><td>MMS - US / CA</td><td id="mms_-_us_ca_canada_short_code_ratio"></td><td>Canadá Short Code</td><td id="mms_-_us_ca_canada_short_code_multiplier"></td><td id="mms_-_us_ca_canada_short_code_credit"></td><td id="mms_-_us_ca_canada_short_code_rates"></td></tr>
  <tr><td>MMS - US / CA</td><td id="mms_-_us_ca_canada_toll_free_ratio"></td><td>Canadá Toll Free</td><td id="mms_-_us_ca_canada_toll_free_multiplier"></td><td id="mms_-_us_ca_canada_toll_free_credit"></td><td id="mms_-_us_ca_canada_toll_free_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_abkhazia_ratio"></td><td>Abcásia</td><td id="sms_mms_-_global_abkhazia_multiplier"></td><td id="sms_mms_-_global_abkhazia_credit"></td><td id="sms_mms_-_global_abkhazia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_afghanistan_ratio"></td><td>Afeganistão</td><td id="sms_mms_-_global_afghanistan_multiplier"></td><td id="sms_mms_-_global_afghanistan_credit"></td><td id="sms_mms_-_global_afghanistan_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_albania_ratio"></td><td>Albânia</td><td id="sms_mms_-_global_albania_multiplier"></td><td id="sms_mms_-_global_albania_credit"></td><td id="sms_mms_-_global_albania_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_algeria_ratio"></td><td>Argélia</td><td id="sms_mms_-_global_algeria_multiplier"></td><td id="sms_mms_-_global_algeria_credit"></td><td id="sms_mms_-_global_algeria_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_american_samoa_ratio"></td><td>Samoa Americana</td><td id="sms_mms_-_global_american_samoa_multiplier"></td><td id="sms_mms_-_global_american_samoa_credit"></td><td id="sms_mms_-_global_american_samoa_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_andorra_ratio"></td><td>Andorra</td><td id="sms_mms_-_global_andorra_multiplier"></td><td id="sms_mms_-_global_andorra_credit"></td><td id="sms_mms_-_global_andorra_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_angola_ratio"></td><td>Angola</td><td id="sms_mms_-_global_angola_multiplier"></td><td id="sms_mms_-_global_angola_credit"></td><td id="sms_mms_-_global_angola_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_anguilla_ratio"></td><td>Anguilla</td><td id="sms_mms_-_global_anguilla_multiplier"></td><td id="sms_mms_-_global_anguilla_credit"></td><td id="sms_mms_-_global_anguilla_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_antigua_and_barbuda_ratio"></td><td>Antígua e Barbuda</td><td id="sms_mms_-_global_antigua_and_barbuda_multiplier"></td><td id="sms_mms_-_global_antigua_and_barbuda_credit"></td><td id="sms_mms_-_global_antigua_and_barbuda_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_argentina_ratio"></td><td>Argentina</td><td id="sms_mms_-_global_argentina_multiplier"></td><td id="sms_mms_-_global_argentina_credit"></td><td id="sms_mms_-_global_argentina_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_armenia_ratio"></td><td>Armênia</td><td id="sms_mms_-_global_armenia_multiplier"></td><td id="sms_mms_-_global_armenia_credit"></td><td id="sms_mms_-_global_armenia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_aruba_ratio"></td><td>Aruba</td><td id="sms_mms_-_global_aruba_multiplier"></td><td id="sms_mms_-_global_aruba_credit"></td><td id="sms_mms_-_global_aruba_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_australia_sms_ratio"></td><td>Austrália SMS</td><td id="sms_mms_-_global_australia_sms_multiplier"></td><td id="sms_mms_-_global_australia_sms_credit"></td><td id="sms_mms_-_global_australia_sms_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_australia_mms_ratio"></td><td>Austrália MMS</td><td id="sms_mms_-_global_australia_mms_multiplier"></td><td id="sms_mms_-_global_australia_mms_credit"></td><td id="sms_mms_-_global_australia_mms_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_austria_ratio"></td><td>Áustria</td><td id="sms_mms_-_global_austria_multiplier"></td><td id="sms_mms_-_global_austria_credit"></td><td id="sms_mms_-_global_austria_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_azerbaijan_ratio"></td><td>Azerbaijão</td><td id="sms_mms_-_global_azerbaijan_multiplier"></td><td id="sms_mms_-_global_azerbaijan_credit"></td><td id="sms_mms_-_global_azerbaijan_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_bahamas_ratio"></td><td>Bahamas</td><td id="sms_mms_-_global_bahamas_multiplier"></td><td id="sms_mms_-_global_bahamas_credit"></td><td id="sms_mms_-_global_bahamas_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_bahrain_ratio"></td><td>Bahrein</td><td id="sms_mms_-_global_bahrain_multiplier"></td><td id="sms_mms_-_global_bahrain_credit"></td><td id="sms_mms_-_global_bahrain_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_bangladesh_ratio"></td><td>Bangladesh</td><td id="sms_mms_-_global_bangladesh_multiplier"></td><td id="sms_mms_-_global_bangladesh_credit"></td><td id="sms_mms_-_global_bangladesh_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_barbados_ratio"></td><td>Barbados</td><td id="sms_mms_-_global_barbados_multiplier"></td><td id="sms_mms_-_global_barbados_credit"></td><td id="sms_mms_-_global_barbados_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_belarus_ratio"></td><td>Belarus</td><td id="sms_mms_-_global_belarus_multiplier"></td><td id="sms_mms_-_global_belarus_credit"></td><td id="sms_mms_-_global_belarus_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_belgium_ratio"></td><td>Bélgica</td><td id="sms_mms_-_global_belgium_multiplier"></td><td id="sms_mms_-_global_belgium_credit"></td><td id="sms_mms_-_global_belgium_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_belize_ratio"></td><td>Belize</td><td id="sms_mms_-_global_belize_multiplier"></td><td id="sms_mms_-_global_belize_credit"></td><td id="sms_mms_-_global_belize_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_benin_ratio"></td><td>Benin</td><td id="sms_mms_-_global_benin_multiplier"></td><td id="sms_mms_-_global_benin_credit"></td><td id="sms_mms_-_global_benin_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_bermuda_ratio"></td><td>Bermudas</td><td id="sms_mms_-_global_bermuda_multiplier"></td><td id="sms_mms_-_global_bermuda_credit"></td><td id="sms_mms_-_global_bermuda_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_bhutan_ratio"></td><td>Butão</td><td id="sms_mms_-_global_bhutan_multiplier"></td><td id="sms_mms_-_global_bhutan_credit"></td><td id="sms_mms_-_global_bhutan_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_bolivia_ratio"></td><td>Bolívia</td><td id="sms_mms_-_global_bolivia_multiplier"></td><td id="sms_mms_-_global_bolivia_credit"></td><td id="sms_mms_-_global_bolivia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_bosnia_and_herzegovina_ratio"></td><td>Bósnia e Herzegovina</td><td id="sms_mms_-_global_bosnia_and_herzegovina_multiplier"></td><td id="sms_mms_-_global_bosnia_and_herzegovina_credit"></td><td id="sms_mms_-_global_bosnia_and_herzegovina_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_botswana_ratio"></td><td>Botsuana</td><td id="sms_mms_-_global_botswana_multiplier"></td><td id="sms_mms_-_global_botswana_credit"></td><td id="sms_mms_-_global_botswana_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_brazil_ratio"></td><td>Brasil</td><td id="sms_mms_-_global_brazil_multiplier"></td><td id="sms_mms_-_global_brazil_credit"></td><td id="sms_mms_-_global_brazil_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_brunei_ratio"></td><td>Brunei</td><td id="sms_mms_-_global_brunei_multiplier"></td><td id="sms_mms_-_global_brunei_credit"></td><td id="sms_mms_-_global_brunei_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_bulgaria_ratio"></td><td>Bulgária</td><td id="sms_mms_-_global_bulgaria_multiplier"></td><td id="sms_mms_-_global_bulgaria_credit"></td><td id="sms_mms_-_global_bulgaria_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_burkina_faso_ratio"></td><td>Burkina Faso</td><td id="sms_mms_-_global_burkina_faso_multiplier"></td><td id="sms_mms_-_global_burkina_faso_credit"></td><td id="sms_mms_-_global_burkina_faso_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_burundi_ratio"></td><td>Burundi</td><td id="sms_mms_-_global_burundi_multiplier"></td><td id="sms_mms_-_global_burundi_credit"></td><td id="sms_mms_-_global_burundi_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_cambodia_ratio"></td><td>Camboja</td><td id="sms_mms_-_global_cambodia_multiplier"></td><td id="sms_mms_-_global_cambodia_credit"></td><td id="sms_mms_-_global_cambodia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_cameroon_ratio"></td><td>Camarões</td><td id="sms_mms_-_global_cameroon_multiplier"></td><td id="sms_mms_-_global_cameroon_credit"></td><td id="sms_mms_-_global_cameroon_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_cape_verde_ratio"></td><td>Cabo Verde</td><td id="sms_mms_-_global_cape_verde_multiplier"></td><td id="sms_mms_-_global_cape_verde_credit"></td><td id="sms_mms_-_global_cape_verde_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_caribbean_netherlands_ratio"></td><td>Países Baixos Caribenhos</td><td id="sms_mms_-_global_caribbean_netherlands_multiplier"></td><td id="sms_mms_-_global_caribbean_netherlands_credit"></td><td id="sms_mms_-_global_caribbean_netherlands_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_cayman_islands_ratio"></td><td>Ilhas Cayman</td><td id="sms_mms_-_global_cayman_islands_multiplier"></td><td id="sms_mms_-_global_cayman_islands_credit"></td><td id="sms_mms_-_global_cayman_islands_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_central_african_republic_ratio"></td><td>República Centro-Africana</td><td id="sms_mms_-_global_central_african_republic_multiplier"></td><td id="sms_mms_-_global_central_african_republic_credit"></td><td id="sms_mms_-_global_central_african_republic_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_chad_ratio"></td><td>Chade</td><td id="sms_mms_-_global_chad_multiplier"></td><td id="sms_mms_-_global_chad_credit"></td><td id="sms_mms_-_global_chad_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_chile_ratio"></td><td>Chile</td><td id="sms_mms_-_global_chile_multiplier"></td><td id="sms_mms_-_global_chile_credit"></td><td id="sms_mms_-_global_chile_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_china_ratio"></td><td>China</td><td id="sms_mms_-_global_china_multiplier"></td><td id="sms_mms_-_global_china_credit"></td><td id="sms_mms_-_global_china_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_colombia_ratio"></td><td>Colômbia</td><td id="sms_mms_-_global_colombia_multiplier"></td><td id="sms_mms_-_global_colombia_credit"></td><td id="sms_mms_-_global_colombia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_comoros_ratio"></td><td>Comores</td><td id="sms_mms_-_global_comoros_multiplier"></td><td id="sms_mms_-_global_comoros_credit"></td><td id="sms_mms_-_global_comoros_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_congo_ratio"></td><td>Congo</td><td id="sms_mms_-_global_congo_multiplier"></td><td id="sms_mms_-_global_congo_credit"></td><td id="sms_mms_-_global_congo_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_cook_islands_ratio"></td><td>Ilhas Cook</td><td id="sms_mms_-_global_cook_islands_multiplier"></td><td id="sms_mms_-_global_cook_islands_credit"></td><td id="sms_mms_-_global_cook_islands_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_costa_rica_ratio"></td><td>Costa Rica</td><td id="sms_mms_-_global_costa_rica_multiplier"></td><td id="sms_mms_-_global_costa_rica_credit"></td><td id="sms_mms_-_global_costa_rica_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_croatia_ratio"></td><td>Croácia</td><td id="sms_mms_-_global_croatia_multiplier"></td><td id="sms_mms_-_global_croatia_credit"></td><td id="sms_mms_-_global_croatia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_cuba_ratio"></td><td>Cuba</td><td id="sms_mms_-_global_cuba_multiplier"></td><td id="sms_mms_-_global_cuba_credit"></td><td id="sms_mms_-_global_cuba_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_curacao_ratio"></td><td>Curaçao</td><td id="sms_mms_-_global_curacao_multiplier"></td><td id="sms_mms_-_global_curacao_credit"></td><td id="sms_mms_-_global_curacao_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_cyprus_ratio"></td><td>Chipre</td><td id="sms_mms_-_global_cyprus_multiplier"></td><td id="sms_mms_-_global_cyprus_credit"></td><td id="sms_mms_-_global_cyprus_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_czech_republic_ratio"></td><td>República Tcheca</td><td id="sms_mms_-_global_czech_republic_multiplier"></td><td id="sms_mms_-_global_czech_republic_credit"></td><td id="sms_mms_-_global_czech_republic_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_denmark_ratio"></td><td>Dinamarca</td><td id="sms_mms_-_global_denmark_multiplier"></td><td id="sms_mms_-_global_denmark_credit"></td><td id="sms_mms_-_global_denmark_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_djibouti_ratio"></td><td>Djibuti</td><td id="sms_mms_-_global_djibouti_multiplier"></td><td id="sms_mms_-_global_djibouti_credit"></td><td id="sms_mms_-_global_djibouti_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_dominica_ratio"></td><td>Dominica</td><td id="sms_mms_-_global_dominica_multiplier"></td><td id="sms_mms_-_global_dominica_credit"></td><td id="sms_mms_-_global_dominica_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_dominican_republic_ratio"></td><td>República Dominicana</td><td id="sms_mms_-_global_dominican_republic_multiplier"></td><td id="sms_mms_-_global_dominican_republic_credit"></td><td id="sms_mms_-_global_dominican_republic_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_dr_congo_ratio"></td><td>RD Congo</td><td id="sms_mms_-_global_dr_congo_multiplier"></td><td id="sms_mms_-_global_dr_congo_credit"></td><td id="sms_mms_-_global_dr_congo_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_ecuador_ratio"></td><td>Equador</td><td id="sms_mms_-_global_ecuador_multiplier"></td><td id="sms_mms_-_global_ecuador_credit"></td><td id="sms_mms_-_global_ecuador_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_egypt_ratio"></td><td>Egito</td><td id="sms_mms_-_global_egypt_multiplier"></td><td id="sms_mms_-_global_egypt_credit"></td><td id="sms_mms_-_global_egypt_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_el_salvador_ratio"></td><td>El Salvador</td><td id="sms_mms_-_global_el_salvador_multiplier"></td><td id="sms_mms_-_global_el_salvador_credit"></td><td id="sms_mms_-_global_el_salvador_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_equatorial_guinea_ratio"></td><td>Guiné Equatorial</td><td id="sms_mms_-_global_equatorial_guinea_multiplier"></td><td id="sms_mms_-_global_equatorial_guinea_credit"></td><td id="sms_mms_-_global_equatorial_guinea_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_eritrea_ratio"></td><td>Eritreia</td><td id="sms_mms_-_global_eritrea_multiplier"></td><td id="sms_mms_-_global_eritrea_credit"></td><td id="sms_mms_-_global_eritrea_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_estonia_ratio"></td><td>Estônia</td><td id="sms_mms_-_global_estonia_multiplier"></td><td id="sms_mms_-_global_estonia_credit"></td><td id="sms_mms_-_global_estonia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_eswatini_ratio"></td><td>Eswatini</td><td id="sms_mms_-_global_eswatini_multiplier"></td><td id="sms_mms_-_global_eswatini_credit"></td><td id="sms_mms_-_global_eswatini_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_ethiopia_ratio"></td><td>Etiópia</td><td id="sms_mms_-_global_ethiopia_multiplier"></td><td id="sms_mms_-_global_ethiopia_credit"></td><td id="sms_mms_-_global_ethiopia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_falkland_islands_ratio"></td><td>Ilhas Malvinas</td><td id="sms_mms_-_global_falkland_islands_multiplier"></td><td id="sms_mms_-_global_falkland_islands_credit"></td><td id="sms_mms_-_global_falkland_islands_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_faroe_islands_ratio"></td><td>Ilhas Faroé</td><td id="sms_mms_-_global_faroe_islands_multiplier"></td><td id="sms_mms_-_global_faroe_islands_credit"></td><td id="sms_mms_-_global_faroe_islands_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_fiji_ratio"></td><td>Fiji</td><td id="sms_mms_-_global_fiji_multiplier"></td><td id="sms_mms_-_global_fiji_credit"></td><td id="sms_mms_-_global_fiji_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_finland_ratio"></td><td>Finlândia</td><td id="sms_mms_-_global_finland_multiplier"></td><td id="sms_mms_-_global_finland_credit"></td><td id="sms_mms_-_global_finland_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_france_ratio"></td><td>França</td><td id="sms_mms_-_global_france_multiplier"></td><td id="sms_mms_-_global_france_credit"></td><td id="sms_mms_-_global_france_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_french_guiana_ratio"></td><td>Guiana Francesa</td><td id="sms_mms_-_global_french_guiana_multiplier"></td><td id="sms_mms_-_global_french_guiana_credit"></td><td id="sms_mms_-_global_french_guiana_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_french_polynesia_ratio"></td><td>Polinésia Francesa</td><td id="sms_mms_-_global_french_polynesia_multiplier"></td><td id="sms_mms_-_global_french_polynesia_credit"></td><td id="sms_mms_-_global_french_polynesia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_gabon_ratio"></td><td>Gabão</td><td id="sms_mms_-_global_gabon_multiplier"></td><td id="sms_mms_-_global_gabon_credit"></td><td id="sms_mms_-_global_gabon_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_gambia_ratio"></td><td>Gâmbia</td><td id="sms_mms_-_global_gambia_multiplier"></td><td id="sms_mms_-_global_gambia_credit"></td><td id="sms_mms_-_global_gambia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_georgia_ratio"></td><td>Geórgia</td><td id="sms_mms_-_global_georgia_multiplier"></td><td id="sms_mms_-_global_georgia_credit"></td><td id="sms_mms_-_global_georgia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_germany_ratio"></td><td>Alemanha</td><td id="sms_mms_-_global_germany_multiplier"></td><td id="sms_mms_-_global_germany_credit"></td><td id="sms_mms_-_global_germany_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_ghana_ratio"></td><td>Gana</td><td id="sms_mms_-_global_ghana_multiplier"></td><td id="sms_mms_-_global_ghana_credit"></td><td id="sms_mms_-_global_ghana_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_gibraltar_ratio"></td><td>Gibraltar</td><td id="sms_mms_-_global_gibraltar_multiplier"></td><td id="sms_mms_-_global_gibraltar_credit"></td><td id="sms_mms_-_global_gibraltar_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_greece_ratio"></td><td>Grécia</td><td id="sms_mms_-_global_greece_multiplier"></td><td id="sms_mms_-_global_greece_credit"></td><td id="sms_mms_-_global_greece_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_greenland_ratio"></td><td>Groenlândia</td><td id="sms_mms_-_global_greenland_multiplier"></td><td id="sms_mms_-_global_greenland_credit"></td><td id="sms_mms_-_global_greenland_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_grenada_ratio"></td><td>Granada</td><td id="sms_mms_-_global_grenada_multiplier"></td><td id="sms_mms_-_global_grenada_credit"></td><td id="sms_mms_-_global_grenada_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_guadeloupe_ratio"></td><td>Guadalupe</td><td id="sms_mms_-_global_guadeloupe_multiplier"></td><td id="sms_mms_-_global_guadeloupe_credit"></td><td id="sms_mms_-_global_guadeloupe_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_guam_ratio"></td><td>Guam</td><td id="sms_mms_-_global_guam_multiplier"></td><td id="sms_mms_-_global_guam_credit"></td><td id="sms_mms_-_global_guam_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_guatemala_ratio"></td><td>Guatemala</td><td id="sms_mms_-_global_guatemala_multiplier"></td><td id="sms_mms_-_global_guatemala_credit"></td><td id="sms_mms_-_global_guatemala_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_guernsey_ratio"></td><td>Guernsey</td><td id="sms_mms_-_global_guernsey_multiplier"></td><td id="sms_mms_-_global_guernsey_credit"></td><td id="sms_mms_-_global_guernsey_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_guinea_ratio"></td><td>Guiné</td><td id="sms_mms_-_global_guinea_multiplier"></td><td id="sms_mms_-_global_guinea_credit"></td><td id="sms_mms_-_global_guinea_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_guinea-bissau_ratio"></td><td>Guiné-Bissau</td><td id="sms_mms_-_global_guinea-bissau_multiplier"></td><td id="sms_mms_-_global_guinea-bissau_credit"></td><td id="sms_mms_-_global_guinea-bissau_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_guyana_ratio"></td><td>Guiana</td><td id="sms_mms_-_global_guyana_multiplier"></td><td id="sms_mms_-_global_guyana_credit"></td><td id="sms_mms_-_global_guyana_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_haiti_ratio"></td><td>Haiti</td><td id="sms_mms_-_global_haiti_multiplier"></td><td id="sms_mms_-_global_haiti_credit"></td><td id="sms_mms_-_global_haiti_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_honduras_ratio"></td><td>Honduras</td><td id="sms_mms_-_global_honduras_multiplier"></td><td id="sms_mms_-_global_honduras_credit"></td><td id="sms_mms_-_global_honduras_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_hong_kong_ratio"></td><td>Hong Kong</td><td id="sms_mms_-_global_hong_kong_multiplier"></td><td id="sms_mms_-_global_hong_kong_credit"></td><td id="sms_mms_-_global_hong_kong_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_hungary_ratio"></td><td>Hungria</td><td id="sms_mms_-_global_hungary_multiplier"></td><td id="sms_mms_-_global_hungary_credit"></td><td id="sms_mms_-_global_hungary_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_iceland_ratio"></td><td>Islândia</td><td id="sms_mms_-_global_iceland_multiplier"></td><td id="sms_mms_-_global_iceland_credit"></td><td id="sms_mms_-_global_iceland_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_india_ratio"></td><td>Índia</td><td id="sms_mms_-_global_india_multiplier"></td><td id="sms_mms_-_global_india_credit"></td><td id="sms_mms_-_global_india_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_indonesia_ratio"></td><td>Indonésia</td><td id="sms_mms_-_global_indonesia_multiplier"></td><td id="sms_mms_-_global_indonesia_credit"></td><td id="sms_mms_-_global_indonesia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_iran_ratio"></td><td>Irã</td><td id="sms_mms_-_global_iran_multiplier"></td><td id="sms_mms_-_global_iran_credit"></td><td id="sms_mms_-_global_iran_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_iraq_ratio"></td><td>Iraque</td><td id="sms_mms_-_global_iraq_multiplier"></td><td id="sms_mms_-_global_iraq_credit"></td><td id="sms_mms_-_global_iraq_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_ireland_ratio"></td><td>Irlanda</td><td id="sms_mms_-_global_ireland_multiplier"></td><td id="sms_mms_-_global_ireland_credit"></td><td id="sms_mms_-_global_ireland_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_isle_of_man_ratio"></td><td>Ilha de Man</td><td id="sms_mms_-_global_isle_of_man_multiplier"></td><td id="sms_mms_-_global_isle_of_man_credit"></td><td id="sms_mms_-_global_isle_of_man_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_israel_ratio"></td><td>Israel</td><td id="sms_mms_-_global_israel_multiplier"></td><td id="sms_mms_-_global_israel_credit"></td><td id="sms_mms_-_global_israel_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_italy_ratio"></td><td>Itália</td><td id="sms_mms_-_global_italy_multiplier"></td><td id="sms_mms_-_global_italy_credit"></td><td id="sms_mms_-_global_italy_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_ivory_coast_ratio"></td><td>Costa do Marfim</td><td id="sms_mms_-_global_ivory_coast_multiplier"></td><td id="sms_mms_-_global_ivory_coast_credit"></td><td id="sms_mms_-_global_ivory_coast_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_jamaica_ratio"></td><td>Jamaica</td><td id="sms_mms_-_global_jamaica_multiplier"></td><td id="sms_mms_-_global_jamaica_credit"></td><td id="sms_mms_-_global_jamaica_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_japan_ratio"></td><td>Japão</td><td id="sms_mms_-_global_japan_multiplier"></td><td id="sms_mms_-_global_japan_credit"></td><td id="sms_mms_-_global_japan_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_jersey_ratio"></td><td>Jersey</td><td id="sms_mms_-_global_jersey_multiplier"></td><td id="sms_mms_-_global_jersey_credit"></td><td id="sms_mms_-_global_jersey_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_jordan_ratio"></td><td>Jordânia</td><td id="sms_mms_-_global_jordan_multiplier"></td><td id="sms_mms_-_global_jordan_credit"></td><td id="sms_mms_-_global_jordan_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_kazakhstan_ratio"></td><td>Cazaquistão</td><td id="sms_mms_-_global_kazakhstan_multiplier"></td><td id="sms_mms_-_global_kazakhstan_credit"></td><td id="sms_mms_-_global_kazakhstan_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_kenya_ratio"></td><td>Quênia</td><td id="sms_mms_-_global_kenya_multiplier"></td><td id="sms_mms_-_global_kenya_credit"></td><td id="sms_mms_-_global_kenya_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_kiribati_ratio"></td><td>Kiribati</td><td id="sms_mms_-_global_kiribati_multiplier"></td><td id="sms_mms_-_global_kiribati_credit"></td><td id="sms_mms_-_global_kiribati_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_korea_republic_of_ratio"></td><td>República da Coreia</td><td id="sms_mms_-_global_korea_republic_of_multiplier"></td><td id="sms_mms_-_global_korea_republic_of_credit"></td><td id="sms_mms_-_global_korea_republic_of_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_kosovo_ratio"></td><td>Kosovo</td><td id="sms_mms_-_global_kosovo_multiplier"></td><td id="sms_mms_-_global_kosovo_credit"></td><td id="sms_mms_-_global_kosovo_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_kuwait_ratio"></td><td>Kuwait</td><td id="sms_mms_-_global_kuwait_multiplier"></td><td id="sms_mms_-_global_kuwait_credit"></td><td id="sms_mms_-_global_kuwait_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_kyrgyzstan_ratio"></td><td>Quirguistão</td><td id="sms_mms_-_global_kyrgyzstan_multiplier"></td><td id="sms_mms_-_global_kyrgyzstan_credit"></td><td id="sms_mms_-_global_kyrgyzstan_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_laos_pdr_ratio"></td><td>Laos RDP</td><td id="sms_mms_-_global_laos_pdr_multiplier"></td><td id="sms_mms_-_global_laos_pdr_credit"></td><td id="sms_mms_-_global_laos_pdr_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_latvia_ratio"></td><td>Letônia</td><td id="sms_mms_-_global_latvia_multiplier"></td><td id="sms_mms_-_global_latvia_credit"></td><td id="sms_mms_-_global_latvia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_lebanon_ratio"></td><td>Líbano</td><td id="sms_mms_-_global_lebanon_multiplier"></td><td id="sms_mms_-_global_lebanon_credit"></td><td id="sms_mms_-_global_lebanon_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_lesotho_ratio"></td><td>Lesoto</td><td id="sms_mms_-_global_lesotho_multiplier"></td><td id="sms_mms_-_global_lesotho_credit"></td><td id="sms_mms_-_global_lesotho_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_liberia_ratio"></td><td>Libéria</td><td id="sms_mms_-_global_liberia_multiplier"></td><td id="sms_mms_-_global_liberia_credit"></td><td id="sms_mms_-_global_liberia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_libya_ratio"></td><td>Líbia</td><td id="sms_mms_-_global_libya_multiplier"></td><td id="sms_mms_-_global_libya_credit"></td><td id="sms_mms_-_global_libya_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_liechtenstein_ratio"></td><td>Liechtenstein</td><td id="sms_mms_-_global_liechtenstein_multiplier"></td><td id="sms_mms_-_global_liechtenstein_credit"></td><td id="sms_mms_-_global_liechtenstein_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_lithuania_ratio"></td><td>Lituânia</td><td id="sms_mms_-_global_lithuania_multiplier"></td><td id="sms_mms_-_global_lithuania_credit"></td><td id="sms_mms_-_global_lithuania_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_luxembourg_ratio"></td><td>Luxemburgo</td><td id="sms_mms_-_global_luxembourg_multiplier"></td><td id="sms_mms_-_global_luxembourg_credit"></td><td id="sms_mms_-_global_luxembourg_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_macao_ratio"></td><td>Macau</td><td id="sms_mms_-_global_macao_multiplier"></td><td id="sms_mms_-_global_macao_credit"></td><td id="sms_mms_-_global_macao_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_macedonia_ratio"></td><td>Macedônia</td><td id="sms_mms_-_global_macedonia_multiplier"></td><td id="sms_mms_-_global_macedonia_credit"></td><td id="sms_mms_-_global_macedonia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_madagascar_ratio"></td><td>Madagascar</td><td id="sms_mms_-_global_madagascar_multiplier"></td><td id="sms_mms_-_global_madagascar_credit"></td><td id="sms_mms_-_global_madagascar_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_malawi_ratio"></td><td>Malawi</td><td id="sms_mms_-_global_malawi_multiplier"></td><td id="sms_mms_-_global_malawi_credit"></td><td id="sms_mms_-_global_malawi_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_malaysia_ratio"></td><td>Malásia</td><td id="sms_mms_-_global_malaysia_multiplier"></td><td id="sms_mms_-_global_malaysia_credit"></td><td id="sms_mms_-_global_malaysia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_maldives_ratio"></td><td>Maldivas</td><td id="sms_mms_-_global_maldives_multiplier"></td><td id="sms_mms_-_global_maldives_credit"></td><td id="sms_mms_-_global_maldives_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_mali_ratio"></td><td>Mali</td><td id="sms_mms_-_global_mali_multiplier"></td><td id="sms_mms_-_global_mali_credit"></td><td id="sms_mms_-_global_mali_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_malta_ratio"></td><td>Malta</td><td id="sms_mms_-_global_malta_multiplier"></td><td id="sms_mms_-_global_malta_credit"></td><td id="sms_mms_-_global_malta_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_marshall_islands_ratio"></td><td>Ilhas Marshall</td><td id="sms_mms_-_global_marshall_islands_multiplier"></td><td id="sms_mms_-_global_marshall_islands_credit"></td><td id="sms_mms_-_global_marshall_islands_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_martinique_ratio"></td><td>Martinica</td><td id="sms_mms_-_global_martinique_multiplier"></td><td id="sms_mms_-_global_martinique_credit"></td><td id="sms_mms_-_global_martinique_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_mauritania_ratio"></td><td>Mauritânia</td><td id="sms_mms_-_global_mauritania_multiplier"></td><td id="sms_mms_-_global_mauritania_credit"></td><td id="sms_mms_-_global_mauritania_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_mauritius_ratio"></td><td>Maurício</td><td id="sms_mms_-_global_mauritius_multiplier"></td><td id="sms_mms_-_global_mauritius_credit"></td><td id="sms_mms_-_global_mauritius_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_mayotte_ratio"></td><td>Mayotte</td><td id="sms_mms_-_global_mayotte_multiplier"></td><td id="sms_mms_-_global_mayotte_credit"></td><td id="sms_mms_-_global_mayotte_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_mexico_ratio"></td><td>México</td><td id="sms_mms_-_global_mexico_multiplier"></td><td id="sms_mms_-_global_mexico_credit"></td><td id="sms_mms_-_global_mexico_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_micronesia_ratio"></td><td>Micronésia</td><td id="sms_mms_-_global_micronesia_multiplier"></td><td id="sms_mms_-_global_micronesia_credit"></td><td id="sms_mms_-_global_micronesia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_moldova_ratio"></td><td>Moldávia</td><td id="sms_mms_-_global_moldova_multiplier"></td><td id="sms_mms_-_global_moldova_credit"></td><td id="sms_mms_-_global_moldova_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_monaco_ratio"></td><td>Mônaco</td><td id="sms_mms_-_global_monaco_multiplier"></td><td id="sms_mms_-_global_monaco_credit"></td><td id="sms_mms_-_global_monaco_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_mongolia_ratio"></td><td>Mongólia</td><td id="sms_mms_-_global_mongolia_multiplier"></td><td id="sms_mms_-_global_mongolia_credit"></td><td id="sms_mms_-_global_mongolia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_montenegro_ratio"></td><td>Montenegro</td><td id="sms_mms_-_global_montenegro_multiplier"></td><td id="sms_mms_-_global_montenegro_credit"></td><td id="sms_mms_-_global_montenegro_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_montserrat_ratio"></td><td>Montserrat</td><td id="sms_mms_-_global_montserrat_multiplier"></td><td id="sms_mms_-_global_montserrat_credit"></td><td id="sms_mms_-_global_montserrat_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_morocco_ratio"></td><td>Marrocos</td><td id="sms_mms_-_global_morocco_multiplier"></td><td id="sms_mms_-_global_morocco_credit"></td><td id="sms_mms_-_global_morocco_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_mozambique_ratio"></td><td>Moçambique</td><td id="sms_mms_-_global_mozambique_multiplier"></td><td id="sms_mms_-_global_mozambique_credit"></td><td id="sms_mms_-_global_mozambique_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_myanmar_ratio"></td><td>Mianmar</td><td id="sms_mms_-_global_myanmar_multiplier"></td><td id="sms_mms_-_global_myanmar_credit"></td><td id="sms_mms_-_global_myanmar_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_namibia_ratio"></td><td>Namíbia</td><td id="sms_mms_-_global_namibia_multiplier"></td><td id="sms_mms_-_global_namibia_credit"></td><td id="sms_mms_-_global_namibia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_nauru_ratio"></td><td>Nauru</td><td id="sms_mms_-_global_nauru_multiplier"></td><td id="sms_mms_-_global_nauru_credit"></td><td id="sms_mms_-_global_nauru_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_nepal_ratio"></td><td>Nepal</td><td id="sms_mms_-_global_nepal_multiplier"></td><td id="sms_mms_-_global_nepal_credit"></td><td id="sms_mms_-_global_nepal_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_netherlands_ratio"></td><td>Países Baixos</td><td id="sms_mms_-_global_netherlands_multiplier"></td><td id="sms_mms_-_global_netherlands_credit"></td><td id="sms_mms_-_global_netherlands_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_new_caledonia_ratio"></td><td>Nova Caledônia</td><td id="sms_mms_-_global_new_caledonia_multiplier"></td><td id="sms_mms_-_global_new_caledonia_credit"></td><td id="sms_mms_-_global_new_caledonia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_new_zealand_ratio"></td><td>Nova Zelândia</td><td id="sms_mms_-_global_new_zealand_multiplier"></td><td id="sms_mms_-_global_new_zealand_credit"></td><td id="sms_mms_-_global_new_zealand_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_nicaragua_ratio"></td><td>Nicarágua</td><td id="sms_mms_-_global_nicaragua_multiplier"></td><td id="sms_mms_-_global_nicaragua_credit"></td><td id="sms_mms_-_global_nicaragua_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_niger_ratio"></td><td>Níger</td><td id="sms_mms_-_global_niger_multiplier"></td><td id="sms_mms_-_global_niger_credit"></td><td id="sms_mms_-_global_niger_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_nigeria_ratio"></td><td>Nigéria</td><td id="sms_mms_-_global_nigeria_multiplier"></td><td id="sms_mms_-_global_nigeria_credit"></td><td id="sms_mms_-_global_nigeria_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_niue_ratio"></td><td>Niue</td><td id="sms_mms_-_global_niue_multiplier"></td><td id="sms_mms_-_global_niue_credit"></td><td id="sms_mms_-_global_niue_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_norfolk_island_ratio"></td><td>Ilha Norfolk</td><td id="sms_mms_-_global_norfolk_island_multiplier"></td><td id="sms_mms_-_global_norfolk_island_credit"></td><td id="sms_mms_-_global_norfolk_island_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_north_macedonia_ratio"></td><td>Macedônia do Norte</td><td id="sms_mms_-_global_north_macedonia_multiplier"></td><td id="sms_mms_-_global_north_macedonia_credit"></td><td id="sms_mms_-_global_north_macedonia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_northern_cyprus_ratio"></td><td>Chipre do Norte</td><td id="sms_mms_-_global_northern_cyprus_multiplier"></td><td id="sms_mms_-_global_northern_cyprus_credit"></td><td id="sms_mms_-_global_northern_cyprus_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_norway_ratio"></td><td>Noruega</td><td id="sms_mms_-_global_norway_multiplier"></td><td id="sms_mms_-_global_norway_credit"></td><td id="sms_mms_-_global_norway_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_oman_ratio"></td><td>Omã</td><td id="sms_mms_-_global_oman_multiplier"></td><td id="sms_mms_-_global_oman_credit"></td><td id="sms_mms_-_global_oman_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_pakistan_ratio"></td><td>Paquistão</td><td id="sms_mms_-_global_pakistan_multiplier"></td><td id="sms_mms_-_global_pakistan_credit"></td><td id="sms_mms_-_global_pakistan_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_palau_ratio"></td><td>Palau</td><td id="sms_mms_-_global_palau_multiplier"></td><td id="sms_mms_-_global_palau_credit"></td><td id="sms_mms_-_global_palau_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_palestinian_territory_ratio"></td><td>Território Palestino</td><td id="sms_mms_-_global_palestinian_territory_multiplier"></td><td id="sms_mms_-_global_palestinian_territory_credit"></td><td id="sms_mms_-_global_palestinian_territory_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_panama_ratio"></td><td>Panamá</td><td id="sms_mms_-_global_panama_multiplier"></td><td id="sms_mms_-_global_panama_credit"></td><td id="sms_mms_-_global_panama_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_papua_new_guinea_ratio"></td><td>Papua-Nova Guiné</td><td id="sms_mms_-_global_papua_new_guinea_multiplier"></td><td id="sms_mms_-_global_papua_new_guinea_credit"></td><td id="sms_mms_-_global_papua_new_guinea_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_paraguay_ratio"></td><td>Paraguai</td><td id="sms_mms_-_global_paraguay_multiplier"></td><td id="sms_mms_-_global_paraguay_credit"></td><td id="sms_mms_-_global_paraguay_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_peru_ratio"></td><td>Peru</td><td id="sms_mms_-_global_peru_multiplier"></td><td id="sms_mms_-_global_peru_credit"></td><td id="sms_mms_-_global_peru_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_philippines_ratio"></td><td>Filipinas</td><td id="sms_mms_-_global_philippines_multiplier"></td><td id="sms_mms_-_global_philippines_credit"></td><td id="sms_mms_-_global_philippines_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_poland_ratio"></td><td>Polônia</td><td id="sms_mms_-_global_poland_multiplier"></td><td id="sms_mms_-_global_poland_credit"></td><td id="sms_mms_-_global_poland_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_portugal_ratio"></td><td>Portugal</td><td id="sms_mms_-_global_portugal_multiplier"></td><td id="sms_mms_-_global_portugal_credit"></td><td id="sms_mms_-_global_portugal_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_puerto_rico_ratio"></td><td>Porto Rico</td><td id="sms_mms_-_global_puerto_rico_multiplier"></td><td id="sms_mms_-_global_puerto_rico_credit"></td><td id="sms_mms_-_global_puerto_rico_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_qatar_ratio"></td><td>Catar</td><td id="sms_mms_-_global_qatar_multiplier"></td><td id="sms_mms_-_global_qatar_credit"></td><td id="sms_mms_-_global_qatar_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_reunion-mayotte_ratio"></td><td>Reunião/Mayotte</td><td id="sms_mms_-_global_reunion-mayotte_multiplier"></td><td id="sms_mms_-_global_reunion-mayotte_credit"></td><td id="sms_mms_-_global_reunion-mayotte_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_romania_ratio"></td><td>Romênia</td><td id="sms_mms_-_global_romania_multiplier"></td><td id="sms_mms_-_global_romania_credit"></td><td id="sms_mms_-_global_romania_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_russia_ratio"></td><td>Rússia</td><td id="sms_mms_-_global_russia_multiplier"></td><td id="sms_mms_-_global_russia_credit"></td><td id="sms_mms_-_global_russia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_rwanda_ratio"></td><td>Ruanda</td><td id="sms_mms_-_global_rwanda_multiplier"></td><td id="sms_mms_-_global_rwanda_credit"></td><td id="sms_mms_-_global_rwanda_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_saint_kitts_and_nevis_ratio"></td><td>São Cristóvão e Névis</td><td id="sms_mms_-_global_saint_kitts_and_nevis_multiplier"></td><td id="sms_mms_-_global_saint_kitts_and_nevis_credit"></td><td id="sms_mms_-_global_saint_kitts_and_nevis_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_saint_lucia_ratio"></td><td>Santa Lúcia</td><td id="sms_mms_-_global_saint_lucia_multiplier"></td><td id="sms_mms_-_global_saint_lucia_credit"></td><td id="sms_mms_-_global_saint_lucia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_saint_pierre_and_miquelon_ratio"></td><td>São Pedro e Miquelão</td><td id="sms_mms_-_global_saint_pierre_and_miquelon_multiplier"></td><td id="sms_mms_-_global_saint_pierre_and_miquelon_credit"></td><td id="sms_mms_-_global_saint_pierre_and_miquelon_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_saint_vincent_and_the_grenadines_ratio"></td><td>São Vicente e Granadinas</td><td id="sms_mms_-_global_saint_vincent_and_the_grenadines_multiplier"></td><td id="sms_mms_-_global_saint_vincent_and_the_grenadines_credit"></td><td id="sms_mms_-_global_saint_vincent_and_the_grenadines_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_samoa_ratio"></td><td>Samoa</td><td id="sms_mms_-_global_samoa_multiplier"></td><td id="sms_mms_-_global_samoa_credit"></td><td id="sms_mms_-_global_samoa_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_san_marino_ratio"></td><td>San Marino</td><td id="sms_mms_-_global_san_marino_multiplier"></td><td id="sms_mms_-_global_san_marino_credit"></td><td id="sms_mms_-_global_san_marino_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_sao_tome_and_principe_ratio"></td><td>São Tomé e Príncipe</td><td id="sms_mms_-_global_sao_tome_and_principe_multiplier"></td><td id="sms_mms_-_global_sao_tome_and_principe_credit"></td><td id="sms_mms_-_global_sao_tome_and_principe_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_saudi_arabia_ratio"></td><td>Arábia Saudita</td><td id="sms_mms_-_global_saudi_arabia_multiplier"></td><td id="sms_mms_-_global_saudi_arabia_credit"></td><td id="sms_mms_-_global_saudi_arabia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_senegal_ratio"></td><td>Senegal</td><td id="sms_mms_-_global_senegal_multiplier"></td><td id="sms_mms_-_global_senegal_credit"></td><td id="sms_mms_-_global_senegal_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_serbia_ratio"></td><td>Sérvia</td><td id="sms_mms_-_global_serbia_multiplier"></td><td id="sms_mms_-_global_serbia_credit"></td><td id="sms_mms_-_global_serbia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_seychelles_ratio"></td><td>Seychelles</td><td id="sms_mms_-_global_seychelles_multiplier"></td><td id="sms_mms_-_global_seychelles_credit"></td><td id="sms_mms_-_global_seychelles_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_sierra_leone_ratio"></td><td>Serra Leoa</td><td id="sms_mms_-_global_sierra_leone_multiplier"></td><td id="sms_mms_-_global_sierra_leone_credit"></td><td id="sms_mms_-_global_sierra_leone_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_singapore_ratio"></td><td>Singapura</td><td id="sms_mms_-_global_singapore_multiplier"></td><td id="sms_mms_-_global_singapore_credit"></td><td id="sms_mms_-_global_singapore_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_sint_maarten_ratio"></td><td>Sint Maarten</td><td id="sms_mms_-_global_sint_maarten_multiplier"></td><td id="sms_mms_-_global_sint_maarten_credit"></td><td id="sms_mms_-_global_sint_maarten_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_slovakia_ratio"></td><td>Eslováquia</td><td id="sms_mms_-_global_slovakia_multiplier"></td><td id="sms_mms_-_global_slovakia_credit"></td><td id="sms_mms_-_global_slovakia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_slovenia_ratio"></td><td>Eslovênia</td><td id="sms_mms_-_global_slovenia_multiplier"></td><td id="sms_mms_-_global_slovenia_credit"></td><td id="sms_mms_-_global_slovenia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_solomon_islands_ratio"></td><td>Ilhas Salomão</td><td id="sms_mms_-_global_solomon_islands_multiplier"></td><td id="sms_mms_-_global_solomon_islands_credit"></td><td id="sms_mms_-_global_solomon_islands_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_somalia_ratio"></td><td>Somália</td><td id="sms_mms_-_global_somalia_multiplier"></td><td id="sms_mms_-_global_somalia_credit"></td><td id="sms_mms_-_global_somalia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_south_africa_ratio"></td><td>África do Sul</td><td id="sms_mms_-_global_south_africa_multiplier"></td><td id="sms_mms_-_global_south_africa_credit"></td><td id="sms_mms_-_global_south_africa_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_south_ossetia_ratio"></td><td>Ossétia do Sul</td><td id="sms_mms_-_global_south_ossetia_multiplier"></td><td id="sms_mms_-_global_south_ossetia_credit"></td><td id="sms_mms_-_global_south_ossetia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_south_sudan_ratio"></td><td>Sudão do Sul</td><td id="sms_mms_-_global_south_sudan_multiplier"></td><td id="sms_mms_-_global_south_sudan_credit"></td><td id="sms_mms_-_global_south_sudan_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_spain_ratio"></td><td>Espanha</td><td id="sms_mms_-_global_spain_multiplier"></td><td id="sms_mms_-_global_spain_credit"></td><td id="sms_mms_-_global_spain_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_sri_lanka_ratio"></td><td>Sri Lanka</td><td id="sms_mms_-_global_sri_lanka_multiplier"></td><td id="sms_mms_-_global_sri_lanka_credit"></td><td id="sms_mms_-_global_sri_lanka_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_st_kitts_and_nevis_ratio"></td><td>St Kitts e Nevis</td><td id="sms_mms_-_global_st_kitts_and_nevis_multiplier"></td><td id="sms_mms_-_global_st_kitts_and_nevis_credit"></td><td id="sms_mms_-_global_st_kitts_and_nevis_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_st_lucia_ratio"></td><td>St Lucia</td><td id="sms_mms_-_global_st_lucia_multiplier"></td><td id="sms_mms_-_global_st_lucia_credit"></td><td id="sms_mms_-_global_st_lucia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_st_pierre_and_miquelon_ratio"></td><td>St Pierre e Miquelon</td><td id="sms_mms_-_global_st_pierre_and_miquelon_multiplier"></td><td id="sms_mms_-_global_st_pierre_and_miquelon_credit"></td><td id="sms_mms_-_global_st_pierre_and_miquelon_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_st_vincent_grenadines_ratio"></td><td>St Vincent Granadinas</td><td id="sms_mms_-_global_st_vincent_grenadines_multiplier"></td><td id="sms_mms_-_global_st_vincent_grenadines_credit"></td><td id="sms_mms_-_global_st_vincent_grenadines_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_sudan_ratio"></td><td>Sudão</td><td id="sms_mms_-_global_sudan_multiplier"></td><td id="sms_mms_-_global_sudan_credit"></td><td id="sms_mms_-_global_sudan_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_suriname_ratio"></td><td>Suriname</td><td id="sms_mms_-_global_suriname_multiplier"></td><td id="sms_mms_-_global_suriname_credit"></td><td id="sms_mms_-_global_suriname_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_swaziland_ratio"></td><td>Suazilândia</td><td id="sms_mms_-_global_swaziland_multiplier"></td><td id="sms_mms_-_global_swaziland_credit"></td><td id="sms_mms_-_global_swaziland_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_sweden_ratio"></td><td>Suécia</td><td id="sms_mms_-_global_sweden_multiplier"></td><td id="sms_mms_-_global_sweden_credit"></td><td id="sms_mms_-_global_sweden_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_switzerland_ratio"></td><td>Suíça</td><td id="sms_mms_-_global_switzerland_multiplier"></td><td id="sms_mms_-_global_switzerland_credit"></td><td id="sms_mms_-_global_switzerland_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_syria_ratio"></td><td>Síria</td><td id="sms_mms_-_global_syria_multiplier"></td><td id="sms_mms_-_global_syria_credit"></td><td id="sms_mms_-_global_syria_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_taiwan_ratio"></td><td>Taiwan</td><td id="sms_mms_-_global_taiwan_multiplier"></td><td id="sms_mms_-_global_taiwan_credit"></td><td id="sms_mms_-_global_taiwan_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_tajikistan_ratio"></td><td>Tajiquistão</td><td id="sms_mms_-_global_tajikistan_multiplier"></td><td id="sms_mms_-_global_tajikistan_credit"></td><td id="sms_mms_-_global_tajikistan_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_tanzania_ratio"></td><td>Tanzânia</td><td id="sms_mms_-_global_tanzania_multiplier"></td><td id="sms_mms_-_global_tanzania_credit"></td><td id="sms_mms_-_global_tanzania_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_thailand_ratio"></td><td>Tailândia</td><td id="sms_mms_-_global_thailand_multiplier"></td><td id="sms_mms_-_global_thailand_credit"></td><td id="sms_mms_-_global_thailand_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_timor-leste_ratio"></td><td>Timor-Leste</td><td id="sms_mms_-_global_timor-leste_multiplier"></td><td id="sms_mms_-_global_timor-leste_credit"></td><td id="sms_mms_-_global_timor-leste_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_togo_ratio"></td><td>Togo</td><td id="sms_mms_-_global_togo_multiplier"></td><td id="sms_mms_-_global_togo_credit"></td><td id="sms_mms_-_global_togo_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_tonga_ratio"></td><td>Tonga</td><td id="sms_mms_-_global_tonga_multiplier"></td><td id="sms_mms_-_global_tonga_credit"></td><td id="sms_mms_-_global_tonga_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_trinidad_and_tobago_ratio"></td><td>Trinidad e Tobago</td><td id="sms_mms_-_global_trinidad_and_tobago_multiplier"></td><td id="sms_mms_-_global_trinidad_and_tobago_credit"></td><td id="sms_mms_-_global_trinidad_and_tobago_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_tunisia_ratio"></td><td>Tunísia</td><td id="sms_mms_-_global_tunisia_multiplier"></td><td id="sms_mms_-_global_tunisia_credit"></td><td id="sms_mms_-_global_tunisia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_turkey_ratio"></td><td>Turquia</td><td id="sms_mms_-_global_turkey_multiplier"></td><td id="sms_mms_-_global_turkey_credit"></td><td id="sms_mms_-_global_turkey_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_turkmenistan_ratio"></td><td>Turcomenistão</td><td id="sms_mms_-_global_turkmenistan_multiplier"></td><td id="sms_mms_-_global_turkmenistan_credit"></td><td id="sms_mms_-_global_turkmenistan_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_turks_and_caicos_islands_ratio"></td><td>Ilhas Turks e Caicos</td><td id="sms_mms_-_global_turks_and_caicos_islands_multiplier"></td><td id="sms_mms_-_global_turks_and_caicos_islands_credit"></td><td id="sms_mms_-_global_turks_and_caicos_islands_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_tuvalu_ratio"></td><td>Tuvalu</td><td id="sms_mms_-_global_tuvalu_multiplier"></td><td id="sms_mms_-_global_tuvalu_credit"></td><td id="sms_mms_-_global_tuvalu_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_uganda_ratio"></td><td>Uganda</td><td id="sms_mms_-_global_uganda_multiplier"></td><td id="sms_mms_-_global_uganda_credit"></td><td id="sms_mms_-_global_uganda_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_ukraine_ratio"></td><td>Ucrânia</td><td id="sms_mms_-_global_ukraine_multiplier"></td><td id="sms_mms_-_global_ukraine_credit"></td><td id="sms_mms_-_global_ukraine_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_united_arab_emirates_ratio"></td><td>Emirados Árabes Unidos</td><td id="sms_mms_-_global_united_arab_emirates_multiplier"></td><td id="sms_mms_-_global_united_arab_emirates_credit"></td><td id="sms_mms_-_global_united_arab_emirates_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_united_kingdom_ratio"></td><td>Reino Unido</td><td id="sms_mms_-_global_united_kingdom_multiplier"></td><td id="sms_mms_-_global_united_kingdom_credit"></td><td id="sms_mms_-_global_united_kingdom_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_unknown_ratio"></td><td>Desconhecido</td><td id="sms_mms_-_global_unknown_multiplier"></td><td id="sms_mms_-_global_unknown_credit"></td><td id="sms_mms_-_global_unknown_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_uruguay_ratio"></td><td>Uruguai</td><td id="sms_mms_-_global_uruguay_multiplier"></td><td id="sms_mms_-_global_uruguay_credit"></td><td id="sms_mms_-_global_uruguay_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_uzbekistan_ratio"></td><td>Uzbequistão</td><td id="sms_mms_-_global_uzbekistan_multiplier"></td><td id="sms_mms_-_global_uzbekistan_credit"></td><td id="sms_mms_-_global_uzbekistan_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_vanuatu_ratio"></td><td>Vanuatu</td><td id="sms_mms_-_global_vanuatu_multiplier"></td><td id="sms_mms_-_global_vanuatu_credit"></td><td id="sms_mms_-_global_vanuatu_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_venezuela_ratio"></td><td>Venezuela</td><td id="sms_mms_-_global_venezuela_multiplier"></td><td id="sms_mms_-_global_venezuela_credit"></td><td id="sms_mms_-_global_venezuela_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_vietnam_ratio"></td><td>Vietnã</td><td id="sms_mms_-_global_vietnam_multiplier"></td><td id="sms_mms_-_global_vietnam_credit"></td><td id="sms_mms_-_global_vietnam_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_virgin_islands-_british_ratio"></td><td>Ilhas Virgens Britânicas</td><td id="sms_mms_-_global_virgin_islands-_british_multiplier"></td><td id="sms_mms_-_global_virgin_islands-_british_credit"></td><td id="sms_mms_-_global_virgin_islands-_british_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_virgin_islands-_us_ratio"></td><td>Ilhas Virgens Americanas</td><td id="sms_mms_-_global_virgin_islands-_us_multiplier"></td><td id="sms_mms_-_global_virgin_islands-_us_credit"></td><td id="sms_mms_-_global_virgin_islands-_us_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_wallis_and_futuna_ratio"></td><td>Wallis e Futuna</td><td id="sms_mms_-_global_wallis_and_futuna_multiplier"></td><td id="sms_mms_-_global_wallis_and_futuna_credit"></td><td id="sms_mms_-_global_wallis_and_futuna_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_yemen_ratio"></td><td>Iêmen</td><td id="sms_mms_-_global_yemen_multiplier"></td><td id="sms_mms_-_global_yemen_credit"></td><td id="sms_mms_-_global_yemen_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_zambia_ratio"></td><td>Zâmbia</td><td id="sms_mms_-_global_zambia_multiplier"></td><td id="sms_mms_-_global_zambia_credit"></td><td id="sms_mms_-_global_zambia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_zimbabwe_ratio"></td><td>Zimbábue</td><td id="sms_mms_-_global_zimbabwe_multiplier"></td><td id="sms_mms_-_global_zimbabwe_credit"></td><td id="sms_mms_-_global_zimbabwe_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_argentina_authentication_ratio"></td><td>Argentina Autenticação</td><td id="whatsapp_argentina_authentication_multiplier"></td><td id="whatsapp_argentina_authentication_credit"></td><td id="whatsapp_argentina_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_argentina_marketing_ratio"></td><td>Argentina Marketing</td><td id="whatsapp_argentina_marketing_multiplier"></td><td id="whatsapp_argentina_marketing_credit"></td><td id="whatsapp_argentina_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_argentina_service_ratio"></td><td>Argentina Atendimento</td><td id="whatsapp_argentina_service_multiplier"></td><td id="whatsapp_argentina_service_credit"></td><td id="whatsapp_argentina_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_argentina_utility_ratio"></td><td>Argentina Utilidade</td><td id="whatsapp_argentina_utility_multiplier"></td><td id="whatsapp_argentina_utility_credit"></td><td id="whatsapp_argentina_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_brazil_authentication_ratio"></td><td>Brasil Autenticação</td><td id="whatsapp_brazil_authentication_multiplier"></td><td id="whatsapp_brazil_authentication_credit"></td><td id="whatsapp_brazil_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_brazil_marketing_ratio"></td><td>Brasil Marketing</td><td id="whatsapp_brazil_marketing_multiplier"></td><td id="whatsapp_brazil_marketing_credit"></td><td id="whatsapp_brazil_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_brazil_service_ratio"></td><td>Brasil Atendimento</td><td id="whatsapp_brazil_service_multiplier"></td><td id="whatsapp_brazil_service_credit"></td><td id="whatsapp_brazil_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_brazil_utility_ratio"></td><td>Brasil Utilidade</td><td id="whatsapp_brazil_utility_multiplier"></td><td id="whatsapp_brazil_utility_credit"></td><td id="whatsapp_brazil_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_chile_authentication_ratio"></td><td>Chile Autenticação</td><td id="whatsapp_chile_authentication_multiplier"></td><td id="whatsapp_chile_authentication_credit"></td><td id="whatsapp_chile_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_chile_marketing_ratio"></td><td>Chile Marketing</td><td id="whatsapp_chile_marketing_multiplier"></td><td id="whatsapp_chile_marketing_credit"></td><td id="whatsapp_chile_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_chile_service_ratio"></td><td>Chile Atendimento</td><td id="whatsapp_chile_service_multiplier"></td><td id="whatsapp_chile_service_credit"></td><td id="whatsapp_chile_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_chile_utility_ratio"></td><td>Chile Utilidade</td><td id="whatsapp_chile_utility_multiplier"></td><td id="whatsapp_chile_utility_credit"></td><td id="whatsapp_chile_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_colombia_authentication_ratio"></td><td>Colômbia Autenticação</td><td id="whatsapp_colombia_authentication_multiplier"></td><td id="whatsapp_colombia_authentication_credit"></td><td id="whatsapp_colombia_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_colombia_marketing_ratio"></td><td>Colômbia Marketing</td><td id="whatsapp_colombia_marketing_multiplier"></td><td id="whatsapp_colombia_marketing_credit"></td><td id="whatsapp_colombia_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_colombia_service_ratio"></td><td>Colômbia Atendimento</td><td id="whatsapp_colombia_service_multiplier"></td><td id="whatsapp_colombia_service_credit"></td><td id="whatsapp_colombia_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_colombia_utility_ratio"></td><td>Colômbia Utilidade</td><td id="whatsapp_colombia_utility_multiplier"></td><td id="whatsapp_colombia_utility_credit"></td><td id="whatsapp_colombia_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_egypt_authentication_ratio"></td><td>Egito Autenticação</td><td id="whatsapp_egypt_authentication_multiplier"></td><td id="whatsapp_egypt_authentication_credit"></td><td id="whatsapp_egypt_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_egypt_marketing_ratio"></td><td>Egito Marketing</td><td id="whatsapp_egypt_marketing_multiplier"></td><td id="whatsapp_egypt_marketing_credit"></td><td id="whatsapp_egypt_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_egypt_service_ratio"></td><td>Egito Atendimento</td><td id="whatsapp_egypt_service_multiplier"></td><td id="whatsapp_egypt_service_credit"></td><td id="whatsapp_egypt_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_egypt_utility_ratio"></td><td>Egito Utilidade</td><td id="whatsapp_egypt_utility_multiplier"></td><td id="whatsapp_egypt_utility_credit"></td><td id="whatsapp_egypt_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_france_authentication_ratio"></td><td>França Autenticação</td><td id="whatsapp_france_authentication_multiplier"></td><td id="whatsapp_france_authentication_credit"></td><td id="whatsapp_france_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_france_marketing_ratio"></td><td>França Marketing</td><td id="whatsapp_france_marketing_multiplier"></td><td id="whatsapp_france_marketing_credit"></td><td id="whatsapp_france_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_france_service_ratio"></td><td>França Atendimento</td><td id="whatsapp_france_service_multiplier"></td><td id="whatsapp_france_service_credit"></td><td id="whatsapp_france_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_france_utility_ratio"></td><td>França Utilidade</td><td id="whatsapp_france_utility_multiplier"></td><td id="whatsapp_france_utility_credit"></td><td id="whatsapp_france_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_germany_authentication_ratio"></td><td>Alemanha Autenticação</td><td id="whatsapp_germany_authentication_multiplier"></td><td id="whatsapp_germany_authentication_credit"></td><td id="whatsapp_germany_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_germany_marketing_ratio"></td><td>Alemanha Marketing</td><td id="whatsapp_germany_marketing_multiplier"></td><td id="whatsapp_germany_marketing_credit"></td><td id="whatsapp_germany_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_germany_service_ratio"></td><td>Alemanha Atendimento</td><td id="whatsapp_germany_service_multiplier"></td><td id="whatsapp_germany_service_credit"></td><td id="whatsapp_germany_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_germany_utility_ratio"></td><td>Alemanha Utilidade</td><td id="whatsapp_germany_utility_multiplier"></td><td id="whatsapp_germany_utility_credit"></td><td id="whatsapp_germany_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_india_authentication_ratio"></td><td>Índia Autenticação</td><td id="whatsapp_india_authentication_multiplier"></td><td id="whatsapp_india_authentication_credit"></td><td id="whatsapp_india_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_india_marketing_ratio"></td><td>Índia Marketing</td><td id="whatsapp_india_marketing_multiplier"></td><td id="whatsapp_india_marketing_credit"></td><td id="whatsapp_india_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_india_service_ratio"></td><td>Índia Atendimento</td><td id="whatsapp_india_service_multiplier"></td><td id="whatsapp_india_service_credit"></td><td id="whatsapp_india_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_india_utility_ratio"></td><td>Índia Utilidade</td><td id="whatsapp_india_utility_multiplier"></td><td id="whatsapp_india_utility_credit"></td><td id="whatsapp_india_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_indonesia_authentication_ratio"></td><td>Indonésia Autenticação</td><td id="whatsapp_indonesia_authentication_multiplier"></td><td id="whatsapp_indonesia_authentication_credit"></td><td id="whatsapp_indonesia_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_indonesia_marketing_ratio"></td><td>Indonésia Marketing</td><td id="whatsapp_indonesia_marketing_multiplier"></td><td id="whatsapp_indonesia_marketing_credit"></td><td id="whatsapp_indonesia_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_indonesia_service_ratio"></td><td>Indonésia Atendimento</td><td id="whatsapp_indonesia_service_multiplier"></td><td id="whatsapp_indonesia_service_credit"></td><td id="whatsapp_indonesia_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_indonesia_utility_ratio"></td><td>Indonésia Utilidade</td><td id="whatsapp_indonesia_utility_multiplier"></td><td id="whatsapp_indonesia_utility_credit"></td><td id="whatsapp_indonesia_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_israel_authentication_ratio"></td><td>Israel Autenticação</td><td id="whatsapp_israel_authentication_multiplier"></td><td id="whatsapp_israel_authentication_credit"></td><td id="whatsapp_israel_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_israel_marketing_ratio"></td><td>Israel Marketing</td><td id="whatsapp_israel_marketing_multiplier"></td><td id="whatsapp_israel_marketing_credit"></td><td id="whatsapp_israel_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_israel_service_ratio"></td><td>Israel Atendimento</td><td id="whatsapp_israel_service_multiplier"></td><td id="whatsapp_israel_service_credit"></td><td id="whatsapp_israel_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_israel_utility_ratio"></td><td>Israel Utilidade</td><td id="whatsapp_israel_utility_multiplier"></td><td id="whatsapp_israel_utility_credit"></td><td id="whatsapp_israel_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_italy_authentication_ratio"></td><td>Itália Autenticação</td><td id="whatsapp_italy_authentication_multiplier"></td><td id="whatsapp_italy_authentication_credit"></td><td id="whatsapp_italy_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_italy_marketing_ratio"></td><td>Itália Marketing</td><td id="whatsapp_italy_marketing_multiplier"></td><td id="whatsapp_italy_marketing_credit"></td><td id="whatsapp_italy_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_italy_service_ratio"></td><td>Itália Atendimento</td><td id="whatsapp_italy_service_multiplier"></td><td id="whatsapp_italy_service_credit"></td><td id="whatsapp_italy_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_italy_utility_ratio"></td><td>Itália Utilidade</td><td id="whatsapp_italy_utility_multiplier"></td><td id="whatsapp_italy_utility_credit"></td><td id="whatsapp_italy_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_malaysia_authentication_ratio"></td><td>Malásia Autenticação</td><td id="whatsapp_malaysia_authentication_multiplier"></td><td id="whatsapp_malaysia_authentication_credit"></td><td id="whatsapp_malaysia_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_malaysia_marketing_ratio"></td><td>Malásia Marketing</td><td id="whatsapp_malaysia_marketing_multiplier"></td><td id="whatsapp_malaysia_marketing_credit"></td><td id="whatsapp_malaysia_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_malaysia_service_ratio"></td><td>Malásia Atendimento</td><td id="whatsapp_malaysia_service_multiplier"></td><td id="whatsapp_malaysia_service_credit"></td><td id="whatsapp_malaysia_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_malaysia_utility_ratio"></td><td>Malásia Utilidade</td><td id="whatsapp_malaysia_utility_multiplier"></td><td id="whatsapp_malaysia_utility_credit"></td><td id="whatsapp_malaysia_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_mexico_authentication_ratio"></td><td>México Autenticação</td><td id="whatsapp_mexico_authentication_multiplier"></td><td id="whatsapp_mexico_authentication_credit"></td><td id="whatsapp_mexico_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_mexico_marketing_ratio"></td><td>México Marketing</td><td id="whatsapp_mexico_marketing_multiplier"></td><td id="whatsapp_mexico_marketing_credit"></td><td id="whatsapp_mexico_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_mexico_service_ratio"></td><td>México Atendimento</td><td id="whatsapp_mexico_service_multiplier"></td><td id="whatsapp_mexico_service_credit"></td><td id="whatsapp_mexico_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_mexico_utility_ratio"></td><td>México Utilidade</td><td id="whatsapp_mexico_utility_multiplier"></td><td id="whatsapp_mexico_utility_credit"></td><td id="whatsapp_mexico_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_netherlands_authentication_ratio"></td><td>Países Baixos Autenticação</td><td id="whatsapp_netherlands_authentication_multiplier"></td><td id="whatsapp_netherlands_authentication_credit"></td><td id="whatsapp_netherlands_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_netherlands_marketing_ratio"></td><td>Países Baixos Marketing</td><td id="whatsapp_netherlands_marketing_multiplier"></td><td id="whatsapp_netherlands_marketing_credit"></td><td id="whatsapp_netherlands_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_netherlands_service_ratio"></td><td>Países Baixos Atendimento</td><td id="whatsapp_netherlands_service_multiplier"></td><td id="whatsapp_netherlands_service_credit"></td><td id="whatsapp_netherlands_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_netherlands_utility_ratio"></td><td>Países Baixos Utilidade</td><td id="whatsapp_netherlands_utility_multiplier"></td><td id="whatsapp_netherlands_utility_credit"></td><td id="whatsapp_netherlands_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_nigeria_authentication_ratio"></td><td>Nigéria Autenticação</td><td id="whatsapp_nigeria_authentication_multiplier"></td><td id="whatsapp_nigeria_authentication_credit"></td><td id="whatsapp_nigeria_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_nigeria_marketing_ratio"></td><td>Nigéria Marketing</td><td id="whatsapp_nigeria_marketing_multiplier"></td><td id="whatsapp_nigeria_marketing_credit"></td><td id="whatsapp_nigeria_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_nigeria_service_ratio"></td><td>Nigéria Atendimento</td><td id="whatsapp_nigeria_service_multiplier"></td><td id="whatsapp_nigeria_service_credit"></td><td id="whatsapp_nigeria_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_nigeria_utility_ratio"></td><td>Nigéria Utilidade</td><td id="whatsapp_nigeria_utility_multiplier"></td><td id="whatsapp_nigeria_utility_credit"></td><td id="whatsapp_nigeria_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_north_america_authentication_ratio"></td><td>América do Norte Autenticação</td><td id="whatsapp_north_america_authentication_multiplier"></td><td id="whatsapp_north_america_authentication_credit"></td><td id="whatsapp_north_america_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_north_america_marketing_ratio"></td><td>América do Norte Marketing</td><td id="whatsapp_north_america_marketing_multiplier"></td><td id="whatsapp_north_america_marketing_credit"></td><td id="whatsapp_north_america_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_north_america_service_ratio"></td><td>América do Norte Atendimento</td><td id="whatsapp_north_america_service_multiplier"></td><td id="whatsapp_north_america_service_credit"></td><td id="whatsapp_north_america_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_north_america_utility_ratio"></td><td>América do Norte Utilidade</td><td id="whatsapp_north_america_utility_multiplier"></td><td id="whatsapp_north_america_utility_credit"></td><td id="whatsapp_north_america_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_other_authentication_ratio"></td><td>Outros Autenticação</td><td id="whatsapp_other_authentication_multiplier"></td><td id="whatsapp_other_authentication_credit"></td><td id="whatsapp_other_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_other_marketing_ratio"></td><td>Outros Marketing</td><td id="whatsapp_other_marketing_multiplier"></td><td id="whatsapp_other_marketing_credit"></td><td id="whatsapp_other_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_other_service_ratio"></td><td>Outros Atendimento</td><td id="whatsapp_other_service_multiplier"></td><td id="whatsapp_other_service_credit"></td><td id="whatsapp_other_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_other_utility_ratio"></td><td>Outros Utilidade</td><td id="whatsapp_other_utility_multiplier"></td><td id="whatsapp_other_utility_credit"></td><td id="whatsapp_other_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_pakistan_authentication_ratio"></td><td>Paquistão Autenticação</td><td id="whatsapp_pakistan_authentication_multiplier"></td><td id="whatsapp_pakistan_authentication_credit"></td><td id="whatsapp_pakistan_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_pakistan_marketing_ratio"></td><td>Paquistão Marketing</td><td id="whatsapp_pakistan_marketing_multiplier"></td><td id="whatsapp_pakistan_marketing_credit"></td><td id="whatsapp_pakistan_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_pakistan_service_ratio"></td><td>Paquistão Atendimento</td><td id="whatsapp_pakistan_service_multiplier"></td><td id="whatsapp_pakistan_service_credit"></td><td id="whatsapp_pakistan_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_pakistan_utility_ratio"></td><td>Paquistão Utilidade</td><td id="whatsapp_pakistan_utility_multiplier"></td><td id="whatsapp_pakistan_utility_credit"></td><td id="whatsapp_pakistan_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_peru_authentication_ratio"></td><td>Peru Autenticação</td><td id="whatsapp_peru_authentication_multiplier"></td><td id="whatsapp_peru_authentication_credit"></td><td id="whatsapp_peru_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_peru_marketing_ratio"></td><td>Peru Marketing</td><td id="whatsapp_peru_marketing_multiplier"></td><td id="whatsapp_peru_marketing_credit"></td><td id="whatsapp_peru_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_peru_service_ratio"></td><td>Peru Atendimento</td><td id="whatsapp_peru_service_multiplier"></td><td id="whatsapp_peru_service_credit"></td><td id="whatsapp_peru_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_peru_utility_ratio"></td><td>Peru Utilidade</td><td id="whatsapp_peru_utility_multiplier"></td><td id="whatsapp_peru_utility_credit"></td><td id="whatsapp_peru_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_africa_authentication_ratio"></td><td>Restante da África Autenticação</td><td id="whatsapp_rest_of_africa_authentication_multiplier"></td><td id="whatsapp_rest_of_africa_authentication_credit"></td><td id="whatsapp_rest_of_africa_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_africa_marketing_ratio"></td><td>Restante da África Marketing</td><td id="whatsapp_rest_of_africa_marketing_multiplier"></td><td id="whatsapp_rest_of_africa_marketing_credit"></td><td id="whatsapp_rest_of_africa_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_africa_service_ratio"></td><td>Restante da África Atendimento</td><td id="whatsapp_rest_of_africa_service_multiplier"></td><td id="whatsapp_rest_of_africa_service_credit"></td><td id="whatsapp_rest_of_africa_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_africa_utility_ratio"></td><td>Restante da África Utilidade</td><td id="whatsapp_rest_of_africa_utility_multiplier"></td><td id="whatsapp_rest_of_africa_utility_credit"></td><td id="whatsapp_rest_of_africa_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_asia_pacific_authentication_ratio"></td><td>Restante da Ásia-Pacífico Autenticação</td><td id="whatsapp_rest_of_asia_pacific_authentication_multiplier"></td><td id="whatsapp_rest_of_asia_pacific_authentication_credit"></td><td id="whatsapp_rest_of_asia_pacific_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_asia_pacific_marketing_ratio"></td><td>Restante da Ásia-Pacífico Marketing</td><td id="whatsapp_rest_of_asia_pacific_marketing_multiplier"></td><td id="whatsapp_rest_of_asia_pacific_marketing_credit"></td><td id="whatsapp_rest_of_asia_pacific_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_asia_pacific_service_ratio"></td><td>Restante da Ásia-Pacífico Atendimento</td><td id="whatsapp_rest_of_asia_pacific_service_multiplier"></td><td id="whatsapp_rest_of_asia_pacific_service_credit"></td><td id="whatsapp_rest_of_asia_pacific_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_asia_pacific_utility_ratio"></td><td>Restante da Ásia-Pacífico Utilidade</td><td id="whatsapp_rest_of_asia_pacific_utility_multiplier"></td><td id="whatsapp_rest_of_asia_pacific_utility_credit"></td><td id="whatsapp_rest_of_asia_pacific_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_central_-_eastern_europe_authentication_ratio"></td><td>Restante da Europa Central e Oriental Autenticação</td><td id="whatsapp_rest_of_central_-_eastern_europe_authentication_multiplier"></td><td id="whatsapp_rest_of_central_-_eastern_europe_authentication_credit"></td><td id="whatsapp_rest_of_central_-_eastern_europe_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_central_-_eastern_europe_marketing_ratio"></td><td>Restante da Europa Central e Oriental Marketing</td><td id="whatsapp_rest_of_central_-_eastern_europe_marketing_multiplier"></td><td id="whatsapp_rest_of_central_-_eastern_europe_marketing_credit"></td><td id="whatsapp_rest_of_central_-_eastern_europe_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_central_-_eastern_europe_service_ratio"></td><td>Restante da Europa Central e Oriental Atendimento</td><td id="whatsapp_rest_of_central_-_eastern_europe_service_multiplier"></td><td id="whatsapp_rest_of_central_-_eastern_europe_service_credit"></td><td id="whatsapp_rest_of_central_-_eastern_europe_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_central_-_eastern_europe_utility_ratio"></td><td>Restante da Europa Central e Oriental Utilidade</td><td id="whatsapp_rest_of_central_-_eastern_europe_utility_multiplier"></td><td id="whatsapp_rest_of_central_-_eastern_europe_utility_credit"></td><td id="whatsapp_rest_of_central_-_eastern_europe_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_latin_america_authentication_ratio"></td><td>Restante da América Latina Autenticação</td><td id="whatsapp_rest_of_latin_america_authentication_multiplier"></td><td id="whatsapp_rest_of_latin_america_authentication_credit"></td><td id="whatsapp_rest_of_latin_america_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_latin_america_marketing_ratio"></td><td>Restante da América Latina Marketing</td><td id="whatsapp_rest_of_latin_america_marketing_multiplier"></td><td id="whatsapp_rest_of_latin_america_marketing_credit"></td><td id="whatsapp_rest_of_latin_america_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_latin_america_service_ratio"></td><td>Restante da América Latina Atendimento</td><td id="whatsapp_rest_of_latin_america_service_multiplier"></td><td id="whatsapp_rest_of_latin_america_service_credit"></td><td id="whatsapp_rest_of_latin_america_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_latin_america_utility_ratio"></td><td>Restante da América Latina Utilidade</td><td id="whatsapp_rest_of_latin_america_utility_multiplier"></td><td id="whatsapp_rest_of_latin_america_utility_credit"></td><td id="whatsapp_rest_of_latin_america_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_middle_east_authentication_ratio"></td><td>Restante do Oriente Médio Autenticação</td><td id="whatsapp_rest_of_middle_east_authentication_multiplier"></td><td id="whatsapp_rest_of_middle_east_authentication_credit"></td><td id="whatsapp_rest_of_middle_east_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_middle_east_marketing_ratio"></td><td>Restante do Oriente Médio Marketing</td><td id="whatsapp_rest_of_middle_east_marketing_multiplier"></td><td id="whatsapp_rest_of_middle_east_marketing_credit"></td><td id="whatsapp_rest_of_middle_east_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_middle_east_service_ratio"></td><td>Restante do Oriente Médio Atendimento</td><td id="whatsapp_rest_of_middle_east_service_multiplier"></td><td id="whatsapp_rest_of_middle_east_service_credit"></td><td id="whatsapp_rest_of_middle_east_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_middle_east_utility_ratio"></td><td>Restante do Oriente Médio Utilidade</td><td id="whatsapp_rest_of_middle_east_utility_multiplier"></td><td id="whatsapp_rest_of_middle_east_utility_credit"></td><td id="whatsapp_rest_of_middle_east_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_western_europe_authentication_ratio"></td><td>Restante da Europa Ocidental Autenticação</td><td id="whatsapp_rest_of_western_europe_authentication_multiplier"></td><td id="whatsapp_rest_of_western_europe_authentication_credit"></td><td id="whatsapp_rest_of_western_europe_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_western_europe_marketing_ratio"></td><td>Restante da Europa Ocidental Marketing</td><td id="whatsapp_rest_of_western_europe_marketing_multiplier"></td><td id="whatsapp_rest_of_western_europe_marketing_credit"></td><td id="whatsapp_rest_of_western_europe_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_western_europe_service_ratio"></td><td>Restante da Europa Ocidental Atendimento</td><td id="whatsapp_rest_of_western_europe_service_multiplier"></td><td id="whatsapp_rest_of_western_europe_service_credit"></td><td id="whatsapp_rest_of_western_europe_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_western_europe_utility_ratio"></td><td>Restante da Europa Ocidental Utilidade</td><td id="whatsapp_rest_of_western_europe_utility_multiplier"></td><td id="whatsapp_rest_of_western_europe_utility_credit"></td><td id="whatsapp_rest_of_western_europe_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_russia_authentication_ratio"></td><td>Rússia Autenticação</td><td id="whatsapp_russia_authentication_multiplier"></td><td id="whatsapp_russia_authentication_credit"></td><td id="whatsapp_russia_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_russia_marketing_ratio"></td><td>Rússia Marketing</td><td id="whatsapp_russia_marketing_multiplier"></td><td id="whatsapp_russia_marketing_credit"></td><td id="whatsapp_russia_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_russia_service_ratio"></td><td>Rússia Atendimento</td><td id="whatsapp_russia_service_multiplier"></td><td id="whatsapp_russia_service_credit"></td><td id="whatsapp_russia_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_russia_utility_ratio"></td><td>Rússia Utilidade</td><td id="whatsapp_russia_utility_multiplier"></td><td id="whatsapp_russia_utility_credit"></td><td id="whatsapp_russia_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_saudi_arabia_authentication_ratio"></td><td>Arábia Saudita Autenticação</td><td id="whatsapp_saudi_arabia_authentication_multiplier"></td><td id="whatsapp_saudi_arabia_authentication_credit"></td><td id="whatsapp_saudi_arabia_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_saudi_arabia_marketing_ratio"></td><td>Arábia Saudita Marketing</td><td id="whatsapp_saudi_arabia_marketing_multiplier"></td><td id="whatsapp_saudi_arabia_marketing_credit"></td><td id="whatsapp_saudi_arabia_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_saudi_arabia_service_ratio"></td><td>Arábia Saudita Atendimento</td><td id="whatsapp_saudi_arabia_service_multiplier"></td><td id="whatsapp_saudi_arabia_service_credit"></td><td id="whatsapp_saudi_arabia_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_saudi_arabia_utility_ratio"></td><td>Arábia Saudita Utilidade</td><td id="whatsapp_saudi_arabia_utility_multiplier"></td><td id="whatsapp_saudi_arabia_utility_credit"></td><td id="whatsapp_saudi_arabia_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_south_africa_authentication_ratio"></td><td>África do Sul Autenticação</td><td id="whatsapp_south_africa_authentication_multiplier"></td><td id="whatsapp_south_africa_authentication_credit"></td><td id="whatsapp_south_africa_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_south_africa_marketing_ratio"></td><td>África do Sul Marketing</td><td id="whatsapp_south_africa_marketing_multiplier"></td><td id="whatsapp_south_africa_marketing_credit"></td><td id="whatsapp_south_africa_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_south_africa_service_ratio"></td><td>África do Sul Atendimento</td><td id="whatsapp_south_africa_service_multiplier"></td><td id="whatsapp_south_africa_service_credit"></td><td id="whatsapp_south_africa_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_south_africa_utility_ratio"></td><td>África do Sul Utilidade</td><td id="whatsapp_south_africa_utility_multiplier"></td><td id="whatsapp_south_africa_utility_credit"></td><td id="whatsapp_south_africa_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_spain_authentication_ratio"></td><td>Espanha Autenticação</td><td id="whatsapp_spain_authentication_multiplier"></td><td id="whatsapp_spain_authentication_credit"></td><td id="whatsapp_spain_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_spain_marketing_ratio"></td><td>Espanha Marketing</td><td id="whatsapp_spain_marketing_multiplier"></td><td id="whatsapp_spain_marketing_credit"></td><td id="whatsapp_spain_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_spain_service_ratio"></td><td>Espanha Atendimento</td><td id="whatsapp_spain_service_multiplier"></td><td id="whatsapp_spain_service_credit"></td><td id="whatsapp_spain_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_spain_utility_ratio"></td><td>Espanha Utilidade</td><td id="whatsapp_spain_utility_multiplier"></td><td id="whatsapp_spain_utility_credit"></td><td id="whatsapp_spain_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_turkey_authentication_ratio"></td><td>Turquia Autenticação</td><td id="whatsapp_turkey_authentication_multiplier"></td><td id="whatsapp_turkey_authentication_credit"></td><td id="whatsapp_turkey_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_turkey_marketing_ratio"></td><td>Turquia Marketing</td><td id="whatsapp_turkey_marketing_multiplier"></td><td id="whatsapp_turkey_marketing_credit"></td><td id="whatsapp_turkey_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_turkey_service_ratio"></td><td>Turquia Atendimento</td><td id="whatsapp_turkey_service_multiplier"></td><td id="whatsapp_turkey_service_credit"></td><td id="whatsapp_turkey_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_turkey_utility_ratio"></td><td>Turquia Utilidade</td><td id="whatsapp_turkey_utility_multiplier"></td><td id="whatsapp_turkey_utility_credit"></td><td id="whatsapp_turkey_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_united_arab_emirates_authentication_ratio"></td><td>Emirados Árabes Unidos Autenticação</td><td id="whatsapp_united_arab_emirates_authentication_multiplier"></td><td id="whatsapp_united_arab_emirates_authentication_credit"></td><td id="whatsapp_united_arab_emirates_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_united_arab_emirates_marketing_ratio"></td><td>Emirados Árabes Unidos Marketing</td><td id="whatsapp_united_arab_emirates_marketing_multiplier"></td><td id="whatsapp_united_arab_emirates_marketing_credit"></td><td id="whatsapp_united_arab_emirates_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_united_arab_emirates_service_ratio"></td><td>Emirados Árabes Unidos Atendimento</td><td id="whatsapp_united_arab_emirates_service_multiplier"></td><td id="whatsapp_united_arab_emirates_service_credit"></td><td id="whatsapp_united_arab_emirates_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_united_arab_emirates_utility_ratio"></td><td>Emirados Árabes Unidos Utilidade</td><td id="whatsapp_united_arab_emirates_utility_multiplier"></td><td id="whatsapp_united_arab_emirates_utility_credit"></td><td id="whatsapp_united_arab_emirates_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_united_kingdom_authentication_ratio"></td><td>Reino Unido Autenticação</td><td id="whatsapp_united_kingdom_authentication_multiplier"></td><td id="whatsapp_united_kingdom_authentication_credit"></td><td id="whatsapp_united_kingdom_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_united_kingdom_marketing_ratio"></td><td>Reino Unido Marketing</td><td id="whatsapp_united_kingdom_marketing_multiplier"></td><td id="whatsapp_united_kingdom_marketing_credit"></td><td id="whatsapp_united_kingdom_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_united_kingdom_service_ratio"></td><td>Reino Unido Atendimento</td><td id="whatsapp_united_kingdom_service_multiplier"></td><td id="whatsapp_united_kingdom_service_credit"></td><td id="whatsapp_united_kingdom_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_united_kingdom_utility_ratio"></td><td>Reino Unido Utilidade</td><td id="whatsapp_united_kingdom_utility_multiplier"></td><td id="whatsapp_united_kingdom_utility_credit"></td><td id="whatsapp_united_kingdom_utility_rates"></td></tr>
  </tbody>
  </table>
</div>

<script type="text/javascript">
// list in order of Delta, Theta, Gamma, Sigma, Lambda
// [Ratio, Multiplier]
var credit_map = {
  "#sms_-_us_ca_united_states":[[1,1],[0.7,1],[0.4,1],[1,1],[1,1]],
"#sms_-_us_ca_united_states_toll_free":[[1,1.5],[0.7,1.5],[0.4,1.5],[1,1.5],[1,1.5]],
"#sms_-_us_ca_canada":[[1,1],[0.7,1],[0.4,1],[1,1],[1,1]],
"#sms_-_us_ca_canada_toll_free":[[1,1.3],[0.7,1.3],[0.4,1.3],[1,1.3],[1,1.3]],
"#mms_-_us_ca_united_states":[[3,1],[2,1],[1.2,1],[3,1],[3,1]],
"#mms_-_us_ca_united_states_toll_free":[[3,2],[2,2],[1.2,2],[3,2],[3,2]],
"#mms_-_us_ca_canada_long_code":[[3,1.5],[2,1.5],[1.2,1.5],[3,1.5],[3,1.5]],
"#mms_-_us_ca_canada_short_code":[[3,4],[2,4],[1.2,4],[3,4],[3,4]],
"#mms_-_us_ca_canada_toll_free":[[3,1.3],[2,1.3],[1.2,1.3],[3,1.3],[3,1.3]],
"#sms_mms_-_global_abkhazia":[[10,0.62],[10,0.62],[10,0.62],[7.5,0.62],[10,0.62]],
"#sms_mms_-_global_afghanistan":[[10,9.47],[10,9.47],[10,9.47],[7.5,9.47],[10,2.48]],
"#sms_mms_-_global_albania":[[10,2.29],[10,2.29],[10,2.29],[7.5,2.29],[10,1.04]],
"#sms_mms_-_global_algeria":[[10,5.23],[10,5.23],[10,5.23],[7.5,5.23],[10,3.26]],
"#sms_mms_-_global_american_samoa":[[10,4.74],[10,4.74],[10,4.74],[7.5,4.74],[10,0.99]],
"#sms_mms_-_global_andorra":[[10,3.32],[10,3.32],[10,3.32],[7.5,3.32],[10,1.18]],
"#sms_mms_-_global_angola":[[10,2.24],[10,2.24],[10,2.24],[7.5,2.24],[10,0.81]],
"#sms_mms_-_global_anguilla":[[10,3.33],[10,3.33],[10,3.33],[7.5,3.33],[10,0.99]],
"#sms_mms_-_global_antigua_and_barbuda":[[10,2.47],[10,2.47],[10,2.47],[7.5,2.47],[10,0.98]],
"#sms_mms_-_global_argentina":[[10,1.02],[10,1.02],[10,1.02],[7.5,1.02],[10,1.4]],
"#sms_mms_-_global_armenia":[[10,3.49],[10,3.49],[10,3.49],[7.5,3.49],[10,1.84]],
"#sms_mms_-_global_aruba":[[10,2.61],[10,2.61],[10,2.61],[7.5,2.61],[10,0.95]],
"#sms_mms_-_global_australia_sms":[[10,0.36],[10,0.36],[10,0.36],[7.5,0.36],[10,0.39]],
"#sms_mms_-_global_australia_mms":[[10,3.1],[10,3.1],[10,3.1],[7.5,3.1],[10,"N/A"]],
"#sms_mms_-_global_austria":[[10,1.77],[10,1.77],[10,1.77],[7.5,1.77],[10,0.53]],
"#sms_mms_-_global_azerbaijan":[[10,9.77],[10,9.77],[10,9.77],[7.5,9.77],[10,3.32]],
"#sms_mms_-_global_bahamas":[[10,1.23],[10,1.23],[10,1.23],[7.5,1.23],[10,0.93]],
"#sms_mms_-_global_bahrain":[[10,0.92],[10,0.92],[10,0.92],[7.5,0.92],[10,0.5]],
"#sms_mms_-_global_bangladesh":[[10,5.81],[10,5.81],[10,5.81],[7.5,5.81],[10,2.76]],
"#sms_mms_-_global_barbados":[[10,3.09],[10,3.09],[10,3.09],[7.5,3.09],[10,1]],
"#sms_mms_-_global_belarus":[[10,6.35],[10,6.35],[10,6.35],[7.5,6.35],[10,3.2]],
"#sms_mms_-_global_belgium":[[10,2.4],[10,2.4],[10,2.4],[7.5,2.4],[10,1.48]],
"#sms_mms_-_global_belize":[[10,6.9],[10,6.9],[10,6.9],[7.5,6.9],[10,1.66]],
"#sms_mms_-_global_benin":[[10,3.64],[10,3.64],[10,3.64],[7.5,3.64],[10,0.92]],
"#sms_mms_-_global_bermuda":[[10,2.99],[10,2.99],[10,2.99],[7.5,2.99],[10,1.04]],
"#sms_mms_-_global_bhutan":[[10,10.1],[10,10.1],[10,10.1],[7.5,10.1],[10,2.5]],
"#sms_mms_-_global_bolivia":[[10,3.66],[10,3.66],[10,3.66],[7.5,3.66],[10,1.4]],
"#sms_mms_-_global_bosnia_and_herzegovina":[[10,2.12],[10,2.12],[10,2.12],[7.5,2.12],[10,1.01]],
"#sms_mms_-_global_botswana":[[10,2.52],[10,2.52],[10,2.52],[7.5,2.52],[10,1.23]],
"#sms_mms_-_global_brazil":[[10,0.25],[10,0.25],[10,0.25],[7.5,0.25],[10,0.21]],
"#sms_mms_-_global_brunei":[[10,0.5],[10,0.5],[10,0.5],[7.5,0.5],[10,0.27]],
"#sms_mms_-_global_bulgaria":[[10,2.7],[10,2.7],[10,2.7],[7.5,2.7],[10,1.94]],
"#sms_mms_-_global_burkina_faso":[[10,3.35],[10,3.35],[10,3.35],[7.5,3.35],[10,1.44]],
"#sms_mms_-_global_burundi":[[10,9.47],[10,9.47],[10,9.47],[7.5,9.47],[10,1.84]],
"#sms_mms_-_global_cambodia":[[10,4.3],[10,4.3],[10,4.3],[7.5,4.3],[10,2.41]],
"#sms_mms_-_global_cameroon":[[10,3.49],[10,3.49],[10,3.49],[7.5,3.49],[10,1.13]],
"#sms_mms_-_global_cape_verde":[[10,3.66],[10,3.66],[10,3.66],[7.5,3.66],[10,1.43]],
"#sms_mms_-_global_caribbean_netherlands":[[10,2.17],[10,2.17],[10,2.17],[7.5,2.17],[10,2.17]],
"#sms_mms_-_global_cayman_islands":[[10,3.37],[10,3.37],[10,3.37],[7.5,3.37],[10,0.99]],
"#sms_mms_-_global_central_african_republic":[[10,3.07],[10,3.07],[10,3.07],[7.5,3.07],[10,0.31]],
"#sms_mms_-_global_chad":[[10,7.3],[10,7.3],[10,7.3],[7.5,7.3],[10,2.31]],
"#sms_mms_-_global_chile":[[10,1.64],[10,1.64],[10,1.64],[7.5,1.64],[10,0.78]],
"#sms_mms_-_global_china":[[10,0.64],[10,0.64],[10,0.64],[7.5,0.64],[10,0.17]],
"#sms_mms_-_global_colombia":[[10,0.02],[10,0.02],[10,0.02],[7.5,0.02],[10,0.03]],
"#sms_mms_-_global_comoros":[[10,6.19],[10,6.19],[10,6.19],[7.5,6.19],[10,0.6]],
"#sms_mms_-_global_congo":[[10,5.04],[10,5.04],[10,5.04],[7.5,5.04],[10,0.68]],
"#sms_mms_-_global_cook_islands":[[10,3.52],[10,3.52],[10,3.52],[7.5,3.52],[10,0.68]],
"#sms_mms_-_global_costa_rica":[[10,1.06],[10,1.06],[10,1.06],[7.5,1.06],[10,0.65]],
"#sms_mms_-_global_croatia":[[10,2.31],[10,2.31],[10,2.31],[7.5,2.31],[10,0.85]],
"#sms_mms_-_global_cuba":[[10,2.12],[10,2.12],[10,2.12],[7.5,2.12],[10,1.86]],
"#sms_mms_-_global_curacao":[[10,0.99],[10,0.99],[10,0.99],[7.5,0.99],[10,0.99]],
"#sms_mms_-_global_cyprus":[[10,2.18],[10,2.18],[10,2.18],[7.5,2.18],[10,0.22]],
"#sms_mms_-_global_czech_republic":[[10,1.01],[10,1.01],[10,1.01],[7.5,1.01],[10,0.9]],
"#sms_mms_-_global_denmark":[[10,1.01],[10,1.01],[10,1.01],[7.5,1.01],[10,0.85]],
"#sms_mms_-_global_djibouti":[[10,4.09],[10,4.09],[10,4.09],[7.5,4.09],[10,1.09]],
"#sms_mms_-_global_dominica":[[10,3.79],[10,3.79],[10,3.79],[7.5,3.79],[10,0.96]],
"#sms_mms_-_global_dominican_republic":[[10,1.29],[10,1.29],[10,1.29],[7.5,1.29],[10,1.02]],
"#sms_mms_-_global_dr_congo":[[10,5.77],[10,5.77],[10,5.77],[7.5,5.77],[10,1.48]],
"#sms_mms_-_global_ecuador":[[10,2.76],[10,2.76],[10,2.76],[7.5,2.76],[10,2.2]],
"#sms_mms_-_global_egypt":[[10,2.43],[10,2.43],[10,2.43],[7.5,2.43],[10,2.1]],
"#sms_mms_-_global_el_salvador":[[10,2.45],[10,2.45],[10,2.45],[7.5,2.45],[10,0.86]],
"#sms_mms_-_global_equatorial_guinea":[[10,4.36],[10,4.36],[10,4.36],[7.5,4.36],[10,0.54]],
"#sms_mms_-_global_eritrea":[[10,2.48],[10,2.48],[10,2.48],[7.5,2.48],[10,1.47]],
"#sms_mms_-_global_estonia":[[10,2.41],[10,2.41],[10,2.41],[7.5,2.41],[10,0.94]],
"#sms_mms_-_global_eswatini":[[10,0.58],[10,0.58],[10,0.58],[7.5,0.58],[10,0.58]],
"#sms_mms_-_global_ethiopia":[[10,8.63],[10,8.63],[10,8.63],[7.5,8.63],[10,2.64]],
"#sms_mms_-_global_falkland_islands":[[10,3.43],[10,3.43],[10,3.43],[7.5,3.43],[10,0.2]],
"#sms_mms_-_global_faroe_islands":[[10,1.7],[10,1.7],[10,1.7],[7.5,1.7],[10,0.23]],
"#sms_mms_-_global_fiji":[[10,4.16],[10,4.16],[10,4.16],[7.5,4.16],[10,1.4]],
"#sms_mms_-_global_finland":[[10,1.46],[10,1.46],[10,1.46],[7.5,1.46],[10,1.15]],
"#sms_mms_-_global_france":[[10,0.98],[10,0.98],[10,0.98],[7.5,0.98],[10,0.93]],
"#sms_mms_-_global_french_guiana":[[10,4.64],[10,4.64],[10,4.64],[7.5,4.64],[10,2.01]],
"#sms_mms_-_global_french_polynesia":[[10,4.53],[10,4.53],[10,4.53],[7.5,4.53],[10,1.58]],
"#sms_mms_-_global_gabon":[[10,6.64],[10,6.64],[10,6.64],[7.5,6.64],[10,2.12]],
"#sms_mms_-_global_gambia":[[10,4.18],[10,4.18],[10,4.18],[7.5,4.18],[10,1.24]],
"#sms_mms_-_global_georgia":[[10,2.63],[10,2.63],[10,2.63],[7.5,2.63],[10,2.18]],
"#sms_mms_-_global_germany":[[10,1.88],[10,1.88],[10,1.88],[7.5,1.88],[10,1.73]],
"#sms_mms_-_global_ghana":[[10,2.26],[10,2.26],[10,2.26],[7.5,2.26],[10,1.74]],
"#sms_mms_-_global_gibraltar":[[10,2.75],[10,2.75],[10,2.75],[7.5,2.75],[10,0.16]],
"#sms_mms_-_global_greece":[[10,0.99],[10,0.99],[10,0.99],[7.5,0.99],[10,1.02]],
"#sms_mms_-_global_greenland":[[10,1.03],[10,1.03],[10,1.03],[7.5,1.03],[10,0.16]],
"#sms_mms_-_global_grenada":[[10,4.09],[10,4.09],[10,4.09],[7.5,4.09],[10,1.03]],
"#sms_mms_-_global_guadeloupe":[[10,3.4],[10,3.4],[10,3.4],[7.5,3.4],[10,2]],
"#sms_mms_-_global_guam":[[10,1.73],[10,1.73],[10,1.73],[7.5,1.73],[10,0.62]],
"#sms_mms_-_global_guatemala":[[10,3.2],[10,3.2],[10,3.2],[7.5,3.2],[10,1.86]],
"#sms_mms_-_global_guernsey":[[10,0.87],[10,0.87],[10,0.87],[7.5,0.87],[10,0.87]],
"#sms_mms_-_global_guinea":[[10,3.82],[10,3.82],[10,3.82],[7.5,3.82],[10,1.83]],
"#sms_mms_-_global_guinea-bissau":[[10,3.97],[10,3.97],[10,3.97],[7.5,3.97],[10,1.45]],
"#sms_mms_-_global_guyana":[[10,4.5],[10,4.5],[10,4.5],[7.5,4.5],[10,1.06]],
"#sms_mms_-_global_haiti":[[10,5.94],[10,5.94],[10,5.94],[7.5,5.94],[10,1.16]],
"#sms_mms_-_global_honduras":[[10,2.13],[10,2.13],[10,2.13],[7.5,2.13],[10,0.72]],
"#sms_mms_-_global_hong_kong":[[10,1.35],[10,1.35],[10,1.35],[7.5,1.35],[10,0.98]],
"#sms_mms_-_global_hungary":[[10,1.91],[10,1.91],[10,1.91],[7.5,1.91],[10,1.16]],
"#sms_mms_-_global_iceland":[[10,1.75],[10,1.75],[10,1.75],[7.5,1.75],[10,1.15]],
"#sms_mms_-_global_india":[[10,1],[10,1],[10,1],[7.5,1],[10,0.84]],
"#sms_mms_-_global_indonesia":[[10,6.63],[10,6.63],[10,6.63],[7.5,6.63],[10,3.66]],
"#sms_mms_-_global_iran":[[10,6.25],[10,6.25],[10,6.25],[7.5,6.25],[10,1.59]],
"#sms_mms_-_global_iraq":[[10,4.79],[10,4.79],[10,4.79],[7.5,4.79],[10,2.38]],
"#sms_mms_-_global_ireland":[[10,1.31],[10,1.31],[10,1.31],[7.5,1.31],[10,1.06]],
"#sms_mms_-_global_isle_of_man":[[10,0.81],[10,0.81],[10,0.81],[7.5,0.81],[10,0.81]],
"#sms_mms_-_global_israel":[[10,3.74],[10,3.74],[10,3.74],[7.5,3.74],[10,1.5]],
"#sms_mms_-_global_italy":[[10,0.78],[10,0.78],[10,0.78],[7.5,0.78],[10,0.89]],
"#sms_mms_-_global_ivory_coast":[[10,2.48],[10,2.48],[10,2.48],[7.5,2.48],[10,1.55]],
"#sms_mms_-_global_jamaica":[[10,3.05],[10,3.05],[10,3.05],[7.5,3.05],[10,1.1]],
"#sms_mms_-_global_japan":[[10,1.02],[10,1.02],[10,1.02],[7.5,1.02],[10,0.92]],
"#sms_mms_-_global_jersey":[[10,0.7],[10,0.7],[10,0.7],[7.5,0.7],[10,0.7]],
"#sms_mms_-_global_jordan":[[10,5.56],[10,5.56],[10,5.56],[7.5,5.56],[10,2.58]],
"#sms_mms_-_global_kazakhstan":[[10,5.52],[10,5.52],[10,5.52],[7.5,5.52],[10,2.54]],
"#sms_mms_-_global_kenya":[[10,2.62],[10,2.62],[10,2.62],[7.5,2.62],[10,2.25]],
"#sms_mms_-_global_kiribati":[[10,3.67],[10,3.67],[10,3.67],[7.5,3.67],[10,0.31]],
"#sms_mms_-_global_korea_republic_of":[[10,0.69],[10,0.69],[10,0.69],[7.5,0.69],[10,0.3]],
"#sms_mms_-_global_kosovo":[[10,0.97],[10,0.97],[10,0.97],[7.5,0.97],[10,0.97]],
"#sms_mms_-_global_kuwait":[[10,3.34],[10,3.34],[10,3.34],[7.5,3.34],[10,2.45]],
"#sms_mms_-_global_kyrgyzstan":[[10,6.12],[10,6.12],[10,6.12],[7.5,6.12],[10,2.64]],
"#sms_mms_-_global_laos_pdr":[[10,1.54],[10,1.54],[10,1.54],[7.5,1.54],[10,0.8]],
"#sms_mms_-_global_latvia":[[10,1.8],[10,1.8],[10,1.8],[7.5,1.8],[10,0.74]],
"#sms_mms_-_global_lebanon":[[10,3.07],[10,3.07],[10,3.07],[7.5,3.07],[10,1.94]],
"#sms_mms_-_global_lesotho":[[10,5.14],[10,5.14],[10,5.14],[7.5,5.14],[10,0.65]],
"#sms_mms_-_global_liberia":[[10,3.47],[10,3.47],[10,3.47],[7.5,3.47],[10,0.72]],
"#sms_mms_-_global_libya":[[10,8.17],[10,8.17],[10,8.17],[7.5,8.17],[10,2.68]],
"#sms_mms_-_global_liechtenstein":[[10,0.84],[10,0.84],[10,0.84],[7.5,0.84],[10,0.38]],
"#sms_mms_-_global_lithuania":[[10,1.37],[10,1.37],[10,1.37],[7.5,1.37],[10,0.5]],
"#sms_mms_-_global_luxembourg":[[10,1.86],[10,1.86],[10,1.86],[7.5,1.86],[10,1.03]],
"#sms_mms_-_global_macao":[[10,1.49],[10,1.49],[10,1.49],[7.5,1.49],[10,0.38]],
"#sms_mms_-_global_macedonia":[[10,1.88],[10,1.88],[10,1.88],[7.5,1.88],[10,"N/A"]],
"#sms_mms_-_global_madagascar":[[10,9.4],[10,9.4],[10,9.4],[7.5,9.4],[10,2.22]],
"#sms_mms_-_global_malawi":[[10,5.72],[10,5.72],[10,5.72],[7.5,5.72],[10,2.24]],
"#sms_mms_-_global_malaysia":[[10,1.47],[10,1.47],[10,1.47],[7.5,1.47],[10,0.79]],
"#sms_mms_-_global_maldives":[[10,1.8],[10,1.8],[10,1.8],[7.5,1.8],[10,0.87]],
"#sms_mms_-_global_mali":[[10,3.97],[10,3.97],[10,3.97],[7.5,3.97],[10,2.17]],
"#sms_mms_-_global_malta":[[10,1.64],[10,1.64],[10,1.64],[7.5,1.64],[10,1.05]],
"#sms_mms_-_global_marshall_islands":[[10,4],[10,4],[10,4],[7.5,4],[10,"N/A"]],
"#sms_mms_-_global_martinique":[[10,3.33],[10,3.33],[10,3.33],[7.5,3.33],[10,1.88]],
"#sms_mms_-_global_mauritania":[[10,6.51],[10,6.51],[10,6.51],[7.5,6.51],[10,1.95]],
"#sms_mms_-_global_mauritius":[[10,4.02],[10,4.02],[10,4.02],[7.5,4.02],[10,1.89]],
"#sms_mms_-_global_mayotte":[[10,2.33],[10,2.33],[10,2.33],[7.5,2.33],[10,2.33]],
"#sms_mms_-_global_mexico":[[10,0.27],[10,0.27],[10,0.27],[7.5,0.27],[10,0.28]],
"#sms_mms_-_global_micronesia":[[10,1.85],[10,1.85],[10,1.85],[7.5,1.85],[10,0.93]],
"#sms_mms_-_global_moldova":[[10,1.59],[10,1.59],[10,1.59],[7.5,1.59],[10,0.87]],
"#sms_mms_-_global_monaco":[[10,4.68],[10,4.68],[10,4.68],[7.5,4.68],[10,1.62]],
"#sms_mms_-_global_mongolia":[[10,7.03],[10,7.03],[10,7.03],[7.5,7.03],[10,1.93]],
"#sms_mms_-_global_montenegro":[[10,2.87],[10,2.87],[10,2.87],[7.5,2.87],[10,0.99]],
"#sms_mms_-_global_montserrat":[[10,2.77],[10,2.77],[10,2.77],[7.5,2.77],[10,0.9]],
"#sms_mms_-_global_morocco":[[10,2.64],[10,2.64],[10,2.64],[7.5,2.64],[10,1.55]],
"#sms_mms_-_global_mozambique":[[10,2.76],[10,2.76],[10,2.76],[7.5,2.76],[10,0.61]],
"#sms_mms_-_global_myanmar":[[10,5.84],[10,5.84],[10,5.84],[7.5,5.84],[10,2.48]],
"#sms_mms_-_global_namibia":[[10,1.58],[10,1.58],[10,1.58],[7.5,1.58],[10,0.5]],
"#sms_mms_-_global_nauru":[[10,1.12],[10,1.12],[10,1.12],[7.5,1.12],[10,1.12]],
"#sms_mms_-_global_nepal":[[10,3.82],[10,3.82],[10,3.82],[7.5,3.82],[10,1.85]],
"#sms_mms_-_global_netherlands":[[10,1.65],[10,1.65],[10,1.65],[7.5,1.65],[10,1.82]],
"#sms_mms_-_global_new_caledonia":[[10,4.44],[10,4.44],[10,4.44],[7.5,4.44],[10,1.49]],
"#sms_mms_-_global_new_zealand":[[10,1.92],[10,1.92],[10,1.92],[7.5,1.92],[10,1.42]],
"#sms_mms_-_global_nicaragua":[[10,1.95],[10,1.95],[10,1.95],[7.5,1.95],[10,1.27]],
"#sms_mms_-_global_niger":[[10,7.49],[10,7.49],[10,7.49],[7.5,7.49],[10,1.6]],
"#sms_mms_-_global_nigeria":[[10,5.01],[10,5.01],[10,5.01],[7.5,5.01],[10,2.13]],
"#sms_mms_-_global_niue":[[10,4.86],[10,4.86],[10,4.86],[7.5,4.86],[10,"N/A"]],
"#sms_mms_-_global_norfolk_island":[[10,0.71],[10,0.71],[10,0.71],[7.5,0.71],[10,"N/A"]],
"#sms_mms_-_global_north_macedonia":[[10,0.34],[10,0.34],[10,0.34],[7.5,0.34],[10,0.34]],
"#sms_mms_-_global_northern_cyprus":[[10,0.2],[10,0.2],[10,0.2],[7.5,0.2],[10,0.2]],
"#sms_mms_-_global_norway":[[10,1.05],[10,1.05],[10,1.05],[7.5,1.05],[10,0.9]],
"#sms_mms_-_global_oman":[[10,3.6],[10,3.6],[10,3.6],[7.5,3.6],[10,1.68]],
"#sms_mms_-_global_pakistan":[[10,7.46],[10,7.46],[10,7.46],[7.5,7.46],[10,2.22]],
"#sms_mms_-_global_palau":[[10,2.52],[10,2.52],[10,2.52],[7.5,2.52],[10,0.37]],
"#sms_mms_-_global_palestinian_territory":[[10,7.68],[10,7.68],[10,7.68],[7.5,7.68],[10,"N/A"]],
"#sms_mms_-_global_panama":[[10,2.23],[10,2.23],[10,2.23],[7.5,2.23],[10,0.93]],
"#sms_mms_-_global_papua_new_guinea":[[10,19.01],[10,19.01],[10,19.01],[7.5,19.01],[10,0.99]],
"#sms_mms_-_global_paraguay":[[10,1.84],[10,1.84],[10,1.84],[7.5,1.84],[10,0.28]],
"#sms_mms_-_global_peru":[[10,0.81],[10,0.81],[10,0.81],[7.5,0.81],[10,1.1]],
"#sms_mms_-_global_philippines":[[10,0.28],[10,0.28],[10,0.28],[7.5,0.28],[10,0.8]],
"#sms_mms_-_global_poland":[[10,0.52],[10,0.52],[10,0.52],[7.5,0.52],[10,0.39]],
"#sms_mms_-_global_portugal":[[10,0.6],[10,0.6],[10,0.6],[7.5,0.6],[10,0.37]],
"#sms_mms_-_global_puerto_rico":[[10,1.06],[10,1.06],[10,1.06],[7.5,1.06],[10,0.13]],
"#sms_mms_-_global_qatar":[[10,0.52],[10,0.52],[10,0.52],[7.5,0.52],[10,0.39]],
"#sms_mms_-_global_reunion-mayotte":[[10,4.82],[10,4.82],[10,4.82],[7.5,4.82],[10,1.13]],
"#sms_mms_-_global_romania":[[10,1.06],[10,1.06],[10,1.06],[7.5,1.06],[10,0.78]],
"#sms_mms_-_global_russia":[[10,9.54],[10,9.54],[10,9.54],[7.5,9.54],[10,1.89]],
"#sms_mms_-_global_rwanda":[[10,4.66],[10,4.66],[10,4.66],[7.5,4.66],[10,1.21]],
"#sms_mms_-_global_saint_kitts_and_nevis":[[10,0.92],[10,0.92],[10,0.92],[7.5,0.92],[10,0.92]],
"#sms_mms_-_global_saint_lucia":[[10,1.07],[10,1.07],[10,1.07],[7.5,1.07],[10,1.07]],
"#sms_mms_-_global_saint_pierre_and_miquelon":[[10,2.31],[10,2.31],[10,2.31],[7.5,2.31],[10,2.31]],
"#sms_mms_-_global_saint_vincent_and_the_grenadines":[[10,1.06],[10,1.06],[10,1.06],[7.5,1.06],[10,1.06]],
"#sms_mms_-_global_samoa":[[10,4.68],[10,4.68],[10,4.68],[7.5,4.68],[10,0.75]],
"#sms_mms_-_global_san_marino":[[10,2.76],[10,2.76],[10,2.76],[7.5,2.76],[10,"N/A"]],
"#sms_mms_-_global_sao_tome_and_principe":[[10,3.29],[10,3.29],[10,3.29],[7.5,3.29],[10,0.65]],
"#sms_mms_-_global_saudi_arabia":[[10,1.91],[10,1.91],[10,1.91],[7.5,1.91],[10,1.07]],
"#sms_mms_-_global_senegal":[[10,5.15],[10,5.15],[10,5.15],[7.5,5.15],[10,2.02]],
"#sms_mms_-_global_serbia":[[10,6.09],[10,6.09],[10,6.09],[7.5,6.09],[10,0.89]],
"#sms_mms_-_global_seychelles":[[10,0.94],[10,0.94],[10,0.94],[7.5,0.94],[10,0.9]],
"#sms_mms_-_global_sierra_leone":[[10,4.73],[10,4.73],[10,4.73],[7.5,4.73],[10,1.35]],
"#sms_mms_-_global_singapore":[[10,0.7],[10,0.7],[10,0.7],[7.5,0.7],[10,0.62]],
"#sms_mms_-_global_sint_maarten":[[10,0.16],[10,0.16],[10,0.16],[7.5,0.16],[10,0.16]],
"#sms_mms_-_global_slovakia":[[10,2.23],[10,2.23],[10,2.23],[7.5,2.23],[10,0.81]],
"#sms_mms_-_global_slovenia":[[10,3.76],[10,3.76],[10,3.76],[7.5,3.76],[10,0.28]],
"#sms_mms_-_global_solomon_islands":[[10,2.09],[10,2.09],[10,2.09],[7.5,2.09],[10,0.78]],
"#sms_mms_-_global_somalia":[[10,4.74],[10,4.74],[10,4.74],[7.5,4.74],[10,1.78]],
"#sms_mms_-_global_south_africa":[[10,0.32],[10,0.32],[10,0.32],[7.5,0.32],[10,0.27]],
"#sms_mms_-_global_south_ossetia":[[10,2.05],[10,2.05],[10,2.05],[7.5,2.05],[10,2.05]],
"#sms_mms_-_global_south_sudan":[[10,0.8],[10,0.8],[10,0.8],[7.5,0.8],[10,0.8]],
"#sms_mms_-_global_spain":[[10,0.8],[10,0.8],[10,0.8],[7.5,0.8],[10,0.7]],
"#sms_mms_-_global_sri_lanka":[[10,5.6],[10,5.6],[10,5.6],[7.5,5.6],[10,2.51]],
"#sms_mms_-_global_st_kitts_and_nevis":[[10,2.8],[10,2.8],[10,2.8],[7.5,2.8],[10,"N/A"]],
"#sms_mms_-_global_st_lucia":[[10,2.59],[10,2.59],[10,2.59],[7.5,2.59],[10,"N/A"]],
"#sms_mms_-_global_st_pierre_and_miquelon":[[10,3.8],[10,3.8],[10,3.8],[7.5,3.8],[10,"N/A"]],
"#sms_mms_-_global_st_vincent_grenadines":[[10,4.08],[10,4.08],[10,4.08],[7.5,4.08],[10,"N/A"]],
"#sms_mms_-_global_sudan":[[10,4.15],[10,4.15],[10,4.15],[7.5,4.15],[10,2.24]],
"#sms_mms_-_global_suriname":[[10,3.28],[10,3.28],[10,3.28],[7.5,3.28],[10,0.73]],
"#sms_mms_-_global_swaziland":[[10,2.32],[10,2.32],[10,2.32],[7.5,2.32],[10,"N/A"]],
"#sms_mms_-_global_sweden":[[10,0.86],[10,0.86],[10,0.86],[7.5,0.86],[10,0.8]],
"#sms_mms_-_global_switzerland":[[10,0.6],[10,0.6],[10,0.6],[7.5,0.6],[10,0.61]],
"#sms_mms_-_global_syria":[[10,7.86],[10,7.86],[10,7.86],[7.5,7.86],[10,"N/A"]],
"#sms_mms_-_global_taiwan":[[10,0.84],[10,0.84],[10,0.84],[7.5,0.84],[10,1.63]],
"#sms_mms_-_global_tajikistan":[[10,11.35],[10,11.35],[10,11.35],[7.5,11.35],[10,3.45]],
"#sms_mms_-_global_tanzania":[[10,5.38],[10,5.38],[10,5.38],[7.5,5.38],[10,1.62]],
"#sms_mms_-_global_thailand":[[10,0.36],[10,0.36],[10,0.36],[7.5,0.36],[10,0.13]],
"#sms_mms_-_global_timor-leste":[[10,2.86],[10,2.86],[10,2.86],[7.5,2.86],[10,0.87]],
"#sms_mms_-_global_togo":[[10,3.84],[10,3.84],[10,3.84],[7.5,3.84],[10,0.62]],
"#sms_mms_-_global_tonga":[[10,3.14],[10,3.14],[10,3.14],[7.5,3.14],[10,0.61]],
"#sms_mms_-_global_trinidad_and_tobago":[[10,3.02],[10,3.02],[10,3.02],[7.5,3.02],[10,1.02]],
"#sms_mms_-_global_tunisia":[[10,7.06],[10,7.06],[10,7.06],[7.5,7.06],[10,2.2]],
"#sms_mms_-_global_turkey":[[10,0.77],[10,0.77],[10,0.77],[7.5,0.77],[10,0.05]],
"#sms_mms_-_global_turkmenistan":[[10,5.04],[10,5.04],[10,5.04],[7.5,5.04],[10,1.97]],
"#sms_mms_-_global_turks_and_caicos_islands":[[10,3.38],[10,3.38],[10,3.38],[7.5,3.38],[10,0.99]],
"#sms_mms_-_global_tuvalu":[[10,3.36],[10,3.36],[10,3.36],[7.5,3.36],[10,"N/A"]],
"#sms_mms_-_global_uganda":[[10,4.05],[10,4.05],[10,4.05],[7.5,4.05],[10,1.9]],
"#sms_mms_-_global_ukraine":[[10,2.86],[10,2.86],[10,2.86],[7.5,2.86],[10,2.28]],
"#sms_mms_-_global_united_arab_emirates":[[10,1.24],[10,1.24],[10,1.24],[7.5,1.24],[10,0.42]],
"#sms_mms_-_global_united_kingdom":[[10,0.65],[10,0.65],[10,0.65],[7.5,0.65],[10,0.61]],
"#sms_mms_-_global_unknown":[[10,3.92],[10,3.92],[10,3.92],[7.5,3.92],[10,"N/A"]],
"#sms_mms_-_global_uruguay":[[10,2.15],[10,2.15],[10,2.15],[7.5,2.15],[10,0.71]],
"#sms_mms_-_global_uzbekistan":[[10,6.88],[10,6.88],[10,6.88],[7.5,6.88],[10,3.52]],
"#sms_mms_-_global_vanuatu":[[10,4.18],[10,4.18],[10,4.18],[7.5,4.18],[10,1.43]],
"#sms_mms_-_global_venezuela":[[10,2.15],[10,2.15],[10,2.15],[7.5,2.15],[10,0.84]],
"#sms_mms_-_global_vietnam":[[10,3.05],[10,3.05],[10,3.05],[7.5,3.05],[10,1.49]],
"#sms_mms_-_global_virgin_islands-_british":[[10,4.73],[10,4.73],[10,4.73],[7.5,4.73],[10,1]],
"#sms_mms_-_global_virgin_islands-_us":[[10,0.5],[10,0.5],[10,0.5],[7.5,0.5],[10,"N/A"]],
"#sms_mms_-_global_wallis_and_futuna":[[10,2.77],[10,2.77],[10,2.77],[7.5,2.77],[10,1.46]],
"#sms_mms_-_global_yemen":[[10,6.03],[10,6.03],[10,6.03],[7.5,6.03],[10,1.63]],
"#sms_mms_-_global_zambia":[[10,6.76],[10,6.76],[10,6.76],[7.5,6.76],[10,1.99]],
"#sms_mms_-_global_zimbabwe":[[10,3.55],[10,3.55],[10,3.55],[7.5,3.55],[10,1.64]],
"#whatsapp_argentina_authentication":[[10,0.95],[10,0.95],[10,0.95],[7.5,0.95],[10,0.95]],
"#whatsapp_argentina_marketing":[[10,1.65],[10,1.65],[10,1.65],[7.5,1.65],[10,1.65]],
"#whatsapp_argentina_service":[[10,0.85],[10,0.85],[10,0.85],[7.5,0.85],[10,0.85]],
"#whatsapp_argentina_utility":[[10,1.1],[10,1.1],[10,1.1],[7.5,1.1],[10,1.1]],
"#whatsapp_brazil_authentication":[[10,0.85],[10,0.85],[10,0.85],[7.5,0.85],[10,0.85]],
"#whatsapp_brazil_marketing":[[10,1.65],[10,1.65],[10,1.65],[7.5,1.65],[10,1.65]],
"#whatsapp_brazil_service":[[10,0.8],[10,0.8],[10,0.8],[7.5,0.8],[10,0.8]],
"#whatsapp_brazil_utility":[[10,0.95],[10,0.95],[10,0.95],[7.5,0.95],[10,0.95]],
"#whatsapp_chile_authentication":[[10,1.4],[10,1.4],[10,1.4],[7.5,1.4],[10,1.4]],
"#whatsapp_chile_marketing":[[10,2.35],[10,2.35],[10,2.35],[7.5,2.35],[10,2.35]],
"#whatsapp_chile_service":[[10,1.2],[10,1.2],[10,1.2],[7.5,1.2],[10,1.2]],
"#whatsapp_chile_utility":[[10,1.55],[10,1.55],[10,1.55],[7.5,1.55],[10,1.55]],
"#whatsapp_colombia_authentication":[[10,0.2],[10,0.2],[10,0.2],[7.5,0.2],[10,0.2]],
"#whatsapp_colombia_marketing":[[10,0.35],[10,0.35],[10,0.35],[7.5,0.35],[10,0.35]],
"#whatsapp_colombia_service":[[10,0.15],[10,0.15],[10,0.15],[7.5,0.15],[10,0.15]],
"#whatsapp_colombia_utility":[[10,0.25],[10,0.25],[10,0.25],[7.5,0.25],[10,0.25]],
"#whatsapp_egypt_authentication":[[10,1.65],[10,1.65],[10,1.65],[7.5,1.65],[10,1.65]],
"#whatsapp_egypt_marketing":[[10,2.85],[10,2.85],[10,2.85],[7.5,2.85],[10,2.85]],
"#whatsapp_egypt_service":[[10,1.7],[10,1.7],[10,1.7],[7.5,1.7],[10,1.7]],
"#whatsapp_egypt_utility":[[10,1.8],[10,1.8],[10,1.8],[7.5,1.8],[10,1.8]],
"#whatsapp_france_authentication":[[10,1.85],[10,1.85],[10,1.85],[7.5,1.85],[10,1.85]],
"#whatsapp_france_marketing":[[10,3.8],[10,3.8],[10,3.8],[7.5,3.8],[10,3.8]],
"#whatsapp_france_service":[[10,2.3],[10,2.3],[10,2.3],[7.5,2.3],[10,2.3]],
"#whatsapp_france_utility":[[10,2.05],[10,2.05],[10,2.05],[7.5,2.05],[10,2.05]],
"#whatsapp_germany_authentication":[[10,2.05],[10,2.05],[10,2.05],[7.5,2.05],[10,2.05]],
"#whatsapp_germany_marketing":[[10,3.6],[10,3.6],[10,3.6],[7.5,3.6],[10,3.6]],
"#whatsapp_germany_service":[[10,2.15],[10,2.15],[10,2.15],[7.5,2.15],[10,2.15]],
"#whatsapp_germany_utility":[[10,2.25],[10,2.25],[10,2.25],[7.5,2.25],[10,2.25]],
"#whatsapp_india_authentication":[["N/A","N/A"],["N/A","N/A"],["N/A","N/A"],["N/A","N/A"],["N/A",0.04]],
"#whatsapp_india_marketing":[[10,0.25],[10,0.25],[10,0.25],[7.5,0.25],[10,0.25]],
"#whatsapp_india_service":[[10,0.1],[10,0.1],[10,0.1],[7.5,0.1],[10,0.1]],
"#whatsapp_india_utility":[[10,0.1],[10,0.1],[10,0.1],[7.5,0.1],[10,0.1]],
"#whatsapp_indonesia_authentication":[["N/A","N/A"],["N/A","N/A"],["N/A","N/A"],["N/A","N/A"],["N/A",0.8]],
"#whatsapp_indonesia_marketing":[[10,1.1],[10,1.1],[10,1.1],[7.5,1.1],[10,1.1]],
"#whatsapp_indonesia_service":[[10,0.5],[10,0.5],[10,0.5],[7.5,0.5],[10,0.5]],
"#whatsapp_indonesia_utility":[[10,0.55],[10,0.55],[10,0.55],[7.5,0.55],[10,0.55]],
"#whatsapp_israel_authentication":[[10,0.45],[10,0.45],[10,0.45],[7.5,0.45],[10,0.45]],
"#whatsapp_israel_marketing":[[10,0.95],[10,0.95],[10,0.95],[7.5,0.95],[10,0.95]],
"#whatsapp_israel_service":[[10,0.5],[10,0.5],[10,0.5],[7.5,0.5],[10,0.5]],
"#whatsapp_israel_utility":[[10,0.5],[10,0.5],[10,0.5],[7.5,0.5],[10,0.5]],
"#whatsapp_italy_authentication":[[10,1],[10,1],[10,1],[7.5,1],[10,1]],
"#whatsapp_italy_marketing":[[10,1.85],[10,1.85],[10,1.85],[7.5,1.85],[10,1.85]],
"#whatsapp_italy_service":[[10,1],[10,1],[10,1],[7.5,1],[10,1]],
"#whatsapp_italy_utility":[[10,1.1],[10,1.1],[10,1.1],[7.5,1.1],[10,1.1]],
"#whatsapp_malaysia_authentication":[[10,0.5],[10,0.5],[10,0.5],[7.5,0.5],[10,0.5]],
"#whatsapp_malaysia_marketing":[[10,2.3],[10,2.3],[10,2.3],[7.5,2.3],[10,2.3]],
"#whatsapp_malaysia_service":[[10,0.6],[10,0.6],[10,0.6],[7.5,0.6],[10,0.6]],
"#whatsapp_malaysia_utility":[[10,0.55],[10,0.55],[10,0.55],[7.5,0.55],[10,0.55]],
"#whatsapp_mexico_authentication":[[10,0.65],[10,0.65],[10,0.65],[7.5,0.65],[10,0.65]],
"#whatsapp_mexico_marketing":[[10,1.15],[10,1.15],[10,1.15],[7.5,1.15],[10,1.15]],
"#whatsapp_mexico_service":[[10,0.3],[10,0.3],[10,0.3],[7.5,0.3],[10,0.3]],
"#whatsapp_mexico_utility":[[10,0.7],[10,0.7],[10,0.7],[7.5,0.7],[10,0.7]],
"#whatsapp_netherlands_authentication":[[10,1.9],[10,1.9],[10,1.9],[7.5,1.9],[10,1.9]],
"#whatsapp_netherlands_marketing":[[10,4.25],[10,4.25],[10,4.25],[7.5,4.25],[10,4.25]],
"#whatsapp_netherlands_service":[[10,2.35],[10,2.35],[10,2.35],[7.5,2.35],[10,2.35]],
"#whatsapp_netherlands_utility":[[10,2.1],[10,2.1],[10,2.1],[7.5,2.1],[10,2.1]],
"#whatsapp_nigeria_authentication":[[10,0.75],[10,0.75],[10,0.75],[7.5,0.75],[10,0.75]],
"#whatsapp_nigeria_marketing":[[10,1.35],[10,1.35],[10,1.35],[7.5,1.35],[10,1.35]],
"#whatsapp_nigeria_service":[[10,0.8],[10,0.8],[10,0.8],[7.5,0.8],[10,0.8]],
"#whatsapp_nigeria_utility":[[10,0.85],[10,0.85],[10,0.85],[7.5,0.85],[10,0.85]],
"#whatsapp_north_america_authentication":[[10,0.35],[10,0.35],[10,0.35],[7.5,0.35],[10,0.35]],
"#whatsapp_north_america_marketing":[[10,0.65],[10,0.65],[10,0.65],[7.5,0.65],[10,0.65]],
"#whatsapp_north_america_service":[[10,0.25],[10,0.25],[10,0.25],[7.5,0.25],[10,0.25]],
"#whatsapp_north_america_utility":[[10,0.4],[10,0.4],[10,0.4],[7.5,0.4],[10,0.4]],
"#whatsapp_other_authentication":[[10,0.8],[10,0.8],[10,0.8],[7.5,0.8],[10,0.8]],
"#whatsapp_other_marketing":[[10,1.6],[10,1.6],[10,1.6],[7.5,1.6],[10,1.6]],
"#whatsapp_other_service":[[10,0.4],[10,0.4],[10,0.4],[7.5,0.4],[10,0.4]],
"#whatsapp_other_utility":[[10,0.9],[10,0.9],[10,0.9],[7.5,0.9],[10,0.9]],
"#whatsapp_pakistan_authentication":[[10,0.6],[10,0.6],[10,0.6],[7.5,0.6],[10,0.6]],
"#whatsapp_pakistan_marketing":[[10,1.25],[10,1.25],[10,1.25],[7.5,1.25],[10,1.25]],
"#whatsapp_pakistan_service":[[10,0.4],[10,0.4],[10,0.4],[7.5,0.4],[10,0.4]],
"#whatsapp_pakistan_utility":[[10,0.65],[10,0.65],[10,0.65],[7.5,0.65],[10,0.65]],
"#whatsapp_peru_authentication":[[10,1],[10,1],[10,1],[7.5,1],[10,1]],
"#whatsapp_peru_marketing":[[10,1.85],[10,1.85],[10,1.85],[7.5,1.85],[10,1.85]],
"#whatsapp_peru_service":[[10,0.5],[10,0.5],[10,0.5],[7.5,0.5],[10,0.5]],
"#whatsapp_peru_utility":[[10,1.1],[10,1.1],[10,1.1],[7.5,1.1],[10,1.1]],
"#whatsapp_rest_of_africa_authentication":[[10,0.4],[10,0.4],[10,0.4],[7.5,0.4],[10,0.4]],
"#whatsapp_rest_of_africa_marketing":[[10,0.6],[10,0.6],[10,0.6],[7.5,0.6],[10,0.6]],
"#whatsapp_rest_of_africa_service":[[10,0.95],[10,0.95],[10,0.95],[7.5,0.95],[10,0.95]],
"#whatsapp_rest_of_africa_utility":[[10,0.4],[10,0.4],[10,0.4],[7.5,0.4],[10,0.4]],
"#whatsapp_rest_of_asia_pacific_authentication":[[10,1.15],[10,1.15],[10,1.15],[7.5,1.15],[10,1.15]],
"#whatsapp_rest_of_asia_pacific_marketing":[[10,1.95],[10,1.95],[10,1.95],[7.5,1.95],[10,1.95]],
"#whatsapp_rest_of_asia_pacific_service":[[10,0.6],[10,0.6],[10,0.6],[7.5,0.6],[10,0.6]],
"#whatsapp_rest_of_asia_pacific_utility":[[10,1.25],[10,1.25],[10,1.25],[7.5,1.25],[10,1.25]],
"#whatsapp_rest_of_central_-_eastern_europe_authentication":[[10,1.5],[10,1.5],[10,1.5],[7.5,1.5],[10,1.5]],
"#whatsapp_rest_of_central_-_eastern_europe_marketing":[[10,2.3],[10,2.3],[10,2.3],[7.5,2.3],[10,2.3]],
"#whatsapp_rest_of_central_-_eastern_europe_service":[[10,0.65],[10,0.65],[10,0.65],[7.5,0.65],[10,0.65]],
"#whatsapp_rest_of_central_-_eastern_europe_utility":[[10,1.65],[10,1.65],[10,1.65],[7.5,1.65],[10,1.65]],
"#whatsapp_rest_of_latin_america_authentication":[[10,1.2],[10,1.2],[10,1.2],[7.5,1.2],[10,1.2]],
"#whatsapp_rest_of_latin_america_marketing":[[10,1.95],[10,1.95],[10,1.95],[7.5,1.95],[10,1.95]],
"#whatsapp_rest_of_latin_america_service":[[10,1.1],[10,1.1],[10,1.1],[7.5,1.1],[10,1.1]],
"#whatsapp_rest_of_latin_america_utility":[[10,1.3],[10,1.3],[10,1.3],[7.5,1.3],[10,1.3]],
"#whatsapp_rest_of_middle_east_authentication":[[10,0.45],[10,0.45],[10,0.45],[7.5,0.45],[10,0.45]],
"#whatsapp_rest_of_middle_east_marketing":[[10,0.9],[10,0.9],[10,0.9],[7.5,0.9],[10,0.9]],
"#whatsapp_rest_of_middle_east_service":[[10,0.6],[10,0.6],[10,0.6],[7.5,0.6],[10,0.6]],
"#whatsapp_rest_of_middle_east_utility":[[10,0.55],[10,0.55],[10,0.55],[7.5,0.55],[10,0.55]],
"#whatsapp_rest_of_western_europe_authentication":[[10,1],[10,1],[10,1],[7.5,1],[10,1]],
"#whatsapp_rest_of_western_europe_marketing":[[10,1.55],[10,1.55],[10,1.55],[7.5,1.55],[10,1.55]],
"#whatsapp_rest_of_western_europe_service":[[10,1.05],[10,1.05],[10,1.05],[7.5,1.05],[10,1.05]],
"#whatsapp_rest_of_western_europe_utility":[[10,1.1],[10,1.1],[10,1.1],[7.5,1.1],[10,1.1]],
"#whatsapp_russia_authentication":[[10,1.15],[10,1.15],[10,1.15],[7.5,1.15],[10,1.15]],
"#whatsapp_russia_marketing":[[10,2.15],[10,2.15],[10,2.15],[7.5,2.15],[10,2.15]],
"#whatsapp_russia_service":[[10,1.05],[10,1.05],[10,1.05],[7.5,1.05],[10,1.05]],
"#whatsapp_russia_utility":[[10,1.25],[10,1.25],[10,1.25],[7.5,1.25],[10,1.25]],
"#whatsapp_saudi_arabia_authentication":[[10,0.6],[10,0.6],[10,0.6],[7.5,0.6],[10,0.6]],
"#whatsapp_saudi_arabia_marketing":[[10,1.1],[10,1.1],[10,1.1],[7.5,1.1],[10,1.1]],
"#whatsapp_saudi_arabia_service":[[10,0.5],[10,0.5],[10,0.5],[7.5,0.5],[10,0.5]],
"#whatsapp_saudi_arabia_utility":[[10,0.65],[10,0.65],[10,0.65],[7.5,0.65],[10,0.65]],
"#whatsapp_south_africa_authentication":[[10,0.5],[10,0.5],[10,0.5],[7.5,0.5],[10,0.5]],
"#whatsapp_south_africa_marketing":[[10,1],[10,1],[10,1],[7.5,1],[10,1]],
"#whatsapp_south_africa_service":[[10,0.45],[10,0.45],[10,0.45],[7.5,0.45],[10,0.45]],
"#whatsapp_south_africa_utility":[[10,0.55],[10,0.55],[10,0.55],[7.5,0.55],[10,0.55]],
"#whatsapp_spain_authentication":[[10,0.9],[10,0.9],[10,0.9],[7.5,0.9],[10,0.9]],
"#whatsapp_spain_marketing":[[10,1.65],[10,1.65],[10,1.65],[7.5,1.65],[10,1.65]],
"#whatsapp_spain_service":[[10,1],[10,1],[10,1],[7.5,1],[10,1]],
"#whatsapp_spain_utility":[[10,1],[10,1],[10,1],[7.5,1],[10,1]],
"#whatsapp_turkey_authentication":[[10,0.2],[10,0.2],[10,0.2],[7.5,0.2],[10,0.2]],
"#whatsapp_turkey_marketing":[[10,0.3],[10,0.3],[10,0.3],[7.5,0.3],[10,0.3]],
"#whatsapp_turkey_service":[[10,0.1],[10,0.1],[10,0.1],[7.5,0.1],[10,0.1]],
"#whatsapp_turkey_utility":[[10,0.25],[10,0.25],[10,0.25],[7.5,0.25],[10,0.25]],
"#whatsapp_united_arab_emirates_authentication":[[10,0.45],[10,0.45],[10,0.45],[7.5,0.45],[10,0.45]],
"#whatsapp_united_arab_emirates_marketing":[[10,0.9],[10,0.9],[10,0.9],[7.5,0.9],[10,0.9]],
"#whatsapp_united_arab_emirates_service":[[10,0.5],[10,0.5],[10,0.5],[7.5,0.5],[10,0.5]],
"#whatsapp_united_arab_emirates_utility":[[10,0.55],[10,0.55],[10,0.55],[7.5,0.55],[10,0.55]],
"#whatsapp_united_kingdom_authentication":[[10,0.95],[10,0.95],[10,0.95],[7.5,0.95],[10,0.95]],
"#whatsapp_united_kingdom_marketing":[[10,1.85],[10,1.85],[10,1.85],[7.5,1.85],[10,1.85]],
"#whatsapp_united_kingdom_service":[[10,1.05],[10,1.05],[10,1.05],[7.5,1.05],[10,1.05]],
"#whatsapp_united_kingdom_utility":[[10,1.05],[10,1.05],[10,1.05],[7.5,1.05],[10,1.05]],
}

$('#credit_type').on('change', function() {
  var credit_type = parseInt(this.value,10);
  var credit_rate = parseFloat( $('#credit_rate').val());
  if (!Number.isNaN(credit_rate)){
    update_credits(credit_type, credit_rate);
  }
});

$('#credit_rate').on('focusout', function() {
  $("#message_error").html('');
  var credit_type = parseInt($('#credit_type :selected').val(),10);
  var credit_rate = parseFloat( this.value );
  if (Number.isNaN(credit_rate)){
    $("#message_error").html('Número inválido');
    return
  }
  update_credits(credit_type, credit_rate);
});

function update_credits(credit_type, credit_rate){
  $.each(credit_map, (k,v) => {
    var ratio = v[credit_type][0];
    var multiplier = v[credit_type][1];
    var calc_credit = "N/A";
    var calc_rates = "N/A";
    if ((ratio != 'N/A') && (multiplier != 'N/A') ){
      calc_credit = (ratio * multiplier).toFixed(2);
      calc_rates = '$' + (calc_credit * credit_rate).toFixed(4);
    }
    $(k + '_ratio').html(ratio);
    $(k + '_multiplier').html(multiplier);
    $(k + '_credit').html(calc_credit);
    $(k + '_rates').html(calc_rates);
  });
}
</script>