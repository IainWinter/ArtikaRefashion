function user_linkAccount(walletId, isDesigner) {
    return talk("user_link_wallet", [
        ["wallet_id", walletId],
        ["is_designer", isDesigner]
    ]);
}

function user_setInfo(walletId, userName, userAddress) {
    return talk("user_set_data", [
        ["wallet_id", walletId],
        ["user_name", userName],
        ["user_address", userAddress],
    ]);
}

function user_getInfo(walletId) {
    return talk("user_get_data", [
        ["wallet_id", walletId]
    ]);
}