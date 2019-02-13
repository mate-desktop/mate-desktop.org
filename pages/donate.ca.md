<!--
.. link:
.. description:
.. tags: 
.. date: 2012-05-22 11:54:14
.. title: Donatius
.. slug: donate
-->

L'entorn d'escriptori MATE és totalment gratuït i tots els involucrats són
voluntaris.

Considereu donar al projecte MATE. És bo que se'ns reconegui l'esforç dipositat.
Els diners recaptats s'utilitzaran per cobrir el cost de l'allotjament, qualsevol
adquisició de maquinari i, possiblement, les despeses dels viatge perquè els
membres de l'equip de MATE puguin assistir a conferències rellevants.

No demanem gaire, està en la vostra discreció.

<style>
img.centered {
    display: block;
    margin-left: auto;
    margin-right: auto }
</style>

## PayPal

<img class="right" src="https://www.paypalobjects.com/webstatic/mktg/Logo/pp-logo-100px.png" alt="Logotip de PayPal">

Preferim que configureu un pagament recurrent per garantir que les despeses
mensuals estiguin sempre coberts i perquè també ens permeti planificar millor com
recompensar els nostres contribuïdors i patrocinar altres projectes de codi obert.
Dit això, les donacions úniques també s'accepten amb gratitud.

<div class="bs-docs-section">
  <div class="row">
    <div class="col-lg-6">
      <div class="well bs-component">
        <form name="monthly" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" onsubmit="return validateMonthlyForm()" method="post">
          <fieldset>
            <legend>Simpatitzant mensual amb PayPal</legend>
            <div class="form-group">
              <label for="donationAmount" class="col-lg-4 control-label">Seleccioneu la quantitat</label>
              <div class="col-lg-6">
                <input type="radio" name="amt" value="5" />5
                <input type="radio" name="amt" value="10" checked="" />10
                <input type="radio" name="amt" value="25" />25
                <input type="radio" name="amt" value="50" />50
                <input type="radio" name="amt" value="100" />100
              </div>
            </div>
            <div class="form-group">
              <label for="specifyAmount" class="col-lg-4 control-label">Especifiqueu la quantitat</label>
              <div class="col-lg-6">
                <input type="text" name="other" value="" size="5" maxlength="5">
              </div>
            </div>
            <div class="form-group">
              <label for="select" class="col-lg-4 control-label">Moneda</label>
              <div class="col-lg-6">
                <select class="form-control" name="currency_code">
                  <option selected="">EUR</option>
                  <option>USD</option>
                  <option>GBP</option>
                </select>
              </div>
            </div>
            <div class="form-group">
              <div class="col-lg-6">
                <button type="submit" class="btn btn-primary">Dóna mensualment</button>
              </div>
            </div>
          </fieldset>
          <input type="hidden" name="cmd" value="_xclick-subscriptions">
          <input type="hidden" name="business" value="6282B4CZGVCB6">
          <input type="hidden" name="item_name" value="Simpatitzant mensual de l'escriptori MATE">
          <input type="hidden" name="no_shipping" value="1">
          <input type="hidden" name="no_note" value="1">
          <input type="hidden" name="charset" value="UTF-8">
          <input type="hidden" name="a3" value="">
          <input type="hidden" name="p3" value="1">
          <input type="hidden" name="t3" value="M">
          <input type="hidden" name="src" value="1">
          <input type="hidden" name="sra" value="1">
          <input type="hidden" name="return" value="http://mate-desktop.org/donation-completed/">
          <input type="hidden" name="cancel_return" value="http://mate-desktop.org/donation-cancelled/">
        </form>
      </div>
    </div>
    <div class="col-lg-6">
      <div class="well bs-component">
        <form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" onsubmit="return validateSingleForm()" method="post">
          <fieldset>
            <legend>Donació unica amb PayPal</legend>
            <div class="form-group">
              <label for="donationAmount" class="col-lg-4 control-label">Seleccioneu una quantitat</label>
              <div class="col-lg-6">
                <input type="radio" name="amt" value="5" />5
                <input type="radio" name="amt" value="10" checked="" />10
                <input type="radio" name="amt" value="25" />25
                <input type="radio" name="amt" value="50" />50
                <input type="radio" name="amt" value="100" />100
              </div>
            </div>
            <div class="form-group">
              <label for="specifyAmount" class="col-lg-4 control-label">Especifiqueu la quantitat</label>
              <div class="col-lg-6">
                <input type="text" name="other" value="" size="5" maxlength="5">
              </div>
            </div>
            <div class="form-group">
              <label for="select" class="col-lg-4 control-label">Moneda</label>
              <div class="col-lg-6">
                <select class="form-control" name="currency_code">
                  <option selected="">EUR</option>
                  <option>USD</option>
                  <option>GBP</option>
                </select>
              </div>
            </div>
            <div class="form-group">
              <div class="col-lg-6">
                <button type="submit" class="btn btn-primary">Dóna una vegada</button>
              </div>
            </div>
          </fieldset>
          <input type="hidden" name="cmd" value="_xclick">
          <input type="hidden" name="business" value="6282B4CZGVCB6">
          <input type="hidden" name="item_name" value="Donació única a l'escriptori MATE">
          <input type="hidden" name="no_shipping" value="1">
          <input type="hidden" name="no_note" value="1">
          <input type="hidden" name="charset" value="UTF-8">
          <input type="hidden" name="amount" value="">
          <input type="hidden" name="src" value="1">
          <input type="hidden" name="sra" value="1">
          <input type="hidden" name="return" value="http://mate-desktop.org/donation-completed/">
          <input type="hidden" name="cancel_return" value="http://mate-desktop.org/donation-cancelled/">
        </form>
      </div>
    </div>
  </div>
</div>

## Bitcoin

<div class="bs-docs-section">
  <div class="row">
    <div class="col-lg-12">
      <div class="well bs-component">
        <legend>Bitcoin</legend>
          <p>Feu clic o escaneu el codi QR de sota per iniciar el vostre client de
             Bitcoin i donar 0,02 btc a l'escriptori MATE. Alternativament, copieu
             i enganxeu l'adreça de Bitcoin al vostre client de Bitcoin per donar
             la quantitat que trieu.</p>
          <p align="center">
            <a href="bitcoin:1Mpan6eExzNKdS8JnFAod5Pwt49aR6JsDB?amount=0.02&label=MATE%20Desktop">
            <img src="https://chart.googleapis.com/chart?chs=384x384&cht=qr&chl=bitcoin:1Mpan6eExzNKdS8JnFAod5Pwt49aR6JsDB?amount=0.02&message=Donate_0.02_btc_to_MATE_Desktop" /></a>
            <br />
            <tt>1Mpan6eExzNKdS8JnFAod5Pwt49aR6JsDB</tt>
          </p>
      </div>
    </div>
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
          alert("Introduïu una quantitat correcta per a la donació, gràcies!");
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
          alert("Introduïu una quantitat correcta per a la donació, gràcies!");
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
