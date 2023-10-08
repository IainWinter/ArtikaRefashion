function talk(endpoint, params) {
    let request = `${g_BackendURL}/${endpoint}?`;

    for (let i = 0; i < params.length; i++) {
        let p = params[i];
        request += `${p[0]}=${p[1]}`;

        if (i != params.length - 1) {
            request += '&';
        }
    }

    return fetch(request).then((r) => { return r.json(); });
}