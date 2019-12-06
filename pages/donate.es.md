<!--
.. link:
.. description:
.. tags: 
.. date: 2012-05-22 11:54:14
.. title: Donaciones
.. slug: donate
-->

El entorno de escritorio MATE es completamente gratis y libre. Todas las
personas envueltas son voluntarias.

Por favor considera hacer una donación al proyecto MATE. Es bueno saber que
el esfuerzo que hemos puesto es reconocido. Cualquier dinero que recibamos se
usará para cubrir los gastos de hosting, cualquier hardware necesario, y
posiblemente gastos de viaje para que los miembros del equipo MATE puedan
asistir a conferencias relevantes.

No pedimos mucho, es a tu discreción.

<style>
img.centered {
    display: block;
    margin-left: auto;
    margin-right: auto }
</style>

## PayPal

<img class="right" src="https://www.paypalobjects.com/webstatic/mktg/Logo/pp-logo-100px.png" alt="PayPal Logo">

Preferiríamos si haces un pago recurrente para ayudar a asegurarnos de
que los gastos mensuales siempre estén cubiertos, y también nos ayuda
a planificar mejor como recompensar a nuestros colaboladores y patrocinar
otros proyectos Open Source.
Dicho esto, donaciones de una sola vez también son muy agradecidas.

<div class="bs-docs-section">
  <div class="row">
    <div class="col-lg-6">
      <div class="well bs-component">
        <form name="monthly" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" onsubmit="return validateMonthlyForm()" method="post">
          <fieldset>
            <legend>Patrocinador mensual con PayPal</legend>
            <div class="form-group">
              <label for="donationAmount" class="col-lg-4 control-label">Selecciona una cantidad</label>
              <div class="col-lg-6">
                <input type="radio" name="amt" value="5" />5
                <input type="radio" name="amt" value="10" checked="" />10
                <input type="radio" name="amt" value="25" />25
                <input type="radio" name="amt" value="50" />50
                <input type="radio" name="amt" value="100" />100
              </div>
            </div>
            <div class="form-group">
              <label for="specifyAmount" class="col-lg-4 control-label">Especifíca tu propia cantidad</label>
              <div class="col-lg-6">
                <input type="text" name="other" value="" size="5" maxlength="5">
              </div>
            </div>
            <div class="form-group">
              <label for="select" class="col-lg-4 control-label">Moneda</label>
              <div class="col-lg-6">
                <select class="form-control" name="currency_code">
                  <option>EUR</option>
                  <option>USD</option>
                  <option selected="">GBP</option>
                </select>
              </div>
            </div>
            <div class="form-group">
              <div class="col-lg-6">
                <button type="submit" class="btn btn-primary">Donación Mensual</button>
              </div>
            </div>
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
    </div>
    <div class="col-lg-6">
      <div class="well bs-component">
        <form name="single" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" onsubmit="return validateSingleForm()" method="post">
          <fieldset>
            <legend>Donación individual con PayPal</legend>
            <div class="form-group">
              <label for="donationAmount" class="col-lg-4 control-label">Selecciona una cantidad</label>
              <div class="col-lg-6">
                <input type="radio" name="amt" value="5" />5
                <input type="radio" name="amt" value="10" checked="" />10
                <input type="radio" name="amt" value="25" />25
                <input type="radio" name="amt" value="50" />50
                <input type="radio" name="amt" value="100" />100
              </div>
            </div>
            <div class="form-group">
              <label for="specifyAmount" class="col-lg-4 control-label">Especifíca tu propia cantidad</label>
              <div class="col-lg-6">
                <input type="text" name="other" value="" size="5" maxlength="5">
              </div>
            </div>
            <div class="form-group">
              <label for="select" class="col-lg-4 control-label">Moneda</label>
              <div class="col-lg-6">
                <select class="form-control" name="currency_code">
                  <option>EUR</option>
                  <option>USD</option>
                  <option selected="">GBP</option>
                </select>
              </div>
            </div>
            <div class="form-group">
              <div class="col-lg-6">
                <button type="submit" class="btn btn-primary">Donación individual</button>
              </div>
            </div>
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
  </div>
</div>

## Bitcoin

<div class="bs-docs-section">
  <div class="row">
    <div class="col-lg-12">
      <div class="well bs-component">
        <legend>Bitcoin</legend>
          <p>Haz click o escanea el código QR abajo para lanzar tu cliente de Bitcoin
          y hacer una donación de 0.02 btc al escritorio MATE. Alternativamente, copia
          y pega la dirección Bitcoin en tu cliente de Bitcoin para donar la cantidad
          que quieras.</p>
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
          alert("Please enter a valid donation amount - thanks!");
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
          alert("Please enter a valid donation amount - thanks!");
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
