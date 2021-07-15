<!--
.. link:
.. description:
.. tags: 
.. date: 2012-05-22 11:54:14
.. title: 寄付
.. slug: donate
-->

MATE デスクトップ環境は完全に無料で提供されています。これに関わる人々全員がボランティアです。

MATE プロジェクトへの寄付を検討してください。私たちが行った努力が認めらるのであれば幸いです。調達された資金は、ホスティング費用、ハードウェアの調達、および MATE チームのメンバーが関連会議に出席可能とするための旅費に充てられます。

私たちはたくさんお願いしません、それはあなたのご判断にお任せします。

<style>
img.centered {
    display: block;
    margin-left: auto;
    margin-right: auto }
</style>

## PayPal

<img class="right" src="https://www.paypalobjects.com/webstatic/mktg/Logo/pp-logo-100px.png" alt="PayPal Logo">

毎月のコストが常時賄えるように、定期的な支払いを設定していただくことをお勧めします。また、それによって、私たちの貢献者に報酬を与えたり、他のオープンソースプロジェクトを支援する方法をより適切に計画することができます。そうはお願いしても、一度限りの寄付でも喜んでお受けします。

<div class="bs-docs-section">
  <div class="well">
    <form name="monthly" class="form-horizontal" action="https://www.paypal.com/cgi-bin/webscr" onsubmit="return validateMonthlyForm()" method="post">
      <fieldset>
        <legend>月々の PayPal 支援者</legend>
        <div class="row">
          <label class="control-label">金額の選択</label>
          <label class="badge badge-info btn-mini"><input type="radio" name="amt" value="5">5</label>
          <label class="badge badge-success btn-mini"><input type="radio" name="amt" value="10" checked>10</label>
          <label class="badge badge-warning btn-mini"><input type="radio" name="amt" value="25">25</label>
          <label class="badge badge-important btn-mini"><input type="radio" name="amt" value="50">50</label>
          <label class="badge badge-inverse btn-mini"><input type="radio" name="amt" value="100">100</label>
        </div>
        <div class="row">
          <label for="monthly-specifyAmount" class="control-label">金額を指定してください</label>
          <input type="text" id="monthly-specifyAmount" name="other" value="" size="5" maxlength="5"/>
        </div>
        <div class="row">
          <label for="monthly-currency" class="control-label">通貨</label>
          <select id="monthly-currency" class="form-control" name="currency_code">
            <option>EUR</option>
            <option>USD</option>
            <option selected="">GBP</option>
          </select>
        </div>
        <button type="submit" class="btn btn-primary">月毎の寄付</button>
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
        <legend>PayPal で一度限りの寄付</legend>
        <div class="row">
          <label class="control-label">金額の選択</label>
          <label class="badge badge-info btn-mini"><input type="radio" name="amt" value="5">5</label>
          <label class="badge badge-success btn-mini"><input type="radio" name="amt" value="10" checked>10</label>
          <label class="badge badge-warning btn-mini"><input type="radio" name="amt" value="25">25</label>
          <label class="badge badge-important btn-mini"><input type="radio" name="amt" value="50">50</label>
          <label class="badge badge-inverse btn-mini"><input type="radio" name="amt" value="100">100</label>
        </div>
        <div class="row">
          <label for="one-time-specifyAmount" class="control-label">金額を指定してください</label>
          <input id="one-time-specifyAmount" type="text" name="other" value="" size="5" maxlength="5">
        </div>
        <div class="row">
          <label for="one-time-currency" class="control-label">通貨</label>
          <select id="one-time-currency" class="form-control" name="currency_code">
            <option>EUR</option>
            <option>USD</option>
            <option selected="">GBP</option>
          </select>
        </div>
        <button type="submit" class="btn btn-primary">一度限りの寄付</button>
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

## ビットコイン

<div class="bs-docs-section">
  <div class="well">
    <fieldset>
      <legend>ビットコイン</legend>
      <p>下の QR コードをクリックまたはスキャンして Bitcoin クライアントを起動して、0.02btc を MATE デスクトップに寄付できます。あるいは、Bitcoin アドレスを Bitcoin クライアントにコピー&ペーストして、好きな金額を寄付することもできます。</p>
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
    var n = document.forms["毎月"]["その他"].value;
      if (n) {
        if (!isNaN(parseFloat(n)) && isFinite(n) && (n > 0)) {
          document.forms["毎月"]["a3"].value = n;
          return true;
        } else {
          alert("適当な寄付額を入力してください - 感謝します！");
          document.forms["毎月"]["その他"].value = "";
          return false;
        }
      }
      else {
        document.forms["毎月"]["a3"].value = document.forms["monthly"]["amt"].value;
        return true;
      }
  }

  function validateSingleForm() {
    var n = document.forms["一度限り"]["その他"].value;
      if (n) {
        if (!isNaN(parseFloat(n)) && isFinite(n) && (n > 0)) {
          document.forms["single"]["amount"].value = n;
          return true;
        } else {
          alert("適当な寄付額を入力してください - 感謝します！");
          document.forms["single"]["other"].value = "";
          return false;
        }
      }
      else {
        document.forms["一度限り"]["金額"].value = document.forms["single"]["amt"].value;
        return true;
      }
  }
</script>
