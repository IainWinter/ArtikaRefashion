function user_ChangeInfo(walletId, userName, userAddress) {
    fetch(`${g_BackendURL}?wallet_id=${walletId}&user_name=${userName}&user_address=${userAddress}`)
        .then((response) => {
            if ("error" in response) {
                console.error(response);
                return;
            }

            console.log("Success");
        });
}
