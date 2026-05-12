---
nav_title: Message Credits - Calculator
permalink: "/message_credits_calc/"
hidden: true
noindex: true
hide_toc: true
---

# Message Credits - Calculator

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
Message Credits:
<select id="credit_type">
<option value="0">Delta</option>
<option value="1">Theta</option>
<option value="2">Gamma</option>
<option value="3">Sigma</option>
<option value="4">Lambda</option>
</select><br />
Credit Unit Rates: <input type="text" id="credit_rate" value="0" />
<div id="message_error"></div><br /><br />
<table>
  <tr>
    <th>
      Channel
    </th>
    <th>
      Credit Ratio
    </th>
    <th>
      Destination
    </th>
    <th>
      Multiplier
    </th>
    <th>
      Credits /Message
    </th>
    <th>
      Impied Rates
    </th>
  </tr>
  <tr><td>SMS - US / CA</td><td id="sms_-_us_ca_united_states_ratio"></td><td>United States</td><td id="sms_-_us_ca_united_states_multipler"></td><td id="sms_-_us_ca_united_states_credit"></td><td id="sms_-_us_ca_united_states_rates"></td></tr>
  <tr><td>SMS - US / CA</td><td id="sms_-_us_ca_united_states_toll_free_ratio"></td><td>United States Toll Free</td><td id="sms_-_us_ca_united_states_toll_free_multipler"></td><td id="sms_-_us_ca_united_states_toll_free_credit"></td><td id="sms_-_us_ca_united_states_toll_free_rates"></td></tr>
  <tr><td>SMS - US / CA</td><td id="sms_-_us_ca_canada_ratio"></td><td>Canada</td><td id="sms_-_us_ca_canada_multipler"></td><td id="sms_-_us_ca_canada_credit"></td><td id="sms_-_us_ca_canada_rates"></td></tr>
  <tr><td>SMS - US / CA</td><td id="sms_-_us_ca_canada_toll_free_ratio"></td><td>Canada Toll Free</td><td id="sms_-_us_ca_canada_toll_free_multipler"></td><td id="sms_-_us_ca_canada_toll_free_credit"></td><td id="sms_-_us_ca_canada_toll_free_rates"></td></tr>
  <tr><td>MMS - US / CA</td><td id="mms_-_us_ca_united_states_ratio"></td><td>United States</td><td id="mms_-_us_ca_united_states_multipler"></td><td id="mms_-_us_ca_united_states_credit"></td><td id="mms_-_us_ca_united_states_rates"></td></tr>
  <tr><td>MMS - US / CA</td><td id="mms_-_us_ca_united_states_toll_free_ratio"></td><td>United States Toll Free</td><td id="mms_-_us_ca_united_states_toll_free_multipler"></td><td id="mms_-_us_ca_united_states_toll_free_credit"></td><td id="mms_-_us_ca_united_states_toll_free_rates"></td></tr>
  <tr><td>MMS - US / CA</td><td id="mms_-_us_ca_canada_long_code_ratio"></td><td>Canada Long Code</td><td id="mms_-_us_ca_canada_long_code_multipler"></td><td id="mms_-_us_ca_canada_long_code_credit"></td><td id="mms_-_us_ca_canada_long_code_rates"></td></tr>
  <tr><td>MMS - US / CA</td><td id="mms_-_us_ca_canada_short_code_ratio"></td><td>Canada Short Code</td><td id="mms_-_us_ca_canada_short_code_multipler"></td><td id="mms_-_us_ca_canada_short_code_credit"></td><td id="mms_-_us_ca_canada_short_code_rates"></td></tr>
  <tr><td>MMS - US / CA</td><td id="mms_-_us_ca_canada_toll_free_ratio"></td><td>Canada Toll Free</td><td id="mms_-_us_ca_canada_toll_free_multipler"></td><td id="mms_-_us_ca_canada_toll_free_credit"></td><td id="mms_-_us_ca_canada_toll_free_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_abkhazia_ratio"></td><td>Abkhazia</td><td id="sms_mms_-_global_abkhazia_multipler"></td><td id="sms_mms_-_global_abkhazia_credit"></td><td id="sms_mms_-_global_abkhazia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_afghanistan_ratio"></td><td>Afghanistan</td><td id="sms_mms_-_global_afghanistan_multipler"></td><td id="sms_mms_-_global_afghanistan_credit"></td><td id="sms_mms_-_global_afghanistan_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_albania_ratio"></td><td>Albania</td><td id="sms_mms_-_global_albania_multipler"></td><td id="sms_mms_-_global_albania_credit"></td><td id="sms_mms_-_global_albania_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_algeria_ratio"></td><td>Algeria</td><td id="sms_mms_-_global_algeria_multipler"></td><td id="sms_mms_-_global_algeria_credit"></td><td id="sms_mms_-_global_algeria_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_american_samoa_ratio"></td><td>American Samoa</td><td id="sms_mms_-_global_american_samoa_multipler"></td><td id="sms_mms_-_global_american_samoa_credit"></td><td id="sms_mms_-_global_american_samoa_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_andorra_ratio"></td><td>Andorra</td><td id="sms_mms_-_global_andorra_multipler"></td><td id="sms_mms_-_global_andorra_credit"></td><td id="sms_mms_-_global_andorra_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_angola_ratio"></td><td>Angola</td><td id="sms_mms_-_global_angola_multipler"></td><td id="sms_mms_-_global_angola_credit"></td><td id="sms_mms_-_global_angola_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_anguilla_ratio"></td><td>Anguilla</td><td id="sms_mms_-_global_anguilla_multipler"></td><td id="sms_mms_-_global_anguilla_credit"></td><td id="sms_mms_-_global_anguilla_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_antigua_and_barbuda_ratio"></td><td>Antigua and Barbuda</td><td id="sms_mms_-_global_antigua_and_barbuda_multipler"></td><td id="sms_mms_-_global_antigua_and_barbuda_credit"></td><td id="sms_mms_-_global_antigua_and_barbuda_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_argentina_ratio"></td><td>Argentina</td><td id="sms_mms_-_global_argentina_multipler"></td><td id="sms_mms_-_global_argentina_credit"></td><td id="sms_mms_-_global_argentina_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_armenia_ratio"></td><td>Armenia</td><td id="sms_mms_-_global_armenia_multipler"></td><td id="sms_mms_-_global_armenia_credit"></td><td id="sms_mms_-_global_armenia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_aruba_ratio"></td><td>Aruba</td><td id="sms_mms_-_global_aruba_multipler"></td><td id="sms_mms_-_global_aruba_credit"></td><td id="sms_mms_-_global_aruba_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_australia_sms_ratio"></td><td>Australia SMS</td><td id="sms_mms_-_global_australia_sms_multipler"></td><td id="sms_mms_-_global_australia_sms_credit"></td><td id="sms_mms_-_global_australia_sms_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_australia_mms_ratio"></td><td>Australia MMS</td><td id="sms_mms_-_global_australia_mms_multipler"></td><td id="sms_mms_-_global_australia_mms_credit"></td><td id="sms_mms_-_global_australia_mms_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_austria_ratio"></td><td>Austria</td><td id="sms_mms_-_global_austria_multipler"></td><td id="sms_mms_-_global_austria_credit"></td><td id="sms_mms_-_global_austria_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_azerbaijan_ratio"></td><td>Azerbaijan</td><td id="sms_mms_-_global_azerbaijan_multipler"></td><td id="sms_mms_-_global_azerbaijan_credit"></td><td id="sms_mms_-_global_azerbaijan_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_bahamas_ratio"></td><td>Bahamas</td><td id="sms_mms_-_global_bahamas_multipler"></td><td id="sms_mms_-_global_bahamas_credit"></td><td id="sms_mms_-_global_bahamas_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_bahrain_ratio"></td><td>Bahrain</td><td id="sms_mms_-_global_bahrain_multipler"></td><td id="sms_mms_-_global_bahrain_credit"></td><td id="sms_mms_-_global_bahrain_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_bangladesh_ratio"></td><td>Bangladesh</td><td id="sms_mms_-_global_bangladesh_multipler"></td><td id="sms_mms_-_global_bangladesh_credit"></td><td id="sms_mms_-_global_bangladesh_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_barbados_ratio"></td><td>Barbados</td><td id="sms_mms_-_global_barbados_multipler"></td><td id="sms_mms_-_global_barbados_credit"></td><td id="sms_mms_-_global_barbados_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_belarus_ratio"></td><td>Belarus</td><td id="sms_mms_-_global_belarus_multipler"></td><td id="sms_mms_-_global_belarus_credit"></td><td id="sms_mms_-_global_belarus_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_belgium_ratio"></td><td>Belgium</td><td id="sms_mms_-_global_belgium_multipler"></td><td id="sms_mms_-_global_belgium_credit"></td><td id="sms_mms_-_global_belgium_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_belize_ratio"></td><td>Belize</td><td id="sms_mms_-_global_belize_multipler"></td><td id="sms_mms_-_global_belize_credit"></td><td id="sms_mms_-_global_belize_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_benin_ratio"></td><td>Benin</td><td id="sms_mms_-_global_benin_multipler"></td><td id="sms_mms_-_global_benin_credit"></td><td id="sms_mms_-_global_benin_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_bermuda_ratio"></td><td>Bermuda</td><td id="sms_mms_-_global_bermuda_multipler"></td><td id="sms_mms_-_global_bermuda_credit"></td><td id="sms_mms_-_global_bermuda_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_bhutan_ratio"></td><td>Bhutan</td><td id="sms_mms_-_global_bhutan_multipler"></td><td id="sms_mms_-_global_bhutan_credit"></td><td id="sms_mms_-_global_bhutan_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_bolivia_ratio"></td><td>Bolivia</td><td id="sms_mms_-_global_bolivia_multipler"></td><td id="sms_mms_-_global_bolivia_credit"></td><td id="sms_mms_-_global_bolivia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_bosnia_and_herzegovina_ratio"></td><td>Bosnia and Herzegovina</td><td id="sms_mms_-_global_bosnia_and_herzegovina_multipler"></td><td id="sms_mms_-_global_bosnia_and_herzegovina_credit"></td><td id="sms_mms_-_global_bosnia_and_herzegovina_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_botswana_ratio"></td><td>Botswana</td><td id="sms_mms_-_global_botswana_multipler"></td><td id="sms_mms_-_global_botswana_credit"></td><td id="sms_mms_-_global_botswana_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_brazil_ratio"></td><td>Brazil</td><td id="sms_mms_-_global_brazil_multipler"></td><td id="sms_mms_-_global_brazil_credit"></td><td id="sms_mms_-_global_brazil_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_brunei_ratio"></td><td>Brunei</td><td id="sms_mms_-_global_brunei_multipler"></td><td id="sms_mms_-_global_brunei_credit"></td><td id="sms_mms_-_global_brunei_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_bulgaria_ratio"></td><td>Bulgaria</td><td id="sms_mms_-_global_bulgaria_multipler"></td><td id="sms_mms_-_global_bulgaria_credit"></td><td id="sms_mms_-_global_bulgaria_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_burkina_faso_ratio"></td><td>Burkina Faso</td><td id="sms_mms_-_global_burkina_faso_multipler"></td><td id="sms_mms_-_global_burkina_faso_credit"></td><td id="sms_mms_-_global_burkina_faso_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_burundi_ratio"></td><td>Burundi</td><td id="sms_mms_-_global_burundi_multipler"></td><td id="sms_mms_-_global_burundi_credit"></td><td id="sms_mms_-_global_burundi_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_cambodia_ratio"></td><td>Cambodia</td><td id="sms_mms_-_global_cambodia_multipler"></td><td id="sms_mms_-_global_cambodia_credit"></td><td id="sms_mms_-_global_cambodia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_cameroon_ratio"></td><td>Cameroon</td><td id="sms_mms_-_global_cameroon_multipler"></td><td id="sms_mms_-_global_cameroon_credit"></td><td id="sms_mms_-_global_cameroon_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_cape_verde_ratio"></td><td>Cape Verde</td><td id="sms_mms_-_global_cape_verde_multipler"></td><td id="sms_mms_-_global_cape_verde_credit"></td><td id="sms_mms_-_global_cape_verde_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_caribbean_netherlands_ratio"></td><td>Caribbean Netherlands</td><td id="sms_mms_-_global_caribbean_netherlands_multipler"></td><td id="sms_mms_-_global_caribbean_netherlands_credit"></td><td id="sms_mms_-_global_caribbean_netherlands_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_cayman_islands_ratio"></td><td>Cayman Islands</td><td id="sms_mms_-_global_cayman_islands_multipler"></td><td id="sms_mms_-_global_cayman_islands_credit"></td><td id="sms_mms_-_global_cayman_islands_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_central_african_republic_ratio"></td><td>Central African Republic</td><td id="sms_mms_-_global_central_african_republic_multipler"></td><td id="sms_mms_-_global_central_african_republic_credit"></td><td id="sms_mms_-_global_central_african_republic_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_chad_ratio"></td><td>Chad</td><td id="sms_mms_-_global_chad_multipler"></td><td id="sms_mms_-_global_chad_credit"></td><td id="sms_mms_-_global_chad_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_chile_ratio"></td><td>Chile</td><td id="sms_mms_-_global_chile_multipler"></td><td id="sms_mms_-_global_chile_credit"></td><td id="sms_mms_-_global_chile_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_china_ratio"></td><td>China</td><td id="sms_mms_-_global_china_multipler"></td><td id="sms_mms_-_global_china_credit"></td><td id="sms_mms_-_global_china_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_colombia_ratio"></td><td>Colombia</td><td id="sms_mms_-_global_colombia_multipler"></td><td id="sms_mms_-_global_colombia_credit"></td><td id="sms_mms_-_global_colombia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_comoros_ratio"></td><td>Comoros</td><td id="sms_mms_-_global_comoros_multipler"></td><td id="sms_mms_-_global_comoros_credit"></td><td id="sms_mms_-_global_comoros_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_congo_ratio"></td><td>Congo</td><td id="sms_mms_-_global_congo_multipler"></td><td id="sms_mms_-_global_congo_credit"></td><td id="sms_mms_-_global_congo_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_cook_islands_ratio"></td><td>Cook Islands</td><td id="sms_mms_-_global_cook_islands_multipler"></td><td id="sms_mms_-_global_cook_islands_credit"></td><td id="sms_mms_-_global_cook_islands_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_costa_rica_ratio"></td><td>Costa Rica</td><td id="sms_mms_-_global_costa_rica_multipler"></td><td id="sms_mms_-_global_costa_rica_credit"></td><td id="sms_mms_-_global_costa_rica_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_croatia_ratio"></td><td>Croatia</td><td id="sms_mms_-_global_croatia_multipler"></td><td id="sms_mms_-_global_croatia_credit"></td><td id="sms_mms_-_global_croatia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_cuba_ratio"></td><td>Cuba</td><td id="sms_mms_-_global_cuba_multipler"></td><td id="sms_mms_-_global_cuba_credit"></td><td id="sms_mms_-_global_cuba_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_curacao_ratio"></td><td>Curacao</td><td id="sms_mms_-_global_curacao_multipler"></td><td id="sms_mms_-_global_curacao_credit"></td><td id="sms_mms_-_global_curacao_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_cyprus_ratio"></td><td>Cyprus</td><td id="sms_mms_-_global_cyprus_multipler"></td><td id="sms_mms_-_global_cyprus_credit"></td><td id="sms_mms_-_global_cyprus_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_czech_republic_ratio"></td><td>Czech Republic</td><td id="sms_mms_-_global_czech_republic_multipler"></td><td id="sms_mms_-_global_czech_republic_credit"></td><td id="sms_mms_-_global_czech_republic_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_denmark_ratio"></td><td>Denmark</td><td id="sms_mms_-_global_denmark_multipler"></td><td id="sms_mms_-_global_denmark_credit"></td><td id="sms_mms_-_global_denmark_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_djibouti_ratio"></td><td>Djibouti</td><td id="sms_mms_-_global_djibouti_multipler"></td><td id="sms_mms_-_global_djibouti_credit"></td><td id="sms_mms_-_global_djibouti_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_dominica_ratio"></td><td>Dominica</td><td id="sms_mms_-_global_dominica_multipler"></td><td id="sms_mms_-_global_dominica_credit"></td><td id="sms_mms_-_global_dominica_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_dominican_republic_ratio"></td><td>Dominican Republic</td><td id="sms_mms_-_global_dominican_republic_multipler"></td><td id="sms_mms_-_global_dominican_republic_credit"></td><td id="sms_mms_-_global_dominican_republic_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_dr_congo_ratio"></td><td>DR Congo</td><td id="sms_mms_-_global_dr_congo_multipler"></td><td id="sms_mms_-_global_dr_congo_credit"></td><td id="sms_mms_-_global_dr_congo_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_ecuador_ratio"></td><td>Ecuador</td><td id="sms_mms_-_global_ecuador_multipler"></td><td id="sms_mms_-_global_ecuador_credit"></td><td id="sms_mms_-_global_ecuador_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_egypt_ratio"></td><td>Egypt</td><td id="sms_mms_-_global_egypt_multipler"></td><td id="sms_mms_-_global_egypt_credit"></td><td id="sms_mms_-_global_egypt_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_el_salvador_ratio"></td><td>El Salvador</td><td id="sms_mms_-_global_el_salvador_multipler"></td><td id="sms_mms_-_global_el_salvador_credit"></td><td id="sms_mms_-_global_el_salvador_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_equatorial_guinea_ratio"></td><td>Equatorial Guinea</td><td id="sms_mms_-_global_equatorial_guinea_multipler"></td><td id="sms_mms_-_global_equatorial_guinea_credit"></td><td id="sms_mms_-_global_equatorial_guinea_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_eritrea_ratio"></td><td>Eritrea</td><td id="sms_mms_-_global_eritrea_multipler"></td><td id="sms_mms_-_global_eritrea_credit"></td><td id="sms_mms_-_global_eritrea_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_estonia_ratio"></td><td>Estonia</td><td id="sms_mms_-_global_estonia_multipler"></td><td id="sms_mms_-_global_estonia_credit"></td><td id="sms_mms_-_global_estonia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_eswatini_ratio"></td><td>Eswatini</td><td id="sms_mms_-_global_eswatini_multipler"></td><td id="sms_mms_-_global_eswatini_credit"></td><td id="sms_mms_-_global_eswatini_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_ethiopia_ratio"></td><td>Ethiopia</td><td id="sms_mms_-_global_ethiopia_multipler"></td><td id="sms_mms_-_global_ethiopia_credit"></td><td id="sms_mms_-_global_ethiopia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_falkland_islands_ratio"></td><td>Falkland Islands</td><td id="sms_mms_-_global_falkland_islands_multipler"></td><td id="sms_mms_-_global_falkland_islands_credit"></td><td id="sms_mms_-_global_falkland_islands_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_faroe_islands_ratio"></td><td>Faroe Islands</td><td id="sms_mms_-_global_faroe_islands_multipler"></td><td id="sms_mms_-_global_faroe_islands_credit"></td><td id="sms_mms_-_global_faroe_islands_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_fiji_ratio"></td><td>Fiji</td><td id="sms_mms_-_global_fiji_multipler"></td><td id="sms_mms_-_global_fiji_credit"></td><td id="sms_mms_-_global_fiji_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_finland_ratio"></td><td>Finland</td><td id="sms_mms_-_global_finland_multipler"></td><td id="sms_mms_-_global_finland_credit"></td><td id="sms_mms_-_global_finland_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_france_ratio"></td><td>France</td><td id="sms_mms_-_global_france_multipler"></td><td id="sms_mms_-_global_france_credit"></td><td id="sms_mms_-_global_france_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_french_guiana_ratio"></td><td>French Guiana</td><td id="sms_mms_-_global_french_guiana_multipler"></td><td id="sms_mms_-_global_french_guiana_credit"></td><td id="sms_mms_-_global_french_guiana_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_french_polynesia_ratio"></td><td>French Polynesia</td><td id="sms_mms_-_global_french_polynesia_multipler"></td><td id="sms_mms_-_global_french_polynesia_credit"></td><td id="sms_mms_-_global_french_polynesia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_gabon_ratio"></td><td>Gabon</td><td id="sms_mms_-_global_gabon_multipler"></td><td id="sms_mms_-_global_gabon_credit"></td><td id="sms_mms_-_global_gabon_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_gambia_ratio"></td><td>Gambia</td><td id="sms_mms_-_global_gambia_multipler"></td><td id="sms_mms_-_global_gambia_credit"></td><td id="sms_mms_-_global_gambia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_georgia_ratio"></td><td>Georgia</td><td id="sms_mms_-_global_georgia_multipler"></td><td id="sms_mms_-_global_georgia_credit"></td><td id="sms_mms_-_global_georgia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_germany_ratio"></td><td>Germany</td><td id="sms_mms_-_global_germany_multipler"></td><td id="sms_mms_-_global_germany_credit"></td><td id="sms_mms_-_global_germany_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_ghana_ratio"></td><td>Ghana</td><td id="sms_mms_-_global_ghana_multipler"></td><td id="sms_mms_-_global_ghana_credit"></td><td id="sms_mms_-_global_ghana_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_gibraltar_ratio"></td><td>Gibraltar</td><td id="sms_mms_-_global_gibraltar_multipler"></td><td id="sms_mms_-_global_gibraltar_credit"></td><td id="sms_mms_-_global_gibraltar_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_greece_ratio"></td><td>Greece</td><td id="sms_mms_-_global_greece_multipler"></td><td id="sms_mms_-_global_greece_credit"></td><td id="sms_mms_-_global_greece_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_greenland_ratio"></td><td>Greenland</td><td id="sms_mms_-_global_greenland_multipler"></td><td id="sms_mms_-_global_greenland_credit"></td><td id="sms_mms_-_global_greenland_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_grenada_ratio"></td><td>Grenada</td><td id="sms_mms_-_global_grenada_multipler"></td><td id="sms_mms_-_global_grenada_credit"></td><td id="sms_mms_-_global_grenada_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_guadeloupe_ratio"></td><td>Guadeloupe</td><td id="sms_mms_-_global_guadeloupe_multipler"></td><td id="sms_mms_-_global_guadeloupe_credit"></td><td id="sms_mms_-_global_guadeloupe_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_guam_ratio"></td><td>Guam</td><td id="sms_mms_-_global_guam_multipler"></td><td id="sms_mms_-_global_guam_credit"></td><td id="sms_mms_-_global_guam_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_guatemala_ratio"></td><td>Guatemala</td><td id="sms_mms_-_global_guatemala_multipler"></td><td id="sms_mms_-_global_guatemala_credit"></td><td id="sms_mms_-_global_guatemala_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_guernsey_ratio"></td><td>Guernsey</td><td id="sms_mms_-_global_guernsey_multipler"></td><td id="sms_mms_-_global_guernsey_credit"></td><td id="sms_mms_-_global_guernsey_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_guinea_ratio"></td><td>Guinea</td><td id="sms_mms_-_global_guinea_multipler"></td><td id="sms_mms_-_global_guinea_credit"></td><td id="sms_mms_-_global_guinea_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_guinea-bissau_ratio"></td><td>Guinea-Bissau</td><td id="sms_mms_-_global_guinea-bissau_multipler"></td><td id="sms_mms_-_global_guinea-bissau_credit"></td><td id="sms_mms_-_global_guinea-bissau_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_guyana_ratio"></td><td>Guyana</td><td id="sms_mms_-_global_guyana_multipler"></td><td id="sms_mms_-_global_guyana_credit"></td><td id="sms_mms_-_global_guyana_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_haiti_ratio"></td><td>Haiti</td><td id="sms_mms_-_global_haiti_multipler"></td><td id="sms_mms_-_global_haiti_credit"></td><td id="sms_mms_-_global_haiti_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_honduras_ratio"></td><td>Honduras</td><td id="sms_mms_-_global_honduras_multipler"></td><td id="sms_mms_-_global_honduras_credit"></td><td id="sms_mms_-_global_honduras_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_hong_kong_ratio"></td><td>Hong Kong</td><td id="sms_mms_-_global_hong_kong_multipler"></td><td id="sms_mms_-_global_hong_kong_credit"></td><td id="sms_mms_-_global_hong_kong_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_hungary_ratio"></td><td>Hungary</td><td id="sms_mms_-_global_hungary_multipler"></td><td id="sms_mms_-_global_hungary_credit"></td><td id="sms_mms_-_global_hungary_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_iceland_ratio"></td><td>Iceland</td><td id="sms_mms_-_global_iceland_multipler"></td><td id="sms_mms_-_global_iceland_credit"></td><td id="sms_mms_-_global_iceland_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_india_ratio"></td><td>India</td><td id="sms_mms_-_global_india_multipler"></td><td id="sms_mms_-_global_india_credit"></td><td id="sms_mms_-_global_india_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_indonesia_ratio"></td><td>Indonesia</td><td id="sms_mms_-_global_indonesia_multipler"></td><td id="sms_mms_-_global_indonesia_credit"></td><td id="sms_mms_-_global_indonesia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_iran_ratio"></td><td>Iran</td><td id="sms_mms_-_global_iran_multipler"></td><td id="sms_mms_-_global_iran_credit"></td><td id="sms_mms_-_global_iran_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_iraq_ratio"></td><td>Iraq</td><td id="sms_mms_-_global_iraq_multipler"></td><td id="sms_mms_-_global_iraq_credit"></td><td id="sms_mms_-_global_iraq_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_ireland_ratio"></td><td>Ireland</td><td id="sms_mms_-_global_ireland_multipler"></td><td id="sms_mms_-_global_ireland_credit"></td><td id="sms_mms_-_global_ireland_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_isle_of_man_ratio"></td><td>Isle of Man</td><td id="sms_mms_-_global_isle_of_man_multipler"></td><td id="sms_mms_-_global_isle_of_man_credit"></td><td id="sms_mms_-_global_isle_of_man_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_israel_ratio"></td><td>Israel</td><td id="sms_mms_-_global_israel_multipler"></td><td id="sms_mms_-_global_israel_credit"></td><td id="sms_mms_-_global_israel_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_italy_ratio"></td><td>Italy</td><td id="sms_mms_-_global_italy_multipler"></td><td id="sms_mms_-_global_italy_credit"></td><td id="sms_mms_-_global_italy_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_ivory_coast_ratio"></td><td>Ivory Coast</td><td id="sms_mms_-_global_ivory_coast_multipler"></td><td id="sms_mms_-_global_ivory_coast_credit"></td><td id="sms_mms_-_global_ivory_coast_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_jamaica_ratio"></td><td>Jamaica</td><td id="sms_mms_-_global_jamaica_multipler"></td><td id="sms_mms_-_global_jamaica_credit"></td><td id="sms_mms_-_global_jamaica_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_japan_ratio"></td><td>Japan</td><td id="sms_mms_-_global_japan_multipler"></td><td id="sms_mms_-_global_japan_credit"></td><td id="sms_mms_-_global_japan_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_jersey_ratio"></td><td>Jersey</td><td id="sms_mms_-_global_jersey_multipler"></td><td id="sms_mms_-_global_jersey_credit"></td><td id="sms_mms_-_global_jersey_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_jordan_ratio"></td><td>Jordan</td><td id="sms_mms_-_global_jordan_multipler"></td><td id="sms_mms_-_global_jordan_credit"></td><td id="sms_mms_-_global_jordan_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_kazakhstan_ratio"></td><td>Kazakhstan</td><td id="sms_mms_-_global_kazakhstan_multipler"></td><td id="sms_mms_-_global_kazakhstan_credit"></td><td id="sms_mms_-_global_kazakhstan_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_kenya_ratio"></td><td>Kenya</td><td id="sms_mms_-_global_kenya_multipler"></td><td id="sms_mms_-_global_kenya_credit"></td><td id="sms_mms_-_global_kenya_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_kiribati_ratio"></td><td>Kiribati</td><td id="sms_mms_-_global_kiribati_multipler"></td><td id="sms_mms_-_global_kiribati_credit"></td><td id="sms_mms_-_global_kiribati_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_korea_republic_of_ratio"></td><td>Korea Republic of</td><td id="sms_mms_-_global_korea_republic_of_multipler"></td><td id="sms_mms_-_global_korea_republic_of_credit"></td><td id="sms_mms_-_global_korea_republic_of_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_kosovo_ratio"></td><td>Kosovo</td><td id="sms_mms_-_global_kosovo_multipler"></td><td id="sms_mms_-_global_kosovo_credit"></td><td id="sms_mms_-_global_kosovo_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_kuwait_ratio"></td><td>Kuwait</td><td id="sms_mms_-_global_kuwait_multipler"></td><td id="sms_mms_-_global_kuwait_credit"></td><td id="sms_mms_-_global_kuwait_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_kyrgyzstan_ratio"></td><td>Kyrgyzstan</td><td id="sms_mms_-_global_kyrgyzstan_multipler"></td><td id="sms_mms_-_global_kyrgyzstan_credit"></td><td id="sms_mms_-_global_kyrgyzstan_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_laos_pdr_ratio"></td><td>Laos PDR</td><td id="sms_mms_-_global_laos_pdr_multipler"></td><td id="sms_mms_-_global_laos_pdr_credit"></td><td id="sms_mms_-_global_laos_pdr_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_latvia_ratio"></td><td>Latvia</td><td id="sms_mms_-_global_latvia_multipler"></td><td id="sms_mms_-_global_latvia_credit"></td><td id="sms_mms_-_global_latvia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_lebanon_ratio"></td><td>Lebanon</td><td id="sms_mms_-_global_lebanon_multipler"></td><td id="sms_mms_-_global_lebanon_credit"></td><td id="sms_mms_-_global_lebanon_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_lesotho_ratio"></td><td>Lesotho</td><td id="sms_mms_-_global_lesotho_multipler"></td><td id="sms_mms_-_global_lesotho_credit"></td><td id="sms_mms_-_global_lesotho_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_liberia_ratio"></td><td>Liberia</td><td id="sms_mms_-_global_liberia_multipler"></td><td id="sms_mms_-_global_liberia_credit"></td><td id="sms_mms_-_global_liberia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_libya_ratio"></td><td>Libya</td><td id="sms_mms_-_global_libya_multipler"></td><td id="sms_mms_-_global_libya_credit"></td><td id="sms_mms_-_global_libya_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_liechtenstein_ratio"></td><td>Liechtenstein</td><td id="sms_mms_-_global_liechtenstein_multipler"></td><td id="sms_mms_-_global_liechtenstein_credit"></td><td id="sms_mms_-_global_liechtenstein_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_lithuania_ratio"></td><td>Lithuania</td><td id="sms_mms_-_global_lithuania_multipler"></td><td id="sms_mms_-_global_lithuania_credit"></td><td id="sms_mms_-_global_lithuania_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_luxembourg_ratio"></td><td>Luxembourg</td><td id="sms_mms_-_global_luxembourg_multipler"></td><td id="sms_mms_-_global_luxembourg_credit"></td><td id="sms_mms_-_global_luxembourg_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_macao_ratio"></td><td>Macao</td><td id="sms_mms_-_global_macao_multipler"></td><td id="sms_mms_-_global_macao_credit"></td><td id="sms_mms_-_global_macao_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_macedonia_ratio"></td><td>Macedonia</td><td id="sms_mms_-_global_macedonia_multipler"></td><td id="sms_mms_-_global_macedonia_credit"></td><td id="sms_mms_-_global_macedonia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_madagascar_ratio"></td><td>Madagascar</td><td id="sms_mms_-_global_madagascar_multipler"></td><td id="sms_mms_-_global_madagascar_credit"></td><td id="sms_mms_-_global_madagascar_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_malawi_ratio"></td><td>Malawi</td><td id="sms_mms_-_global_malawi_multipler"></td><td id="sms_mms_-_global_malawi_credit"></td><td id="sms_mms_-_global_malawi_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_malaysia_ratio"></td><td>Malaysia</td><td id="sms_mms_-_global_malaysia_multipler"></td><td id="sms_mms_-_global_malaysia_credit"></td><td id="sms_mms_-_global_malaysia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_maldives_ratio"></td><td>Maldives</td><td id="sms_mms_-_global_maldives_multipler"></td><td id="sms_mms_-_global_maldives_credit"></td><td id="sms_mms_-_global_maldives_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_mali_ratio"></td><td>Mali</td><td id="sms_mms_-_global_mali_multipler"></td><td id="sms_mms_-_global_mali_credit"></td><td id="sms_mms_-_global_mali_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_malta_ratio"></td><td>Malta</td><td id="sms_mms_-_global_malta_multipler"></td><td id="sms_mms_-_global_malta_credit"></td><td id="sms_mms_-_global_malta_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_marshall_islands_ratio"></td><td>Marshall Islands</td><td id="sms_mms_-_global_marshall_islands_multipler"></td><td id="sms_mms_-_global_marshall_islands_credit"></td><td id="sms_mms_-_global_marshall_islands_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_martinique_ratio"></td><td>Martinique</td><td id="sms_mms_-_global_martinique_multipler"></td><td id="sms_mms_-_global_martinique_credit"></td><td id="sms_mms_-_global_martinique_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_mauritania_ratio"></td><td>Mauritania</td><td id="sms_mms_-_global_mauritania_multipler"></td><td id="sms_mms_-_global_mauritania_credit"></td><td id="sms_mms_-_global_mauritania_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_mauritius_ratio"></td><td>Mauritius</td><td id="sms_mms_-_global_mauritius_multipler"></td><td id="sms_mms_-_global_mauritius_credit"></td><td id="sms_mms_-_global_mauritius_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_mayotte_ratio"></td><td>Mayotte</td><td id="sms_mms_-_global_mayotte_multipler"></td><td id="sms_mms_-_global_mayotte_credit"></td><td id="sms_mms_-_global_mayotte_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_mexico_ratio"></td><td>Mexico</td><td id="sms_mms_-_global_mexico_multipler"></td><td id="sms_mms_-_global_mexico_credit"></td><td id="sms_mms_-_global_mexico_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_micronesia_ratio"></td><td>Micronesia</td><td id="sms_mms_-_global_micronesia_multipler"></td><td id="sms_mms_-_global_micronesia_credit"></td><td id="sms_mms_-_global_micronesia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_moldova_ratio"></td><td>Moldova</td><td id="sms_mms_-_global_moldova_multipler"></td><td id="sms_mms_-_global_moldova_credit"></td><td id="sms_mms_-_global_moldova_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_monaco_ratio"></td><td>Monaco</td><td id="sms_mms_-_global_monaco_multipler"></td><td id="sms_mms_-_global_monaco_credit"></td><td id="sms_mms_-_global_monaco_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_mongolia_ratio"></td><td>Mongolia</td><td id="sms_mms_-_global_mongolia_multipler"></td><td id="sms_mms_-_global_mongolia_credit"></td><td id="sms_mms_-_global_mongolia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_montenegro_ratio"></td><td>Montenegro</td><td id="sms_mms_-_global_montenegro_multipler"></td><td id="sms_mms_-_global_montenegro_credit"></td><td id="sms_mms_-_global_montenegro_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_montserrat_ratio"></td><td>Montserrat</td><td id="sms_mms_-_global_montserrat_multipler"></td><td id="sms_mms_-_global_montserrat_credit"></td><td id="sms_mms_-_global_montserrat_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_morocco_ratio"></td><td>Morocco</td><td id="sms_mms_-_global_morocco_multipler"></td><td id="sms_mms_-_global_morocco_credit"></td><td id="sms_mms_-_global_morocco_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_mozambique_ratio"></td><td>Mozambique</td><td id="sms_mms_-_global_mozambique_multipler"></td><td id="sms_mms_-_global_mozambique_credit"></td><td id="sms_mms_-_global_mozambique_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_myanmar_ratio"></td><td>Myanmar</td><td id="sms_mms_-_global_myanmar_multipler"></td><td id="sms_mms_-_global_myanmar_credit"></td><td id="sms_mms_-_global_myanmar_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_namibia_ratio"></td><td>Namibia</td><td id="sms_mms_-_global_namibia_multipler"></td><td id="sms_mms_-_global_namibia_credit"></td><td id="sms_mms_-_global_namibia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_nauru_ratio"></td><td>Nauru</td><td id="sms_mms_-_global_nauru_multipler"></td><td id="sms_mms_-_global_nauru_credit"></td><td id="sms_mms_-_global_nauru_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_nepal_ratio"></td><td>Nepal</td><td id="sms_mms_-_global_nepal_multipler"></td><td id="sms_mms_-_global_nepal_credit"></td><td id="sms_mms_-_global_nepal_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_netherlands_ratio"></td><td>Netherlands</td><td id="sms_mms_-_global_netherlands_multipler"></td><td id="sms_mms_-_global_netherlands_credit"></td><td id="sms_mms_-_global_netherlands_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_new_caledonia_ratio"></td><td>New Caledonia</td><td id="sms_mms_-_global_new_caledonia_multipler"></td><td id="sms_mms_-_global_new_caledonia_credit"></td><td id="sms_mms_-_global_new_caledonia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_new_zealand_ratio"></td><td>New Zealand</td><td id="sms_mms_-_global_new_zealand_multipler"></td><td id="sms_mms_-_global_new_zealand_credit"></td><td id="sms_mms_-_global_new_zealand_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_nicaragua_ratio"></td><td>Nicaragua</td><td id="sms_mms_-_global_nicaragua_multipler"></td><td id="sms_mms_-_global_nicaragua_credit"></td><td id="sms_mms_-_global_nicaragua_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_niger_ratio"></td><td>Niger</td><td id="sms_mms_-_global_niger_multipler"></td><td id="sms_mms_-_global_niger_credit"></td><td id="sms_mms_-_global_niger_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_nigeria_ratio"></td><td>Nigeria</td><td id="sms_mms_-_global_nigeria_multipler"></td><td id="sms_mms_-_global_nigeria_credit"></td><td id="sms_mms_-_global_nigeria_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_niue_ratio"></td><td>Niue</td><td id="sms_mms_-_global_niue_multipler"></td><td id="sms_mms_-_global_niue_credit"></td><td id="sms_mms_-_global_niue_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_norfolk_island_ratio"></td><td>Norfolk Island</td><td id="sms_mms_-_global_norfolk_island_multipler"></td><td id="sms_mms_-_global_norfolk_island_credit"></td><td id="sms_mms_-_global_norfolk_island_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_north_macedonia_ratio"></td><td>North Macedonia</td><td id="sms_mms_-_global_north_macedonia_multipler"></td><td id="sms_mms_-_global_north_macedonia_credit"></td><td id="sms_mms_-_global_north_macedonia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_northern_cyprus_ratio"></td><td>Northern Cyprus</td><td id="sms_mms_-_global_northern_cyprus_multipler"></td><td id="sms_mms_-_global_northern_cyprus_credit"></td><td id="sms_mms_-_global_northern_cyprus_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_norway_ratio"></td><td>Norway</td><td id="sms_mms_-_global_norway_multipler"></td><td id="sms_mms_-_global_norway_credit"></td><td id="sms_mms_-_global_norway_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_oman_ratio"></td><td>Oman</td><td id="sms_mms_-_global_oman_multipler"></td><td id="sms_mms_-_global_oman_credit"></td><td id="sms_mms_-_global_oman_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_pakistan_ratio"></td><td>Pakistan</td><td id="sms_mms_-_global_pakistan_multipler"></td><td id="sms_mms_-_global_pakistan_credit"></td><td id="sms_mms_-_global_pakistan_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_palau_ratio"></td><td>Palau</td><td id="sms_mms_-_global_palau_multipler"></td><td id="sms_mms_-_global_palau_credit"></td><td id="sms_mms_-_global_palau_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_palestinian_territory_ratio"></td><td>Palestinian Territory</td><td id="sms_mms_-_global_palestinian_territory_multipler"></td><td id="sms_mms_-_global_palestinian_territory_credit"></td><td id="sms_mms_-_global_palestinian_territory_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_panama_ratio"></td><td>Panama</td><td id="sms_mms_-_global_panama_multipler"></td><td id="sms_mms_-_global_panama_credit"></td><td id="sms_mms_-_global_panama_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_papua_new_guinea_ratio"></td><td>Papua New Guinea</td><td id="sms_mms_-_global_papua_new_guinea_multipler"></td><td id="sms_mms_-_global_papua_new_guinea_credit"></td><td id="sms_mms_-_global_papua_new_guinea_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_paraguay_ratio"></td><td>Paraguay</td><td id="sms_mms_-_global_paraguay_multipler"></td><td id="sms_mms_-_global_paraguay_credit"></td><td id="sms_mms_-_global_paraguay_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_peru_ratio"></td><td>Peru</td><td id="sms_mms_-_global_peru_multipler"></td><td id="sms_mms_-_global_peru_credit"></td><td id="sms_mms_-_global_peru_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_philippines_ratio"></td><td>Philippines</td><td id="sms_mms_-_global_philippines_multipler"></td><td id="sms_mms_-_global_philippines_credit"></td><td id="sms_mms_-_global_philippines_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_poland_ratio"></td><td>Poland</td><td id="sms_mms_-_global_poland_multipler"></td><td id="sms_mms_-_global_poland_credit"></td><td id="sms_mms_-_global_poland_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_portugal_ratio"></td><td>Portugal</td><td id="sms_mms_-_global_portugal_multipler"></td><td id="sms_mms_-_global_portugal_credit"></td><td id="sms_mms_-_global_portugal_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_puerto_rico_ratio"></td><td>Puerto Rico</td><td id="sms_mms_-_global_puerto_rico_multipler"></td><td id="sms_mms_-_global_puerto_rico_credit"></td><td id="sms_mms_-_global_puerto_rico_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_qatar_ratio"></td><td>Qatar</td><td id="sms_mms_-_global_qatar_multipler"></td><td id="sms_mms_-_global_qatar_credit"></td><td id="sms_mms_-_global_qatar_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_reunion-mayotte_ratio"></td><td>Reunion/Mayotte</td><td id="sms_mms_-_global_reunion-mayotte_multipler"></td><td id="sms_mms_-_global_reunion-mayotte_credit"></td><td id="sms_mms_-_global_reunion-mayotte_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_romania_ratio"></td><td>Romania</td><td id="sms_mms_-_global_romania_multipler"></td><td id="sms_mms_-_global_romania_credit"></td><td id="sms_mms_-_global_romania_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_russia_ratio"></td><td>Russia</td><td id="sms_mms_-_global_russia_multipler"></td><td id="sms_mms_-_global_russia_credit"></td><td id="sms_mms_-_global_russia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_rwanda_ratio"></td><td>Rwanda</td><td id="sms_mms_-_global_rwanda_multipler"></td><td id="sms_mms_-_global_rwanda_credit"></td><td id="sms_mms_-_global_rwanda_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_saint_kitts_and_nevis_ratio"></td><td>Saint Kitts and Nevis</td><td id="sms_mms_-_global_saint_kitts_and_nevis_multipler"></td><td id="sms_mms_-_global_saint_kitts_and_nevis_credit"></td><td id="sms_mms_-_global_saint_kitts_and_nevis_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_saint_lucia_ratio"></td><td>Saint Lucia</td><td id="sms_mms_-_global_saint_lucia_multipler"></td><td id="sms_mms_-_global_saint_lucia_credit"></td><td id="sms_mms_-_global_saint_lucia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_saint_pierre_and_miquelon_ratio"></td><td>Saint Pierre and Miquelon</td><td id="sms_mms_-_global_saint_pierre_and_miquelon_multipler"></td><td id="sms_mms_-_global_saint_pierre_and_miquelon_credit"></td><td id="sms_mms_-_global_saint_pierre_and_miquelon_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_saint_vincent_and_the_grenadines_ratio"></td><td>Saint Vincent and The Grenadines</td><td id="sms_mms_-_global_saint_vincent_and_the_grenadines_multipler"></td><td id="sms_mms_-_global_saint_vincent_and_the_grenadines_credit"></td><td id="sms_mms_-_global_saint_vincent_and_the_grenadines_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_samoa_ratio"></td><td>Samoa</td><td id="sms_mms_-_global_samoa_multipler"></td><td id="sms_mms_-_global_samoa_credit"></td><td id="sms_mms_-_global_samoa_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_san_marino_ratio"></td><td>San Marino</td><td id="sms_mms_-_global_san_marino_multipler"></td><td id="sms_mms_-_global_san_marino_credit"></td><td id="sms_mms_-_global_san_marino_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_sao_tome_and_principe_ratio"></td><td>Sao Tome and Principe</td><td id="sms_mms_-_global_sao_tome_and_principe_multipler"></td><td id="sms_mms_-_global_sao_tome_and_principe_credit"></td><td id="sms_mms_-_global_sao_tome_and_principe_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_saudi_arabia_ratio"></td><td>Saudi Arabia</td><td id="sms_mms_-_global_saudi_arabia_multipler"></td><td id="sms_mms_-_global_saudi_arabia_credit"></td><td id="sms_mms_-_global_saudi_arabia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_senegal_ratio"></td><td>Senegal</td><td id="sms_mms_-_global_senegal_multipler"></td><td id="sms_mms_-_global_senegal_credit"></td><td id="sms_mms_-_global_senegal_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_serbia_ratio"></td><td>Serbia</td><td id="sms_mms_-_global_serbia_multipler"></td><td id="sms_mms_-_global_serbia_credit"></td><td id="sms_mms_-_global_serbia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_seychelles_ratio"></td><td>Seychelles</td><td id="sms_mms_-_global_seychelles_multipler"></td><td id="sms_mms_-_global_seychelles_credit"></td><td id="sms_mms_-_global_seychelles_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_sierra_leone_ratio"></td><td>Sierra Leone</td><td id="sms_mms_-_global_sierra_leone_multipler"></td><td id="sms_mms_-_global_sierra_leone_credit"></td><td id="sms_mms_-_global_sierra_leone_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_singapore_ratio"></td><td>Singapore</td><td id="sms_mms_-_global_singapore_multipler"></td><td id="sms_mms_-_global_singapore_credit"></td><td id="sms_mms_-_global_singapore_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_sint_maarten_ratio"></td><td>Sint Maarten</td><td id="sms_mms_-_global_sint_maarten_multipler"></td><td id="sms_mms_-_global_sint_maarten_credit"></td><td id="sms_mms_-_global_sint_maarten_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_slovakia_ratio"></td><td>Slovakia</td><td id="sms_mms_-_global_slovakia_multipler"></td><td id="sms_mms_-_global_slovakia_credit"></td><td id="sms_mms_-_global_slovakia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_slovenia_ratio"></td><td>Slovenia</td><td id="sms_mms_-_global_slovenia_multipler"></td><td id="sms_mms_-_global_slovenia_credit"></td><td id="sms_mms_-_global_slovenia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_solomon_islands_ratio"></td><td>Solomon Islands</td><td id="sms_mms_-_global_solomon_islands_multipler"></td><td id="sms_mms_-_global_solomon_islands_credit"></td><td id="sms_mms_-_global_solomon_islands_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_somalia_ratio"></td><td>Somalia</td><td id="sms_mms_-_global_somalia_multipler"></td><td id="sms_mms_-_global_somalia_credit"></td><td id="sms_mms_-_global_somalia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_south_africa_ratio"></td><td>South Africa</td><td id="sms_mms_-_global_south_africa_multipler"></td><td id="sms_mms_-_global_south_africa_credit"></td><td id="sms_mms_-_global_south_africa_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_south_ossetia_ratio"></td><td>South Ossetia</td><td id="sms_mms_-_global_south_ossetia_multipler"></td><td id="sms_mms_-_global_south_ossetia_credit"></td><td id="sms_mms_-_global_south_ossetia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_south_sudan_ratio"></td><td>South Sudan</td><td id="sms_mms_-_global_south_sudan_multipler"></td><td id="sms_mms_-_global_south_sudan_credit"></td><td id="sms_mms_-_global_south_sudan_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_spain_ratio"></td><td>Spain</td><td id="sms_mms_-_global_spain_multipler"></td><td id="sms_mms_-_global_spain_credit"></td><td id="sms_mms_-_global_spain_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_sri_lanka_ratio"></td><td>Sri Lanka</td><td id="sms_mms_-_global_sri_lanka_multipler"></td><td id="sms_mms_-_global_sri_lanka_credit"></td><td id="sms_mms_-_global_sri_lanka_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_st_kitts_and_nevis_ratio"></td><td>St Kitts and Nevis</td><td id="sms_mms_-_global_st_kitts_and_nevis_multipler"></td><td id="sms_mms_-_global_st_kitts_and_nevis_credit"></td><td id="sms_mms_-_global_st_kitts_and_nevis_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_st_lucia_ratio"></td><td>St Lucia</td><td id="sms_mms_-_global_st_lucia_multipler"></td><td id="sms_mms_-_global_st_lucia_credit"></td><td id="sms_mms_-_global_st_lucia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_st_pierre_and_miquelon_ratio"></td><td>St Pierre and Miquelon</td><td id="sms_mms_-_global_st_pierre_and_miquelon_multipler"></td><td id="sms_mms_-_global_st_pierre_and_miquelon_credit"></td><td id="sms_mms_-_global_st_pierre_and_miquelon_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_st_vincent_grenadines_ratio"></td><td>St Vincent Grenadines</td><td id="sms_mms_-_global_st_vincent_grenadines_multipler"></td><td id="sms_mms_-_global_st_vincent_grenadines_credit"></td><td id="sms_mms_-_global_st_vincent_grenadines_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_sudan_ratio"></td><td>Sudan</td><td id="sms_mms_-_global_sudan_multipler"></td><td id="sms_mms_-_global_sudan_credit"></td><td id="sms_mms_-_global_sudan_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_suriname_ratio"></td><td>Suriname</td><td id="sms_mms_-_global_suriname_multipler"></td><td id="sms_mms_-_global_suriname_credit"></td><td id="sms_mms_-_global_suriname_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_swaziland_ratio"></td><td>Swaziland</td><td id="sms_mms_-_global_swaziland_multipler"></td><td id="sms_mms_-_global_swaziland_credit"></td><td id="sms_mms_-_global_swaziland_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_sweden_ratio"></td><td>Sweden</td><td id="sms_mms_-_global_sweden_multipler"></td><td id="sms_mms_-_global_sweden_credit"></td><td id="sms_mms_-_global_sweden_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_switzerland_ratio"></td><td>Switzerland</td><td id="sms_mms_-_global_switzerland_multipler"></td><td id="sms_mms_-_global_switzerland_credit"></td><td id="sms_mms_-_global_switzerland_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_syria_ratio"></td><td>Syria</td><td id="sms_mms_-_global_syria_multipler"></td><td id="sms_mms_-_global_syria_credit"></td><td id="sms_mms_-_global_syria_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_taiwan_ratio"></td><td>Taiwan</td><td id="sms_mms_-_global_taiwan_multipler"></td><td id="sms_mms_-_global_taiwan_credit"></td><td id="sms_mms_-_global_taiwan_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_tajikistan_ratio"></td><td>Tajikistan</td><td id="sms_mms_-_global_tajikistan_multipler"></td><td id="sms_mms_-_global_tajikistan_credit"></td><td id="sms_mms_-_global_tajikistan_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_tanzania_ratio"></td><td>Tanzania</td><td id="sms_mms_-_global_tanzania_multipler"></td><td id="sms_mms_-_global_tanzania_credit"></td><td id="sms_mms_-_global_tanzania_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_thailand_ratio"></td><td>Thailand</td><td id="sms_mms_-_global_thailand_multipler"></td><td id="sms_mms_-_global_thailand_credit"></td><td id="sms_mms_-_global_thailand_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_timor-leste_ratio"></td><td>Timor-Leste</td><td id="sms_mms_-_global_timor-leste_multipler"></td><td id="sms_mms_-_global_timor-leste_credit"></td><td id="sms_mms_-_global_timor-leste_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_togo_ratio"></td><td>Togo</td><td id="sms_mms_-_global_togo_multipler"></td><td id="sms_mms_-_global_togo_credit"></td><td id="sms_mms_-_global_togo_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_tonga_ratio"></td><td>Tonga</td><td id="sms_mms_-_global_tonga_multipler"></td><td id="sms_mms_-_global_tonga_credit"></td><td id="sms_mms_-_global_tonga_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_trinidad_and_tobago_ratio"></td><td>Trinidad and Tobago</td><td id="sms_mms_-_global_trinidad_and_tobago_multipler"></td><td id="sms_mms_-_global_trinidad_and_tobago_credit"></td><td id="sms_mms_-_global_trinidad_and_tobago_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_tunisia_ratio"></td><td>Tunisia</td><td id="sms_mms_-_global_tunisia_multipler"></td><td id="sms_mms_-_global_tunisia_credit"></td><td id="sms_mms_-_global_tunisia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_turkey_ratio"></td><td>Turkey</td><td id="sms_mms_-_global_turkey_multipler"></td><td id="sms_mms_-_global_turkey_credit"></td><td id="sms_mms_-_global_turkey_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_turkmenistan_ratio"></td><td>Turkmenistan</td><td id="sms_mms_-_global_turkmenistan_multipler"></td><td id="sms_mms_-_global_turkmenistan_credit"></td><td id="sms_mms_-_global_turkmenistan_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_turks_and_caicos_islands_ratio"></td><td>Turks and Caicos Islands</td><td id="sms_mms_-_global_turks_and_caicos_islands_multipler"></td><td id="sms_mms_-_global_turks_and_caicos_islands_credit"></td><td id="sms_mms_-_global_turks_and_caicos_islands_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_tuvalu_ratio"></td><td>Tuvalu</td><td id="sms_mms_-_global_tuvalu_multipler"></td><td id="sms_mms_-_global_tuvalu_credit"></td><td id="sms_mms_-_global_tuvalu_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_uganda_ratio"></td><td>Uganda</td><td id="sms_mms_-_global_uganda_multipler"></td><td id="sms_mms_-_global_uganda_credit"></td><td id="sms_mms_-_global_uganda_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_ukraine_ratio"></td><td>Ukraine</td><td id="sms_mms_-_global_ukraine_multipler"></td><td id="sms_mms_-_global_ukraine_credit"></td><td id="sms_mms_-_global_ukraine_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_united_arab_emirates_ratio"></td><td>United Arab Emirates</td><td id="sms_mms_-_global_united_arab_emirates_multipler"></td><td id="sms_mms_-_global_united_arab_emirates_credit"></td><td id="sms_mms_-_global_united_arab_emirates_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_united_kingdom_ratio"></td><td>United Kingdom</td><td id="sms_mms_-_global_united_kingdom_multipler"></td><td id="sms_mms_-_global_united_kingdom_credit"></td><td id="sms_mms_-_global_united_kingdom_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_unknown_ratio"></td><td>Unknown</td><td id="sms_mms_-_global_unknown_multipler"></td><td id="sms_mms_-_global_unknown_credit"></td><td id="sms_mms_-_global_unknown_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_uruguay_ratio"></td><td>Uruguay</td><td id="sms_mms_-_global_uruguay_multipler"></td><td id="sms_mms_-_global_uruguay_credit"></td><td id="sms_mms_-_global_uruguay_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_uzbekistan_ratio"></td><td>Uzbekistan</td><td id="sms_mms_-_global_uzbekistan_multipler"></td><td id="sms_mms_-_global_uzbekistan_credit"></td><td id="sms_mms_-_global_uzbekistan_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_vanuatu_ratio"></td><td>Vanuatu</td><td id="sms_mms_-_global_vanuatu_multipler"></td><td id="sms_mms_-_global_vanuatu_credit"></td><td id="sms_mms_-_global_vanuatu_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_venezuela_ratio"></td><td>Venezuela</td><td id="sms_mms_-_global_venezuela_multipler"></td><td id="sms_mms_-_global_venezuela_credit"></td><td id="sms_mms_-_global_venezuela_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_vietnam_ratio"></td><td>Vietnam</td><td id="sms_mms_-_global_vietnam_multipler"></td><td id="sms_mms_-_global_vietnam_credit"></td><td id="sms_mms_-_global_vietnam_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_virgin_islands-_british_ratio"></td><td>Virgin Islands, British</td><td id="sms_mms_-_global_virgin_islands-_british_multipler"></td><td id="sms_mms_-_global_virgin_islands-_british_credit"></td><td id="sms_mms_-_global_virgin_islands-_british_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_virgin_islands-_us_ratio"></td><td>Virgin Islands, U.S.</td><td id="sms_mms_-_global_virgin_islands-_us_multipler"></td><td id="sms_mms_-_global_virgin_islands-_us_credit"></td><td id="sms_mms_-_global_virgin_islands-_us_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_wallis_and_futuna_ratio"></td><td>Wallis and Futuna</td><td id="sms_mms_-_global_wallis_and_futuna_multipler"></td><td id="sms_mms_-_global_wallis_and_futuna_credit"></td><td id="sms_mms_-_global_wallis_and_futuna_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_yemen_ratio"></td><td>Yemen</td><td id="sms_mms_-_global_yemen_multipler"></td><td id="sms_mms_-_global_yemen_credit"></td><td id="sms_mms_-_global_yemen_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_zambia_ratio"></td><td>Zambia</td><td id="sms_mms_-_global_zambia_multipler"></td><td id="sms_mms_-_global_zambia_credit"></td><td id="sms_mms_-_global_zambia_rates"></td></tr>
  <tr><td>SMS / MMS - Global</td><td id="sms_mms_-_global_zimbabwe_ratio"></td><td>Zimbabwe</td><td id="sms_mms_-_global_zimbabwe_multipler"></td><td id="sms_mms_-_global_zimbabwe_credit"></td><td id="sms_mms_-_global_zimbabwe_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_argentina_authentication_ratio"></td><td>Argentina Authentication</td><td id="whatsapp_argentina_authentication_multipler"></td><td id="whatsapp_argentina_authentication_credit"></td><td id="whatsapp_argentina_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_argentina_marketing_ratio"></td><td>Argentina Marketing</td><td id="whatsapp_argentina_marketing_multipler"></td><td id="whatsapp_argentina_marketing_credit"></td><td id="whatsapp_argentina_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_argentina_service_ratio"></td><td>Argentina Service</td><td id="whatsapp_argentina_service_multipler"></td><td id="whatsapp_argentina_service_credit"></td><td id="whatsapp_argentina_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_argentina_utility_ratio"></td><td>Argentina Utility</td><td id="whatsapp_argentina_utility_multipler"></td><td id="whatsapp_argentina_utility_credit"></td><td id="whatsapp_argentina_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_brazil_authentication_ratio"></td><td>Brazil Authentication</td><td id="whatsapp_brazil_authentication_multipler"></td><td id="whatsapp_brazil_authentication_credit"></td><td id="whatsapp_brazil_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_brazil_marketing_ratio"></td><td>Brazil Marketing</td><td id="whatsapp_brazil_marketing_multipler"></td><td id="whatsapp_brazil_marketing_credit"></td><td id="whatsapp_brazil_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_brazil_service_ratio"></td><td>Brazil Service</td><td id="whatsapp_brazil_service_multipler"></td><td id="whatsapp_brazil_service_credit"></td><td id="whatsapp_brazil_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_brazil_utility_ratio"></td><td>Brazil Utility</td><td id="whatsapp_brazil_utility_multipler"></td><td id="whatsapp_brazil_utility_credit"></td><td id="whatsapp_brazil_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_chile_authentication_ratio"></td><td>Chile Authentication</td><td id="whatsapp_chile_authentication_multipler"></td><td id="whatsapp_chile_authentication_credit"></td><td id="whatsapp_chile_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_chile_marketing_ratio"></td><td>Chile Marketing</td><td id="whatsapp_chile_marketing_multipler"></td><td id="whatsapp_chile_marketing_credit"></td><td id="whatsapp_chile_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_chile_service_ratio"></td><td>Chile Service</td><td id="whatsapp_chile_service_multipler"></td><td id="whatsapp_chile_service_credit"></td><td id="whatsapp_chile_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_chile_utility_ratio"></td><td>Chile Utility</td><td id="whatsapp_chile_utility_multipler"></td><td id="whatsapp_chile_utility_credit"></td><td id="whatsapp_chile_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_colombia_authentication_ratio"></td><td>Colombia Authentication</td><td id="whatsapp_colombia_authentication_multipler"></td><td id="whatsapp_colombia_authentication_credit"></td><td id="whatsapp_colombia_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_colombia_marketing_ratio"></td><td>Colombia Marketing</td><td id="whatsapp_colombia_marketing_multipler"></td><td id="whatsapp_colombia_marketing_credit"></td><td id="whatsapp_colombia_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_colombia_service_ratio"></td><td>Colombia Service</td><td id="whatsapp_colombia_service_multipler"></td><td id="whatsapp_colombia_service_credit"></td><td id="whatsapp_colombia_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_colombia_utility_ratio"></td><td>Colombia Utility</td><td id="whatsapp_colombia_utility_multipler"></td><td id="whatsapp_colombia_utility_credit"></td><td id="whatsapp_colombia_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_egypt_authentication_ratio"></td><td>Egypt Authentication</td><td id="whatsapp_egypt_authentication_multipler"></td><td id="whatsapp_egypt_authentication_credit"></td><td id="whatsapp_egypt_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_egypt_marketing_ratio"></td><td>Egypt Marketing</td><td id="whatsapp_egypt_marketing_multipler"></td><td id="whatsapp_egypt_marketing_credit"></td><td id="whatsapp_egypt_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_egypt_service_ratio"></td><td>Egypt Service</td><td id="whatsapp_egypt_service_multipler"></td><td id="whatsapp_egypt_service_credit"></td><td id="whatsapp_egypt_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_egypt_utility_ratio"></td><td>Egypt Utility</td><td id="whatsapp_egypt_utility_multipler"></td><td id="whatsapp_egypt_utility_credit"></td><td id="whatsapp_egypt_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_france_authentication_ratio"></td><td>France Authentication</td><td id="whatsapp_france_authentication_multipler"></td><td id="whatsapp_france_authentication_credit"></td><td id="whatsapp_france_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_france_marketing_ratio"></td><td>France Marketing</td><td id="whatsapp_france_marketing_multipler"></td><td id="whatsapp_france_marketing_credit"></td><td id="whatsapp_france_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_france_service_ratio"></td><td>France Service</td><td id="whatsapp_france_service_multipler"></td><td id="whatsapp_france_service_credit"></td><td id="whatsapp_france_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_france_utility_ratio"></td><td>France Utility</td><td id="whatsapp_france_utility_multipler"></td><td id="whatsapp_france_utility_credit"></td><td id="whatsapp_france_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_germany_authentication_ratio"></td><td>Germany Authentication</td><td id="whatsapp_germany_authentication_multipler"></td><td id="whatsapp_germany_authentication_credit"></td><td id="whatsapp_germany_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_germany_marketing_ratio"></td><td>Germany Marketing</td><td id="whatsapp_germany_marketing_multipler"></td><td id="whatsapp_germany_marketing_credit"></td><td id="whatsapp_germany_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_germany_service_ratio"></td><td>Germany Service</td><td id="whatsapp_germany_service_multipler"></td><td id="whatsapp_germany_service_credit"></td><td id="whatsapp_germany_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_germany_utility_ratio"></td><td>Germany Utility</td><td id="whatsapp_germany_utility_multipler"></td><td id="whatsapp_germany_utility_credit"></td><td id="whatsapp_germany_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_india_authentication_ratio"></td><td>India Authentication</td><td id="whatsapp_india_authentication_multipler"></td><td id="whatsapp_india_authentication_credit"></td><td id="whatsapp_india_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_india_marketing_ratio"></td><td>India Marketing</td><td id="whatsapp_india_marketing_multipler"></td><td id="whatsapp_india_marketing_credit"></td><td id="whatsapp_india_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_india_service_ratio"></td><td>India Service</td><td id="whatsapp_india_service_multipler"></td><td id="whatsapp_india_service_credit"></td><td id="whatsapp_india_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_india_utility_ratio"></td><td>India Utility</td><td id="whatsapp_india_utility_multipler"></td><td id="whatsapp_india_utility_credit"></td><td id="whatsapp_india_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_indonesia_authentication_ratio"></td><td>Indonesia Authentication</td><td id="whatsapp_indonesia_authentication_multipler"></td><td id="whatsapp_indonesia_authentication_credit"></td><td id="whatsapp_indonesia_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_indonesia_marketing_ratio"></td><td>Indonesia Marketing</td><td id="whatsapp_indonesia_marketing_multipler"></td><td id="whatsapp_indonesia_marketing_credit"></td><td id="whatsapp_indonesia_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_indonesia_service_ratio"></td><td>Indonesia Service</td><td id="whatsapp_indonesia_service_multipler"></td><td id="whatsapp_indonesia_service_credit"></td><td id="whatsapp_indonesia_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_indonesia_utility_ratio"></td><td>Indonesia Utility</td><td id="whatsapp_indonesia_utility_multipler"></td><td id="whatsapp_indonesia_utility_credit"></td><td id="whatsapp_indonesia_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_israel_authentication_ratio"></td><td>Israel Authentication</td><td id="whatsapp_israel_authentication_multipler"></td><td id="whatsapp_israel_authentication_credit"></td><td id="whatsapp_israel_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_israel_marketing_ratio"></td><td>Israel Marketing</td><td id="whatsapp_israel_marketing_multipler"></td><td id="whatsapp_israel_marketing_credit"></td><td id="whatsapp_israel_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_israel_service_ratio"></td><td>Israel Service</td><td id="whatsapp_israel_service_multipler"></td><td id="whatsapp_israel_service_credit"></td><td id="whatsapp_israel_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_israel_utility_ratio"></td><td>Israel Utility</td><td id="whatsapp_israel_utility_multipler"></td><td id="whatsapp_israel_utility_credit"></td><td id="whatsapp_israel_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_italy_authentication_ratio"></td><td>Italy Authentication</td><td id="whatsapp_italy_authentication_multipler"></td><td id="whatsapp_italy_authentication_credit"></td><td id="whatsapp_italy_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_italy_marketing_ratio"></td><td>Italy Marketing</td><td id="whatsapp_italy_marketing_multipler"></td><td id="whatsapp_italy_marketing_credit"></td><td id="whatsapp_italy_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_italy_service_ratio"></td><td>Italy Service</td><td id="whatsapp_italy_service_multipler"></td><td id="whatsapp_italy_service_credit"></td><td id="whatsapp_italy_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_italy_utility_ratio"></td><td>Italy Utility</td><td id="whatsapp_italy_utility_multipler"></td><td id="whatsapp_italy_utility_credit"></td><td id="whatsapp_italy_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_malaysia_authentication_ratio"></td><td>Malaysia Authentication</td><td id="whatsapp_malaysia_authentication_multipler"></td><td id="whatsapp_malaysia_authentication_credit"></td><td id="whatsapp_malaysia_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_malaysia_marketing_ratio"></td><td>Malaysia Marketing</td><td id="whatsapp_malaysia_marketing_multipler"></td><td id="whatsapp_malaysia_marketing_credit"></td><td id="whatsapp_malaysia_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_malaysia_service_ratio"></td><td>Malaysia Service</td><td id="whatsapp_malaysia_service_multipler"></td><td id="whatsapp_malaysia_service_credit"></td><td id="whatsapp_malaysia_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_malaysia_utility_ratio"></td><td>Malaysia Utility</td><td id="whatsapp_malaysia_utility_multipler"></td><td id="whatsapp_malaysia_utility_credit"></td><td id="whatsapp_malaysia_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_mexico_authentication_ratio"></td><td>Mexico Authentication</td><td id="whatsapp_mexico_authentication_multipler"></td><td id="whatsapp_mexico_authentication_credit"></td><td id="whatsapp_mexico_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_mexico_marketing_ratio"></td><td>Mexico Marketing</td><td id="whatsapp_mexico_marketing_multipler"></td><td id="whatsapp_mexico_marketing_credit"></td><td id="whatsapp_mexico_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_mexico_service_ratio"></td><td>Mexico Service</td><td id="whatsapp_mexico_service_multipler"></td><td id="whatsapp_mexico_service_credit"></td><td id="whatsapp_mexico_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_mexico_utility_ratio"></td><td>Mexico Utility</td><td id="whatsapp_mexico_utility_multipler"></td><td id="whatsapp_mexico_utility_credit"></td><td id="whatsapp_mexico_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_netherlands_authentication_ratio"></td><td>Netherlands Authentication</td><td id="whatsapp_netherlands_authentication_multipler"></td><td id="whatsapp_netherlands_authentication_credit"></td><td id="whatsapp_netherlands_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_netherlands_marketing_ratio"></td><td>Netherlands Marketing</td><td id="whatsapp_netherlands_marketing_multipler"></td><td id="whatsapp_netherlands_marketing_credit"></td><td id="whatsapp_netherlands_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_netherlands_service_ratio"></td><td>Netherlands Service</td><td id="whatsapp_netherlands_service_multipler"></td><td id="whatsapp_netherlands_service_credit"></td><td id="whatsapp_netherlands_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_netherlands_utility_ratio"></td><td>Netherlands Utility</td><td id="whatsapp_netherlands_utility_multipler"></td><td id="whatsapp_netherlands_utility_credit"></td><td id="whatsapp_netherlands_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_nigeria_authentication_ratio"></td><td>Nigeria Authentication</td><td id="whatsapp_nigeria_authentication_multipler"></td><td id="whatsapp_nigeria_authentication_credit"></td><td id="whatsapp_nigeria_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_nigeria_marketing_ratio"></td><td>Nigeria Marketing</td><td id="whatsapp_nigeria_marketing_multipler"></td><td id="whatsapp_nigeria_marketing_credit"></td><td id="whatsapp_nigeria_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_nigeria_service_ratio"></td><td>Nigeria Service</td><td id="whatsapp_nigeria_service_multipler"></td><td id="whatsapp_nigeria_service_credit"></td><td id="whatsapp_nigeria_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_nigeria_utility_ratio"></td><td>Nigeria Utility</td><td id="whatsapp_nigeria_utility_multipler"></td><td id="whatsapp_nigeria_utility_credit"></td><td id="whatsapp_nigeria_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_north_america_authentication_ratio"></td><td>North America Authentication</td><td id="whatsapp_north_america_authentication_multipler"></td><td id="whatsapp_north_america_authentication_credit"></td><td id="whatsapp_north_america_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_north_america_marketing_ratio"></td><td>North America Marketing</td><td id="whatsapp_north_america_marketing_multipler"></td><td id="whatsapp_north_america_marketing_credit"></td><td id="whatsapp_north_america_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_north_america_service_ratio"></td><td>North America Service</td><td id="whatsapp_north_america_service_multipler"></td><td id="whatsapp_north_america_service_credit"></td><td id="whatsapp_north_america_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_north_america_utility_ratio"></td><td>North America Utility</td><td id="whatsapp_north_america_utility_multipler"></td><td id="whatsapp_north_america_utility_credit"></td><td id="whatsapp_north_america_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_other_authentication_ratio"></td><td>Other Authentication</td><td id="whatsapp_other_authentication_multipler"></td><td id="whatsapp_other_authentication_credit"></td><td id="whatsapp_other_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_other_marketing_ratio"></td><td>Other Marketing</td><td id="whatsapp_other_marketing_multipler"></td><td id="whatsapp_other_marketing_credit"></td><td id="whatsapp_other_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_other_service_ratio"></td><td>Other Service</td><td id="whatsapp_other_service_multipler"></td><td id="whatsapp_other_service_credit"></td><td id="whatsapp_other_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_other_utility_ratio"></td><td>Other Utility</td><td id="whatsapp_other_utility_multipler"></td><td id="whatsapp_other_utility_credit"></td><td id="whatsapp_other_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_pakistan_authentication_ratio"></td><td>Pakistan Authentication</td><td id="whatsapp_pakistan_authentication_multipler"></td><td id="whatsapp_pakistan_authentication_credit"></td><td id="whatsapp_pakistan_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_pakistan_marketing_ratio"></td><td>Pakistan Marketing</td><td id="whatsapp_pakistan_marketing_multipler"></td><td id="whatsapp_pakistan_marketing_credit"></td><td id="whatsapp_pakistan_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_pakistan_service_ratio"></td><td>Pakistan Service</td><td id="whatsapp_pakistan_service_multipler"></td><td id="whatsapp_pakistan_service_credit"></td><td id="whatsapp_pakistan_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_pakistan_utility_ratio"></td><td>Pakistan Utility</td><td id="whatsapp_pakistan_utility_multipler"></td><td id="whatsapp_pakistan_utility_credit"></td><td id="whatsapp_pakistan_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_peru_authentication_ratio"></td><td>Peru Authentication</td><td id="whatsapp_peru_authentication_multipler"></td><td id="whatsapp_peru_authentication_credit"></td><td id="whatsapp_peru_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_peru_marketing_ratio"></td><td>Peru Marketing</td><td id="whatsapp_peru_marketing_multipler"></td><td id="whatsapp_peru_marketing_credit"></td><td id="whatsapp_peru_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_peru_service_ratio"></td><td>Peru Service</td><td id="whatsapp_peru_service_multipler"></td><td id="whatsapp_peru_service_credit"></td><td id="whatsapp_peru_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_peru_utility_ratio"></td><td>Peru Utility</td><td id="whatsapp_peru_utility_multipler"></td><td id="whatsapp_peru_utility_credit"></td><td id="whatsapp_peru_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_africa_authentication_ratio"></td><td>Rest of Africa Authentication</td><td id="whatsapp_rest_of_africa_authentication_multipler"></td><td id="whatsapp_rest_of_africa_authentication_credit"></td><td id="whatsapp_rest_of_africa_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_africa_marketing_ratio"></td><td>Rest of Africa Marketing</td><td id="whatsapp_rest_of_africa_marketing_multipler"></td><td id="whatsapp_rest_of_africa_marketing_credit"></td><td id="whatsapp_rest_of_africa_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_africa_service_ratio"></td><td>Rest of Africa Service</td><td id="whatsapp_rest_of_africa_service_multipler"></td><td id="whatsapp_rest_of_africa_service_credit"></td><td id="whatsapp_rest_of_africa_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_africa_utility_ratio"></td><td>Rest of Africa Utility</td><td id="whatsapp_rest_of_africa_utility_multipler"></td><td id="whatsapp_rest_of_africa_utility_credit"></td><td id="whatsapp_rest_of_africa_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_asia_pacific_authentication_ratio"></td><td>Rest of Asia Pacific Authentication</td><td id="whatsapp_rest_of_asia_pacific_authentication_multipler"></td><td id="whatsapp_rest_of_asia_pacific_authentication_credit"></td><td id="whatsapp_rest_of_asia_pacific_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_asia_pacific_marketing_ratio"></td><td>Rest of Asia Pacific Marketing</td><td id="whatsapp_rest_of_asia_pacific_marketing_multipler"></td><td id="whatsapp_rest_of_asia_pacific_marketing_credit"></td><td id="whatsapp_rest_of_asia_pacific_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_asia_pacific_service_ratio"></td><td>Rest of Asia Pacific Service</td><td id="whatsapp_rest_of_asia_pacific_service_multipler"></td><td id="whatsapp_rest_of_asia_pacific_service_credit"></td><td id="whatsapp_rest_of_asia_pacific_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_asia_pacific_utility_ratio"></td><td>Rest of Asia Pacific Utility</td><td id="whatsapp_rest_of_asia_pacific_utility_multipler"></td><td id="whatsapp_rest_of_asia_pacific_utility_credit"></td><td id="whatsapp_rest_of_asia_pacific_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_central_-_eastern_europe_authentication_ratio"></td><td>Rest of Central & Eastern Europe Authentication</td><td id="whatsapp_rest_of_central_-_eastern_europe_authentication_multipler"></td><td id="whatsapp_rest_of_central_-_eastern_europe_authentication_credit"></td><td id="whatsapp_rest_of_central_-_eastern_europe_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_central_-_eastern_europe_marketing_ratio"></td><td>Rest of Central & Eastern Europe Marketing</td><td id="whatsapp_rest_of_central_-_eastern_europe_marketing_multipler"></td><td id="whatsapp_rest_of_central_-_eastern_europe_marketing_credit"></td><td id="whatsapp_rest_of_central_-_eastern_europe_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_central_-_eastern_europe_service_ratio"></td><td>Rest of Central & Eastern Europe Service</td><td id="whatsapp_rest_of_central_-_eastern_europe_service_multipler"></td><td id="whatsapp_rest_of_central_-_eastern_europe_service_credit"></td><td id="whatsapp_rest_of_central_-_eastern_europe_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_central_-_eastern_europe_utility_ratio"></td><td>Rest of Central & Eastern Europe Utility</td><td id="whatsapp_rest_of_central_-_eastern_europe_utility_multipler"></td><td id="whatsapp_rest_of_central_-_eastern_europe_utility_credit"></td><td id="whatsapp_rest_of_central_-_eastern_europe_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_latin_america_authentication_ratio"></td><td>Rest of Latin America Authentication</td><td id="whatsapp_rest_of_latin_america_authentication_multipler"></td><td id="whatsapp_rest_of_latin_america_authentication_credit"></td><td id="whatsapp_rest_of_latin_america_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_latin_america_marketing_ratio"></td><td>Rest of Latin America Marketing</td><td id="whatsapp_rest_of_latin_america_marketing_multipler"></td><td id="whatsapp_rest_of_latin_america_marketing_credit"></td><td id="whatsapp_rest_of_latin_america_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_latin_america_service_ratio"></td><td>Rest of Latin America Service</td><td id="whatsapp_rest_of_latin_america_service_multipler"></td><td id="whatsapp_rest_of_latin_america_service_credit"></td><td id="whatsapp_rest_of_latin_america_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_latin_america_utility_ratio"></td><td>Rest of Latin America Utility</td><td id="whatsapp_rest_of_latin_america_utility_multipler"></td><td id="whatsapp_rest_of_latin_america_utility_credit"></td><td id="whatsapp_rest_of_latin_america_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_middle_east_authentication_ratio"></td><td>Rest of Middle East Authentication</td><td id="whatsapp_rest_of_middle_east_authentication_multipler"></td><td id="whatsapp_rest_of_middle_east_authentication_credit"></td><td id="whatsapp_rest_of_middle_east_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_middle_east_marketing_ratio"></td><td>Rest of Middle East Marketing</td><td id="whatsapp_rest_of_middle_east_marketing_multipler"></td><td id="whatsapp_rest_of_middle_east_marketing_credit"></td><td id="whatsapp_rest_of_middle_east_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_middle_east_service_ratio"></td><td>Rest of Middle East Service</td><td id="whatsapp_rest_of_middle_east_service_multipler"></td><td id="whatsapp_rest_of_middle_east_service_credit"></td><td id="whatsapp_rest_of_middle_east_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_middle_east_utility_ratio"></td><td>Rest of Middle East Utility</td><td id="whatsapp_rest_of_middle_east_utility_multipler"></td><td id="whatsapp_rest_of_middle_east_utility_credit"></td><td id="whatsapp_rest_of_middle_east_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_western_europe_authentication_ratio"></td><td>Rest of Western Europe Authentication</td><td id="whatsapp_rest_of_western_europe_authentication_multipler"></td><td id="whatsapp_rest_of_western_europe_authentication_credit"></td><td id="whatsapp_rest_of_western_europe_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_western_europe_marketing_ratio"></td><td>Rest of Western Europe Marketing</td><td id="whatsapp_rest_of_western_europe_marketing_multipler"></td><td id="whatsapp_rest_of_western_europe_marketing_credit"></td><td id="whatsapp_rest_of_western_europe_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_western_europe_service_ratio"></td><td>Rest of Western Europe Service</td><td id="whatsapp_rest_of_western_europe_service_multipler"></td><td id="whatsapp_rest_of_western_europe_service_credit"></td><td id="whatsapp_rest_of_western_europe_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_rest_of_western_europe_utility_ratio"></td><td>Rest of Western Europe Utility</td><td id="whatsapp_rest_of_western_europe_utility_multipler"></td><td id="whatsapp_rest_of_western_europe_utility_credit"></td><td id="whatsapp_rest_of_western_europe_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_russia_authentication_ratio"></td><td>Russia Authentication</td><td id="whatsapp_russia_authentication_multipler"></td><td id="whatsapp_russia_authentication_credit"></td><td id="whatsapp_russia_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_russia_marketing_ratio"></td><td>Russia Marketing</td><td id="whatsapp_russia_marketing_multipler"></td><td id="whatsapp_russia_marketing_credit"></td><td id="whatsapp_russia_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_russia_service_ratio"></td><td>Russia Service</td><td id="whatsapp_russia_service_multipler"></td><td id="whatsapp_russia_service_credit"></td><td id="whatsapp_russia_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_russia_utility_ratio"></td><td>Russia Utility</td><td id="whatsapp_russia_utility_multipler"></td><td id="whatsapp_russia_utility_credit"></td><td id="whatsapp_russia_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_saudi_arabia_authentication_ratio"></td><td>Saudi Arabia Authentication</td><td id="whatsapp_saudi_arabia_authentication_multipler"></td><td id="whatsapp_saudi_arabia_authentication_credit"></td><td id="whatsapp_saudi_arabia_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_saudi_arabia_marketing_ratio"></td><td>Saudi Arabia Marketing</td><td id="whatsapp_saudi_arabia_marketing_multipler"></td><td id="whatsapp_saudi_arabia_marketing_credit"></td><td id="whatsapp_saudi_arabia_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_saudi_arabia_service_ratio"></td><td>Saudi Arabia Service</td><td id="whatsapp_saudi_arabia_service_multipler"></td><td id="whatsapp_saudi_arabia_service_credit"></td><td id="whatsapp_saudi_arabia_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_saudi_arabia_utility_ratio"></td><td>Saudi Arabia Utility</td><td id="whatsapp_saudi_arabia_utility_multipler"></td><td id="whatsapp_saudi_arabia_utility_credit"></td><td id="whatsapp_saudi_arabia_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_south_africa_authentication_ratio"></td><td>South Africa Authentication</td><td id="whatsapp_south_africa_authentication_multipler"></td><td id="whatsapp_south_africa_authentication_credit"></td><td id="whatsapp_south_africa_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_south_africa_marketing_ratio"></td><td>South Africa Marketing</td><td id="whatsapp_south_africa_marketing_multipler"></td><td id="whatsapp_south_africa_marketing_credit"></td><td id="whatsapp_south_africa_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_south_africa_service_ratio"></td><td>South Africa Service</td><td id="whatsapp_south_africa_service_multipler"></td><td id="whatsapp_south_africa_service_credit"></td><td id="whatsapp_south_africa_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_south_africa_utility_ratio"></td><td>South Africa Utility</td><td id="whatsapp_south_africa_utility_multipler"></td><td id="whatsapp_south_africa_utility_credit"></td><td id="whatsapp_south_africa_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_spain_authentication_ratio"></td><td>Spain Authentication</td><td id="whatsapp_spain_authentication_multipler"></td><td id="whatsapp_spain_authentication_credit"></td><td id="whatsapp_spain_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_spain_marketing_ratio"></td><td>Spain Marketing</td><td id="whatsapp_spain_marketing_multipler"></td><td id="whatsapp_spain_marketing_credit"></td><td id="whatsapp_spain_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_spain_service_ratio"></td><td>Spain Service</td><td id="whatsapp_spain_service_multipler"></td><td id="whatsapp_spain_service_credit"></td><td id="whatsapp_spain_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_spain_utility_ratio"></td><td>Spain Utility</td><td id="whatsapp_spain_utility_multipler"></td><td id="whatsapp_spain_utility_credit"></td><td id="whatsapp_spain_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_turkey_authentication_ratio"></td><td>Turkey Authentication</td><td id="whatsapp_turkey_authentication_multipler"></td><td id="whatsapp_turkey_authentication_credit"></td><td id="whatsapp_turkey_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_turkey_marketing_ratio"></td><td>Turkey Marketing</td><td id="whatsapp_turkey_marketing_multipler"></td><td id="whatsapp_turkey_marketing_credit"></td><td id="whatsapp_turkey_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_turkey_service_ratio"></td><td>Turkey Service</td><td id="whatsapp_turkey_service_multipler"></td><td id="whatsapp_turkey_service_credit"></td><td id="whatsapp_turkey_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_turkey_utility_ratio"></td><td>Turkey Utility</td><td id="whatsapp_turkey_utility_multipler"></td><td id="whatsapp_turkey_utility_credit"></td><td id="whatsapp_turkey_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_united_arab_emirates_authentication_ratio"></td><td>United Arab Emirates Authentication</td><td id="whatsapp_united_arab_emirates_authentication_multipler"></td><td id="whatsapp_united_arab_emirates_authentication_credit"></td><td id="whatsapp_united_arab_emirates_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_united_arab_emirates_marketing_ratio"></td><td>United Arab Emirates Marketing</td><td id="whatsapp_united_arab_emirates_marketing_multipler"></td><td id="whatsapp_united_arab_emirates_marketing_credit"></td><td id="whatsapp_united_arab_emirates_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_united_arab_emirates_service_ratio"></td><td>United Arab Emirates Service</td><td id="whatsapp_united_arab_emirates_service_multipler"></td><td id="whatsapp_united_arab_emirates_service_credit"></td><td id="whatsapp_united_arab_emirates_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_united_arab_emirates_utility_ratio"></td><td>United Arab Emirates Utility</td><td id="whatsapp_united_arab_emirates_utility_multipler"></td><td id="whatsapp_united_arab_emirates_utility_credit"></td><td id="whatsapp_united_arab_emirates_utility_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_united_kingdom_authentication_ratio"></td><td>United Kingdom Authentication</td><td id="whatsapp_united_kingdom_authentication_multipler"></td><td id="whatsapp_united_kingdom_authentication_credit"></td><td id="whatsapp_united_kingdom_authentication_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_united_kingdom_marketing_ratio"></td><td>United Kingdom Marketing</td><td id="whatsapp_united_kingdom_marketing_multipler"></td><td id="whatsapp_united_kingdom_marketing_credit"></td><td id="whatsapp_united_kingdom_marketing_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_united_kingdom_service_ratio"></td><td>United Kingdom Service</td><td id="whatsapp_united_kingdom_service_multipler"></td><td id="whatsapp_united_kingdom_service_credit"></td><td id="whatsapp_united_kingdom_service_rates"></td></tr>
  <tr><td>WhatsApp</td><td id="whatsapp_united_kingdom_utility_ratio"></td><td>United Kingdom Utility</td><td id="whatsapp_united_kingdom_utility_multipler"></td><td id="whatsapp_united_kingdom_utility_credit"></td><td id="whatsapp_united_kingdom_utility_rates"></td></tr>
  </table>
</div>

<script type="text/javascript">
// list in order of Delta, Theta, Gamma, Sigma, Lambda
// [Ratio, Multipler]
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
    $("#message_error").html('Invalid number');
    return
  }
  update_credits(credit_type, credit_rate);
});

function update_credits(credit_type, credit_rate){
  $.each(credit_map, (k,v) => {
    var ratio = v[credit_type][0];
    var multipler = v[credit_type][1];
    var calc_credit = "N/A";
    var calc_rates = "N/A";
    if ((ratio != 'N/A') && (multipler != 'N/A') ){
      calc_credit = (ratio * multipler).toFixed(2);
      calc_rates = '$' + (calc_credit * credit_rate).toFixed(4);
    }
    $(k + '_ratio').html(ratio);
    $(k + '_multipler').html(multipler);
    $(k + '_credit').html(calc_credit);
    $(k + '_rates').html(calc_rates);
  });
}
</script>
