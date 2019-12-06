<!--
.. link:
.. description:
.. tags:
.. date: 2012-05-22 11:54:14
.. title: Donate
.. slug: donate
-->

L'ambiente Desktop MATE è totalmente gratuito e tutte le persone coinvolte sono volontari.

Considera la possibilità di fare una donazione al progetto MATE. E' bello aver riconosciuti gli sforzi che abbiamo
messo nel progetto. Il denaro raccolto verrà usato per coprire i costi
di hosting, qualsiasi hardware acquistato e possibilmente le spese di volo in modo che
i membri del team MATE possano partecipare alle conferenze più rilevanti.

Non ti chiediamo tanto, è a tua completa discrezione.

<style>
img.centered {
    display: block;
    margin-left: auto;
    margin-right: auto }
</style>

## PayPal

<img class="right" src="https://www.paypalobjects.com/webstatic/mktg/Logo/pp-logo-100px.png" alt="PayPal Logo">

Preferiremmo che tu impostassi un pagamento ricorrente per aiutare ad assicurare che i costi
mensili siano sempre coperti e questo inoltre ci permette di pianificare meglio come
premiare i nostri contributori e sponsorizzare altri progetti Open Source.
Detto questo, anche le singole donazioni sono molto ben accette.

<div class="bs-docs-section">
  <div class="row">
    <div class="col-lg-6">
      <div class="well bs-component">
        <form name="monthly" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" onsubmit="return validateMonthlyForm()" method="post">
          <fieldset>
            <legend>Support PayPal mensile</legend>
            <div class="form-group">
              <label for="donationAmount" class="col-lg-4 control-label">Seleziona una somma</label>
              <div class="col-lg-6">
                <input type="radio" name="amt" value="5" />5
                <input type="radio" name="amt" value="10" checked="" />10
                <input type="radio" name="amt" value="25" />25
                <input type="radio" name="amt" value="50" />50
                <input type="radio" name="amt" value="100" />100
              </div>
            </div>
            <div class="form-group">
              <label for="specifyAmount" class="col-lg-4 control-label">Specifica la tua somma</label>
              <div class="col-lg-6">
                <input type="text" name="other" value="" size="5" maxlength="5">
              </div>
            </div>
            <div class="form-group">
              <label for="select" class="col-lg-4 control-label">Valuta</label>
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
                <button type="submit" class="btn btn-primary">Donazione Mensile</button>
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
            <legend>Donazione PayPal Singola</legend>
            <div class="form-group">
              <label for="donationAmount" class="col-lg-4 control-label">Seleziona una somma</label>
              <div class="col-lg-6">
                <input type="radio" name="amt" value="5" />5
                <input type="radio" name="amt" value="10" checked="" />10
                <input type="radio" name="amt" value="25" />25
                <input type="radio" name="amt" value="50" />50
                <input type="radio" name="amt" value="100" />100
              </div>
            </div>
            <div class="form-group">
              <label for="specifyAmount" class="col-lg-4 control-label">Specifica la tua somma</label>
              <div class="col-lg-6">
                <input type="text" name="other" value="" size="5" maxlength="5">
              </div>
            </div>
            <div class="form-group">
              <label for="select" class="col-lg-4 control-label">Valuta</label>
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
                <button type="submit" class="btn btn-primary">Singola Donazione</button>
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
          <p>Clicca o scansione il codice QR qui sotto per lanciare il tuo client Bitcoin e
          dona 0.02 btc al Desktop MATE. In Alternativa, copia e incolla l'
          indirizzo Bitcoin nel tuo client Bitcoin per donare una somma a tua scelta.
          </p>
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
          alert("Inserisci una somma valida - grazie!");
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
          alert("Inserisci una somma valida - grazie!");
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
