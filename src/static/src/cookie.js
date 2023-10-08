function cookie_set(name, value, days) {
  const expires = new Date();
  expires.setTime(expires.getTime() + (days * 24 * 60 * 60 * 1000));
  const expiresStr = "expires=" + expires.toUTCString();
  document.cookie = name + "=" + value + ";" + expiresStr + ";path=/";
}

function cookie_get(name) {
  const cookieName = name + "=";
  const cookies = document.cookie.split(';');
  for (let i = 0; i < cookies.length; i++) {
    let cookie = cookies[i].trim();
    if (cookie.indexOf(cookieName) === 0) {
      return cookie.substring(cookieName.length, cookie.length);
    }
  }
  return null;
}

function cookie_delete(cookieName) {
  document.cookie = cookieName + "=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
}

function cookie_getWalletCookie() {
  return cookie_get(g_WalletCookieName);
}

function cookie_setWalletCookie(walletId) {
  cookie_set(g_WalletCookieName, walletId);
}

function cookie_deleteWalletCookie() {
  return cookie_delete(g_WalletCookieName);
}