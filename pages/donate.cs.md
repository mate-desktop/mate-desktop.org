<!--
.. link:
.. description:
.. tags: 
.. date: 2012-05-22 11:54:14
.. title: Přispět
.. slug: donate
-->

Pracovní prostředí MATE je zcela zdarma a všichni zúčastnění jsou dobrovolníci.

Zvažte prosím příspěvek projektu MATE. Je hezké uznat úsilí, které jsme do něj
vložili. Veškeré získané peníze budou použity na pokrytí nákladů na hosting,
pořízení hardwaru a případně cestovní výdaje, aby se členové MATE týmu mohli
zúčastnit příslušných konferencí.

Nepožadujeme mnoho, záleží na vašem uvážení. 

<style>
img.centered {
    display: block;
    margin-left: auto;
    margin-right: auto }
</style>

## PayPal

<img class="right" src="https://www.paypalobjects.com/webstatic/mktg/Logo/pp-logo-100px.png" alt="PayPal Logo">

Dali bychom přednost tomu, abyste nastavili opakovanou platbu, abychom mohli
zajistit, že budou vždy pokryty měsíční náklady, a také nám to umožní lépe
plánovat, jak odměnit naše přispěvatele a sponzorovat další open source projekty.
Jednorázové dary jsou ale také vděčně přijímány. 

<div class="bs-docs-section">
  <div class="well">
    <form name="monthly" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" onsubmit="return validateMonthlyForm()" method="post">
      <fieldset>
        <legend>Měsíční PayPal podporovatel</legend>
        <div class="row">
          <label class="control-label">Vyberte částku</label>
          <label class="badge badge-info btn-mini"><input type="radio" name="amt" value="5">5</label>
          <label class="badge badge-success btn-mini"><input type="radio" name="amt" value="10" checked>10</label>
          <label class="badge badge-warning btn-mini"><input type="radio" name="amt" value="25">25</label>
          <label class="badge badge-important btn-mini"><input type="radio" name="amt" value="50">50</label>
          <label class="badge badge-inverse btn-mini"><input type="radio" name="amt" value="100">100</label>
        </div>
        <div class="row">
          <label for="monthly-specifyAmount" class="control-label">Uveďte vlastní částku</label>
          <input type="text" id="monthly-specifyAmount" name="other" value="" size="5" maxlength="5"/>
        </div>
        <div class="row">
          <label for="monthly-currency" class="control-label">Měna</label>
          <select id="monthly-currency" class="form-control" name="currency_code">
            <option>EUR</option>
            <option>USD</option>
            <option selected="">GBP</option>
          </select>
        </div>
        <button type="submit" class="btn btn-primary">Měsíční příspěvek</button>
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
        <legend>Jednorázový PayPal dar</legend>
        <div class="row">
          <label class="control-label">Vyberte částku</label>
          <label class="badge badge-info btn-mini"><input type="radio" name="amt" value="5">5</label>
          <label class="badge badge-success btn-mini"><input type="radio" name="amt" value="10" checked>10</label>
          <label class="badge badge-warning btn-mini"><input type="radio" name="amt" value="25">25</label>
          <label class="badge badge-important btn-mini"><input type="radio" name="amt" value="50">50</label>
          <label class="badge badge-inverse btn-mini"><input type="radio" name="amt" value="100">100</label>
        </div>
        <div class="row">
          <label for="one-time-specifyAmount" class="control-label">Uveďte vlastní částku</label>
          <input id="one-time-specifyAmount" type="text" name="other" value="" size="5" maxlength="5">
        </div>
        <div class="row">
          <label for="one-time-currency" class="control-label">Měna</label>
          <select id="one-time-currency" class="form-control" name="currency_code">
            <option>EUR</option>
            <option>USD</option>
            <option selected="">GBP</option>
          </select>
        </div>
        <button type="submit" class="btn btn-primary">Jednorázový příspěvek</button>
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
      <legend>Bitcoin</legend>
      <p>Kliknutím do QR kódu níže nebo jeho naskenováním spustíte svého 
      bitcoinového klienta a darujete MATE 0,02 BTC. Případně zkopírujte a vložte
      bitcoinovou adresu  do svého bitcoinového klienta a darujte částku podle
      svého výběru.</p>      
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
          alert("Zadejte prosím platnou částku daru - děkujeme!");
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
          alert("Zadejte prosím platnou částku daru - děkujeme!");
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
