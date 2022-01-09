<!--
.. link:
.. description:
.. tags: 
.. date: 2012-05-22 11:54:14
.. title: Донација
.. slug: donate
-->

Мејтова радна површ је потпуно бесплатна и сви који учествују су добровољци.

Размотрите случај о добровољном прилогу Мејтовом пројекту. Лепо је
када је препознат напор који смо у њега уложили. Сав прикупљени новац
биће искоришћен за покривање трошкова удомљавања, набавку хардвера
и могућих путних трошкова како би чланови Мејтове екипе могли да
присуствују одговарајућим конференцијама.

Не тражимо много, на вама је да одлучите.

<style>
img.centered {
    display: block;
    margin-left: auto;
    margin-right: auto }
</style>

## PayPal

<img class="right" src="https://www.paypalobjects.com/webstatic/mktg/Logo/pp-logo-100px.png" alt="PayPal Logo">

Више бисмо волели да подесите периодично плаћање како бисмо били сигурни
да су месечни трошкови увек покривени и што ће нам такође омогућити да боље
планирамо како да наградимо наше сараднике и спонзоришемо друге пројекте
отвореног кода. Ипак, и једнократне донације се такође са захвалношћу прихватају. 

<div class="bs-docs-section">
  <div class="well">
    <form name="monthly" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" onsubmit="return validateMonthlyForm()" method="post">
      <fieldset>
        <legend>Месечни PayPal подржавалац</legend>
        <div class="row">
          <label class="control-label">Изаберите износ</label>
          <label class="badge badge-info btn-mini"><input type="radio" name="amt" value="5">5</label>
          <label class="badge badge-success btn-mini"><input type="radio" name="amt" value="10" checked>10</label>
          <label class="badge badge-warning btn-mini"><input type="radio" name="amt" value="25">25</label>
          <label class="badge badge-important btn-mini"><input type="radio" name="amt" value="50">50</label>
          <label class="badge badge-inverse btn-mini"><input type="radio" name="amt" value="100">100</label>
        </div>
        <div class="row">
          <label for="monthly-specifyAmount" class="control-label">Наведите ваш износ</label>
          <input type="text" id="monthly-specifyAmount" name="other" value="" size="5" maxlength="5"/>
        </div>
        <div class="row">
          <label for="monthly-currency" class="control-label">Валута</label>
          <select id="monthly-currency" class="form-control" name="currency_code">
            <option>EUR</option>
            <option>USD</option>
            <option selected="">GBP</option>
          </select>
        </div>
        <button type="submit" class="btn btn-primary">Месечна донација</button>
      </fieldset>
      <input type="hidden" name="cmd" value="_xclick-subscriptions">
      <input type="hidden" name="business" value="6282B4CZGVCB6">
      <input type="hidden" name="item_name" value="MATE Desktop Monthly Supporter">
      <input type="hidden" name="no_shipping" value="1">
      <input type="hidden" name="no_note" value="1">
      <input type="hidden" name="charset" value="UTF-8">
      <input type="hidden" name="a3" value="">
      <input type="hidden" name="p3" value="1">
      <input type="hidden" name="t3" value="M">
      <input type="hidden" name="src" value="1">
      <input type="hidden" name="sra" value="1">
      <input type="hidden" name="return" value="https://mate-desktop.org/donation-completed/">
      <input type="hidden" name="cancel_return" value="https://mate-desktop.org/donation-cancelled/">
    </form>
  </div>

  <div class="well">
    <form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" onsubmit="return validateSingleForm()" method="post">
      <fieldset>
        <legend>Једнократна PayPal донација</legend>
        <div class="row">
          <label class="control-label">Изаберите износ</label>
          <label class="badge badge-info btn-mini"><input type="radio" name="amt" value="5">5</label>
          <label class="badge badge-success btn-mini"><input type="radio" name="amt" value="10" checked>10</label>
          <label class="badge badge-warning btn-mini"><input type="radio" name="amt" value="25">25</label>
          <label class="badge badge-important btn-mini"><input type="radio" name="amt" value="50">50</label>
          <label class="badge badge-inverse btn-mini"><input type="radio" name="amt" value="100">100</label>
        </div>
        <div class="row">
          <label for="one-time-specifyAmount" class="control-label">Набедите ваш износ</label>
          <input id="one-time-specifyAmount" type="text" name="other" value="" size="5" maxlength="5">
        </div>
        <div class="row">
          <label for="one-time-currency" class="control-label">Валута</label>
          <select id="one-time-currency" class="form-control" name="currency_code">
            <option>EUR</option>
            <option>USD</option>
            <option selected="">GBP</option>
          </select>
        </div>
        <button type="submit" class="btn btn-primary">Једна донација</button>
      </fieldset>
      <input type="hidden" name="cmd" value="_xclick">
      <input type="hidden" name="business" value="6282B4CZGVCB6">
      <input type="hidden" name="item_name" value="MATE Desktop One-time Donation">
      <input type="hidden" name="no_shipping" value="1">
      <input type="hidden" name="no_note" value="1">
      <input type="hidden" name="charset" value="UTF-8">
      <input type="hidden" name="amount" value="">
      <input type="hidden" name="src" value="1">
      <input type="hidden" name="sra" value="1">
      <input type="hidden" name="return" value="https://mate-desktop.org/donation-completed/">
      <input type="hidden" name="cancel_return" value="https://mate-desktop.org/donation-cancelled/">
    </form>
  </div>
</div>

## Bitcoin

<div class="bs-docs-section">
  <div class="well">
    <fieldset>
      <legend>Бит-новчић</legend>
      <p>Кликните или скенирајте QR код испод да покренете ваш програм Бит-новчића
      и да донирате 0.02 btc Мејтовој радној површи. Или, умножите и убаците
      адресу Бит-новчића у ваш програм Бит-новчића да донирате износ по вашем
      избору.</p>
      <p align="center">
      <a href="bitcoin:1Mpan6eExzNKdS8JnFAod5Pwt49aR6JsDB?amount=0.02&label=MATE%20Desktop">
        <img src="https://chart.googleapis.com/chart?chs=384x384&cht=qr&chl=bitcoin:1Mpan6eExzNKdS8JnFAod5Pwt49aR6JsDB?amount=0.02&message=Donate_0.02_btc_to_MATE_Desktop" /></a>
      <br />
      <span style="font-family: monospace;">1Mpan6eExzNKdS8JnFAod5Pwt49aR6JsDB</span>
      </p>
    </fieldset>
  </div>
</div>

<script type="text/javascript">
  function validateMonthlyForm() {
    var n = document.forms["monthly"]["other"].value;
      if (n) {
        if (!isNaN(parseFloat(n)) && isFinite(n) && (n > 0)) {
          document.forms["monthly"]["a3"].value = n;
          return true;
        } else {
          alert("Упишите исправан износ донације - хвала!");
          document.forms["monthly"]["other"].value = "";
          return false;
        }
      }
      else {
        document.forms["monthly"]["a3"].value = document.forms["monthly"]["amt"].value;
        return true;
      }
  }

  function validateSingleForm() {
    var n = document.forms["single"]["other"].value;
      if (n) {
        if (!isNaN(parseFloat(n)) && isFinite(n) && (n > 0)) {
          document.forms["single"]["amount"].value = n;
          return true;
        } else {
          alert("Упишите исправан износ донације - хвала!");
          document.forms["single"]["other"].value = "";
          return false;
        }
      }
      else {
        document.forms["single"]["amount"].value = document.forms["single"]["amt"].value;
        return true;
      }
  }
</script>
